#!/usr/bin/env python3
"""
fable5_communicators.py
------------------------
"Communicator" mode for Fable 5 Offline Agent: a small roster of agent
personas that talk to *each other* (propose -> critique -> refine ->
synthesize) instead of a single fixed research/writer/critic pipeline,
and that turn what they learned into a new skills/*.md file so every
future run of ANY mode (--loop, --hermes, --team, --commune, ...)
starts smarter, because read_skills_bundle() in the main harness loads
skills/*.md into the system prompt on every run.

This file is intentionally self-contained (stdlib only, no import of
fable5_offline_agent.py at module load time) so it can be dropped next
to fable5_offline_agent.py and either:

  1. run completely standalone:  python fable5_communicators.py --commune "topic"
  2. wired into the main CLI with ~6 lines of glue code (see
     INTEGRATION.md that ships alongside this file).

Design goals, matching the conventions already visible in Fable 5:
  - flat, single-file, stdlib-first (repo's only deps are openai + pypdf)
  - agent personas are short markdown "briefs" under agents/communicators/*.md,
    the same pattern as agents/hermes-agent.md, agents/fable-loop-agent.md, etc.
  - env-var configuration named FABLE5_* like the rest of the project
  - respects the existing self-improve gate: --no-self-improve /
    FABLE5_SELF_IMPROVE=0 disables writing new skill files
  - respects the existing HITL gate: FABLE5_HITL=1 (default) asks for a
    confirmation before a skill file is written to disk
  - session transcripts land under memory/communicator_sessions/, next
    to the existing memory/LOOP_STATE.md convention

NOTE ON HOW THIS WAS BUILT: the author's cloud workspace could not
reach github.com's git endpoints directly (network allowlist), so this
was written against a summary of fable5_offline_agent.py's public
architecture (function names/signatures for make_client(), stream_chat(),
read_skills_bundle(), the --team supervisor, and the FABLE5_* env vars)
rather than the literal source file. The two integration touch points
in INTEGRATION.md are therefore something to eyeball against your actual
file before running --diff-free.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, List, Optional, Sequence

# ---------------------------------------------------------------------------
# Configuration (mirrors the FABLE5_* env-var convention used elsewhere)
# ---------------------------------------------------------------------------

MODEL_NAME = os.environ.get("FABLE5_MODEL", "qwen2.5:7b")
LOCAL_LLM_BASE_URL = os.environ.get("FABLE5_BASE_URL", "http://localhost:11434/v1")
MEMORY_DIR = Path(os.path.expanduser(os.environ.get("FABLE5_MEMORY", "memory")))
SKILLS_DIR = Path(os.path.expanduser(os.environ.get("FABLE5_SKILLS", "skills")))
AGENTS_DIR = Path(os.path.expanduser(os.environ.get("FABLE5_AGENTS", "agents")))
TEMPERATURE = float(os.environ.get("FABLE5_TEMPERATURE", "0.3"))

DEFAULT_SELF_IMPROVE = os.environ.get("FABLE5_SELF_IMPROVE", "1") not in {"0", "false", "no"}
HITL = os.environ.get("FABLE5_HITL", "1") not in {"0", "false", "no"}
DEFAULT_ROUNDS = int(os.environ.get("FABLE5_COMM_ROUNDS", "5"))
DEFAULT_ROSTER = os.environ.get("FABLE5_COMM_AGENTS", "proposer,challenger,synthesizer")

COMMUNICATORS_SUBDIR = "communicators"  # agents/communicators/*.md
SESSIONS_SUBDIR = "communicator_sessions"  # memory/communicator_sessions/*.md

_BUILTIN_BRIEFS = {
    "proposer": (
        "# Proposer\n\n"
        "You open the discussion. Given the topic, state ONE concrete "
        "approach in 4-8 sentences: what you'd do, the key assumption "
        "it rests on, and the biggest risk. Be specific, not generic.\n"
    ),
    "challenger": (
        "# Challenger\n\n"
        "You critique the most recent message from a peer. Name the single "
        "weakest point (a wrong assumption, a missing edge case, or a "
        "cost/benefit that doesn't hold up) in 3-6 sentences. Do not "
        "restate what's good; only the sharpest flaw and why it matters. "
        "If the prior message already addressed your best objection, say "
        "so plainly instead of manufacturing a critique.\n"
    ),
    "synthesizer": (
        "# Synthesizer\n\n"
        "You read the full exchange and produce two things, clearly "
        "labeled:\n"
        "1) FINAL APPROACH - the best version of the plan after the "
        "critique/refinement rounds, in a short paragraph.\n"
        "2) LESSONS - 1 to 3 bullet points, each a general, reusable "
        "principle (not specific to this topic) that a future agent "
        "should know. Phrase each as an imperative instruction, the way "
        "a skill file would read.\n"
    ),
    "mentor": (
        "# Mentor\n\n"
        "You act as a fresh-context reviewer of the whole exchange. Judge "
        "only whether the FINAL APPROACH actually resolves the sharpest "
        "critique raised. Answer 'resolved' or 'unresolved' with one "
        "sentence of justification.\n"
    ),
}

_ROLE_KIND = {
    "proposer": "proposal",
    "challenger": "critique",
    "synthesizer": "synthesis",
    "mentor": "review",
}


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class CommunicatorAgent:
    name: str
    brief: str
    temperature: float = TEMPERATURE

    @classmethod
    def load(cls, name: str, agents_dir: Path = AGENTS_DIR, temperature: float = TEMPERATURE) -> "CommunicatorAgent":
        brief_path = agents_dir / COMMUNICATORS_SUBDIR / f"{name}.md"
        if brief_path.exists():
            brief = brief_path.read_text(encoding="utf-8")
        else:
            brief = _BUILTIN_BRIEFS.get(name, f"# {name.title()}\n\nParticipate constructively as '{name}'.\n")
        return cls(name=name, brief=brief, temperature=temperature)


@dataclass
class Message:
    round: int
    author: str
    kind: str  # proposal | critique | refinement | synthesis | review
    content: str
    target: Optional[str] = None  # whose message this responds to, if any

    def as_transcript_line(self) -> str:
        head = f"### Round {self.round} — {self.author} ({self.kind})"
        if self.target:
            head += f", re: {self.target}"
        return f"{head}\n\n{self.content.strip()}\n"


@dataclass
class CommunicatorResult:
    topic: str
    transcript: List[Message] = field(default_factory=list)
    final_approach: str = ""
    lessons: List[str] = field(default_factory=list)
    skill_path: Optional[Path] = None
    memory_path: Optional[Path] = None

    def transcript_markdown(self) -> str:
        lines = [f"# Communicator session: {self.topic}", ""]
        lines += [m.as_transcript_line() for m in self.transcript]
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Chat call abstraction — injectable so this module is testable without a
# running Ollama server and without importing the main harness.
# ---------------------------------------------------------------------------

ChatFn = Callable[..., str]


def default_chat_fn(client, messages: list[dict], *, temperature: float = TEMPERATURE, prefix: str = "") -> str:
    """
    Falls back to the main harness's stream_chat() at call time (lazy
    import, so importing this module never requires fable5_offline_agent.py
    or the openai package to be installed unless you actually run for real).
    """
    from fable5_offline_agent import stream_chat  # type: ignore
    return stream_chat(client, messages, temperature=temperature, prefix=prefix)


def make_client_lazy():
    from fable5_offline_agent import make_client  # type: ignore
    return make_client()


# ---------------------------------------------------------------------------
# Skills bundle (best-effort — falls back to empty string if the harness
# isn't importable, e.g. during standalone testing)
# ---------------------------------------------------------------------------

def _read_skills_bundle(skills_dir: Path, limit_chars: int = 5000) -> str:
    try:
        from fable5_offline_agent import read_skills_bundle  # type: ignore
        return read_skills_bundle(limit_chars=limit_chars)
    except Exception:
        pass
    if not skills_dir.exists():
        return ""
    chunks = []
    total = 0
    for p in sorted(skills_dir.glob("*.md"))[:12]:
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            continue
        if total + len(text) > limit_chars:
            text = text[: max(0, limit_chars - total)]
        chunks.append(text)
        total += len(text)
        if total >= limit_chars:
            break
    return "\n\n".join(chunks)


# ---------------------------------------------------------------------------
# Core session logic
# ---------------------------------------------------------------------------

def _slugify(text: str, max_len: int = 40) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:max_len] or "session"


def _build_messages(system_core: str, agent: CommunicatorAgent, skills_bundle: str,
                     topic: str, transcript: Sequence[Message], instruction: str) -> list[dict]:
    system_parts = [system_core.strip()] if system_core else []
    system_parts.append(agent.brief.strip())
    if skills_bundle.strip():
        system_parts.append("## Skills learned from prior sessions\n\n" + skills_bundle.strip())
    system_msg = "\n\n---\n\n".join(p for p in system_parts if p)

    transcript_text = "\n\n".join(m.as_transcript_line() for m in transcript) or "(no messages yet)"
    user_msg = (
        f"Topic: {topic}\n\n"
        f"Conversation so far:\n\n{transcript_text}\n\n"
        f"Your task now: {instruction}"
    )
    return [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg},
    ]


def _extract_lessons(synthesis_text: str) -> List[str]:
    lessons: List[str] = []
    in_lessons = False
    for line in synthesis_text.splitlines():
        stripped = line.strip()
        if re.match(r"(?i)^\**\s*lessons?\b", stripped):
            in_lessons = True
            continue
        if in_lessons:
            m = re.match(r"^[-*\d.)]+\s*(.+)$", stripped)
            if m and m.group(1).strip():
                lessons.append(m.group(1).strip())
            elif stripped == "" and lessons:
                break
    if not lessons:
        # Fallback: grab up to 3 non-empty lines after the word "lesson"
        idx = synthesis_text.lower().find("lesson")
        if idx != -1:
            tail = synthesis_text[idx:].splitlines()[1:4]
            lessons = [t.strip("-* ").strip() for t in tail if t.strip()]
    return lessons[:3]


def run_communicator_session(
    topic: str,
    *,
    client=None,
    chat_fn: ChatFn = default_chat_fn,
    agent_names: Optional[Sequence[str]] = None,
    rounds: int = DEFAULT_ROUNDS,
    system_core: str = "",
    agents_dir: Path = AGENTS_DIR,
    skills_dir: Path = SKILLS_DIR,
    memory_dir: Path = MEMORY_DIR,
    self_improve: bool = DEFAULT_SELF_IMPROVE,
    hitl: bool = HITL,
    approve_fn: Callable[[str], bool] = lambda skill_text: True,
    write_files: bool = True,
) -> CommunicatorResult:
    """
    Run one communicator session: proposer opens, challenger/refiner rounds
    alternate, synthesizer closes with a final approach + reusable lessons.
    If self_improve is on, the lessons are written to a new skills/*.md file
    (gated by approve_fn when hitl is True) so future sessions of ANY mode
    load them via read_skills_bundle().
    """
    names = list(agent_names) if agent_names else [n.strip() for n in DEFAULT_ROSTER.split(",") if n.strip()]
    if "proposer" not in names:
        names.insert(0, "proposer")
    if "synthesizer" not in names:
        names.append("synthesizer")

    roster = {n: CommunicatorAgent.load(n, agents_dir=agents_dir) for n in set(names) | {"proposer", "synthesizer"}}
    skills_bundle = _read_skills_bundle(skills_dir)

    result = CommunicatorResult(topic=topic)
    critics = [n for n in names if n not in ("proposer", "synthesizer")] or ["challenger"]
    for c in critics:
        roster.setdefault(c, CommunicatorAgent.load(c, agents_dir=agents_dir))

    # Round 1: proposer opens.
    proposer = roster["proposer"]
    msgs = _build_messages(system_core, proposer, skills_bundle, topic, result.transcript,
                            f"Propose an initial approach to: {topic}")
    content = chat_fn(client, msgs, temperature=proposer.temperature, prefix="[proposer] ")
    result.transcript.append(Message(round=1, author="proposer", kind="proposal", content=content))

    # Rounds 2..rounds: alternate critique / refinement, rotating critics.
    critic_i = 0
    for rnd in range(2, max(rounds, 2) + 1):
        last = result.transcript[-1]
        if last.kind in ("proposal", "refinement"):
            critic_name = critics[critic_i % len(critics)]
            critic_i += 1
            critic = roster[critic_name]
            msgs = _build_messages(system_core, critic, skills_bundle, topic, result.transcript,
                                    f"Critique the most recent message (by '{last.author}').")
            content = chat_fn(client, msgs, temperature=critic.temperature, prefix=f"[{critic_name}] ")
            result.transcript.append(Message(round=rnd, author=critic_name, kind="critique",
                                              content=content, target=last.author))
        else:
            # last was a critique -> the original author refines.
            author_name = last.target or "proposer"
            author = roster.get(author_name, proposer)
            msgs = _build_messages(system_core, author, skills_bundle, topic, result.transcript,
                                    f"Refine your earlier message to address the critique from '{last.author}'.")
            content = chat_fn(client, msgs, temperature=author.temperature, prefix=f"[{author_name}] ")
            result.transcript.append(Message(round=rnd, author=author_name, kind="refinement",
                                              content=content, target=last.author))

    # Final round: synthesizer closes the session.
    synth = roster["synthesizer"]
    msgs = _build_messages(system_core, synth, skills_bundle, topic, result.transcript,
                            "Write the FINAL APPROACH and the LESSONS as specified in your brief.")
    synthesis = chat_fn(client, msgs, temperature=synth.temperature, prefix="[synthesizer] ")
    result.transcript.append(Message(round=rounds + 1, author="synthesizer", kind="synthesis", content=synthesis))
    result.final_approach = synthesis
    result.lessons = _extract_lessons(synthesis)

    if write_files:
        result.memory_path = _write_transcript(result, memory_dir)
        if self_improve and result.lessons:
            skill_text = _render_skill_file(result)
            if (not hitl) or approve_fn(skill_text):
                result.skill_path = _write_skill_file(result, skill_text, skills_dir)

    return result


def _write_transcript(result: CommunicatorResult, memory_dir: Path) -> Path:
    sessions_dir = memory_dir / SESSIONS_SUBDIR
    sessions_dir.mkdir(parents=True, exist_ok=True)
    stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = sessions_dir / f"{stamp}-{_slugify(result.topic)}.md"
    path.write_text(result.transcript_markdown(), encoding="utf-8", newline="\n")
    return path


def _render_skill_file(result: CommunicatorResult) -> str:
    stamp = _dt.datetime.now().strftime("%Y-%m-%d")
    lines = [
        f"# Skill: lessons from communicator session ({stamp})",
        "",
        f"Source: communicator session on \"{result.topic}\"",
        "Applies-to: general",
        "",
        "## Lessons",
        "",
    ]
    lines += [f"- {lesson}" for lesson in result.lessons]
    lines.append("")
    return "\n".join(lines)


def _write_skill_file(result: CommunicatorResult, skill_text: str, skills_dir: Path) -> Path:
    skills_dir.mkdir(parents=True, exist_ok=True)
    stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = skills_dir / f"commune-{_slugify(result.topic)}-{stamp}.md"
    path.write_text(skill_text, encoding="utf-8", newline="\n")
    return path


# ---------------------------------------------------------------------------
# Standalone CLI
# ---------------------------------------------------------------------------

def _cli_approve(skill_text: str) -> bool:
    print("\n--- proposed new skill file (HITL, FABLE5_HITL=1) ---\n")
    print(skill_text)
    try:
        answer = input("\nWrite this skill file? [y/N] ").strip().lower()
    except EOFError:
        return False
    return answer in {"y", "yes"}


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="fable5_communicators.py",
        description="Run a multi-agent communicator session (propose -> critique -> refine -> synthesize -> learn).",
    )
    parser.add_argument("--commune", type=str, required=True, metavar="TOPIC",
                         help="Topic/goal for the communicator agents to discuss.")
    parser.add_argument("--rounds", type=int, default=DEFAULT_ROUNDS,
                         help=f"Number of critique/refinement rounds after the opening proposal (default {DEFAULT_ROUNDS}).")
    parser.add_argument("--agents", type=str, default=DEFAULT_ROSTER,
                         help=f"Comma-separated roster (default '{DEFAULT_ROSTER}').")
    parser.add_argument("--no-self-improve", action="store_true",
                         help="Don't write a new skills/*.md file from this session's lessons.")
    args = parser.parse_args(argv)

    client = make_client_lazy()
    result = run_communicator_session(
        args.commune,
        client=client,
        agent_names=[n.strip() for n in args.agents.split(",") if n.strip()],
        rounds=args.rounds,
        self_improve=(DEFAULT_SELF_IMPROVE and not args.no_self_improve),
        approve_fn=_cli_approve if HITL else (lambda _t: True),
    )

    print("\n" + "=" * 70)
    print(result.transcript_markdown())
    print("=" * 70)
    if result.memory_path:
        print(f"\nTranscript saved: {result.memory_path}")
    if result.skill_path:
        print(f"New skill written: {result.skill_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
