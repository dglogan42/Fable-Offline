#!/usr/bin/env python3
"""
Fable 5 Offline Agent
Local reasoning + loop engineering + self-improvement (skills) harness.

Usage:
  python fable5_offline_agent.py
  python fable5_offline_agent.py --loop "…"
  python fable5_offline_agent.py --improve
  python fable5_offline_agent.py --loop "…" --self-improve

In chat:
  /loop <goal>   /improve [focus]   /skills   /memory   /doctor   /help   quit

Self-improvement (offline):
  Reflect on memory + cycles → propose skills → fresh-context grade → write skills/
  Skills reload into the system prompt so later runs compound.

Requires: pip install openai
Ollama:  ollama serve && ollama pull <MODEL_NAME>
"""

from __future__ import annotations

import argparse
import os
import platform
import re
import shutil
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ==================== CONFIG ====================
LOCAL_LLM_BASE_URL = os.environ.get("FABLE5_BASE_URL", "http://localhost:11434/v1")
MODEL_NAME = os.environ.get("FABLE5_MODEL", "qwen2.5:7b")
SYSTEM_PROMPT_FILE = os.environ.get("FABLE5_MANUAL", "Fable5_Operating_Manual.md")
MEMORY_DIR = Path(os.path.expanduser(os.environ.get("FABLE5_MEMORY", "memory")))
SKILLS_DIR = Path(os.path.expanduser(os.environ.get("FABLE5_SKILLS", "skills")))
DEFAULT_MAX_CYCLES = int(os.environ.get("FABLE5_MAX_CYCLES", "6"))
RETRY_CEILING = int(os.environ.get("FABLE5_RETRY_CEILING", "3"))
TEMPERATURE = float(os.environ.get("FABLE5_TEMPERATURE", "0.3"))
MAX_TOKENS = int(os.environ.get("FABLE5_MAX_TOKENS", "8192"))
# Self-improve after loops unless FABLE5_SELF_IMPROVE=0
DEFAULT_SELF_IMPROVE = os.environ.get("FABLE5_SELF_IMPROVE", "1").strip().lower() not in {
    "0",
    "false",
    "no",
    "off",
}
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


def load_system_prompt() -> str:
    """Manual + active skills (self-improving compound context)."""
    core = load_manual_core()
    skills = read_skills_bundle(limit_chars=5000)
    if not skills.strip():
        return core
    return (
        core
        + "\n\n---\n## Active skills (self-improved library)\n"
        "Apply any skill whose WHEN_TO_USE matches the task. Prefer skills over inventing "
        "a new procedure when they fit.\n\n"
        + skills
    )


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


def parse_executor_output(text: str) -> dict:
    unit = ""
    m = re.search(r"^UNIT:\s*(.+)$", text, re.M)
    if m:
        unit = m.group(1).strip()
    art_m = re.search(r"ARTIFACT:\s*\n(.*?)(?=\nCLAIMS:|\Z)", text, re.S | re.I)
    claims_m = re.search(r"CLAIMS:\s*\n(.*?)(?=\nOPEN:|\Z)", text, re.S | re.I)
    open_m = re.search(r"OPEN:\s*\n(.*)\Z", text, re.S | re.I)
    return {
        "unit": unit or "(unit not labeled)",
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


def run_loop(
    client,
    system: str,
    goal: str,
    *,
    success_condition: Optional[str] = None,
    max_cycles: int = DEFAULT_MAX_CYCLES,
    retry_ceiling: int = RETRY_CEILING,
    self_improve: bool = DEFAULT_SELF_IMPROVE,
) -> None:
    success_condition = success_condition or (
        "The goal is met with checkable evidence; key claims pass independent verification; "
        "remaining open items are empty or explicitly deferred with reason."
    )
    print(ui("╔════════════════════════════════════════════════════════════╗"))
    print(ui("║     FABLE 5 LOOP ENGINE — offline · maker ≠ grader         ║"))
    print(ui("╚════════════════════════════════════════════════════════════╝"))
    print(f"Platform: {PLATFORM_LABEL}")
    print(f"Model:    {MODEL_NAME}")
    print(f"Goal:     {goal}")
    print(f"Success:  {success_condition}")
    print(f"Budget:   {max_cycles} cycles · retry ceiling {retry_ceiling}")
    print(f"Memory:   {memory_root()}\n")

    fail_streak = 0
    prev_unit = ""
    final_stop = "budget"

    for cycle in range(1, max_cycles + 1):
        print(ui(f"{'─' * 60}"))
        print(ui(f"▶ Cycle {cycle}/{max_cycles}"))
        print(ui(f"{'─' * 60}"))
        mem = read_memory_bundle()

        skills_ctx = read_skills_bundle(limit_chars=2500)
        exec_user = (
            f"GOAL:\n{goal}\n\n"
            f"SUCCESS CONDITION:\n{success_condition}\n\n"
            f"CYCLE NUMBER: {cycle} of max {max_cycles}\n"
            f"FAIL STREAK ON SIMILAR UNIT: {fail_streak}\n"
            f"PREVIOUS UNIT: {prev_unit or '(none)'}\n\n"
            f"ACTIVE SKILLS (apply if relevant):\n{skills_ctx or '(none)'}\n\n"
            f"MEMORY (read before acting):\n{mem}\n\n"
            "Do ONE bounded unit now. Output in the required shape."
        )
        print("\n[executor]\n")
        exec_text = stream_chat(
            client,
            [
                {"role": "system", "content": system + "\n\n" + EXECUTOR_ROLE},
                {"role": "user", "content": exec_user},
            ],
            prefix="Executor: ",
        )
        parsed = parse_executor_output(exec_text)
        unit = parsed["unit"]

        # Fresh context — verifier never sees executor reasoning trail
        ver_user = (
            f"GOAL:\n{goal}\n\n"
            f"SUCCESS CONDITION:\n{success_condition}\n\n"
            f"UNIT CLAIMED:\n{unit}\n\n"
            f"ARTIFACT:\n{parsed['artifact']}\n\n"
            f"CLAIMS TO GRADE:\n{parsed['claims']}\n\n"
            f"OPEN ITEMS FROM MAKER:\n{parsed['open']}\n\n"
            f"PRIOR FAIL STREAK: {fail_streak}\n"
            f"PREVIOUS UNIT: {prev_unit or '(none)'}\n"
            "Grade only from the artifact and claims. No benefit of the doubt from missing work."
        )
        print("\n[verifier — fresh context]\n")
        verdict = stream_chat(
            client,
            [
                {"role": "system", "content": VERIFIER_ROLE},
                {"role": "user", "content": ver_user},
            ],
            temperature=0.2,
            prefix="Verifier: ",
        )

        stop_reason: Optional[str] = None
        passed = overall_pass(verdict)
        done = success_met(verdict)
        stuck = same_failure(verdict) or (
            bool(prev_unit)
            and unit.lower()[:50] == prev_unit.lower()[:50]
            and not passed
        )

        if passed and done:
            stop_reason = "success"
            fail_streak = 0
        elif not passed:
            fail_streak = fail_streak + 1 if stuck or fail_streak > 0 else 1
            if not stuck and prev_unit and unit.lower()[:50] != prev_unit.lower()[:50]:
                fail_streak = 1  # new failing unit resets streak base
            if fail_streak >= retry_ceiling:
                stop_reason = "retry_ceiling"
        else:
            # Pass on this unit but goal not fully met — continue
            fail_streak = 0

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
        prev_unit = unit

        if stop_reason == "success":
            final_stop = "success"
            print(ui("\n✓ Loop stopped: success condition met (verifier confirmed).\n"))
            break
        if stop_reason == "retry_ceiling":
            final_stop = "retry_ceiling"
            print(
                ui(
                    f"\n✗ Loop stopped: retry ceiling ({retry_ceiling}). "
                    "Escalate to a human — same unit is not converging.\n"
                )
            )
            break
        if cycle == max_cycles:
            final_stop = "budget"
            print(ui(f"\n⏸ Loop parked: cycle budget ({max_cycles}) spent.\n"))
        else:
            print(ui(f"\n→ Cycle complete. Fail streak={fail_streak}. Continuing…\n"))

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

    # Self-improvement: encode durable skills from this run (workshop layer 5)
    if self_improve:
        print(ui("\n[self-improve after loop]\n"))
        try:
            run_self_improve(
                client,
                load_system_prompt(),
                focus=f"Lessons from goal: {goal[:200]} (stop={final_stop})",
            )
        except Exception as e:
            print(ui(f"⚠️  Self-improve skipped: {e}\n"))


# -------------------- Chat REPL --------------------


def print_banner() -> None:
    print(ui("╔════════════════════════════════════════════════════════════╗"))
    print(ui("║  FABLE 5 OFFLINE — reason · loop · verify · self-improve   ║"))
    print(ui("║  Local · skills compound · maker ≠ grader                  ║"))
    print(ui("╚════════════════════════════════════════════════════════════╝"))
    print(ui(f"Platform: {PLATFORM_LABEL}  ·  Model: {MODEL_NAME}"))
    print(f"Manual:   {_resolve(SYSTEM_PROMPT_FILE).name}")
    print(f"Skills:   {len(list_skill_paths())} loaded from {skills_root().name}/")
    print("Commands: /loop  /improve  /skills  /memory  /doctor  /help  quit\n")


def print_help() -> None:
    py = "python" if IS_WINDOWS else "python3"
    print(
        f"""
Commands
  /loop <goal>       Loop harness (executor + fresh verifier + memory)
  /improve [focus]   Self-improve: propose skills from memory, verify, write skills/
  /skills            List skill library
  /memory            Print memory/INDEX.md
  /doctor            Check Python, deps, Ollama backend
  /help              This help
  quit | exit | q    Leave

Self-improvement (offline)
  Does NOT retrain weights. Writes reusable skills into skills/ and reloads them
  into context so the *system* compounds (workshop: tools + skills + memory).

Launchers
  Windows:  fable5.cmd   or   .\\scripts\\fable5.ps1
  macOS/Linux:  ./fable5

CLI
  {py} fable5_offline_agent.py
  {py} fable5_offline_agent.py --doctor
  {py} fable5_offline_agent.py --improve
  {py} fable5_offline_agent.py --improve "numeric claims"
  {py} fable5_offline_agent.py --loop "your goal"
  {py} fable5_offline_agent.py --loop "…" --no-self-improve

Env
  FABLE5_MODEL  FABLE5_BASE_URL  FABLE5_MEMORY  FABLE5_SKILLS
  FABLE5_MAX_CYCLES  FABLE5_SELF_IMPROVE  FABLE5_ASCII
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
        if low == "/memory":
            print(read_memory_bundle(limit_chars=12000))
            print()
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
        if low.startswith("/improve"):
            focus = user_input[8:].strip() or None
            try:
                run_self_improve(client, load_system_prompt(), focus=focus)
                messages = refresh_chat_system(messages)
                print("Chat system prompt reloaded with updated skills.\n")
            except Exception as e:
                print(ui(f"\n❌ Improve error: {e}\n"))
            continue
        if low.startswith("/loop"):
            goal = user_input[5:].strip()
            if not goal:
                goal = input("Loop goal: ").strip()
            if not goal:
                print("No goal — cancelled.\n")
                continue
            try:
                run_loop(client, load_system_prompt(), goal)
                messages = refresh_chat_system(messages)
            except Exception as e:
                print(ui(f"\n❌ Loop error: {e}\n"))
            print("Back to chat. Type another question, /improve, or /loop.\n")
            continue

        messages.append({"role": "user", "content": user_input})
        print(ui("\nThinking… (Fable 5 mode)\n"))
        try:
            full = stream_chat(client, messages, prefix="Fable5: ")
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
        description="Fable 5 Offline Agent — chat, loops, self-improving skills "
        f"({PLATFORM_LABEL})"
    )
    parser.add_argument("--loop", metavar="GOAL", help="Run loop mode with this goal, then exit")
    parser.add_argument("--success", metavar="COND", help="Checkable success condition for --loop")
    parser.add_argument("--max-cycles", type=int, default=DEFAULT_MAX_CYCLES)
    parser.add_argument("--retry-ceiling", type=int, default=RETRY_CEILING)
    parser.add_argument("--model", help="Override MODEL_NAME")
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

    # Ensure skills dir exists early
    skills_root()

    if args.doctor:
        return doctor()

    system = load_system_prompt()
    client = make_client()

    ok, msg = check_backend()
    if not ok:
        print(ui(f"⚠️  {msg}"))
        print("  Run with --doctor for a full multi-platform check.")
        print(f"  Then: ollama pull {MODEL_NAME}  (if using Ollama)\n")

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
