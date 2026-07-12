#!/usr/bin/env python3
"""
Fable 5 Offline Agent
Local reasoning agent + loop-engineering harness (Ollama / OpenAI-compatible).

Usage:
  python fable5_offline_agent.py
  python fable5_offline_agent.py --loop "Re-derive and stress-test this pricing claim: ..."
  python fable5_offline_agent.py --loop "Draft a one-page decision memo on X" --max-cycles 6

In chat:
  /loop <goal>     start a goal-directed loop
  /memory          show memory index
  /help            commands
  quit / exit / q  leave

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
DEFAULT_MAX_CYCLES = int(os.environ.get("FABLE5_MAX_CYCLES", "6"))
RETRY_CEILING = int(os.environ.get("FABLE5_RETRY_CEILING", "3"))
TEMPERATURE = float(os.environ.get("FABLE5_TEMPERATURE", "0.3"))
MAX_TOKENS = int(os.environ.get("FABLE5_MAX_TOKENS", "8192"))
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


def load_system_prompt() -> str:
    """Load the Fable 5 Operating Manual if present, else a built-in core."""
    path = _resolve(SYSTEM_PROMPT_FILE)
    if path.is_file():
        content = path.read_text(encoding="utf-8")
        # Prefer core rules + loop sections; skip marketing intro only
        for marker in (
            "This document governs every response you produce",
            "## 1. Read the request beneath the words",
        ):
            if marker in content:
                return content[content.find(marker) :]
        return content
    print(ui("⚠️  Fable5_Operating_Manual.md not found — using built-in core rules only."))
    return (
        "You are a brutally rigorous reasoning engine with loop-engineering discipline.\n"
        "1. Serve real intent, not only the literal ask.\n"
        "2. Break problems into independently checkable pieces.\n"
        "3. Put effort where being wrong is expensive.\n"
        "4. Re-derive every number, fact, and claim.\n"
        "5. Label guesses at the claim.\n"
        "6. Attack your own conclusion before sending.\n"
        "7. Answer first. Then reasoning. Then concrete risk.\n"
        "8. In loops: ONE bounded unit per cycle; maker is never the grader; stop on success, "
        "retry ceiling, or budget.\n"
        "Pre-send self-test every time. No bullshit."
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

        exec_user = (
            f"GOAL:\n{goal}\n\n"
            f"SUCCESS CONDITION:\n{success_condition}\n\n"
            f"CYCLE NUMBER: {cycle} of max {max_cycles}\n"
            f"FAIL STREAK ON SIMILAR UNIT: {fail_streak}\n"
            f"PREVIOUS UNIT: {prev_unit or '(none)'}\n\n"
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


# -------------------- Chat REPL --------------------


def print_banner() -> None:
    print(ui("╔════════════════════════════════════════════════════════════╗"))
    print(ui("║     FABLE 5 OFFLINE AGENT — reason · loop · verify         ║"))
    print(ui("║     Local · no cloud · maker ≠ grader in /loop             ║"))
    print(ui("╚════════════════════════════════════════════════════════════╝"))
    print(ui(f"Platform: {PLATFORM_LABEL}  ·  Model: {MODEL_NAME}"))
    print(f"Manual:   {_resolve(SYSTEM_PROMPT_FILE).name}")
    print("Commands: /loop <goal>  /memory  /doctor  /help  quit\n")


def print_help() -> None:
    py = "python" if IS_WINDOWS else "python3"
    print(
        f"""
Commands
  /loop <goal>     Run the loop harness (executor + fresh verifier + memory)
  /loop            Prompt for a goal interactively
  /memory          Print memory/INDEX.md
  /doctor          Check Python, deps, Ollama backend
  /help            This help
  quit | exit | q  Leave

Launchers (multi-platform)
  Windows:  fable5.cmd   or   .\\scripts\\fable5.ps1
  macOS:    ./fable5     or   ./scripts/fable5.sh
  Linux:    ./fable5     or   ./scripts/fable5.sh
  Any:      {py} fable5_offline_agent.py

CLI
  {py} fable5_offline_agent.py
  {py} fable5_offline_agent.py --doctor
  {py} fable5_offline_agent.py --loop "your goal"
  {py} fable5_offline_agent.py --loop "..." --max-cycles 8

Env (all platforms)
  FABLE5_MODEL  FABLE5_BASE_URL  FABLE5_MEMORY  FABLE5_MAX_CYCLES  FABLE5_ASCII
"""
    )


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
        if low.startswith("/loop"):
            goal = user_input[5:].strip()
            if not goal:
                goal = input("Loop goal: ").strip()
            if not goal:
                print("No goal — cancelled.\n")
                continue
            try:
                run_loop(client, system, goal)
            except Exception as e:
                print(ui(f"\n❌ Loop error: {e}\n"))
            print("Back to chat. Type another question or /loop.\n")
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
        description="Fable 5 Offline Agent — multi-platform chat + loop engineering "
        f"({PLATFORM_LABEL})"
    )
    parser.add_argument("--loop", metavar="GOAL", help="Run loop mode with this goal, then exit")
    parser.add_argument("--success", metavar="COND", help="Checkable success condition for --loop")
    parser.add_argument("--max-cycles", type=int, default=DEFAULT_MAX_CYCLES)
    parser.add_argument("--retry-ceiling", type=int, default=RETRY_CEILING)
    parser.add_argument("--model", help="Override MODEL_NAME")
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

    # Resolve assets next to this script regardless of cwd (Win/macOS/Linux)
    try:
        os.chdir(SCRIPT_DIR)
    except OSError:
        pass

    if args.doctor:
        return doctor()

    system = load_system_prompt()
    client = make_client()

    ok, msg = check_backend()
    if not ok:
        print(ui(f"⚠️  {msg}"))
        print("  Run with --doctor for a full multi-platform check.")
        print(f"  Then: ollama pull {MODEL_NAME}  (if using Ollama)\n")

    if args.loop:
        try:
            run_loop(
                client,
                system,
                args.loop,
                success_condition=args.success,
                max_cycles=args.max_cycles,
                retry_ceiling=args.retry_ceiling,
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
