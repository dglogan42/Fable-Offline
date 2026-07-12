#!/usr/bin/env python3
"""
Fable 5 Offline Agent
Local reasoning + loop engineering + self-improvement + Hermes-style behaviors.

Usage:
  python fable5_offline_agent.py
  python fable5_offline_agent.py --loop "…"
  python fable5_offline_agent.py --hermes "…"
  python fable5_offline_agent.py --improve
  python fable5_offline_agent.py --compress-memory

In chat:
  /loop  /hermes  /improve  /skills  /soul  /memory  /compress  /doctor  /help  quit

Hermes behaviors (offline, inspired by self-improving agent courses + Hermes loops):
  SOUL.md identity · smart RAG (top-K relevant memory) · self-stopping loop
  mid-run prompt repair · memory compression · skill compound

Requires: pip install openai
Ollama:  ollama serve && ollama pull <MODEL_NAME>
"""

from __future__ import annotations

import argparse
import json
import math
import os
import platform
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# ==================== CONFIG ====================
LOCAL_LLM_BASE_URL = os.environ.get("FABLE5_BASE_URL", "http://localhost:11434/v1")
MODEL_NAME = os.environ.get("FABLE5_MODEL", "qwen2.5:7b")
SYSTEM_PROMPT_FILE = os.environ.get("FABLE5_MANUAL", "Fable5_Operating_Manual.md")
SOUL_FILE = os.environ.get("FABLE5_SOUL", "SOUL.md")
MEMORY_DIR = Path(os.path.expanduser(os.environ.get("FABLE5_MEMORY", "memory")))
SKILLS_DIR = Path(os.path.expanduser(os.environ.get("FABLE5_SKILLS", "skills")))
WORKFLOWS_DIR = Path(os.path.expanduser(os.environ.get("FABLE5_WORKFLOWS", "workflows")))
WORKSPACE_DIR = Path(os.path.expanduser(os.environ.get("FABLE5_WORKSPACE", "workspace")))
DEFAULT_MAX_CYCLES = int(os.environ.get("FABLE5_MAX_CYCLES", "6"))
RETRY_CEILING = int(os.environ.get("FABLE5_RETRY_CEILING", "3"))
TEMPERATURE = float(os.environ.get("FABLE5_TEMPERATURE", "0.3"))
MAX_TOKENS = int(os.environ.get("FABLE5_MAX_TOKENS", "8192"))
# Smart RAG: retrieve this many memory chunks (course: ~20 relevant, not 2000)
RAG_TOP_K = int(os.environ.get("FABLE5_RAG_TOP_K", "20"))
# Self-improve after loops unless FABLE5_SELF_IMPROVE=0
DEFAULT_SELF_IMPROVE = os.environ.get("FABLE5_SELF_IMPROVE", "1").strip().lower() not in {
    "0",
    "false",
    "no",
    "off",
}
# Shell automation: off by default; set FABLE5_ALLOW_SHELL=1 to run allowlisted commands
ALLOW_SHELL = os.environ.get("FABLE5_ALLOW_SHELL", "").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}
# Engineer loop: require min score 1-10 on each success criterion (default 8)
ENGINEER_MIN_SCORE = int(os.environ.get("FABLE5_ENGINEER_MIN_SCORE", "8"))
# Bilevel outer loop every N cycles (0 = off)
BILEVEL_EVERY = int(os.environ.get("FABLE5_BILEVEL_EVERY", "3"))
PROGRAM_FILE = os.environ.get("FABLE5_PROGRAM", "program.md")
ROADMAP_FILE = os.environ.get("FABLE5_ROADMAP", "ROADMAP.md")
# Human-in-the-loop: prompt before high-risk steps (default on for team/shell)
HITL = os.environ.get("FABLE5_HITL", "1").strip().lower() not in {"0", "false", "no", "off"}
# Set FABLE5_ASCII=1 to force ASCII UI (legacy Windows consoles)
USE_ASCII = os.environ.get("FABLE5_ASCII", "").strip() in {"1", "true", "yes"}
# ===============================================

SCRIPT_DIR = Path(__file__).resolve().parent
IS_WINDOWS = sys.platform == "win32"
IS_MAC = sys.platform == "darwin"
IS_LINUX = sys.platform.startswith("linux")
PLATFORM_LABEL = {
    "win32": "Windows",
    "darwin": "macOS",
}.get(sys.platform, "Linux" if IS_LINUX else platform.system() or sys.platform)


def configure_stdio() -> None:
    """UTF-8 stdio on all platforms (critical for Windows consoles)."""
    os.environ.setdefault("PYTHONUTF8", "1")
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    for stream in (sys.stdout, sys.stderr, sys.stdin):
        try:
            if hasattr(stream, "reconfigure"):
                stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    # Windows: enable ANSI if possible (Win10+)
    if IS_WINDOWS:
        try:
            import ctypes

            kernel32 = ctypes.windll.kernel32  # type: ignore[attr-defined]
            handle = kernel32.GetStdHandle(-11)
            mode = ctypes.c_uint32()
            if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                kernel32.SetConsoleMode(handle, mode.value | 0x0004)
        except Exception:
            pass


def ui(text: str) -> str:
    """Optionally strip non-ASCII for broken terminals."""
    if not USE_ASCII:
        return text
    repl = {
        "╔": "+", "╗": "+", "╚": "+", "╝": "+", "║": "|", "═": "=",
        "─": "-", "▶": ">", "→": "->", "✓": "[OK]", "✗": "[X]",
        "⏸": "[||]", "⚠": "!", "📝": "[note]", "…": "...", "—": "-",
        "·": "*", "❌": "[error]",
    }
    out = text
    for a, b in repl.items():
        out = out.replace(a, b)
    return out.encode("ascii", errors="replace").decode("ascii")


def _resolve(path: str | Path) -> Path:
    """Resolve paths relative to the script dir; expand ~ on all platforms."""
    p = Path(os.path.expanduser(str(path)))
    if p.is_file() or p.is_absolute():
        return p.resolve() if p.exists() else p
    here = (SCRIPT_DIR / p).resolve()
    return here if here.exists() else (SCRIPT_DIR / p)


def load_manual_core() -> str:
    """Load the Fable 5 Operating Manual body if present, else a built-in core."""
    path = _resolve(SYSTEM_PROMPT_FILE)
    if path.is_file():
        content = path.read_text(encoding="utf-8")
        for marker in (
            "This document governs every response you produce",
            "## 1. Read the request beneath the words",
        ):
            if marker in content:
                return content[content.find(marker) :]
        return content
    print(ui("⚠️  Fable5_Operating_Manual.md not found — using built-in core rules only."))
    return (
        "You are a brutally rigorous reasoning engine with loop-engineering and "
        "self-improvement discipline.\n"
        "1. Serve real intent, not only the literal ask.\n"
        "2. Break problems into independently checkable pieces.\n"
        "3. Put effort where being wrong is expensive.\n"
        "4. Re-derive every number, fact, and claim.\n"
        "5. Label guesses at the claim.\n"
        "6. Attack your own conclusion before sending.\n"
        "7. Answer first. Then reasoning. Then concrete risk.\n"
        "8. In loops: ONE bounded unit per cycle; maker is never the grader.\n"
        "9. Self-improve by writing durable skills from verified lessons — not weight updates.\n"
        "Pre-send self-test every time. No bullshit."
    )


def load_soul() -> str:
    """Load SOUL.md — Hermes-style identity/steering file that controls agent persona."""
    path = _resolve(SOUL_FILE)
    if not path.is_file():
        # Seed default soul next to the script
        path = SCRIPT_DIR / "SOUL.md"
        if not path.is_file():
            path.write_text(DEFAULT_SOUL_MD, encoding="utf-8", newline="\n")
    if path.is_file():
        return path.read_text(encoding="utf-8").strip()
    return DEFAULT_SOUL_MD.strip()


DEFAULT_SOUL_MD = """# SOUL.md — Fable 5 Offline Agent

You are a **local, offline reasoning agent**. You do not phone home.
You optimize for correctness over fluency. You compound via skills and memory, not weight updates.

## Identity
- Name: Fable5 Offline
- Style: precise, skeptical, useful; answer first, then reasoning, then risk
- Values: re-derive numbers, label guesses, attack own conclusions, maker ≠ grader

## Boundaries
- Never invent tool results or test output
- Prefer one bounded unit of progress over finishing everything at once
- Escalate to the human after repeated failure of the same unit
- Do not dump entire chat history into context — use retrieved memory only

## Hermes behaviors (always on when /hermes or --hermes)
1. **Soul-first** — this file steers identity and stop ethics
2. **Smart RAG** — only the most relevant memory chunks, not the whole archive
3. **Self-stop** — stop on success, retry ceiling, or budget without waiting for a human
4. **Live repair** — when the verifier fails, repair strategy/prompt before the next unit
5. **Memory compress** — periodically fold lessons into shorter durable notes
6. **Skill compound** — write reusable skills from verified wins and failure-preventers
"""


def load_system_prompt(*, hermes: bool = False) -> str:
    """Manual + soul + active skills (self-improving compound context)."""
    core = load_manual_core()
    soul = load_soul()
    skills = read_skills_bundle(limit_chars=5000)
    parts = [
        core,
        "\n\n---\n## SOUL.md (identity / steering)\n\n" + soul,
    ]
    if hermes:
        parts.append(
            "\n\n---\n## Hermes mode active\n"
            "You are running Hermes-style offline behaviors: soul-steered, RAG-limited memory, "
            "self-stopping loops, mid-run repair after failed verification, and skill compound.\n"
        )
    if skills.strip():
        parts.append(
            "\n\n---\n## Active skills (self-improved library)\n"
            "Apply any skill whose WHEN_TO_USE matches the task. Prefer skills over inventing "
            "a new procedure when they fit.\n\n"
            + skills
        )
    return "".join(parts)


def make_client():
    try:
        from openai import OpenAI
    except ImportError as e:
        print(ui("❌ Missing dependency: openai"))
        print("  Install on all platforms:")
        print("    python -m pip install -r requirements.txt")
        print("  or: python -m pip install openai")
        raise SystemExit(1) from e
    return OpenAI(base_url=LOCAL_LLM_BASE_URL, api_key=os.environ.get("FABLE5_API_KEY", "ollama"))


def ollama_base_http() -> str:
    """Map OpenAI-compatible base (.../v1) to Ollama root for health checks."""
    base = LOCAL_LLM_BASE_URL.rstrip("/")
    if base.endswith("/v1"):
        return base[:-3]
    return base


def check_backend(timeout: float = 2.5) -> tuple[bool, str]:
    """Return (ok, message) for the local LLM HTTP endpoint."""
    root = ollama_base_http()
    url = root + "/api/tags"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "fable5-offline-agent"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if 200 <= resp.status < 300:
                return True, f"OK — backend reachable at {root}"
            return False, f"HTTP {resp.status} from {url}"
    except urllib.error.URLError as e:
        return False, f"Cannot reach {url} ({e.reason})"
    except Exception as e:
        return False, f"Cannot reach {url} ({e})"


def which_python() -> str:
    return sys.executable or shutil.which("python3") or shutil.which("python") or "python"


def doctor() -> int:
    """Cross-platform environment report (no model inference)."""
    print(ui("Fable 5 — doctor (multi-platform check)\n"))
    print(f"  OS:          {PLATFORM_LABEL} ({platform.platform()})")
    print(f"  Arch:        {platform.machine()}")
    print(f"  Python:      {sys.version.split()[0]}  ({which_python()})")
    print(f"  Script dir:  {SCRIPT_DIR}")
    print(f"  CWD:         {Path.cwd()}")
    print(f"  Model:       {MODEL_NAME}")
    print(f"  API base:    {LOCAL_LLM_BASE_URL}")
    print(f"  Memory dir:  {memory_root()}")
    print(f"  Skills dir:  {skills_root()}")
    n_skills = len(list_skill_paths())
    print(f"  Skills:      {n_skills} file(s)")
    print(f"  Workflows:   {workflows_root()}")
    print(f"  Workspace:   {workspace_root()}")
    print(f"  Shell auto:  {'enabled' if ALLOW_SHELL else 'disabled (dry-run)'}")
    print(f"  RAG top-K:   {RAG_TOP_K}")
    soul_path = _resolve(SOUL_FILE)
    if not soul_path.is_file():
        soul_path = SCRIPT_DIR / "SOUL.md"
    print(f"  Soul:        {soul_path}  ({'found' if soul_path.is_file() else 'will seed'})")
    manual = _resolve(SYSTEM_PROMPT_FILE)
    print(f"  Manual:      {manual}  ({'found' if manual.is_file() else 'MISSING'})")
    try:
        import openai  # noqa: F401

        print("  openai pkg:  installed")
    except ImportError:
        print("  openai pkg:  MISSING — run: python -m pip install -r requirements.txt")
    ollama = shutil.which("ollama")
    print(f"  ollama CLI:  {ollama or 'not on PATH (optional if API is up)'}")
    ok, msg = check_backend()
    print(f"  Backend:     {msg}")
    if not ok:
        print()
        print("  Next steps:")
        if IS_WINDOWS:
            print("    - Install Ollama from https://ollama.com/download")
            print("    - Start the Ollama app, then: ollama pull " + MODEL_NAME)
        elif IS_MAC:
            print("    - brew install ollama   OR  https://ollama.com/download")
            print("    - ollama serve   # if not running as a service")
            print("    - ollama pull " + MODEL_NAME)
        else:
            print("    - curl -fsSL https://ollama.com/install.sh | sh")
            print("    - ollama serve && ollama pull " + MODEL_NAME)
        return 1
    print(ui("\n✓ Environment looks ready."))
    return 0


def stream_chat(
    client,
    messages: list[dict],
    *,
    temperature: float = TEMPERATURE,
    prefix: str = "",
) -> str:
    """Stream a completion to stdout; return full text."""
    if prefix:
        print(prefix, end="", flush=True)
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=temperature,
        max_tokens=MAX_TOKENS,
        stream=True,
    )
    full = ""
    for chunk in response:
        delta = chunk.choices[0].delta.content if chunk.choices else None
        if delta:
            print(delta, end="", flush=True)
            full += delta
    print("\n")
    return full


def complete(
    client,
    messages: list[dict],
    *,
    temperature: float = TEMPERATURE,
) -> str:
    """Non-streaming completion (used when quiet)."""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=temperature,
        max_tokens=MAX_TOKENS,
        stream=False,
    )
    return (response.choices[0].message.content or "").strip()


# -------------------- Memory --------------------


def memory_root() -> Path:
    if MEMORY_DIR.is_absolute():
        root = MEMORY_DIR
    else:
        root = SCRIPT_DIR / MEMORY_DIR
    root = root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    (root / "lessons").mkdir(exist_ok=True)
    index = root / "INDEX.md"
    if not index.exists():
        index.write_text(
            "# Fable 5 Loop Memory\n\n"
            "Lessons and cycle logs for offline loop engineering.\n"
            "The harness and executor read this each cycle.\n\n"
            "## Active lessons\n\n"
            "_(none yet)_\n\n"
            "## Recent cycles\n\n"
            "_(none yet)_\n",
            encoding="utf-8",
            newline="\n",
        )
    return root


def read_memory_bundle(limit_chars: int = 6000) -> str:
    root = memory_root()
    parts: list[str] = []
    index = root / "INDEX.md"
    if index.exists():
        parts.append(index.read_text(encoding="utf-8"))
    lessons = sorted((root / "lessons").glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    for lesson in lessons[:8]:
        text = lesson.read_text(encoding="utf-8")
        parts.append(f"### File: lessons/{lesson.name}\n{text}")
    bundle = "\n\n---\n\n".join(parts)
    if len(bundle) > limit_chars:
        bundle = bundle[:limit_chars] + "\n\n…[memory truncated for context]…"
    return bundle


# -------------------- Hermes: smart RAG + repair + compress --------------------


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]{2,}", text.lower())


def _chunk_memory_corpus() -> list[dict]:
    """Collect memory documents as RAG chunks (Hermes: don't load 2000 messages)."""
    root = memory_root()
    chunks: list[dict] = []
    for path in sorted(root.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        # Split long files into ~800-char paragraphs
        pieces = re.split(r"\n{2,}", text)
        buf = ""
        for p in pieces:
            if len(buf) + len(p) < 900:
                buf = (buf + "\n\n" + p).strip()
            else:
                if buf:
                    chunks.append({"id": f"{path.name}:{len(chunks)}", "source": path.name, "text": buf})
                buf = p.strip()
        if buf:
            chunks.append({"id": f"{path.name}:{len(chunks)}", "source": path.name, "text": buf})
    return chunks


def retrieve_relevant_memory(query: str, top_k: int = RAG_TOP_K, limit_chars: int = 6000) -> str:
    """
    Smart RAG: score memory chunks against the query; return top-K only.
    Course framing: bring ~20 relevant items, not the entire archive.
    Pure local TF-style scoring — no external embedding service.
    """
    chunks = _chunk_memory_corpus()
    if not chunks:
        return "(no memory yet)"
    q_tokens = _tokenize(query)
    if not q_tokens:
        # fall back to newest chunks
        selected = chunks[-top_k:]
    else:
        q_set = Counter(q_tokens)
        scored: list[tuple[float, dict]] = []
        for ch in chunks:
            t = _tokenize(ch["text"])
            if not t:
                continue
            t_set = Counter(t)
            # TF overlap + light IDF-ish rarity
            overlap = sum((q_set & t_set).values())
            if overlap == 0:
                continue
            rarity = sum(1.0 / (1 + math.log(1 + t_set[w])) for w in q_set if w in t_set)
            score = overlap + 0.3 * rarity
            # recency boost for cycle logs
            if ch["source"].startswith("cycle_"):
                score += 0.5
            scored.append((score, ch))
        scored.sort(key=lambda x: x[0], reverse=True)
        selected = [c for _, c in scored[:top_k]]
        if not selected:
            selected = chunks[-min(top_k, len(chunks)) :]

    parts = [
        f"### [{c['source']}] (rag)\n{c['text'][:1200]}"
        for c in selected
    ]
    bundle = (
        f"# Retrieved memory (top {len(selected)} of {len(chunks)} chunks — Hermes smart RAG)\n\n"
        + "\n\n---\n\n".join(parts)
    )
    if len(bundle) > limit_chars:
        bundle = bundle[:limit_chars] + "\n\n…[rag truncated]…"
    return bundle


REPAIR_ROLE = """You are the LIVE REPAIR engine (Hermes behavior: detect error → fix strategy now).
The verifier failed. Do NOT redo the whole goal. Output a short repair for the NEXT unit only.

Format exactly:
REPAIR_STRATEGY: <one sentence change in approach>
NEXT_UNIT: <the single next bounded unit to attempt>
PROMPT_PATCH: <extra instructions for the executor this cycle only>
AVOID: <what failed pattern to not repeat>
"""


def live_repair(
    client,
    *,
    goal: str,
    unit: str,
    artifact: str,
    verdict: str,
    fail_streak: int,
) -> str:
    """On verifier FAIL: produce a prompt/strategy patch for the next cycle."""
    user = (
        f"GOAL: {goal}\n"
        f"FAILED UNIT: {unit}\n"
        f"FAIL STREAK: {fail_streak}\n\n"
        f"ARTIFACT (excerpt):\n{artifact[:2000]}\n\n"
        f"VERIFIER:\n{verdict[:1500]}\n\n"
        "Repair the approach for the next cycle only."
    )
    print(ui("\n[hermes live-repair]\n"))
    return stream_chat(
        client,
        [
            {"role": "system", "content": REPAIR_ROLE},
            {"role": "user", "content": user},
        ],
        temperature=0.25,
        prefix="Repair: ",
    )


COMPRESS_ROLE = """You are the MEMORY COMPRESSOR (Hermes behavior: fold history into durable notes).
Given raw memory excerpts, produce a short compressed memory document.

Rules:
- Keep only durable facts, decisions, corrections, and open risks
- Drop chat fluff and duplicate cycles
- Max ~40 lines
- Start with: # Compressed memory (YYYY-MM-DD)
- Bullet lists preferred
"""


def compress_memory(client, system: str, *, focus: Optional[str] = None) -> Path:
    """Compress memory archive into a single durable note (course: auto memory optimize)."""
    raw = read_memory_bundle(limit_chars=10000)
    rag = retrieve_relevant_memory(focus or "lessons failures decisions risks", top_k=RAG_TOP_K)
    print(ui("\n[hermes memory-compress]\n"))
    out = stream_chat(
        client,
        [
            {"role": "system", "content": COMPRESS_ROLE},
            {
                "role": "user",
                "content": (
                    f"FOCUS: {focus or 'general durable lessons'}\n\n"
                    f"RAG SLICE:\n{rag}\n\n"
                    f"INDEX BUNDLE (excerpt):\n{raw[:4000]}\n"
                ),
            },
        ],
        temperature=0.2,
        prefix="Compress: ",
    )
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    path = memory_root() / "lessons" / f"compressed-{stamp}.md"
    path.write_text(out.strip() + "\n", encoding="utf-8", newline="\n")
    index = memory_root() / "INDEX.md"
    text = index.read_text(encoding="utf-8") if index.exists() else "# Memory\n\n## Active lessons\n\n"
    entry = f"- [Compressed {stamp}](lessons/{path.name})\n"
    if path.name not in text:
        if "## Active lessons" in text:
            text = text.replace("## Active lessons\n\n", f"## Active lessons\n\n{entry}", 1)
            text = text.replace("_(none yet)_\n", "")
        else:
            text += f"\n## Active lessons\n\n{entry}"
        index.write_text(text, encoding="utf-8", newline="\n")
    print(ui(f"  ✓ Compressed memory → {path}\n"))
    return path


def append_cycle_log(
    cycle: int,
    goal: str,
    unit_summary: str,
    artifact: str,
    claims: str,
    verdict: str,
    stop_reason: Optional[str],
) -> None:
    root = memory_root()
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    log_path = root / f"cycle_{cycle:03d}.md"
    log_path.write_text(
        f"# Cycle {cycle}\n\n"
        f"- **When:** {stamp}\n"
        f"- **Goal:** {goal}\n"
        f"- **Unit:** {unit_summary}\n"
        f"- **Stop:** {stop_reason or 'continue'}\n\n"
        f"## Artifact\n\n{artifact}\n\n"
        f"## Claims\n\n{claims}\n\n"
        f"## Verifier\n\n{verdict}\n",
        encoding="utf-8",
        newline="\n",
    )
    index = root / "INDEX.md"
    block = (
        f"- Cycle {cycle} ({stamp}): {unit_summary[:120]} "
        f"— **{stop_reason or 'continue'}** · `{log_path.name}`\n"
    )
    text = index.read_text(encoding="utf-8")
    if "## Recent cycles" in text:
        text = text.replace("## Recent cycles\n\n", f"## Recent cycles\n\n{block}", 1)
        text = text.replace("_(none yet)_\n", "", 1)
    else:
        text += f"\n## Recent cycles\n\n{block}"
    index.write_text(text, encoding="utf-8", newline="\n")


def maybe_write_lesson(client, system: str, goal: str, cycle: int, verdict: str, artifact: str) -> None:
    """Ask model if a durable lesson should be filed; write at most one short note."""
    prompt = (
        "You are the memory clerk for a Fable 5 loop.\n"
        f"Goal: {goal}\nCycle: {cycle}\n\n"
        f"Verifier verdict:\n{verdict}\n\n"
        f"Artifact (excerpt):\n{artifact[:2500]}\n\n"
        "If there is ONE durable lesson worth keeping for future cycles "
        "(a correction, a confirmed approach, a definition that must stick), "
        "reply with exactly:\n"
        "LESSON: <one-line summary>\nBODY:\n<2-6 short lines>\n\n"
        "If nothing is worth saving, reply with exactly: NONE"
    )
    try:
        out = complete(
            client,
            [
                {"role": "system", "content": "Be terse. File only high-value lessons. No fluff."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )
    except Exception:
        return
    if not out or out.strip().upper().startswith("NONE"):
        return
    m = re.search(r"LESSON:\s*(.+)", out)
    summary = (m.group(1).strip() if m else f"cycle-{cycle}-lesson")[:80]
    body = out
    if "BODY:" in out:
        body = out.split("BODY:", 1)[1].strip()
    safe = re.sub(r"[^\w\-]+", "-", summary.lower()).strip("-")[:40] or f"c{cycle}"
    path = memory_root() / "lessons" / f"{datetime.now(timezone.utc).strftime('%Y%m%d')}-{safe}.md"
    path.write_text(f"# {summary}\n\n{body}\n", encoding="utf-8", newline="\n")
    index = memory_root() / "INDEX.md"
    text = index.read_text(encoding="utf-8")
    entry = f"- [{summary}](lessons/{path.name})\n"
    if "## Active lessons" in text:
        text = text.replace("## Active lessons\n\n", f"## Active lessons\n\n{entry}", 1)
        text = text.replace("_(none yet)_\n", "", 1)
        index.write_text(text, encoding="utf-8", newline="\n")
    print(ui(f"  📝 Lesson filed: {path.name}"))


# -------------------- Skills + self-improvement --------------------
# Offline compound improvement: system around the model (skills/memory), not weight updates.
# Workshop stack: memory → autonomy (loops) → self-improving agents (tools + skills).


def skills_root() -> Path:
    if SKILLS_DIR.is_absolute():
        root = SKILLS_DIR
    else:
        root = SCRIPT_DIR / SKILLS_DIR
    root = root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    index = root / "INDEX.md"
    if not index.exists():
        index.write_text(
            "# Fable 5 Skills Library\n\n"
            "Reusable procedures the offline agent wrote or upgraded via **self-improve**.\n"
            "Loaded into context on every run so the system compounds without retraining weights.\n\n"
            "## Skills\n\n"
            "_(none yet — run `/improve` or `--improve` after a loop)_\n",
            encoding="utf-8",
            newline="\n",
        )
    # Seed one foundational skill if library is empty (INDEX only)
    skill_files = [p for p in root.glob("*.md") if p.name.upper() != "INDEX.MD"]
    starter = root / "rederive-numbers.md"
    if not skill_files and not starter.exists():
        starter.write_text(
            "# Re-derive numbers\n\n"
            "**WHEN_TO_USE:** Any task that contains percentages, growth rates, totals, or "
            "quoted financial/metric claims.\n\n"
            "## Procedure\n"
            "1. Extract every numeric claim and its stated inputs.\n"
            "2. Recompute from endpoints (for %: change / base).\n"
            "3. Flag mismatches before polishing prose.\n"
            "4. Put the corrected verdict first.\n",
            encoding="utf-8",
            newline="\n",
        )
        _index_skill("rederive-numbers", "Re-derive numbers", starter.name, root=root)
    return root


def list_skill_paths() -> list[Path]:
    root = skills_root()
    return sorted(
        [p for p in root.glob("*.md") if p.name.upper() != "INDEX.MD"],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )


def _index_skill(
    skill_id: str,
    title: str,
    filename: str,
    *,
    root: Optional[Path] = None,
) -> None:
    base = root if root is not None else skills_root()
    index = base / "INDEX.md"
    text = index.read_text(encoding="utf-8") if index.exists() else "# Skills\n\n## Skills\n\n"
    entry = f"- **{skill_id}**: [{title}]({filename})\n"
    if filename in text or f"**{skill_id}**" in text:
        return
    if "## Skills" in text:
        text = text.replace("## Skills\n\n", f"## Skills\n\n{entry}", 1)
        text = text.replace("_(none yet — run `/improve` or `--improve` after a loop)_\n", "")
        text = text.replace("_(none yet)_\n", "")
    else:
        text += f"\n## Skills\n\n{entry}"
    index.write_text(text, encoding="utf-8", newline="\n")


def read_skills_bundle(limit_chars: int = 5000) -> str:
    paths = list_skill_paths()
    if not paths:
        return ""
    parts: list[str] = []
    for p in paths[:12]:
        body = p.read_text(encoding="utf-8")
        parts.append(f"### skill:{p.stem}\n{body}")
    bundle = "\n\n---\n\n".join(parts)
    if len(bundle) > limit_chars:
        bundle = bundle[:limit_chars] + "\n\n…[skills truncated for context]…"
    return bundle


def write_skill_file(skill_id: str, title: str, when_to_use: str, body: str) -> Path:
    safe = re.sub(r"[^\w\-]+", "-", skill_id.lower()).strip("-")[:48] or "skill"
    path = skills_root() / f"{safe}.md"
    content = (
        f"# {title.strip()}\n\n"
        f"**WHEN_TO_USE:** {when_to_use.strip()}\n\n"
        f"{body.strip()}\n"
    )
    path.write_text(content, encoding="utf-8", newline="\n")
    _index_skill(safe, title.strip(), path.name)
    # Log to memory
    log = memory_root() / "self_improve_log.md"
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    prev = log.read_text(encoding="utf-8") if log.exists() else "# Self-improve log\n\n"
    log.write_text(
        prev + f"- {stamp}: wrote skill `{safe}` — {title.strip()}\n",
        encoding="utf-8",
        newline="\n",
    )
    return path


def parse_skill_blocks(text: str) -> list[dict]:
    """Parse one or more skill proposals from the improver model."""
    blocks = re.split(r"\n(?=SKILL_ID\s*:)", text.strip(), flags=re.I)
    skills: list[dict] = []
    for block in blocks:
        if not re.search(r"SKILL_ID\s*:", block, re.I):
            continue
        def field(name: str, default: str = "") -> str:
            m = re.search(rf"^{name}\s*:\s*(.+)$", block, re.M | re.I)
            return m.group(1).strip() if m else default

        body_m = re.search(r"^BODY\s*:\s*\n(.*?)(?=\nSKILL_ID\s*:|\Z)", block, re.S | re.I | re.M)
        if not body_m:
            body_m = re.search(r"^BODY\s*:\s*\n(.*)", block, re.S | re.I | re.M)
        action = field("ACTION", "create").lower()
        if action in {"noop", "none", "skip"}:
            continue
        sid = field("SKILL_ID")
        if not sid:
            continue
        skills.append(
            {
                "id": sid,
                "action": action,
                "title": field("TITLE", sid),
                "when": field("WHEN_TO_USE", "When the task matches this skill's domain."),
                "body": (body_m.group(1).strip() if body_m else block.strip()),
            }
        )
    return skills


IMPROVER_ROLE = """You are the SELF-IMPROVEMENT engine for an offline Fable 5 agent.
You do NOT update model weights. You improve the *system*: durable skills and procedures
that will be loaded into future context windows.

Self-improving stack (offline):
1. Read memory + recent cycle outcomes.
2. Extract reusable procedures (skills), not one-off chat dumps.
3. Each skill must be actionable without the original conversation.

Output 1 to 3 skills in this exact format (repeat the block per skill):

SKILL_ID: snake_case_id
ACTION: create
TITLE: short human title
WHEN_TO_USE: one line trigger
BODY:
## Steps
1. ...
2. ...
## Checks
- ...

Rules:
- Prefer creating a skill that would have prevented a verified failure or encoded a verified win.
- Do not invent secrets or fake tool APIs.
- If nothing is worth keeping, output exactly: NO_SKILLS
- Body must be procedural, short, and checkable.
"""


SKILL_VERIFIER_ROLE = """You are a fresh-context SKILL VERIFIER.
You only see the proposed skill text — not the improver's excuses.
Judge: Is this skill reusable, specific, non-harmful, and better than having no skill?
Reply with exactly:
VERDICT: ACCEPT
or
VERDICT: REJECT
Then one line of reason.
Reject vague platitudes, duplicates of the operating manual, and uncheckable advice.
"""


def run_self_improve(
    client,
    system: str,
    *,
    focus: Optional[str] = None,
    max_skills: int = 3,
) -> list[Path]:
    """
    Self-improvement function (offline):
    reflect on memory/cycles → propose skills → fresh-context grade → write skills/.

    This is the workshop 'self-improving agents (tools, skills)' layer adapted for local models.
    """
    print(ui("╔════════════════════════════════════════════════════════════╗"))
    print(ui("║   FABLE 5 SELF-IMPROVE — skills · memory · compound        ║"))
    print(ui("╚════════════════════════════════════════════════════════════╝"))
    print(f"Platform: {PLATFORM_LABEL}  ·  Model: {MODEL_NAME}")
    print(f"Skills:   {skills_root()}")
    if focus:
        print(f"Focus:    {focus}")
    print()

    mem = read_memory_bundle(limit_chars=7000)
    existing = read_skills_bundle(limit_chars=3000) or "(no skills yet)"
    # Recent cycle files
    cycles = sorted(memory_root().glob("cycle_*.md"), key=lambda p: p.name, reverse=True)[:4]
    cycle_text = "\n\n".join(p.read_text(encoding="utf-8")[:1500] for p in cycles) or "(no cycles)"

    improve_user = (
        f"FOCUS (optional): {focus or 'general: encode durable wins and failure-preventers'}\n\n"
        f"EXISTING SKILLS:\n{existing}\n\n"
        f"MEMORY INDEX / LESSONS:\n{mem}\n\n"
        f"RECENT CYCLES (excerpts):\n{cycle_text}\n\n"
        f"Propose up to {max_skills} high-value skills. Prefer gaps not already covered."
    )
    print("[improver — propose skills]\n")
    proposal = stream_chat(
        client,
        [
            {"role": "system", "content": system + "\n\n" + IMPROVER_ROLE},
            {"role": "user", "content": improve_user},
        ],
        temperature=0.35,
        prefix="Improver: ",
    )

    if re.search(r"^\s*NO_SKILLS\s*$", proposal.strip(), re.I | re.M) or "NO_SKILLS" in proposal[:80]:
        # still try parse
        if not parse_skill_blocks(proposal):
            print(ui("\n→ No durable skills proposed this round.\n"))
            return []

    proposed = parse_skill_blocks(proposal)
    if not proposed:
        print(ui("\n→ Could not parse skill blocks; nothing written.\n"))
        return []

    written: list[Path] = []
    for i, sk in enumerate(proposed[:max_skills], 1):
        print(ui(f"\n[skill verifier — fresh context] ({i}/{min(len(proposed), max_skills)})\n"))
        skill_doc = (
            f"SKILL_ID: {sk['id']}\nTITLE: {sk['title']}\n"
            f"WHEN_TO_USE: {sk['when']}\n\n{sk['body']}"
        )
        verdict = stream_chat(
            client,
            [
                {"role": "system", "content": SKILL_VERIFIER_ROLE},
                {
                    "role": "user",
                    "content": (
                        f"Proposed skill:\n{skill_doc}\n\n"
                        f"Existing skill ids: "
                        + ", ".join(p.stem for p in list_skill_paths())
                        + "\nAccept only if this adds reusable procedure value."
                    ),
                },
            ],
            temperature=0.15,
            prefix="SkillVerifier: ",
        )
        if re.search(r"VERDICT\s*:\s*ACCEPT", verdict, re.I):
            path = write_skill_file(sk["id"], sk["title"], sk["when"], sk["body"])
            written.append(path)
            print(ui(f"  ✓ Skill accepted → {path.name}"))
        else:
            print(ui(f"  ✗ Skill rejected: {sk['id']}"))

    print(ui(f"\n→ Self-improve complete. {len(written)} skill(s) written to {skills_root()}\n"))
    if written:
        print("Active skills will load on the next prompt / loop.\n")
    return written


# -------------------- Loop harness --------------------

EXECUTOR_ROLE = """You are the EXECUTOR in a Fable 5 offline loop.
Follow the Operating Manual (especially Sections 1–8 and 9).
This cycle you do exactly ONE bounded unit of work toward the goal.
Do not finish the entire goal unless it truly fits one unit.
Do not grade yourself as final authority — a fresh verifier will grade the artifact.
Output exactly in this shape:

CYCLE: <n>
UNIT: <one sentence naming the unit>
ARTIFACT:
<the deliverable piece>
CLAIMS:
- <checkable claim 1>
- <checkable claim 2>
OPEN:
- <remaining work, or "none">
"""

ENGINEER_EXECUTOR_ROLE = """You are the MAKER in a Fable 5 LOOP ENGINEER session.
A prompt is one instruction. A loop is a goal you keep working toward without babysitting.

Protocol every cycle (PLAN → DO → VERIFY later by a separate agent):
1. PLAN  — single next step only (fix the weakest open criterion first).
2. DO    — produce or improve the work for that step only.
3. Do NOT declare FINAL yourself. A separate verifier scores criteria.

You never grade your own homework as final. Read LOOP_STATE for what already failed.

Output exactly:
CYCLE: <n>
PLAN: <one next step>
UNIT: <bounded unit name>
ARTIFACT:
<the work product>
CLAIMS:
- <checkable claim>
OPEN:
- <remaining weakness to fix next>
WEAKEST: <name the weakest criterion you are targeting this cycle>
"""

VERIFIER_ROLE = """You are the VERIFIER in a Fable 5 offline loop.
You are NOT the maker. You have a fresh context: only the goal, success condition,
artifact, and claims. You do not trust the maker's private reasoning.
For each claim: PASS, FAIL, or INSUFFICIENT — one line of evidence why.
End with exactly one of:
OVERALL: PASS
OVERALL: FAIL
OVERALL: BLOCKED
And one line: SUCCESS_MET: yes|no
And one line: SAME_FAILURE: yes|no  (true if this looks like the same failed unit as prior notes)
Be harsh on unsupported claims. Prefer evidence over eloquence.
"""

ENGINEER_VERIFIER_ROLE = """You are the CHECKER in a Fable 5 LOOP ENGINEER session (sub-agent, fresh context).
Maker is never the grader. Be brutally honest.

Score EACH success criterion 1-10. List exactly what is still weak.
Never inflate scores to be nice.

Format exactly:
CRITERION: <name or quote>
SCORE: <1-10>
WEAK: <what is missing or wrong>

(repeat for each criterion)

OVERALL: PASS or FAIL
SUCCESS_MET: yes|no   (yes only if EVERY criterion is >= MIN_SCORE given)
SAME_FAILURE: yes|no
WEAKEST: <criterion with lowest score>
MIN_SCORE_REQUIRED: <echo the min score>
"""

BILEVEL_ROLE = """You are the OUTER (bilevel) loop for Fable 5 Loop Engineer.
You do not do the task. You watch the INNER loop's search process.
If the maker keeps falling into the same priors/patterns, break the pattern.

Output exactly:
PATTERN: <stuck search pattern you observe>
FORCE_EXPLORE: <one concrete direction the next unit MUST try instead>
CONSTRAINT: <what to forbid next cycle>
"""


def parse_executor_output(text: str) -> dict:
    unit = ""
    m = re.search(r"^UNIT:\s*(.+)$", text, re.M)
    if m:
        unit = m.group(1).strip()
    plan_m = re.search(r"^PLAN:\s*(.+)$", text, re.M)
    weak_m = re.search(r"^WEAKEST:\s*(.+)$", text, re.M)
    art_m = re.search(r"ARTIFACT:\s*\n(.*?)(?=\nCLAIMS:|\Z)", text, re.S | re.I)
    claims_m = re.search(r"CLAIMS:\s*\n(.*?)(?=\nOPEN:|\nWEAKEST:|\Z)", text, re.S | re.I)
    open_m = re.search(r"OPEN:\s*\n(.*?)(?=\nWEAKEST:|\Z)", text, re.S | re.I)
    return {
        "unit": unit or "(unit not labeled)",
        "plan": (plan_m.group(1).strip() if plan_m else ""),
        "weakest": (weak_m.group(1).strip() if weak_m else ""),
        "artifact": (art_m.group(1).strip() if art_m else text.strip()),
        "claims": (claims_m.group(1).strip() if claims_m else "(no claims listed)"),
        "open": (open_m.group(1).strip() if open_m else ""),
    }


def overall_pass(verdict: str) -> bool:
    return bool(re.search(r"OVERALL:\s*PASS", verdict, re.I))


def success_met(verdict: str) -> bool:
    return bool(re.search(r"SUCCESS_MET:\s*yes", verdict, re.I))


def same_failure(verdict: str) -> bool:
    return bool(re.search(r"SAME_FAILURE:\s*yes", verdict, re.I))


def parse_criteria_scores(verdict: str) -> list[tuple[str, int]]:
    scores: list[tuple[str, int]] = []
    blocks = re.split(r"(?=^CRITERION:)", verdict, flags=re.M)
    for b in blocks:
        cm = re.search(r"^CRITERION:\s*(.+)$", b, re.M)
        sm = re.search(r"^SCORE:\s*(\d+)", b, re.M)
        if cm and sm:
            scores.append((cm.group(1).strip(), int(sm.group(1))))
    return scores


def engineer_all_clear(verdict: str, min_score: int = ENGINEER_MIN_SCORE) -> bool:
    scores = parse_criteria_scores(verdict)
    if not scores:
        return success_met(verdict) and overall_pass(verdict)
    return all(s >= min_score for _, s in scores) and success_met(verdict)


def load_program() -> str:
    path = _resolve(PROGRAM_FILE)
    if not path.is_file():
        path = SCRIPT_DIR / "program.md"
        if not path.is_file():
            path.write_text(DEFAULT_PROGRAM_MD, encoding="utf-8", newline="\n")
    if path.is_file():
        return path.read_text(encoding="utf-8")
    return DEFAULT_PROGRAM_MD


DEFAULT_PROGRAM_MD = """# program.md — Loop Engineer constraints (Karpathy-style)

You explore under these constraints. The human writes purpose once; the loop executes.

## Objective
Improve the deliverable against SUCCESS CRITERIA. Prefer one change per cycle.

## Allowed to change
- The artifact under construction (workspace or stated deliverable)
- LOOP_STATE (via harness) records of tries/failures

## Not allowed
- Weakening the success criteria to make the test pass
- Claiming success without a separate verifier gate
- Repeating a failed unit without a new strategy

## Explore
- Fix the WEAKEST criterion first
- If stuck in the same pattern twice, force a different approach (bilevel outer loop may inject this)

## Stop
- SUCCESS: every criterion ≥ min score and SUCCESS_MET: yes
- HARD LIMIT: max cycles or retry ceiling → stop and report
"""


def loop_state_path() -> Path:
    return memory_root() / "LOOP_STATE.md"


def read_loop_state() -> str:
    p = loop_state_path()
    if not p.exists():
        return "(no prior loop state — first cycle)"
    return p.read_text(encoding="utf-8")


def write_loop_state(
    *,
    goal: str,
    cycle: int,
    unit: str,
    plan: str,
    verdict: str,
    stop: Optional[str],
    tried: list[str],
    failed: list[str],
    next_action: str,
) -> None:
    """Persistent state so tomorrow's run resumes instead of starting from zero."""
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    scores = parse_criteria_scores(verdict)
    score_lines = "\n".join(f"- {n}: {s}/10" for n, s in scores) or "- (no per-criterion scores)"
    body = (
        f"# LOOP_STATE\n\n"
        f"- **Updated:** {stamp}\n"
        f"- **Goal:** {goal}\n"
        f"- **Last cycle:** {cycle}\n"
        f"- **Last unit:** {unit}\n"
        f"- **Last plan:** {plan or '(n/a)'}\n"
        f"- **Stop:** {stop or 'continue'}\n\n"
        f"## Scores (last verifier)\n{score_lines}\n\n"
        f"## Tried\n"
        + ("\n".join(f"- {t}" for t in tried[-20:]) or "- (none)")
        + "\n\n## Failed\n"
        + ("\n".join(f"- {t}" for t in failed[-20:]) or "- (none)")
        + f"\n\n## Next\n- {next_action}\n\n"
        f"## Last verifier excerpt\n```\n{verdict[:1500]}\n```\n"
    )
    loop_state_path().write_text(body, encoding="utf-8", newline="\n")


def loop_preflight_print(goal: str) -> None:
    """Honest gates: when a loop earns its cost (article checklist)."""
    print(ui("Loop preflight — a loop earns its cost only if:"))
    print("  1. Task repeats (or is high-stakes multi-step) — not a one-line Q&A")
    print("  2. Verification is automated or strict criteria (not self-cheer)")
    print("  3. Token budget can absorb re-reads / retries")
    print("  4. Agent has tools or checkable artifacts (not blind iteration)")
    print(ui(f"  Goal: {goal[:120]}"))
    print(ui("  Three make-or-break parts: VERIFIER · STATE · STOP\n"))


def run_loop(
    client,
    system: str,
    goal: str,
    *,
    success_condition: Optional[str] = None,
    max_cycles: int = DEFAULT_MAX_CYCLES,
    retry_ceiling: int = RETRY_CEILING,
    self_improve: bool = DEFAULT_SELF_IMPROVE,
    hermes: bool = False,
    engineer: bool = False,
    criteria: Optional[list[str]] = None,
    min_score: int = ENGINEER_MIN_SCORE,
) -> None:
    success_condition = success_condition or (
        "The goal is met with checkable evidence; key claims pass independent verification; "
        "remaining open items are empty or explicitly deferred with reason."
    )
    if engineer and criteria:
        success_condition = (
            success_condition
            + "\n\nSUCCESS CRITERIA (score each 1-10; all must be ≥ "
            + str(min_score)
            + "):\n"
            + "\n".join(f"- {c}" for c in criteria)
        )

    if engineer:
        title = "FABLE 5 LOOP ENGINEER — plan·do·verify·state·stop"
    elif hermes:
        title = "FABLE 5 HERMES LOOP — soul · rag · repair · stop"
    else:
        title = "FABLE 5 LOOP ENGINE — offline · maker ≠ grader"

    print(ui("╔════════════════════════════════════════════════════════════╗"))
    print(ui(f"║  {title[:56]:<56}║"))
    print(ui("╚════════════════════════════════════════════════════════════╝"))
    print(f"Platform: {PLATFORM_LABEL}")
    print(f"Model:    {MODEL_NAME}")
    mode = "ENGINEER" if engineer else ("HERMES" if hermes else "standard loop")
    print(f"Mode:     {mode}")
    print(f"Goal:     {goal}")
    print(f"Success:  {success_condition[:200]}{'…' if len(success_condition) > 200 else ''}")
    print(f"Budget:   {max_cycles} cycles · retry ceiling {retry_ceiling}")
    if engineer:
        print(f"Min score:{min_score}/10 per criterion · program: {PROGRAM_FILE}")
        print(f"Bilevel:  every {BILEVEL_EVERY} cycles" if BILEVEL_EVERY else "Bilevel:  off")
        loop_preflight_print(goal)
    if hermes:
        print(f"RAG top-K:{RAG_TOP_K}  ·  Soul: {SOUL_FILE}")
    print(f"Memory:   {memory_root()}")
    print(f"State:    {loop_state_path()}\n")

    fail_streak = 0
    prev_unit = ""
    final_stop = "budget"
    repair_patch = ""
    bilevel_patch = ""
    last_cycle = 0
    tried: list[str] = []
    failed: list[str] = []
    program = load_program() if engineer else ""

    for cycle in range(1, max_cycles + 1):
        last_cycle = cycle
        print(ui(f"{'─' * 60}"))
        print(ui(f"▶ Cycle {cycle}/{max_cycles}"))
        print(ui(f"{'─' * 60}"))
        # Hermes / engineer: smart RAG; else fuller dump
        if hermes or engineer:
            mem = retrieve_relevant_memory(
                f"{goal}\n{prev_unit}\n{success_condition}",
                top_k=RAG_TOP_K,
            )
        else:
            mem = read_memory_bundle()

        state = read_loop_state() if engineer else ""
        skills_ctx = read_skills_bundle(limit_chars=2500)
        exec_user = (
            f"GOAL:\n{goal}\n\n"
            f"SUCCESS CONDITION:\n{success_condition}\n\n"
            f"CYCLE NUMBER: {cycle} of max {max_cycles}\n"
            f"FAIL STREAK ON SIMILAR UNIT: {fail_streak}\n"
            f"PREVIOUS UNIT: {prev_unit or '(none)'}\n\n"
            f"ACTIVE SKILLS (apply if relevant):\n{skills_ctx or '(none)'}\n\n"
            f"{'RETRIEVED MEMORY (smart RAG)' if (hermes or engineer) else 'MEMORY'}:\n{mem}\n\n"
        )
        if engineer:
            exec_user += f"PROGRAM.MD (constraints):\n{program[:3000]}\n\n"
            exec_user += f"LOOP_STATE (what already tried — do not repeat blindly):\n{state}\n\n"
        if repair_patch:
            exec_user += f"LIVE REPAIR FROM PREVIOUS FAIL:\n{repair_patch}\n\n"
        if bilevel_patch:
            exec_user += f"BILEVEL OUTER LOOP (break search priors):\n{bilevel_patch}\n\n"
        if hermes and not engineer:
            exec_user += (
                "HERMES RULES: one bounded unit; stop when success is evidence-backed; "
                "do not narrate the whole archive.\n"
            )
        if engineer:
            exec_user += (
                "ENGINEER RULES: PLAN→DO only this cycle; fix WEAKEST first; "
                "never call FINAL yourself; one change preferred.\n"
            )
        exec_user += "Do ONE bounded unit now. Output in the required shape."
        print("\n[executor / maker]\n")
        role = ENGINEER_EXECUTOR_ROLE if engineer else EXECUTOR_ROLE
        exec_text = stream_chat(
            client,
            [
                {"role": "system", "content": system + "\n\n" + role},
                {"role": "user", "content": exec_user},
            ],
            prefix="Executor: ",
        )
        parsed = parse_executor_output(exec_text)
        unit = parsed["unit"]
        tried.append(f"c{cycle}: {unit}")

        # Fresh context — verifier never sees executor reasoning trail
        ver_user = (
            f"GOAL:\n{goal}\n\n"
            f"SUCCESS CONDITION / CRITERIA:\n{success_condition}\n\n"
            f"MIN_SCORE: {min_score}\n"
            f"UNIT CLAIMED:\n{unit}\n\n"
            f"ARTIFACT:\n{parsed['artifact']}\n\n"
            f"CLAIMS TO GRADE:\n{parsed['claims']}\n\n"
            f"OPEN ITEMS FROM MAKER:\n{parsed['open']}\n\n"
            f"PRIOR FAIL STREAK: {fail_streak}\n"
            f"PREVIOUS UNIT: {prev_unit or '(none)'}\n"
            "Grade only from the artifact. No benefit of the doubt. Maker is never the grader."
        )
        print("\n[verifier — fresh context / sub-agent]\n")
        vrole = ENGINEER_VERIFIER_ROLE if engineer else VERIFIER_ROLE
        verdict = stream_chat(
            client,
            [
                {"role": "system", "content": vrole},
                {"role": "user", "content": ver_user},
            ],
            temperature=0.2,
            prefix="Verifier: ",
        )

        stop_reason: Optional[str] = None
        if engineer:
            passed = overall_pass(verdict) or bool(parse_criteria_scores(verdict))
            done = engineer_all_clear(verdict, min_score)
            # Treat not-all-clear as fail for streak purposes
            if not done:
                passed = False if parse_criteria_scores(verdict) else overall_pass(verdict)
        else:
            passed = overall_pass(verdict)
            done = success_met(verdict)

        stuck = same_failure(verdict) or (
            bool(prev_unit)
            and unit.lower()[:50] == prev_unit.lower()[:50]
            and not done
        )

        if done:
            stop_reason = "success"
            fail_streak = 0
            repair_patch = ""
            bilevel_patch = ""
            next_action = "Goal met. Stop."
        elif not done and (not passed or engineer):
            fail_streak = fail_streak + 1 if stuck or fail_streak > 0 else 1
            if not stuck and prev_unit and unit.lower()[:50] != prev_unit.lower()[:50]:
                fail_streak = 1
            failed.append(f"c{cycle}: {unit}")
            if fail_streak >= retry_ceiling:
                stop_reason = "retry_ceiling"
                next_action = "Escalate to human — same unit not converging."
            else:
                next_action = parsed.get("open") or "Fix weakest criterion next cycle."
                if hermes or engineer:
                    try:
                        repair_patch = live_repair(
                            client,
                            goal=goal,
                            unit=unit,
                            artifact=parsed["artifact"],
                            verdict=verdict,
                            fail_streak=fail_streak,
                        )
                    except Exception as e:
                        repair_patch = f"(repair failed: {e})"
                # Bilevel outer loop: meta-search when stuck in patterns
                if engineer and BILEVEL_EVERY > 0 and cycle % BILEVEL_EVERY == 0:
                    print(ui("\n[bilevel outer loop — meta-search]\n"))
                    try:
                        bilevel_patch = stream_chat(
                            client,
                            [
                                {"role": "system", "content": BILEVEL_ROLE},
                                {
                                    "role": "user",
                                    "content": (
                                        f"GOAL: {goal}\nCYCLE: {cycle}\n"
                                        f"TRIED:\n" + "\n".join(tried[-12:]) + "\n"
                                        f"FAILED:\n" + "\n".join(failed[-12:]) + "\n"
                                        f"LAST VERDICT:\n{verdict[:2000]}\n"
                                        f"STATE:\n{state[:2000]}\n"
                                    ),
                                },
                            ],
                            temperature=0.4,
                            prefix="Bilevel: ",
                        )
                    except Exception as e:
                        bilevel_patch = f"(bilevel failed: {e})"
        else:
            fail_streak = 0
            repair_patch = ""
            next_action = "Continue toward remaining open items."

        append_cycle_log(
            cycle,
            goal,
            unit,
            parsed["artifact"],
            parsed["claims"],
            verdict,
            stop_reason,
        )
        maybe_write_lesson(client, system, goal, cycle, verdict, parsed["artifact"])
        if engineer or hermes:
            write_loop_state(
                goal=goal,
                cycle=cycle,
                unit=unit,
                plan=parsed.get("plan", ""),
                verdict=verdict,
                stop=stop_reason,
                tried=tried,
                failed=failed,
                next_action=next_action,
            )
        prev_unit = unit

        if stop_reason == "success":
            final_stop = "success"
            print(ui("\n✓ Loop self-stopped: success condition met (verifier gate).\n"))
            break
        if stop_reason == "retry_ceiling":
            final_stop = "retry_ceiling"
            print(
                ui(
                    f"\n✗ Loop self-stopped: retry ceiling ({retry_ceiling}). "
                    "Escalate to a human — same unit is not converging.\n"
                )
            )
            break
        if cycle == max_cycles:
            final_stop = "budget"
            print(ui(f"\n⏸ Loop self-stopped: hard limit {max_cycles} cycles — report and stop.\n"))
        else:
            print(ui(f"\n→ ITERATING. Fail streak={fail_streak}. Continuing…\n"))

    # Final synthesis for the human
    print(ui(f"{'─' * 60}"))
    print("[final report for human]")
    print(ui(f"{'─' * 60}\n"))
    mem = read_memory_bundle(limit_chars=8000)
    report_user = (
        f"The loop ended with stop reason: {final_stop}.\n"
        f"GOAL: {goal}\nSUCCESS CONDITION: {success_condition}\n\n"
        f"MEMORY / CYCLE LOGS:\n{mem}\n\n"
        "Write a human-facing report: (1) verdict first, (2) what was accomplished, "
        "(3) what remains, (4) concrete risks, (5) recommended next unit if not done. "
        "Follow Section 7 answer-first style."
    )
    stream_chat(
        client,
        [
            {"role": "system", "content": system},
            {"role": "user", "content": report_user},
        ],
        prefix="Fable5: ",
    )

    # Hermes: compress memory after multi-cycle runs
    if hermes and last_cycle >= 2:
        try:
            compress_memory(client, system, focus=f"goal={goal[:120]} stop={final_stop}")
        except Exception as e:
            print(ui(f"⚠️  Memory compress skipped: {e}\n"))

    # Self-improvement: encode durable skills from this run (workshop layer 5)
    if self_improve:
        print(ui("\n[self-improve after loop]\n"))
        try:
            run_self_improve(
                client,
                load_system_prompt(hermes=hermes),
                focus=f"Lessons from goal: {goal[:200]} (stop={final_stop})",
            )
        except Exception as e:
            print(ui(f"⚠️  Self-improve skipped: {e}\n"))


# -------------------- Build + Automate (course: BUILD and AUTOMATE) --------------------


def workflows_root() -> Path:
    root = WORKFLOWS_DIR if WORKFLOWS_DIR.is_absolute() else SCRIPT_DIR / WORKFLOWS_DIR
    root = root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    return root


def workspace_root() -> Path:
    root = WORKSPACE_DIR if WORKSPACE_DIR.is_absolute() else SCRIPT_DIR / WORKSPACE_DIR
    root = root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    return root


def ensure_default_workflows() -> None:
    """Seed example automation recipes if missing."""
    root = workflows_root()
    samples = {
        "hello-project.json": {
            "name": "hello-project",
            "description": "Scaffold a tiny multi-file hello project under workspace/",
            "steps": [
                {
                    "type": "build",
                    "goal": "Create a minimal multi-file hello CLI: README, main.py, requirements.txt",
                },
                {"type": "note", "text": "Open workspace/ and run the generated main if present."},
            ],
        },
        "daily-review.json": {
            "name": "daily-review",
            "description": "Compress memory, then self-improve skills from recent work",
            "steps": [
                {"type": "compress", "focus": "daily durable lessons and open risks"},
                {"type": "improve", "focus": "procedures that prevented failures this week"},
            ],
        },
        "rigor-check.json": {
            "name": "rigor-check",
            "description": "Hermes loop: re-derive a numeric claim then stop",
            "steps": [
                {
                    "type": "hermes",
                    "goal": "Re-derive: revenue grew from $4.0M to $4.2M, a 20% gain. Verdict first.",
                    "max_cycles": 3,
                }
            ],
        },
    }
    for name, data in samples.items():
        path = root / name
        if not path.exists():
            path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")


BUILD_ROLE = """You are the BUILD engine for Fable 5 Offline (course skill: BUILD anything).
Produce a complete, multi-file project scaffold the user can run offline.

Output EXACTLY in this machine-parseable format (repeat FILE blocks):

PLAN:
- bullet goals and how to run

FILE: relative/path.ext
```
file contents here
```

FILE: another/path.ext
```
more contents
```

DONE: one-line summary

Rules:
- Prefer small, complete, runnable scaffolds
- Use relative paths only (no absolute paths, no ..)
- Do not invent secrets or network credentials
- Include a README with run instructions for Windows, macOS, and Linux when useful
- Max ~12 files unless the goal truly needs more
"""


def parse_build_files(text: str) -> tuple[str, list[tuple[str, str]], str]:
    """Return (plan, [(relpath, content), ...], done)."""
    plan_m = re.search(r"^PLAN:\s*\n(.*?)(?=^FILE:|\Z)", text, re.M | re.S)
    plan = plan_m.group(1).strip() if plan_m else ""
    done_m = re.search(r"^DONE:\s*(.+)$", text, re.M)
    done = done_m.group(1).strip() if done_m else ""
    files: list[tuple[str, str]] = []
    for m in re.finditer(
        r"^FILE:\s*(.+?)\s*\n```(?:\w+)?\n(.*?)```",
        text,
        re.M | re.S,
    ):
        rel = m.group(1).strip().lstrip("./").replace("\\", "/")
        if ".." in rel.split("/") or rel.startswith("/") or re.match(r"^[A-Za-z]:", rel):
            continue
        files.append((rel, m.group(2)))
    return plan, files, done


def safe_workspace_path(base: Path, rel: str) -> Optional[Path]:
    rel = rel.strip().lstrip("/").replace("\\", "/")
    if not rel or ".." in Path(rel).parts:
        return None
    target = (base / rel).resolve()
    try:
        target.relative_to(base.resolve())
    except ValueError:
        return None
    return target


def run_build(client, system: str, goal: str, *, name: Optional[str] = None) -> Path:
    """
    BUILD behavior: plan + write multi-file scaffold under workspace/.
    Offline, local disk only — no cloud deploy.
    """
    ensure_default_workflows()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    slug = re.sub(r"[^\w\-]+", "-", (name or goal[:40]).lower()).strip("-")[:40] or "build"
    out_dir = workspace_root() / f"build-{slug}-{stamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(ui("╔════════════════════════════════════════════════════════════╗"))
    print(ui("║   FABLE 5 BUILD — scaffold · multi-file · offline          ║"))
    print(ui("╚════════════════════════════════════════════════════════════╝"))
    print(f"Goal:      {goal}")
    print(f"Workspace: {out_dir}\n")

    mem = retrieve_relevant_memory(goal, top_k=min(10, RAG_TOP_K), limit_chars=3000)
    skills = read_skills_bundle(limit_chars=2000)
    print("[builder]\n")
    raw = stream_chat(
        client,
        [
            {"role": "system", "content": system + "\n\n" + BUILD_ROLE},
            {
                "role": "user",
                "content": (
                    f"BUILD GOAL:\n{goal}\n\n"
                    f"RELEVANT MEMORY:\n{mem}\n\n"
                    f"SKILLS:\n{skills or '(none)'}\n\n"
                    "Produce PLAN + FILE blocks + DONE."
                ),
            },
        ],
        temperature=0.35,
        prefix="Build: ",
    )
    plan, files, done = parse_build_files(raw)
    if plan:
        (out_dir / "PLAN.md").write_text(f"# Build plan\n\n{plan}\n", encoding="utf-8", newline="\n")
    written: list[str] = []
    for rel, content in files:
        path = safe_workspace_path(out_dir, rel)
        if not path:
            print(ui(f"  ✗ skipped unsafe path: {rel}"))
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        written.append(rel)
        print(ui(f"  ✓ wrote {rel}"))

    # Project instructions (CLAUDE.md-style) for follow-on agent work
    proj = out_dir / "PROJECT.md"
    proj.write_text(
        f"# Project\n\n"
        f"- **Goal:** {goal}\n"
        f"- **Built:** {stamp} UTC\n"
        f"- **Done:** {done or '(see PLAN.md)'}\n"
        f"- **Files:** {', '.join(written) if written else '(none parsed — see raw below)'}\n\n"
        f"## Raw builder output\n\n```\n{raw[:8000]}\n```\n",
        encoding="utf-8",
        newline="\n",
    )
    if not written:
        (out_dir / "BUILD_RAW.md").write_text(raw, encoding="utf-8", newline="\n")
        print(ui("  ⚠ no FILE blocks parsed — saved BUILD_RAW.md"))

    log = memory_root() / "build_log.md"
    prev = log.read_text(encoding="utf-8") if log.exists() else "# Build log\n\n"
    log.write_text(
        prev + f"- {stamp}: `{out_dir.name}` — {goal[:100]} ({len(written)} files)\n",
        encoding="utf-8",
        newline="\n",
    )
    print(ui(f"\n✓ Build complete → {out_dir}\n"))
    return out_dir


# Shell allowlist prefixes (automation). Only used when ALLOW_SHELL is true.
_SHELL_ALLOW = (
    "python ",
    "python3 ",
    "py -3 ",
    "pip ",
    "pip3 ",
    "python -m ",
    "python3 -m ",
    "ollama ",
    "git status",
    "git log",
    "git diff",
    "git branch",
    "dir",
    "ls",
    "echo ",
    "type ",
    "cat ",
    "where ",
    "which ",
)


def shell_allowed(cmd: str) -> bool:
    c = cmd.strip()
    low = c.lower()
    if not c or "|" in c or ";" in c or "&" in c or "`" in c or "$(" in c:
        # keep pipelines simple / block chaining for safety
        if "|" in c or ";" in c or "&&" in c or "||" in c:
            return False
    return any(low.startswith(p) or low == p.strip() for p in _SHELL_ALLOW)


def run_shell_step(cmd: str, *, cwd: Path) -> str:
    if not ALLOW_SHELL:
        return f"[dry-run] shell disabled (set FABLE5_ALLOW_SHELL=1). would run: {cmd}"
    if not shell_allowed(cmd):
        return f"[blocked] command not on allowlist: {cmd}"
    try:
        proc = subprocess.run(
            cmd,
            shell=True,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=120,
            encoding="utf-8",
            errors="replace",
        )
        out = (proc.stdout or "") + (proc.stderr or "")
        return f"exit={proc.returncode}\n{out[:4000]}"
    except Exception as e:
        return f"[error] {e}"


def load_workflow(name_or_path: str) -> dict[str, Any]:
    ensure_default_workflows()
    p = Path(name_or_path)
    if not p.is_file():
        cand = workflows_root() / name_or_path
        if not cand.suffix:
            cand = workflows_root() / f"{name_or_path}.json"
        p = cand
    if not p.is_file():
        raise FileNotFoundError(f"Workflow not found: {name_or_path} (looked in {workflows_root()})")
    return json.loads(p.read_text(encoding="utf-8"))


def list_workflows() -> list[Path]:
    ensure_default_workflows()
    return sorted(workflows_root().glob("*.json"))


def run_automate(
    client,
    system: str,
    workflow_name: str,
    *,
    extra_goal: Optional[str] = None,
) -> None:
    """
    AUTOMATE behavior: run a multi-step workflow recipe (JSON).
    Steps: build | hermes | loop | improve | compress | shell | note | llm
    """
    wf = load_workflow(workflow_name)
    name = wf.get("name", workflow_name)
    steps = wf.get("steps") or []
    print(ui("╔════════════════════════════════════════════════════════════╗"))
    print(ui("║   FABLE 5 AUTOMATE — recipe · pipeline · offline           ║"))
    print(ui("╚════════════════════════════════════════════════════════════╝"))
    print(f"Workflow: {name}")
    print(f"Desc:     {wf.get('description', '')}")
    print(f"Steps:    {len(steps)}")
    print(f"Shell:    {'ENABLED' if ALLOW_SHELL else 'dry-run (FABLE5_ALLOW_SHELL=0)'}\n")

    results: list[str] = []
    for i, step in enumerate(steps, 1):
        stype = (step.get("type") or "note").lower()
        print(ui(f"{'─' * 60}"))
        print(ui(f"▶ Step {i}/{len(steps)} · type={stype}"))
        print(ui(f"{'─' * 60}"))
        try:
            if stype == "build":
                goal = step.get("goal") or extra_goal or "scaffold a minimal project"
                out = run_build(client, system, goal, name=step.get("name"))
                results.append(f"build → {out}")
            elif stype == "engineer":
                goal = step.get("goal") or extra_goal or "complete the engineered goal"
                crit = step.get("criteria")
                if isinstance(crit, str):
                    crit = [c.strip() for c in crit.split(",") if c.strip()]
                run_loop(
                    client,
                    load_system_prompt(hermes=True),
                    goal,
                    success_condition=step.get("success"),
                    max_cycles=int(step.get("max_cycles", DEFAULT_MAX_CYCLES)),
                    hermes=True,
                    engineer=True,
                    criteria=crit,
                    min_score=int(step.get("min_score", ENGINEER_MIN_SCORE)),
                    self_improve=bool(step.get("self_improve", False)),
                )
                results.append("engineer → done")
            elif stype == "hermes":
                goal = step.get("goal") or extra_goal or "complete the automated goal"
                run_loop(
                    client,
                    load_system_prompt(hermes=True),
                    goal,
                    success_condition=step.get("success"),
                    max_cycles=int(step.get("max_cycles", DEFAULT_MAX_CYCLES)),
                    hermes=True,
                    self_improve=bool(step.get("self_improve", False)),
                )
                results.append(f"hermes → done")
            elif stype == "loop":
                goal = step.get("goal") or extra_goal or "complete the automated goal"
                run_loop(
                    client,
                    system,
                    goal,
                    success_condition=step.get("success"),
                    max_cycles=int(step.get("max_cycles", DEFAULT_MAX_CYCLES)),
                    hermes=False,
                    self_improve=bool(step.get("self_improve", False)),
                )
                results.append("loop → done")
            elif stype == "improve":
                run_self_improve(client, system, focus=step.get("focus") or extra_goal)
                results.append("improve → done")
            elif stype == "compress":
                compress_memory(client, system, focus=step.get("focus") or extra_goal)
                results.append("compress → done")
            elif stype == "team":
                task = step.get("task") or step.get("goal") or extra_goal or "complete the team task"
                run_team(
                    client,
                    system,
                    task,
                    output_format=step.get("format", "report"),
                    max_revisions=int(step.get("max_revisions", 3)),
                )
                results.append("team → done")
            elif stype == "hitl":
                action = step.get("action") or step.get("text") or "continue workflow"
                if not hitl_approve(action, step.get("detail", "")):
                    results.append(f"HITL DENIED → {action[:60]}")
                    if step.get("stop_on_deny", True):
                        print(ui("\nAutomation stopped (HITL denied).\n"))
                        break
                else:
                    results.append(f"HITL APPROVED → {action[:60]}")
            elif stype == "shell":
                cmd = step.get("command") or step.get("cmd") or "echo hello"
                if not hitl_approve(f"shell: {cmd}", "Allowlisted only if FABLE5_ALLOW_SHELL=1"):
                    results.append(f"shell DENIED → {cmd[:60]}")
                    if step.get("stop_on_error", True):
                        break
                    continue
                out = run_shell_step(cmd, cwd=workspace_root())
                print(out)
                results.append(f"shell → {cmd[:60]}")
            elif stype == "llm":
                prompt = step.get("prompt") or extra_goal or "Summarize current memory."
                print("\n[llm step]\n")
                ans = stream_chat(
                    client,
                    [
                        {"role": "system", "content": system},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="Auto: ",
                )
                results.append(f"llm → {len(ans)} chars")
            elif stype == "note":
                text = step.get("text") or step.get("message") or ""
                print(text)
                results.append(f"note → {text[:60]}")
            else:
                print(ui(f"⚠ unknown step type: {stype}"))
                results.append(f"skip → {stype}")
        except Exception as e:
            print(ui(f"❌ step failed: {e}"))
            results.append(f"FAIL {stype}: {e}")
            if step.get("stop_on_error", True):
                print(ui("\nAutomation stopped (stop_on_error).\n"))
                break

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    log = memory_root() / "automate_log.md"
    prev = log.read_text(encoding="utf-8") if log.exists() else "# Automate log\n\n"
    log.write_text(
        prev
        + f"\n## {stamp} · {name}\n"
        + "\n".join(f"- {r}" for r in results)
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(ui(f"\n✓ Automation finished: {name}\n"))


# -------------------- Multi-agent team + HITL (roadmap stages 6–7) --------------------


def hitl_approve(action: str, detail: str = "") -> bool:
    """Human-in-the-loop gate. Returns True if approved (or HITL disabled)."""
    if not HITL:
        return True
    print(ui(f"\n⏸ HITL approval required: {action}"))
    if detail:
        print(detail[:500])
    try:
        ans = input("Approve? [y/N]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return False
    ok = ans in {"y", "yes"}
    log = memory_root() / "hitl_log.md"
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    prev = log.read_text(encoding="utf-8") if log.exists() else "# HITL audit log\n\n"
    log.write_text(
        prev + f"- {stamp}: {'APPROVED' if ok else 'DENIED'} — {action}\n",
        encoding="utf-8",
        newline="\n",
    )
    return ok


def run_team(client, system: str, task: str, *, output_format: str = "report", max_revisions: int = 3) -> str:
    """
    Multi-agent supervisor: research → write → critic (Stage 6).
    Critic is a separate call (maker ≠ grader). Max revision loops.
    """
    print(ui("╔════════════════════════════════════════════════════════════╗"))
    print(ui("║   FABLE 5 TEAM — research · write · critic (supervisor)    ║"))
    print(ui("╚════════════════════════════════════════════════════════════╝"))
    print(f"Task:   {task}")
    print(f"Format: {output_format}")
    print(f"HITL:   {'on' if HITL else 'off'}\n")

    if not hitl_approve("start multi-agent team run", task):
        print(ui("Team run cancelled by human.\n"))
        return ""

    # Research specialist
    print(ui("→ Research agent…\n"))
    research = stream_chat(
        client,
        [
            {
                "role": "system",
                "content": (
                    system
                    + "\n\nYou are the RESEARCH specialist. Find facts, structure, risks, unknowns. "
                    "Be thorough. Label guesses. Do not write the final deliverable."
                ),
            },
            {"role": "user", "content": f"Research for this task:\n{task}"},
        ],
        temperature=0.4,
        prefix="Research: ",
    )

    content = ""
    for attempt in range(1, max_revisions + 1):
        print(ui(f"→ Writer agent (attempt {attempt}/{max_revisions})…\n"))
        write_prompt = (
            f"Task: {task}\nDesired format: {output_format}\n\n"
            f"Research notes:\n{research}\n\n"
            "Write the deliverable. Verdict/lead first when appropriate."
        )
        if content:
            write_prompt += f"\n\nPrevious draft to revise:\n{content}\n"
        content = stream_chat(
            client,
            [
                {
                    "role": "system",
                    "content": (
                        system
                        + "\n\nYou are the WRITER specialist. Turn research into clear deliverable. "
                        "Do not invent sources."
                    ),
                },
                {"role": "user", "content": write_prompt},
            ],
            temperature=0.45,
            prefix="Writer: ",
        )

        print(ui(f"→ Critic agent (fresh context, attempt {attempt})…\n"))
        review = stream_chat(
            client,
            [
                {
                    "role": "system",
                    "content": (
                        "You are the CRITIC. Fresh context. Maker is never the grader.\n"
                        "Return exactly:\n"
                        "APPROVED: yes|no\n"
                        "ISSUES:\n- ...\n"
                        "SUGGESTIONS:\n- ...\n"
                        "SCORE: <1-10>\n"
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"TASK:\n{task}\n\nFORMAT:\n{output_format}\n\n"
                        f"DRAFT:\n{content}\n\n"
                        "Approve only if ready to ship without follow-up on critical issues."
                    ),
                },
            ],
            temperature=0.2,
            prefix="Critic: ",
        )
        approved = bool(re.search(r"APPROVED:\s*yes", review, re.I))
        if approved:
            print(ui("\n✓ Critic approved. Supervisor done.\n"))
            break
        print(ui(f"\n✗ Not approved — revising (attempt {attempt})…\n"))
        # Feed issues into next writer via content already set; research stays fixed
    else:
        print(ui("\n⚠ Max revisions reached — returning best attempt.\n"))

    if HITL and not hitl_approve("ship team deliverable", content[:400]):
        print(ui("Deliverable held — human denied ship.\n"))
        return content

    # Persist episode
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    out = workspace_root() / f"team-{stamp}.md"
    out.write_text(
        f"# Team run {stamp}\n\n## Task\n{task}\n\n## Research\n{research}\n\n"
        f"## Deliverable\n{content}\n\n## Last critic\n{review}\n",
        encoding="utf-8",
        newline="\n",
    )
    print(ui(f"Saved → {out}\n"))
    return content


def show_roadmap() -> None:
    path = _resolve(ROADMAP_FILE)
    if not path.is_file():
        path = SCRIPT_DIR / "ROADMAP.md"
    if path.is_file():
        print(path.read_text(encoding="utf-8"))
    else:
        print("ROADMAP.md not found.")


# -------------------- Chat REPL --------------------


def print_banner() -> None:
    print(ui("╔════════════════════════════════════════════════════════════╗"))
    print(ui("║  FABLE 5 OFFLINE — agentic engineer · loops · team · build ║"))
    print(ui("║  soul · RAG · verifier · skills · HITL · maker ≠ grader    ║"))
    print(ui("╚════════════════════════════════════════════════════════════╝"))
    print(ui(f"Platform: {PLATFORM_LABEL}  ·  Model: {MODEL_NAME}"))
    print(f"Manual:   {_resolve(SYSTEM_PROMPT_FILE).name}  ·  Soul: {SOUL_FILE}")
    print(f"Skills:   {len(list_skill_paths())}  ·  Shell: {'on' if ALLOW_SHELL else 'off'}  ·  HITL: {'on' if HITL else 'off'}")
    print("Commands: /team /build /automate /engineer /loop /hermes /roadmap /help quit\n")


def print_help() -> None:
    py = "python" if IS_WINDOWS else "python3"
    print(
        f"""
Commands
  /roadmap           6-month agentic engineer roadmap (ROADMAP.md)
  /team <task>       Multi-agent: research → write → critic (supervisor)
  /build <goal>      BUILD multi-file scaffold under workspace/
  /automate <name>   Run workflow recipe from workflows/*.json
  /workflows         List automation recipes
  /loop <goal>       Standard loop (executor + fresh verifier + memory)
  /engineer <goal>   Loop engineer: PLAN→DO→VERIFY · STATE · STOP
  /hermes <goal>     Hermes loop: SOUL + smart RAG + live repair + self-stop
  /improve [focus]   Self-improve: propose skills, verify, write skills/
  /skills            List skill library
  /soul              Show SOUL.md identity file
  /memory            Print memory index (full)
  /compress [focus]  Compress memory into a durable lesson note
  /doctor            Check Python, deps, Ollama backend
  /help              This help
  quit | exit | q    Leave

Agentic engineer stack (offline)
  Roadmap — 12 stages / 6 months (build real things, order matters)
  Team    — multi-agent supervisor (Stage 6)
  HITL    — human approval gates (Stage 7); FABLE5_HITL=0 to disable
  Shell   — only if FABLE5_ALLOW_SHELL=1 and allowlisted

CLI
  {py} fable5_offline_agent.py --roadmap
  {py} fable5_offline_agent.py --team "Research X and write a one-page brief"
  {py} fable5_offline_agent.py --build "tiny flask hello app"
  {py} fable5_offline_agent.py --automate agentic-checkpoint
  {py} fable5_offline_agent.py --engineer "…" --criteria "…"
  {py} fable5_offline_agent.py --doctor

Env
  FABLE5_MODEL  FABLE5_SOUL  FABLE5_PROGRAM  FABLE5_ROADMAP  FABLE5_HITL
  FABLE5_ENGINEER_MIN_SCORE  FABLE5_BILEVEL_EVERY  FABLE5_RAG_TOP_K
  FABLE5_WORKFLOWS  FABLE5_WORKSPACE  FABLE5_ALLOW_SHELL  FABLE5_MEMORY  FABLE5_SKILLS
"""
    )


def refresh_chat_system(messages: list[dict]) -> list[dict]:
    """Reload manual + skills into the system message (after /improve)."""
    new_system = load_system_prompt()
    if messages and messages[0].get("role") == "system":
        messages[0] = {"role": "system", "content": new_system}
    else:
        messages.insert(0, {"role": "system", "content": new_system})
    return messages


def chat_repl(client, system: str) -> None:
    print_banner()
    messages: list[dict] = [{"role": "system", "content": system}]
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nCaught ya. Shutting down cleanly.")
            break

        if not user_input:
            continue
        low = user_input.lower()
        if low in {"quit", "exit", "q"}:
            print("\nRighto, catch ya later. Agent shutting down.")
            break
        if low in {"/help", "help", "?"}:
            print_help()
            continue
        if low in {"/doctor", "doctor"}:
            doctor()
            print()
            continue
        if low in {"/roadmap", "roadmap"}:
            show_roadmap()
            print()
            continue
        if low.startswith("/team"):
            task = user_input[5:].strip()
            if not task:
                task = input("Team task: ").strip()
            if not task:
                print("No task — cancelled.\n")
                continue
            try:
                run_team(client, load_system_prompt(), task)
            except Exception as e:
                print(ui(f"\n❌ Team error: {e}\n"))
            continue
        if low == "/memory":
            print(read_memory_bundle(limit_chars=12000))
            print()
            continue
        if low in {"/soul", "soul"}:
            print(load_soul())
            print()
            continue
        if low.startswith("/compress"):
            focus = user_input[9:].strip() or None
            try:
                compress_memory(client, load_system_prompt(), focus=focus)
            except Exception as e:
                print(ui(f"\n❌ Compress error: {e}\n"))
            continue
        if low in {"/skills", "skills"}:
            paths = list_skill_paths()
            if not paths:
                print("(no skills yet — run /improve)\n")
            else:
                print(f"Skills in {skills_root()}:\n")
                for p in paths:
                    print(f"  - {p.stem}  ({p.name})")
                print()
                print(read_skills_bundle(limit_chars=8000))
                print()
            continue
        if low in {"/workflows", "workflows"}:
            ensure_default_workflows()
            wfs = list_workflows()
            print(f"Workflows in {workflows_root()}:\n")
            for p in wfs:
                try:
                    data = json.loads(p.read_text(encoding="utf-8"))
                    print(f"  - {p.stem}: {data.get('description', '')[:80]}")
                except Exception:
                    print(f"  - {p.name}")
            print()
            continue
        if low.startswith("/build"):
            goal = user_input[6:].strip()
            if not goal:
                goal = input("Build goal: ").strip()
            if not goal:
                print("No goal — cancelled.\n")
                continue
            try:
                run_build(client, load_system_prompt(), goal)
            except Exception as e:
                print(ui(f"\n❌ Build error: {e}\n"))
            continue
        if low.startswith("/automate"):
            name = user_input[9:].strip()
            if not name:
                name = input("Workflow name (e.g. daily-review): ").strip()
            if not name:
                print("No workflow — cancelled.\n")
                continue
            try:
                run_automate(client, load_system_prompt(), name)
                messages = refresh_chat_system(messages)
            except Exception as e:
                print(ui(f"\n❌ Automate error: {e}\n"))
            continue
        if low.startswith("/improve"):
            focus = user_input[8:].strip() or None
            try:
                run_self_improve(client, load_system_prompt(), focus=focus)
                messages = refresh_chat_system(messages)
                print("Chat system prompt reloaded with updated skills.\n")
            except Exception as e:
                print(ui(f"\n❌ Improve error: {e}\n"))
            continue
        if low.startswith("/hermes"):
            goal = user_input[7:].strip()
            if not goal:
                goal = input("Hermes goal: ").strip()
            if not goal:
                print("No goal — cancelled.\n")
                continue
            try:
                run_loop(
                    client,
                    load_system_prompt(hermes=True),
                    goal,
                    hermes=True,
                )
                messages = refresh_chat_system(messages)
            except Exception as e:
                print(ui(f"\n❌ Hermes error: {e}\n"))
            print("Back to chat. Try /hermes, /engineer, /loop, or /improve.\n")
            continue
        if low.startswith("/engineer"):
            goal = user_input[9:].strip()
            if not goal:
                goal = input("Engineer goal: ").strip()
            if not goal:
                print("No goal — cancelled.\n")
                continue
            crit_raw = input(
                "Success criteria (comma-separated, or Enter for defaults): "
            ).strip()
            criteria = (
                [c.strip() for c in crit_raw.split(",") if c.strip()]
                if crit_raw
                else None
            )
            try:
                run_loop(
                    client,
                    load_system_prompt(hermes=True),
                    goal,
                    hermes=True,
                    engineer=True,
                    criteria=criteria,
                    min_score=ENGINEER_MIN_SCORE,
                )
                messages = refresh_chat_system(messages)
            except Exception as e:
                print(ui(f"\n❌ Engineer error: {e}\n"))
            print("Back to chat. Try /engineer, /hermes, or /build.\n")
            continue
        if low.startswith("/loop"):
            goal = user_input[5:].strip()
            if not goal:
                goal = input("Loop goal: ").strip()
            if not goal:
                print("No goal — cancelled.\n")
                continue
            try:
                run_loop(client, load_system_prompt(), goal, hermes=False)
                messages = refresh_chat_system(messages)
            except Exception as e:
                print(ui(f"\n❌ Loop error: {e}\n"))
            print("Back to chat. Type another question, /improve, /hermes, or /loop.\n")
            continue

        # Chat: store clean user text; inject smart RAG only for this call
        rag = retrieve_relevant_memory(user_input, top_k=min(8, RAG_TOP_K), limit_chars=2500)
        enriched = user_input
        if rag and "(no memory yet)" not in rag:
            enriched = (
                f"{user_input}\n\n---\nRelevant memory (smart RAG, optional):\n{rag}"
            )
        messages.append({"role": "user", "content": user_input})
        api_messages = messages[:-1] + [{"role": "user", "content": enriched}]
        print(ui("\nThinking… (Fable 5 mode)\n"))
        try:
            full = stream_chat(client, api_messages, prefix="Fable5: ")
            messages.append({"role": "assistant", "content": full})
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            print("Make sure Ollama is running and the model is pulled.")
            print(f"Try: ollama run {MODEL_NAME}")
            messages.pop()
            break


def main(argv: Optional[list[str]] = None) -> int:
    configure_stdio()

    parser = argparse.ArgumentParser(
        description="Fable 5 Offline Agent — chat, build, automate, loops, hermes "
        f"({PLATFORM_LABEL})"
    )
    parser.add_argument("--loop", metavar="GOAL", help="Run loop mode with this goal, then exit")
    parser.add_argument(
        "--hermes",
        metavar="GOAL",
        help="Hermes loop: SOUL + smart RAG + live repair + self-stop + compress",
    )
    parser.add_argument(
        "--build",
        metavar="GOAL",
        help="BUILD multi-file scaffold under workspace/",
    )
    parser.add_argument(
        "--automate",
        metavar="WORKFLOW",
        help="Run automation recipe (name or path under workflows/)",
    )
    parser.add_argument(
        "--engineer",
        metavar="GOAL",
        help="Loop like an engineer: PLAN→DO→VERIFY, LOOP_STATE, stop gates, optional bilevel",
    )
    parser.add_argument(
        "--team",
        metavar="TASK",
        help="Multi-agent supervisor: research → write → critic",
    )
    parser.add_argument(
        "--format",
        default="report",
        help="Output format for --team (default: report)",
    )
    parser.add_argument(
        "--roadmap",
        action="store_true",
        help="Print the 6-month agentic engineer roadmap",
    )
    parser.add_argument(
        "--criteria",
        metavar="LIST",
        help="Comma-separated success criteria for --engineer (scored 1-10)",
    )
    parser.add_argument(
        "--min-score",
        type=int,
        default=ENGINEER_MIN_SCORE,
        help=f"Min score per criterion for --engineer (default {ENGINEER_MIN_SCORE})",
    )
    parser.add_argument("--success", metavar="COND", help="Checkable success condition for --loop/--hermes")
    parser.add_argument("--max-cycles", type=int, default=DEFAULT_MAX_CYCLES)
    parser.add_argument("--retry-ceiling", type=int, default=RETRY_CEILING)
    parser.add_argument("--model", help="Override MODEL_NAME")
    parser.add_argument(
        "--compress-memory",
        nargs="?",
        const="",
        default=None,
        metavar="FOCUS",
        help="Compress memory archive into a durable lesson note",
    )
    parser.add_argument(
        "--improve",
        nargs="?",
        const="",
        default=None,
        metavar="FOCUS",
        help="Run self-improve (optional focus text), write skills/, then exit",
    )
    parser.add_argument(
        "--self-improve",
        action="store_true",
        default=None,
        help="After --loop, run self-improve (default on unless disabled)",
    )
    parser.add_argument(
        "--no-self-improve",
        action="store_true",
        help="After --loop, skip self-improve skill writing",
    )
    parser.add_argument(
        "--doctor",
        action="store_true",
        help="Check OS, Python, dependencies, and Ollama/API health",
    )
    parser.add_argument(
        "--ascii",
        action="store_true",
        help="Force ASCII UI (also: set FABLE5_ASCII=1)",
    )
    args = parser.parse_args(argv)

    global MODEL_NAME, USE_ASCII
    if args.model:
        MODEL_NAME = args.model
    if args.ascii:
        USE_ASCII = True

    try:
        os.chdir(SCRIPT_DIR)
    except OSError:
        pass

    # Ensure dirs exist early
    skills_root()
    ensure_default_workflows()
    workspace_root()

    if args.doctor:
        return doctor()

    if args.roadmap:
        show_roadmap()
        return 0

    system = load_system_prompt()
    client = make_client()

    ok, msg = check_backend()
    if not ok:
        print(ui(f"⚠️  {msg}"))
        print("  Run with --doctor for a full multi-platform check.")
        print(f"  Then: ollama pull {MODEL_NAME}  (if using Ollama)\n")

    if args.team:
        try:
            run_team(client, system, args.team, output_format=args.format)
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.build:
        try:
            run_build(client, system, args.build)
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.automate:
        try:
            run_automate(client, system, args.automate)
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.compress_memory is not None:
        focus = args.compress_memory.strip() or None
        try:
            compress_memory(client, system, focus=focus)
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.improve is not None:
        focus = args.improve.strip() or None
        try:
            run_self_improve(client, system, focus=focus)
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    do_improve = DEFAULT_SELF_IMPROVE
    if args.no_self_improve:
        do_improve = False
    if args.self_improve:
        do_improve = True

    if args.engineer:
        crit = (
            [c.strip() for c in args.criteria.split(",") if c.strip()]
            if args.criteria
            else [
                "Deliverable is complete and usable without follow-up questions",
                "Every number/claim is re-derived or labeled as unverified",
                "Weakest risk is named concretely",
            ]
        )
        try:
            run_loop(
                client,
                load_system_prompt(hermes=True),
                args.engineer,
                success_condition=args.success,
                max_cycles=args.max_cycles,
                retry_ceiling=args.retry_ceiling,
                self_improve=do_improve,
                hermes=True,
                engineer=True,
                criteria=crit,
                min_score=args.min_score,
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            print(f"Make sure Ollama is running. Try: ollama run {MODEL_NAME}")
            print("Or: python fable5_offline_agent.py --doctor")
            return 1

    if args.hermes:
        try:
            run_loop(
                client,
                load_system_prompt(hermes=True),
                args.hermes,
                success_condition=args.success,
                max_cycles=args.max_cycles,
                retry_ceiling=args.retry_ceiling,
                self_improve=do_improve,
                hermes=True,
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            print(f"Make sure Ollama is running. Try: ollama run {MODEL_NAME}")
            print("Or: python fable5_offline_agent.py --doctor")
            return 1

    if args.loop:
        try:
            run_loop(
                client,
                system,
                args.loop,
                success_condition=args.success,
                max_cycles=args.max_cycles,
                retry_ceiling=args.retry_ceiling,
                self_improve=do_improve,
                hermes=False,
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            print(f"Make sure Ollama is running. Try: ollama run {MODEL_NAME}")
            print("Or: python fable5_offline_agent.py --doctor")
            return 1

    try:
        chat_repl(client, system)
        return 0
    except Exception as e:
        print(ui(f"\n❌ Error: {e}"))
        return 1


if __name__ == "__main__":
    sys.exit(main())
