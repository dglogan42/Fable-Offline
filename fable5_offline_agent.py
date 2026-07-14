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
  /loop  /hermes  /improve  /skills  /soul  /mbti  /memory  /compress  /doctor  /help  quit

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
KNOWLEDGE_DIR = Path(os.path.expanduser(os.environ.get("FABLE5_KNOWLEDGE", "knowledge")))
AGENTS_DIR = Path(os.path.expanduser(os.environ.get("FABLE5_AGENTS", "agents")))
# Generated system prompts from offline prompt generator (local; often gitignored)
PROMPT_GEN_DIR = Path(
    os.path.expanduser(os.environ.get("FABLE5_PROMPT_GEN_DIR", "generated_prompts"))
)
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


def knowledge_root() -> Path:
    root = KNOWLEDGE_DIR if KNOWLEDGE_DIR.is_absolute() else SCRIPT_DIR / KNOWLEDGE_DIR
    root = root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    (root / "brokers").mkdir(parents=True, exist_ok=True)
    (root / "legal").mkdir(parents=True, exist_ok=True)
    (root / "education").mkdir(parents=True, exist_ok=True)
    (root / "privacy").mkdir(parents=True, exist_ok=True)
    (root / "urban-planning").mkdir(parents=True, exist_ok=True)
    (root / "pdf").mkdir(parents=True, exist_ok=True)
    (root / "climate").mkdir(parents=True, exist_ok=True)
    (root / "trade").mkdir(parents=True, exist_ok=True)
    (root / "culture").mkdir(parents=True, exist_ok=True)
    (root / "aem").mkdir(parents=True, exist_ok=True)
    (root / "health").mkdir(parents=True, exist_ok=True)
    (root / "public-safety").mkdir(parents=True, exist_ok=True)
    (root / "property").mkdir(parents=True, exist_ok=True)
    (root / "animals").mkdir(parents=True, exist_ok=True)
    (root / "steam").mkdir(parents=True, exist_ok=True)
    return root


def agents_root() -> Path:
    """Offline loop agent briefing files for Hermes / Fable loops."""
    root = AGENTS_DIR if AGENTS_DIR.is_absolute() else SCRIPT_DIR / AGENTS_DIR
    root = root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    return root


def prompt_gen_root() -> Path:
    """Directory for auto-generated agent system prompts (local)."""
    root = PROMPT_GEN_DIR if PROMPT_GEN_DIR.is_absolute() else SCRIPT_DIR / PROMPT_GEN_DIR
    root = root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    return root


def run_prompt_generator(
    spec: str,
    *,
    model: Optional[str] = None,
    num_agents: int = 4,
    quiet: bool = False,
) -> list[Path]:
    """
    Run offline auto_prompt_generator.

    spec examples:
      quant | list
      swarm: 4-agent blog team
      agent: rigorous code reviewer
      free text → treated as custom swarm description
    """
    # Import sibling module
    if str(SCRIPT_DIR) not in sys.path:
        sys.path.insert(0, str(SCRIPT_DIR))
    try:
        import auto_prompt_generator as apg  # type: ignore
    except ImportError as e:
        raise RuntimeError(
            "auto_prompt_generator.py not found next to fable5_offline_agent.py"
        ) from e

    raw = (spec or "").strip()
    out = prompt_gen_root()
    m = model or MODEL_NAME
    low = raw.lower()

    if not raw or low in {"help", "?", "plan"}:
        return []  # caller should chat with skill

    if low in {"list", "ls", "show"}:
        return apg.run_mode("list", out_dir=out, quiet=quiet)

    if low in {"quant", "quant-swarm", "quant_swarm", "1"}:
        return apg.run_mode(
            "quant",
            model=m,
            out_dir=out,
            base_url=LOCAL_LLM_BASE_URL,
            quiet=quiet,
        )

    # swarm: description  |  agent: role
    if low.startswith("swarm:"):
        desc = raw.split(":", 1)[1].strip()
        # optional leading N agents: "swarm:4: blog team" or "swarm: blog"
        n = num_agents
        parts = desc.split(":", 1)
        if len(parts) == 2 and parts[0].strip().isdigit():
            n = max(2, min(int(parts[0].strip()), 12))
            desc = parts[1].strip()
        return apg.run_mode(
            "swarm",
            description=desc or "custom multi-agent swarm",
            num_agents=n,
            model=m,
            out_dir=out,
            base_url=LOCAL_LLM_BASE_URL,
            quiet=quiet,
        )

    if low.startswith("agent:") or low.startswith("single:"):
        role = raw.split(":", 1)[1].strip()
        return apg.run_mode(
            "single",
            description=role or "Specialized offline agent",
            model=m,
            out_dir=out,
            base_url=LOCAL_LLM_BASE_URL,
            quiet=quiet,
        )

    # Bare keywords without colon
    if low.startswith("swarm "):
        return apg.run_mode(
            "swarm",
            description=raw[6:].strip(),
            num_agents=num_agents,
            model=m,
            out_dir=out,
            base_url=LOCAL_LLM_BASE_URL,
            quiet=quiet,
        )
    if low.startswith("agent "):
        return apg.run_mode(
            "single",
            description=raw[6:].strip(),
            model=m,
            out_dir=out,
            base_url=LOCAL_LLM_BASE_URL,
            quiet=quiet,
        )

    # Free text → custom swarm (default 4 agents)
    return apg.run_mode(
        "swarm",
        description=raw,
        num_agents=num_agents,
        model=m,
        out_dir=out,
        base_url=LOCAL_LLM_BASE_URL,
        quiet=quiet,
    )


def read_agents_brief(
    *,
    hermes: bool = False,
    loop: bool = False,
    engineer: bool = False,
    limit_chars: int = 4500,
) -> str:
    """
    Load agent briefing markdown that informs Hermes and Fable loops.
    Always includes shared offline-loop protocol when present.
    """
    root = agents_root()
    names: list[str] = ["offline-loop-protocol.md", "goal-quality.md", "shared-state.md"]
    if hermes:
        names.append("hermes-agent.md")
    if loop or engineer:
        names.append("fable-loop-agent.md")
    if not hermes and not loop and not engineer:
        # Chat / default: still give shared loop awareness (short)
        names = ["offline-loop-protocol.md", "goal-quality.md"]

    parts: list[str] = []
    seen: set[str] = set()
    for name in names:
        if name in seen:
            continue
        seen.add(name)
        path = root / name
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        parts.append(f"### agents/{name}\n{text.strip()}")
    if not parts:
        return ""
    bundle = "\n\n---\n\n".join(parts)
    if len(bundle) > limit_chars:
        bundle = bundle[:limit_chars] + "\n\n…[agents brief truncated]…"
    return bundle


def read_knowledge_bundle(subdir: str = "", limit_chars: int = 8000) -> str:
    base = knowledge_root() / subdir if subdir else knowledge_root()
    if not base.exists():
        return ""
    parts: list[str] = []
    for path in sorted(base.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        rel = path.relative_to(knowledge_root())
        parts.append(f"### knowledge/{rel.as_posix()}\n{text[:4000]}")
    bundle = "\n\n---\n\n".join(parts)
    if len(bundle) > limit_chars:
        bundle = bundle[:limit_chars] + "\n\n…[knowledge truncated]…"
    return bundle


def scrape_url_to_knowledge(url: str, out_dir: Optional[Path] = None) -> Path:
    """Fetch URL, strip HTML, save text under knowledge/ (for broker reg scrapes)."""
    out_dir = out_dir or (knowledge_root() / "brokers")
    out_dir.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Fable5OfflineAgent/1.0 (local research; +https://github.com/dglogan42/Fable-Offline)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
    html = raw.decode("utf-8", errors="replace")
    text = re.sub(r"(?is)<script[^>]*>.*?</script>", " ", html)
    text = re.sub(r"(?is)<style[^>]*>.*?</style>", " ", text)
    text = re.sub(r"(?is)<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    slug = re.sub(r"[^\w\-]+", "-", url.lower())[:80].strip("-")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    path = out_dir / f"scrape-{stamp}-{slug}.md"
    path.write_text(
        f"# Scrape\n\n- **URL:** {url}\n- **When:** {stamp} UTC\n\n## Text extract\n\n{text[:50000]}\n",
        encoding="utf-8",
        newline="\n",
    )
    # also keep raw html lightly
    (out_dir / f"scrape-{stamp}-{slug}.html").write_bytes(raw[:500_000])
    return path


def _parse_pdf_page_spec(spec: Optional[str], n_pages: int) -> range:
    if not spec:
        return range(n_pages)
    spec = spec.strip()
    if re.fullmatch(r"\d+", spec):
        i = int(spec) - 1
        if i < 0 or i >= n_pages:
            raise ValueError(f"Page {spec} out of range 1..{n_pages}")
        return range(i, i + 1)
    m = re.fullmatch(r"(\d+)-(\d+)", spec)
    if not m:
        raise ValueError("Use page N or A-B (1-based)")
    a, b = int(m.group(1)), int(m.group(2))
    if a < 1 or b < a or b > n_pages:
        raise ValueError(f"Range {spec} invalid for 1..{n_pages}")
    return range(a - 1, b)


def extract_pdf_to_markdown(
    pdf_path: Path,
    *,
    pages_spec: Optional[str] = None,
    out_path: Optional[Path] = None,
) -> Path:
    """
    Extract text layer from a local PDF to markdown under workspace/ (skill pdf-render).
    Requires optional dependency: pypdf.
    """
    try:
        from pypdf import PdfReader
    except ImportError as e:
        print(ui("❌ Missing optional dependency: pypdf"))
        print("  Install: python -m pip install pypdf")
        print("  Or: python -m pip install -r requirements.txt")
        raise SystemExit(1) from e

    pdf_path = pdf_path.expanduser().resolve()
    if not pdf_path.is_file():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    reader = PdfReader(str(pdf_path))
    n = len(reader.pages)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    slug = re.sub(r"[^\w\-]+", "-", pdf_path.stem.lower())[:40].strip("-") or "doc"
    if out_path is None:
        out_dir = workspace_root() / f"pdf-{slug}-{stamp}"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "extract.md"
    else:
        out_path = out_path.expanduser()
        out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        f"# PDF extract: {pdf_path.name}",
        "",
        f"- **Source:** `{pdf_path}`",
        f"- **Pages (file):** {n}",
        f"- **Tool:** pypdf / fable5 --pdf",
        f"- **Skill:** pdf-render",
        "",
    ]
    if getattr(reader, "is_encrypted", False):
        lines.append("- **Encrypted:** yes")
        lines.append("")

    empty = 0
    for i in _parse_pdf_page_spec(pages_spec, n):
        text = (reader.pages[i].extract_text() or "").strip()
        lines.append(f"## Page {i + 1}")
        lines.append("")
        if text:
            lines.append(text)
        else:
            empty += 1
            lines.append("*(no text layer — possible scan/image page; OCR needed)*")
        lines.append("")

    if empty:
        lines.append("---")
        lines.append(
            f"**Note:** {empty} page(s) had no extractable text. "
            "Skill pdf-render procedure **ocr-gap**."
        )
        lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return out_path


def parse_ics_to_markdown(
    ics_path: Path,
    *,
    out_path: Optional[Path] = None,
) -> Path:
    """Parse local .ics to markdown under workspace/ (skill calendar-mail-meetings)."""
    scripts_dir = SCRIPT_DIR / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    try:
        from ical_parse import parse_ics, to_markdown  # type: ignore
    except ImportError as e:
        raise RuntimeError(
            "Could not import scripts/ical_parse.py — ensure the file exists"
        ) from e

    ics_path = ics_path.expanduser().resolve()
    if not ics_path.is_file():
        raise FileNotFoundError(f"iCal file not found: {ics_path}")

    text = ics_path.read_text(encoding="utf-8", errors="replace")
    cal = parse_ics(text)
    md = to_markdown(cal, str(ics_path))

    if out_path is None:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        slug = re.sub(r"[^\w\-]+", "-", ics_path.stem.lower())[:40].strip("-") or "ical"
        out_dir = workspace_root() / f"ical-{slug}-{stamp}"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "summary.md"
    else:
        out_path = out_path.expanduser()
        out_path.parent.mkdir(parents=True, exist_ok=True)

    out_path.write_text(md, encoding="utf-8", newline="\n")
    return out_path


def load_system_prompt(
    *,
    hermes: bool = False,
    broker_mode: bool = False,
    legal_mode: bool = False,
    education_mode: bool = False,
    privacy_mode: bool = False,
    pdf_mode: bool = False,
    calendar_mode: bool = False,
    windows_mode: bool = False,
    macos_mode: bool = False,
    fit_mode: bool = False,
    outfit_mode: bool = False,
    doc_mode: bool = False,
    tiktok_ads_mode: bool = False,
    loop_mode: bool = False,
    engineer_mode: bool = False,
    math_mode: bool = False,
    prompt_gen_mode: bool = False,
    mbti_type: Optional[str] = None,
    mbti_rigour: Optional[bool] = None,
    mbti_mode: bool = False,
) -> str:
    """Manual + soul + agent briefs + active skills (+ domain knowledge when relevant)."""
    core = load_manual_core()
    soul = load_soul()
    skills = read_skills_bundle(limit_chars=5000)
    parts = [
        core,
        "\n\n---\n## SOUL.md (identity / steering)\n\n" + soul,
    ]
    # Active MBTI personality customiser (style lens; SOUL + skills outrank flavour)
    try:
        from mbti_types import build_mbti_layer, get_active_type

        layer = build_mbti_layer(mbti_type, rigour=mbti_rigour)
        if layer:
            parts.append(layer)
        elif mbti_mode:
            parts.append(
                "\n\n---\n## MBTI personality customiser mode\n"
                "Apply skill **mbti-personality-customiser**. Help the user switch agent "
                "personality lenses (16 MBTI types via `mbti_types.py`). Commands: "
                "`/mbti list|switch TYPE|current|off|rigour on|off|multi …`. "
                "Style only — not clinical diagnosis. SOUL and accuracy outrank persona.\n"
            )
            know = read_knowledge_bundle("personality", limit_chars=6000)
            if know.strip():
                parts.append("\n\n---\n## Local MBTI / personality knowledge\n\n" + know)
    except ImportError:
        pass
    # Offline loop agent pack — informs Hermes, Fable loops, and chat awareness
    agents_brief = read_agents_brief(
        hermes=hermes,
        loop=loop_mode or engineer_mode,
        engineer=engineer_mode,
        limit_chars=4500 if (hermes or loop_mode or engineer_mode) else 2200,
    )
    if agents_brief.strip():
        parts.append(
            "\n\n---\n## Offline loop agents (briefing pack)\n"
            "Follow agents/*.md protocol when looping, verifying, or stating goals. "
            "Verifier · state · stop. Maker ≠ grader.\n\n"
            + agents_brief
        )
    if hermes:
        parts.append(
            "\n\n---\n## Hermes mode active\n"
            "You are running Hermes-style offline behaviors: soul-steered, RAG-limited memory, "
            "self-stopping loops, mid-run repair after failed verification, and skill compound. "
            "Obey agents/hermes-agent.md and agents/offline-loop-protocol.md.\n"
        )
    if broker_mode:
        parts.append(
            "\n\n---\n## Broker user model mode\n"
            "Apply skills broker-user-model and broker-claim-audit. "
            "Not financial advice. Entity-first. No live trading instructions unless explicitly enabled.\n"
        )
        know = read_knowledge_bundle("brokers", limit_chars=6000)
        if know.strip():
            parts.append("\n\n---\n## Local broker knowledge (scraped)\n\n" + know)
    if legal_mode:
        parts.append(
            "\n\n---\n## Legal playbook mode\n"
            "Apply skill legal-playbook. Use knowledge/legal/playbook.md positions for "
            "GREEN/YELLOW/RED flags. Procedures: review-contract, triage-nda, vendor-check, "
            "brief, respond. Not legal advice. Licensed attorney must review all real-matter outputs. "
            "Do not invent statutes, case law, or party facts.\n"
        )
        know = read_knowledge_bundle("legal", limit_chars=8000)
        if know.strip():
            parts.append("\n\n---\n## Local legal playbook & notes\n\n" + know)
    if education_mode:
        parts.append(
            "\n\n---\n## Education claim audit mode\n"
            "Apply skill education-claim-audit. Treat school marketing as claims. "
            "Distinguish state operate license, institutional accreditation, partner degree "
            "validation, and professional board pathways. For University of Canterbury Arts "
            "postgraduate hubs, also apply skill **uc-arts-postgraduate** and curated "
            "knowledge/education/uc-arts-postgraduate-study.md (VERIFY LIVE fees/entry). "
            "Not educational, career, or medical advice.\n"
        )
        know = read_knowledge_bundle("education", limit_chars=10000)
        if know.strip():
            parts.append("\n\n---\n## Local education knowledge (scraped / curated)\n\n" + know)
    if privacy_mode:
        parts.append(
            "\n\n---\n## Privacy mode (host map + design planner)\n"
            "Apply skills **privacy-host-map** (evidence: LOAD/CONFIG/CLICK/BUNDLE) and "
            "**privacy-design-planner** (design briefs, phases, agent architecture, risk register). "
            "For TikTok pixels / analytics.tiktok.com / ttq / _ttp, also apply **tiktok-analytics** "
            "(scan-html, confirm-network, map-tiktok). "
            "Do not treat minified JS host strings as confirmed network calls. "
            "Map sensitive widgets (e.g. Shielded Site) separately from parent-page tags. "
            "For multi-step programmes or privacy-aware agent design, plan before mapping bulk sites. "
            "Not legal advice. Not a penetration test. Not a DPIA substitute.\n"
        )
        know = read_knowledge_bundle("privacy", limit_chars=9000)
        if know.strip():
            parts.append("\n\n---\n## Local privacy knowledge (maps + design)\n\n" + know)
    if pdf_mode:
        parts.append(
            "\n\n---\n## PDF render / extract mode\n"
            "Apply skill **pdf-render**. Prefer local text extracts (pypdf / --pdf) over inventing "
            "page content. Identify PDF.js dumps as Mozilla viewer libraries, not site business logic. "
            "Image-only pages need OCR (ocr-gap). Hand off to legal/education/urban/privacy skills "
            "when the document domain matches. Do not claim text that is not in the extract.\n"
        )
        know = read_knowledge_bundle("pdf", limit_chars=4000)
        if know.strip():
            parts.append("\n\n---\n## Local PDF knowledge\n\n" + know)
    if calendar_mode:
        parts.append(
            "\n\n---\n## Calendar / mail / meetings mode\n"
            "Apply skill **calendar-mail-meetings**. Google Calendar UI is "
            "https://calendar.google.com/ (user CLICK — no authenticated scrape). "
            "Zoom Web Client join is https://app.zoom.us/wc/join (user CLICK — never auto-join). "
            "Prefer local .ics via scripts/ical_parse.py or pasted VCALENDAR. "
            "Procedures: parse-ical, meeting-prep, meeting-notes, mail-draft, schedule-hygiene, "
            "gcal-guide, join-zoom, map-calendar-privacy. Draft mail/events only; user sends, "
            "creates, or joins. Never store OAuth tokens, app passwords, Zoom passcodes, or "
            "secret iCal feed URLs in git. Not legal advice. Not a mail or Zoom client.\n"
        )
        know = read_knowledge_bundle("calendar", limit_chars=8000)
        if know.strip():
            parts.append("\n\n---\n## Local calendar / meetings knowledge\n\n" + know)
        for label, rel in (
            ("Google Calendar seed", "google-calendar-hosts.md"),
            ("Zoom seed", "zoom-hosts.md"),
        ):
            host_path = knowledge_root() / "privacy" / rel
            if not host_path.is_file():
                continue
            try:
                host_txt = host_path.read_text(encoding="utf-8", errors="replace")
                if len(host_txt) > 2500:
                    host_txt = host_txt[:2500] + "\n\n…[truncated]"
                parts.append(f"\n\n---\n## Privacy host map ({label})\n\n" + host_txt)
            except OSError:
                pass
    if windows_mode:
        parts.append(
            "\n\n---\n## Windows install prep mode (licensed only)\n"
            "Apply skill **windows-install-prep**. Official media: "
            "https://www.microsoft.com/software-download/windows11 (user CLICK). "
            "Procedures: official-media-plan, dism-service-plan, unattend-skeleton, "
            "preflight-checklist, post-install-baseline, refuse-piracy. "
            "Stay on genuine Windows 11 (or real Microsoft SKUs). "
            "Refuse Windows 12 rebrand, ISO crack compilers, activators, and generic keys. "
            "Never put ProductKey secrets in git. Not legal advice. Not Microsoft support.\n"
        )
        know = read_knowledge_bundle("windows", limit_chars=8000)
        if know.strip():
            parts.append("\n\n---\n## Local Windows install knowledge\n\n" + know)
    if macos_mode:
        parts.append(
            "\n\n---\n## macOS install prep mode (Apple-licensed only)\n"
            "Apply skill **macos-install-prep**. Primary doc: "
            "https://support.apple.com/en-nz/101578 (bootable installer / createinstallmedia). "
            "Procedures: method-chooser, bootable-installer-plan, createinstallmedia-guide, "
            "boot-from-installer, preflight-checklist, post-install-baseline, refuse-piracy. "
            "USB volume is erased (MyVolume pattern). Target Macs need internet during install. "
            "Refuse Hackintosh, cracked installers, Activation Lock bypass without ownership. "
            "VERIFY LIVE Apple command table for new macOS names. Not legal advice. Not Apple Support.\n"
        )
        know = read_knowledge_bundle("macos", limit_chars=9000)
        if know.strip():
            parts.append("\n\n---\n## Local macOS install knowledge\n\n" + know)
    if fit_mode:
        parts.append(
            "\n\n---\n## Instagram selfie / fit / makeup selector mode\n"
            "Apply skill **instagram-selfie-selector**. Hype-honest creative direction for the "
            "user's own photos: select-hero, fit-check, makeup-check, slay-score, caption-pack, "
            "format-fit, post-safety. No body shame. No fake viral guarantees. No auto-post to "
            "Instagram. Privacy: crop IDs, non-consenting people, sensitive locations. "
            "Refuse content that sexualises minors. Not medical or mental-health care. "
            "If the user is designing/sewing a new outfit, also apply **outfit-selector-create** "
            "and Seamly download https://seamly.io/download/ .\n"
        )
        know = read_knowledge_bundle("social", limit_chars=6000)
        if know.strip():
            parts.append("\n\n---\n## Local social / fit knowledge\n\n" + know)
        fashion = read_knowledge_bundle("fashion", limit_chars=4000)
        if fashion.strip():
            parts.append("\n\n---\n## Local fashion / Seamly knowledge\n\n" + fashion)
    if outfit_mode:
        parts.append(
            "\n\n---\n## Outfit selector / create mode (Seamly)\n"
            "Apply skill **outfit-selector-create**. Select wardrobe combos or create outfit "
            "briefs; plan Seamly2D pattern projects. Official download: "
            "https://seamly.io/download/ (user CLICK — form emails link). FOSS apparel CAD for "
            "Windows/Linux/macOS. Procedures: select-outfit, create-outfit-brief, "
            "seamly-download-guide, measure-sheet, seamly-project-plan, materials-list, "
            "fit-iteration, hand-off-slay → instagram-selfie-selector. No body shame. "
            "No commercial pattern piracy. Not medical advice. Not a Seamly binary host.\n"
        )
        know = read_knowledge_bundle("fashion", limit_chars=8000)
        if know.strip():
            parts.append("\n\n---\n## Local fashion / Seamly knowledge\n\n" + know)
    if doc_mode:
        parts.append(
            "\n\n---\n## DOC ranger pathway mode (NZ conservation careers)\n"
            "Apply skill **doc-ranger-pathway**. Use knowledge/conservation/doc-ranger-pathway.md "
            "(DOC blog seed 2020 Becoming a DOC ranger). Procedures: pathway-map, "
            "trainee-ranger-plan, volunteer-routes, apply-checklist, doc-public-faq. "
            "Trainee Ranger / L4 Conservation Operations is one path — limited vacancies, "
            "no job guarantee. VERIFY LIVE doc.govt.nz/careers and provider pages. "
            "Not careers or immigration advice. Not DOC recruitment.\n"
        )
        know = read_knowledge_bundle("conservation", limit_chars=8000)
        if know.strip():
            parts.append("\n\n---\n## Local conservation / DOC knowledge\n\n" + know)
    if tiktok_ads_mode:
        parts.append(
            "\n\n---\n## TikTok Ads creation mode\n"
            "Apply skill **tiktok-ads-create** with knowledge/ads/ (tiktok-ads-create.md, "
            "tiktok-creative-exchange.md). Structure: Campaign → Ad group → Ad. "
            "Creative marketplace: TTCX / Partner Exchange (ttcx-brief). Procedures: "
            "create-campaign-plan, account-setup, measurement-setup (tiktok-analytics), "
            "audience-plan, creative-brief, ttcx-brief, ad-build, launch-checklist, "
            "optimise-loop. Official: ads.tiktok.com + creativeexchange. UI: TikTok Text, "
            "#fe2c55, TTAM. User publishes/spends HITL. Refuse fraud and policy evasion. "
            "VERIFY LIVE. Not financial or contract advice.\n"
        )
        know = read_knowledge_bundle("ads", limit_chars=12000)
        if know.strip():
            parts.append("\n\n---\n## Local TikTok / ads knowledge\n\n" + know)
        tt = read_knowledge_bundle("privacy", limit_chars=4000)
        # only append if tiktok-related files present in bundle - bundle is whole privacy folder truncated
        if tt.strip() and "tiktok" in tt.lower():
            parts.append(
                "\n\n---\n## Related privacy / pixel notes (excerpt may include other maps)\n\n"
                + tt[:3500]
            )
    if math_mode:
        parts.append(
            "\n\n---\n## Math / physics agent mode\n"
            "Apply skill **math-physics-agent**. Procedures: deep-explain, theorem, "
            "physics-solve, dim-check, write-lesson. Prefer durable markdown under "
            "workspace/lessons/ or memory/lessons/. Re-derive; define symbols; "
            "dimensional analysis gate for physics. Not course credit or PE stamp. "
            "Slash intents: /deep-explain /theorem /physics.\n"
        )
        m = read_knowledge_bundle("math", limit_chars=5000)
        if m.strip():
            parts.append("\n\n---\n## Local math frameworks\n\n" + m)
        p = read_knowledge_bundle("physics", limit_chars=4000)
        if p.strip():
            parts.append("\n\n---\n## Local physics frameworks\n\n" + p)
        stem = agents_root() / "math-physics-agent.md"
        if stem.is_file():
            try:
                parts.append(
                    "\n\n---\n## agents/math-physics-agent.md\n\n"
                    + stem.read_text(encoding="utf-8")[:2500]
                )
            except OSError:
                pass
    if prompt_gen_mode:
        parts.append(
            "\n\n---\n## Offline prompt generator mode\n"
            "Apply skill **prompt-generator**. Help design agent swarms and system "
            "prompts with Fable5 rigour, maker≠checker, clear I/O contracts, and "
            "stopping conditions. Actual file generation is done by "
            "`auto_prompt_generator.py` (CLI: --prompt-gen / /prompt-gen). "
            "Output dir: generated_prompts/ (or FABLE5_PROMPT_GEN_DIR). "
            "After generation, hand off prompts to /hermes, /team, offline_goal_loop, "
            "or agents/*.md. Prefer strong local models for generation quality. "
            "Not financial advice when generating quant swarm prompts.\n"
        )
        know = read_knowledge_bundle("swarm", limit_chars=6000)
        if know.strip():
            parts.append("\n\n---\n## Local swarm / prompt-gen knowledge\n\n" + know)
        pga = agents_root() / "prompt-generator-agent.md"
        if pga.is_file():
            try:
                parts.append(
                    "\n\n---\n## agents/prompt-generator-agent.md\n\n"
                    + pga.read_text(encoding="utf-8")[:2500]
                )
            except OSError:
                pass
        # Index of already-generated prompts (names only)
        try:
            gen_root = prompt_gen_root()
            if gen_root.is_dir():
                names = sorted(
                    {p.relative_to(gen_root).as_posix() for p in gen_root.rglob("*.md")}
                )[:40]
                if names:
                    parts.append(
                        "\n\n---\n## Existing generated_prompts/ (names)\n"
                        + "\n".join(f"- `{n}`" for n in names)
                    )
        except OSError:
            pass
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
    print(f"  Agents dir:  {agents_root()}")
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
    print(f"Agents:   {agents_root()}")
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
    agents_cycle = read_agents_brief(
        hermes=hermes,
        loop=True,
        engineer=engineer,
        limit_chars=3200,
    )

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
            f"OFFLINE LOOP AGENTS (obey protocol):\n{agents_cycle or '(none)'}\n\n"
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
    Steps: build | hermes | loop | improve | compress | shell | note | llm |
           broker | legal | education | privacy | calendar | windows | macos | fit | outfit | doc | tiktok_ads | math | prompt_gen | pdf | scrape | hitl | team | engineer
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
                    load_system_prompt(hermes=True, engineer_mode=True, loop_mode=True),
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
                    load_system_prompt(hermes=True, loop_mode=True),
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
                    load_system_prompt(loop_mode=True),
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
            elif stype == "scrape":
                urls = step.get("urls") or []
                if isinstance(urls, str):
                    urls = [u.strip() for u in urls.split(",") if u.strip()]
                out_rel = step.get("out_dir") or "knowledge/brokers"
                out_path = SCRIPT_DIR / out_rel
                out_path.mkdir(parents=True, exist_ok=True)
                for url in urls:
                    try:
                        p = scrape_url_to_knowledge(url, out_dir=out_path)
                        print(ui(f"  ✓ scraped {url} → {p.name}"))
                        results.append(f"scrape → {p.name}")
                    except Exception as e:
                        print(ui(f"  ✗ scrape failed {url}: {e}"))
                        results.append(f"scrape FAIL → {url}: {e}")
            elif stype == "broker":
                # Reload system with broker knowledge + user model
                bsys = load_system_prompt(broker_mode=True)
                prompt = step.get("prompt") or (
                    "Using broker-user-model and broker-claim-audit plus knowledge/brokers/, "
                    "audit the broker and coach disciplined retail user behaviors. Not advice."
                )
                print("\n[broker user model]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": bsys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="BrokerMode: ",
                )
                results.append("broker → done")
            elif stype == "legal":
                lsys = load_system_prompt(legal_mode=True)
                prompt = step.get("prompt") or (
                    "Using skill legal-playbook and knowledge/legal/playbook.md, run the "
                    "appropriate procedure (review-contract, triage-nda, vendor-check, brief, "
                    "or respond). GREEN/YELLOW/RED where applicable. Not legal advice. "
                    "Attorney review required before any real-matter use."
                )
                print("\n[legal playbook]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": lsys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="LegalMode: ",
                )
                results.append("legal → done")
            elif stype == "education":
                esys = load_system_prompt(education_mode=True)
                prompt = step.get("prompt") or (
                    "Using skill education-claim-audit and knowledge/education/, audit "
                    "credential/accreditation marketing claims. Not educational or medical advice."
                )
                print("\n[education claim audit]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": esys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="EduMode: ",
                )
                results.append("education → done")
            elif stype == "privacy":
                psys = load_system_prompt(privacy_mode=True)
                prompt = step.get("prompt") or (
                    "Using skills privacy-host-map and privacy-design-planner with "
                    "knowledge/privacy/, produce a third-party host map and/or design plan. "
                    "LOAD/CONFIG/CLICK/BUNDLE for evidence. Not legal advice."
                )
                print("\n[privacy mode — map + design planner]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": psys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="PrivacyMode: ",
                )
                results.append("privacy → done")
            elif stype == "pdf":
                pdf_rel = step.get("path") or step.get("pdf")
                pages = step.get("pages")
                extract_note = ""
                if pdf_rel:
                    try:
                        p = extract_pdf_to_markdown(Path(pdf_rel), pages_spec=pages)
                        print(ui(f"  ✓ PDF extract → {p}"))
                        extract_note = p.read_text(encoding="utf-8")[:12000]
                        results.append(f"pdf extract → {p.name}")
                    except Exception as e:
                        print(ui(f"  ✗ PDF extract failed: {e}"))
                        results.append(f"pdf FAIL → {e}")
                psys = load_system_prompt(pdf_mode=True)
                prompt = step.get("prompt") or (
                    "Using skill pdf-render, structure and review the PDF extract. "
                    "Do not invent text. Flag OCR gaps."
                )
                if extract_note:
                    prompt = prompt + "\n\n---\n## Extract\n\n" + extract_note
                print("\n[pdf render / extract]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": psys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="PdfMode: ",
                )
                results.append("pdf → done")
            elif stype == "calendar":
                ics_rel = step.get("path") or step.get("ics") or step.get("ical")
                extract_note = ""
                if ics_rel:
                    try:
                        p = parse_ics_to_markdown(Path(ics_rel))
                        print(ui(f"  ✓ iCal parse → {p}"))
                        extract_note = p.read_text(encoding="utf-8")[:12000]
                        results.append(f"ical parse → {p.name}")
                    except Exception as e:
                        print(ui(f"  ✗ iCal parse failed: {e}"))
                        results.append(f"ical FAIL → {e}")
                csys = load_system_prompt(calendar_mode=True)
                prompt = step.get("prompt") or (
                    "Using skill calendar-mail-meetings and knowledge/calendar/, run meeting-prep "
                    "or parse-ical as appropriate. Google Calendar: https://calendar.google.com/ "
                    "(user CLICK). Not legal advice."
                )
                if extract_note:
                    prompt = prompt + "\n\n---\n## iCal summary\n\n" + extract_note
                print("\n[calendar / mail / meetings]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": csys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="CalendarMode: ",
                )
                results.append("calendar → done")
            elif stype == "windows":
                wsys = load_system_prompt(windows_mode=True)
                prompt = step.get("prompt") or (
                    "Using skill windows-install-prep and knowledge/windows/, produce an "
                    "official-media-plan for licensed Windows 11. Refuse piracy/rebrand. "
                    "Not legal advice."
                )
                print("\n[windows install prep — licensed]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": wsys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="WindowsMode: ",
                )
                results.append("windows → done")
            elif stype == "macos":
                msys = load_system_prompt(macos_mode=True)
                prompt = step.get("prompt") or (
                    "Using skill macos-install-prep and knowledge/macos/, produce a "
                    "method-chooser and bootable-installer-plan per Apple 101578. "
                    "Refuse piracy/Hackintosh. Not legal advice."
                )
                print("\n[macos install prep — Apple-licensed]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": msys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="MacOSMode: ",
                )
                results.append("macos → done")
            elif stype in {"fit", "slay", "instagram"}:
                fsys = load_system_prompt(fit_mode=True)
                prompt = step.get("prompt") or (
                    "Using skill instagram-selfie-selector, help pick a hero fit/selfie "
                    "and draft caption-pack + post-safety. User posts manually."
                )
                print("\n[instagram fit / selfie selector]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": fsys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="FitMode: ",
                )
                results.append("fit → done")
            elif stype in {"outfit", "seamly", "wardrobe"}:
                osys = load_system_prompt(outfit_mode=True)
                prompt = step.get("prompt") or (
                    "Using skill outfit-selector-create and knowledge/fashion/, plan outfit "
                    "select or create + Seamly project. Download: https://seamly.io/download/"
                )
                print("\n[outfit selector / create · Seamly]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": osys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="OutfitMode: ",
                )
                results.append("outfit → done")
            elif stype in {"doc", "ranger", "conservation"}:
                dsys = load_system_prompt(doc_mode=True)
                prompt = step.get("prompt") or (
                    "Using skill doc-ranger-pathway and knowledge/conservation/, run pathway-map "
                    "for becoming a DOC ranger. VERIFY LIVE. Not careers advice."
                )
                print("\n[DOC ranger pathway]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": dsys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="DocMode: ",
                )
                results.append("doc → done")
            elif stype in {"tiktok_ads", "tiktok-ads", "ttads"}:
                tsys = load_system_prompt(tiktok_ads_mode=True)
                prompt = step.get("prompt") or (
                    "Using skill tiktok-ads-create and knowledge/ads/tiktok-ads-create.md, "
                    "produce create-campaign-plan. No fraud. User publishes in Ads Manager."
                )
                print("\n[TikTok Ads creation]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": tsys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="TikTokAds: ",
                )
                results.append("tiktok_ads → done")
            elif stype in {"math", "physics", "theorem", "deep-explain", "deep_explain"}:
                msys = load_system_prompt(math_mode=True)
                prompt = step.get("prompt") or (
                    "Using skill math-physics-agent, run deep-explain or physics-solve "
                    "as appropriate. Durable lesson structure. Dimensions gate for physics."
                )
                print("\n[math / physics agent]\n")
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": msys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="MathPhys: ",
                )
                results.append("math → done")
            elif stype in {"prompt_gen", "prompt-gen", "promptgen", "swarm-prompts"}:
                spec = (
                    step.get("spec")
                    or step.get("mode")
                    or step.get("goal")
                    or extra_goal
                    or "quant"
                )
                n_agents = int(step.get("agents", step.get("num_agents", 4)))
                print("\n[offline prompt generator]\n")
                try:
                    paths = run_prompt_generator(
                        str(spec),
                        model=step.get("model") or MODEL_NAME,
                        num_agents=n_agents,
                    )
                    if paths:
                        for p in paths:
                            print(ui(f"  ✓ {p}"))
                        results.append(f"prompt_gen → {len(paths)} files")
                    else:
                        # Advisory chat if no files produced (help/plan)
                        pgsys = load_system_prompt(prompt_gen_mode=True)
                        prompt = step.get("prompt") or (
                            "Using skill prompt-generator, explain how to generate a "
                            "quant swarm, custom swarm, or single agent prompt offline."
                        )
                        stream_chat(
                            client,
                            [
                                {"role": "system", "content": pgsys},
                                {"role": "user", "content": prompt},
                            ],
                            prefix="PromptGen: ",
                        )
                        results.append("prompt_gen → plan chat")
                except Exception as e:
                    print(ui(f"  ✗ prompt_gen failed: {e}"))
                    results.append(f"prompt_gen FAIL → {e}")
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
    print(
        "Commands: /team /broker /legal /education /privacy /calendar /windows /macos "
        "/fit /slay /outfit /doc /tiktok-ads /deep-explain /theorem /physics "
        "/prompt-gen /pdf /build /automate /loop /help quit\n"
    )


def print_help() -> None:
    py = "python" if IS_WINDOWS else "python3"
    print(
        f"""
Commands
  /roadmap           6-month agentic engineer roadmap (ROADMAP.md)
  /team <task>       Multi-agent: research → write → critic (supervisor)
  /broker [prompt]   Broker user-model + claim audit (uses knowledge/brokers/)
  /legal [prompt]    Legal playbook: contract/NDA/vendor/brief/respond (knowledge/legal/)
  /education [prompt] Education/credential claim audit (knowledge/education/)
  /privacy [prompt]  Privacy host map + design planner (knowledge/privacy/)
  /calendar [prompt] Calendar / iCal / mail / meetings (knowledge/calendar/)
  /meetings [prompt] Alias for /calendar
  /windows [prompt]  Licensed Windows 11 install / DISM hygiene (knowledge/windows/)
  /macos [prompt]    Apple-licensed macOS bootable installer / recovery (knowledge/macos/)
  /fit [prompt]      Instagram selfie / fit / makeup selector (knowledge/social/)
  /slay [prompt]     Alias for /fit
  /outfit [prompt]   Outfit select/create + Seamly2D plan (knowledge/fashion/)
  /seamly [prompt]   Alias for /outfit
  /doc [prompt]      DOC ranger / Trainee Ranger pathway (knowledge/conservation/)
  /ranger [prompt]   Alias for /doc
  /tiktok-ads [prompt]  TikTok Ads Manager creation plan (knowledge/ads/)
  /ttads [prompt]    Alias for /tiktok-ads
  /deep-explain [topic]  Bottom-up math/physics lesson (durable markdown)
  /theorem [claim]   Formal theorem + proof structure
  /physics [problem] Physics solve with dimensional analysis gate
  /prompt-gen [spec] Offline swarm/agent prompt generator → generated_prompts/
  /prompts           Alias: list generated prompts (/prompt-gen list)
  /pdf <path>        Extract PDF text (pypdf) then structure with skill pdf-render
  /scrape <url>      Fetch URL text into knowledge/ (default brokers/; --scrape-dir)
  /build <goal>      BUILD multi-file scaffold under workspace/
  /automate <name>   Run workflow recipe from workflows/*.json
  /workflows         List automation recipes
  /loop <goal>       Standard loop (executor + fresh verifier + memory)
  /engineer <goal>   Loop engineer: PLAN→DO→VERIFY · STATE · STOP
  /hermes <goal>     Hermes loop: SOUL + smart RAG + live repair + self-stop
  /improve [focus]   Self-improve: propose skills, verify, write skills/
  /skills            List skill library
  /soul              Show SOUL.md identity file
  /mbti [cmd]        Personality customiser — list|switch TYPE|current|off|rigour on|off|multi …
  /personality       Alias for /mbti
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
  {py} fable5_offline_agent.py --broker
  {py} fable5_offline_agent.py --legal "Review this NDA: [paste]"
  {py} fable5_offline_agent.py --education
  {py} fable5_offline_agent.py --privacy
  {py} fable5_offline_agent.py --calendar
  {py} fable5_offline_agent.py --calendar "meeting-prep: sprint review tomorrow 10:00 NZST"
  {py} fable5_offline_agent.py --ical path/to/invite.ics
  {py} fable5_offline_agent.py --windows
  {py} fable5_offline_agent.py --windows "official-media-plan for Win11 Pro reinstall"
  {py} fable5_offline_agent.py --automate windows-install-prep
  {py} fable5_offline_agent.py --macos
  {py} fable5_offline_agent.py --macos "bootable-installer-plan for Sequoia USB"
  {py} fable5_offline_agent.py --automate macos-install-prep
  {py} fable5_offline_agent.py --fit
  {py} fable5_offline_agent.py --fit "A black blazer fit vs B soft glam mirror selfie — feed post"
  {py} fable5_offline_agent.py --automate instagram-fit-select
  {py} fable5_offline_agent.py --outfit
  {py} fable5_offline_agent.py --outfit "create skirt pattern brief for Seamly"
  {py} fable5_offline_agent.py --automate outfit-seamly-plan
  {py} fable5_offline_agent.py --doc
  {py} fable5_offline_agent.py --doc "pathway-map: how do I become a DOC ranger?"
  {py} fable5_offline_agent.py --automate doc-ranger-pathway
  {py} fable5_offline_agent.py --tiktok-ads
  {py} fable5_offline_agent.py --tiktok-ads "conversions campaign for NZ fashion DTC"
  {py} fable5_offline_agent.py --automate tiktok-ads-create
  {py} fable5_offline_agent.py --deep-explain "eigenvalues from first principles"
  {py} fable5_offline_agent.py --theorem "fundamental theorem of calculus"
  {py} fable5_offline_agent.py --physics "block on incline with friction"
  {py} fable5_offline_agent.py --automate math-deep-explain
  {py} fable5_offline_agent.py --automate physics-solve
  {py} fable5_offline_agent.py --prompt-gen quant
  {py} fable5_offline_agent.py --prompt-gen "swarm: technical blog team"
  {py} fable5_offline_agent.py --prompt-gen "agent: rigorous code reviewer"
  {py} fable5_offline_agent.py --prompt-gen list
  {py} fable5_offline_agent.py --automate prompt-gen-quant
  {py} fable5_offline_agent.py --mbti INTJ
  {py} fable5_offline_agent.py --mbti ENFP --mbti-rigour
  {py} fable5_offline_agent.py --mbti off
  {py} fable5_offline_agent.py --automate mbti-personality-customiser
  {py} fable5_offline_agent.py --scrape https://www.lifestyleprescription.tv/accreditation --scrape-dir education
  {py} fable5_offline_agent.py --automate broker-full-audit
  {py} fable5_offline_agent.py --automate legal-contract-review
  {py} fable5_offline_agent.py --automate lpu-full-audit
  {py} fable5_offline_agent.py --automate privacy-host-map
  {py} fable5_offline_agent.py --automate privacy-design-plan
  {py} fable5_offline_agent.py --automate calendar-meeting-prep
  {py} fable5_offline_agent.py --pdf path/to/file.pdf
  {py} fable5_offline_agent.py --automate pdf-extract-review
  {py} fable5_offline_agent.py --build "tiny flask hello app"
  {py} fable5_offline_agent.py --doctor

Env
  FABLE5_MODEL  FABLE5_SOUL  FABLE5_PROGRAM  FABLE5_ROADMAP  FABLE5_KNOWLEDGE  FABLE5_HITL
  FABLE5_AGENTS  (default agents/ — offline loop briefs for Hermes + Fable)
  FABLE5_ENGINEER_MIN_SCORE  FABLE5_BILEVEL_EVERY  FABLE5_RAG_TOP_K
  FABLE5_WORKFLOWS  FABLE5_WORKSPACE  FABLE5_ALLOW_SHELL  FABLE5_MEMORY  FABLE5_SKILLS
  FABLE5_MBTI_STATE  (default mbti_state.json — active personality switch)
"""
    )


def handle_mbti_command(user_input: str, messages: list[dict]) -> tuple[list[dict], bool]:
    """
    Process /mbti or /personality. Returns (messages, handled).
    Always refreshes system prompt after state changes.
    """
    try:
        from mbti_types import (
            VALID_TYPES,
            get_active_type,
            get_rigour,
            list_types_table,
            load_mbti_state,
            normalize_type,
            set_active_type,
            set_rigour,
        )
    except ImportError:
        print(ui("\n❌ mbti_types.py missing — cannot switch personality.\n"))
        return messages, True

    raw = user_input.strip()
    low = raw.lower()
    # Strip command prefix
    if low.startswith("/personality"):
        body = raw[len("/personality") :].strip()
    elif low.startswith("/mbti"):
        body = raw[len("/mbti") :].strip()
    else:
        body = raw

    parts = body.split()
    cmd = (parts[0].lower() if parts else "") or "help"
    arg = " ".join(parts[1:]).strip() if len(parts) > 1 else ""

    def _refresh() -> list[dict]:
        return refresh_chat_system(messages)

    # /mbti INTJ  or  /mbti switch INTJ
    if cmd in VALID_TYPES or (cmd == "switch" and arg):
        code = normalize_type(cmd if cmd in VALID_TYPES else arg.split()[0])
        if not code:
            print(ui(f"\nUnknown type. Try /mbti list\n"))
            return messages, True
        set_active_type(code)
        messages = _refresh()
        print(ui(f"\n[MBTI switch → {code} | rigour={'ON' if get_rigour() else 'OFF'}]\n"))
        return messages, True

    if cmd in {"list", "types", "ls"}:
        print(ui("\nMBTI personality catalogue (style lenses):\n"))
        print(list_types_table())
        print(ui("\nSwitch: /mbti switch INTJ   Clear: /mbti off   Rigour: /mbti rigour on|off\n"))
        return messages, True

    if cmd in {"current", "status", "show"}:
        st = load_mbti_state()
        active = get_active_type(st)
        print(ui("\nMBTI customiser status"))
        print(f"  Active type: {active or '(none — SOUL default voice)'}")
        print(f"  Rigour:      {'ON' if get_rigour(st) else 'OFF'}")
        print(f"  State file:  mbti_state.json (or FABLE5_MBTI_STATE)")
        hist = st.get("history") or []
        if hist:
            print("  Recent:")
            for h in hist[-5:]:
                print(f"    - {h.get('type')} @ {h.get('at', '')[:19]}")
        print()
        return messages, True

    if cmd in {"off", "clear", "none", "default", "soul"}:
        set_active_type(None)
        messages = _refresh()
        print(ui("\n[MBTI cleared — SOUL + skills only]\n"))
        return messages, True

    if cmd in {"rigour", "rigor"}:
        sub = (arg or "").lower().strip()
        if sub in {"on", "1", "true", "yes"}:
            set_rigour(True)
            messages = _refresh()
            print(ui("\n[MBTI rigour ON — Fable5 accuracy overlay]\n"))
        elif sub in {"off", "0", "false", "no"}:
            set_rigour(False)
            messages = _refresh()
            print(ui("\n[MBTI rigour OFF — stronger pure persona flavour]\n"))
        else:
            print(ui(f"\nRigour is {'ON' if get_rigour() else 'OFF'}. Use: /mbti rigour on|off\n"))
        return messages, True

    if cmd == "multi":
        type_tokens = arg.split()
        codes = [normalize_type(t) for t in type_tokens]
        codes = [c for c in codes if c]
        if len(codes) < 2:
            print(ui("\nUsage: /mbti multi INTJ ENTP ISFJ\nThen ask your question.\n"))
            return messages, True
        set_active_type(codes[0])  # primary active type for status line
        st = load_mbti_state()
        st["multi_lens"] = codes
        from mbti_types import save_mbti_state

        save_mbti_state(st)
        messages = _refresh()
        print(ui(f"\n[Multi-lens armed: {', '.join(codes)}]"))
        print(ui("Ask your question next — separate labelled type sections.\n"))
        return messages, True

    if cmd in {"help", "?", ""}:
        active = get_active_type()
        print(
            ui(
                f"""
MBTI personality customiser (active: {active or 'none'})
  /mbti list                 All 16 types
  /mbti switch INTJ          Activate type (or: /mbti ENFP)
  /mbti current              Show status
  /mbti off                  Clear persona layer
  /mbti rigour on|off        Fable5 accuracy overlay
  /mbti multi INTJ ENTP ISFJ Multi-perspective next answers
  /personality               Alias for /mbti

CLI:  python fable5_offline_agent.py --mbti INTJ
Skill: mbti-personality-customiser · catalogue: mbti_types.py
Style lens only — not a clinical diagnosis. SOUL outranks persona.
"""
            )
        )
        return messages, True

    print(ui(f"\nUnknown /mbti command {cmd!r}. Try /mbti help\n"))
    return messages, True


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
        if low.startswith("/broker"):
            prompt = user_input[7:].strip() or (
                "Audit known broker knowledge and coach disciplined retail user behaviors. "
                "Use broker-user-model + broker-claim-audit. Not financial advice."
            )
            try:
                bsys = load_system_prompt(broker_mode=True)
                print(ui("\n[broker user model]\n"))
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": bsys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="BrokerMode: ",
                )
            except Exception as e:
                print(ui(f"\n❌ Broker mode error: {e}\n"))
            continue
        if low.startswith("/legal"):
            prompt = user_input[6:].strip() or (
                "Using skill legal-playbook and knowledge/legal/playbook.md, explain available "
                "procedures (review-contract, triage-nda, vendor-check, brief, respond) and wait "
                "for document text or a specific task. Not legal advice."
            )
            try:
                lsys = load_system_prompt(legal_mode=True)
                print(ui("\n[legal playbook]\n"))
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": lsys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="LegalMode: ",
                )
            except Exception as e:
                print(ui(f"\n❌ Legal mode error: {e}\n"))
            continue
        if low.startswith("/education"):
            prompt = user_input[10:].strip() or (
                "Using skill education-claim-audit and knowledge/education/ (incl. "
                "lpu-credential-claims.md if present), audit credential marketing. "
                "Verdict first. Not educational or medical advice."
            )
            try:
                esys = load_system_prompt(education_mode=True)
                print(ui("\n[education claim audit]\n"))
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": esys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="EduMode: ",
                )
            except Exception as e:
                print(ui(f"\n❌ Education mode error: {e}\n"))
            continue
        if low.startswith("/privacy"):
            prompt = user_input[8:].strip() or (
                "Using skills privacy-host-map and privacy-design-planner with knowledge/privacy/, "
                "default to a host map if HTML was provided; otherwise outline a design plan from "
                "DESIGN_PLANNER.md and existing maps. Verdict first. Not legal advice."
            )
            try:
                psys = load_system_prompt(privacy_mode=True)
                print(ui("\n[privacy mode — map + design planner]\n"))
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": psys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="PrivacyMode: ",
                )
            except Exception as e:
                print(ui(f"\n❌ Privacy mode error: {e}\n"))
            continue
        if low.startswith("/calendar") or low.startswith("/meetings") or low.startswith("/mail"):
            if low.startswith("/calendar"):
                prompt = user_input[9:].strip()
            elif low.startswith("/meetings"):
                prompt = user_input[9:].strip()
            else:
                prompt = user_input[5:].strip()
            prompt = prompt or (
                "Using skill calendar-mail-meetings and knowledge/calendar/, explain procedures "
                "(parse-ical, meeting-prep, meeting-notes, mail-draft, gcal-guide) and Google Calendar "
                "at https://calendar.google.com/ as user CLICK. Prefer local .ics. Not legal advice."
            )
            try:
                csys = load_system_prompt(calendar_mode=True)
                print(ui("\n[calendar / mail / meetings]\n"))
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": csys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="CalendarMode: ",
                )
            except Exception as e:
                print(ui(f"\n❌ Calendar mode error: {e}\n"))
            continue
        if low.startswith("/windows"):
            prompt = user_input[8:].strip() or (
                "Using skill windows-install-prep and knowledge/windows/, outline "
                "official-media-plan via https://www.microsoft.com/software-download/windows11. "
                "Refuse fake Windows 12 / cracks. Not legal advice."
            )
            try:
                wsys = load_system_prompt(windows_mode=True)
                print(ui("\n[windows install prep — licensed]\n"))
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": wsys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="WindowsMode: ",
                )
            except Exception as e:
                print(ui(f"\n❌ Windows mode error: {e}\n"))
            continue
        if low.startswith("/macos") or low.startswith("/mac "):
            if low.startswith("/macos"):
                prompt = user_input[6:].strip()
            else:
                prompt = user_input[4:].strip()
            prompt = prompt or (
                "Using skill macos-install-prep and knowledge/macos/, outline method-chooser "
                "and bootable installer steps per https://support.apple.com/en-nz/101578. "
                "Warn USB erase. Refuse Hackintosh/piracy. Not legal advice."
            )
            try:
                msys = load_system_prompt(macos_mode=True)
                print(ui("\n[macos install prep — Apple-licensed]\n"))
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": msys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="MacOSMode: ",
                )
            except Exception as e:
                print(ui(f"\n❌ macOS mode error: {e}\n"))
            continue
        if (
            low.startswith("/fit")
            or low.startswith("/slay")
            or low.startswith("/ootd")
            or low.startswith("/selfie")
        ):
            if low.startswith("/fit"):
                prompt = user_input[4:].strip()
            elif low.startswith("/slay"):
                prompt = user_input[5:].strip()
            elif low.startswith("/ootd"):
                prompt = user_input[5:].strip()
            else:
                prompt = user_input[7:].strip()
            prompt = prompt or (
                "Using skill instagram-selfie-selector, explain select-hero / fit-check / "
                "makeup-check and ask for 2–5 labeled photo options plus goal (feed/Story/Reel). "
                "Hype-honest. No body shame. User posts manually."
            )
            try:
                fsys = load_system_prompt(fit_mode=True)
                print(ui("\n[instagram fit / selfie selector]\n"))
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": fsys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="FitMode: ",
                )
            except Exception as e:
                print(ui(f"\n❌ Fit mode error: {e}\n"))
            continue
        if low.startswith("/outfit") or low.startswith("/seamly") or low.startswith("/wardrobe"):
            if low.startswith("/outfit"):
                prompt = user_input[7:].strip()
            elif low.startswith("/seamly"):
                prompt = user_input[7:].strip()
            else:
                prompt = user_input[9:].strip()
            prompt = prompt or (
                "Using skill outfit-selector-create and knowledge/fashion/, explain select-outfit "
                "vs create-outfit-brief vs seamly-project-plan. Point download to "
                "https://seamly.io/download/ . Ask for occasion, vibe, and closet or sew intent."
            )
            try:
                osys = load_system_prompt(outfit_mode=True)
                print(ui("\n[outfit selector / create · Seamly]\n"))
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": osys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="OutfitMode: ",
                )
            except Exception as e:
                print(ui(f"\n❌ Outfit mode error: {e}\n"))
            continue
        if low.startswith("/doc") or low.startswith("/ranger") or low.startswith("/conservation"):
            if low.startswith("/doc"):
                prompt = user_input[4:].strip()
            elif low.startswith("/ranger"):
                prompt = user_input[7:].strip()
            else:
                prompt = user_input[14:].strip()
            prompt = prompt or (
                "Using skill doc-ranger-pathway and knowledge/conservation/doc-ranger-pathway.md, "
                "run pathway-map for becoming a DOC ranger. Note 2020 blog seed; VERIFY LIVE "
                "doc.govt.nz/careers. Not careers advice."
            )
            try:
                dsys = load_system_prompt(doc_mode=True)
                print(ui("\n[DOC ranger pathway]\n"))
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": dsys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="DocMode: ",
                )
            except Exception as e:
                print(ui(f"\n❌ DOC mode error: {e}\n"))
            continue
        if low.startswith("/tiktok-ads") or low.startswith("/ttads"):
            if low.startswith("/tiktok-ads"):
                prompt = user_input[11:].strip()
            else:
                prompt = user_input[6:].strip()
            prompt = prompt or (
                "Using skill tiktok-ads-create and knowledge/ads/tiktok-ads-create.md, "
                "outline Campaign→Ad group→Ad creation and measurement-setup. "
                "Point to ads.tiktok.com. No fraud. Not financial advice."
            )
            try:
                tsys = load_system_prompt(tiktok_ads_mode=True)
                print(ui("\n[TikTok Ads creation]\n"))
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": tsys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="TikTokAds: ",
                )
            except Exception as e:
                print(ui(f"\n❌ TikTok Ads mode error: {e}\n"))
            continue
        if (
            low.startswith("/deep-explain")
            or low.startswith("/deepexplain")
            or low.startswith("/theorem")
            or low.startswith("/physics")
            or low.startswith("/math")
        ):
            if low.startswith("/deep-explain"):
                rest = user_input[len("/deep-explain") :].strip()
                kind = "deep-explain"
            elif low.startswith("/deepexplain"):
                rest = user_input[len("/deepexplain") :].strip()
                kind = "deep-explain"
            elif low.startswith("/theorem"):
                rest = user_input[len("/theorem") :].strip()
                kind = "theorem"
            elif low.startswith("/physics"):
                rest = user_input[len("/physics") :].strip()
                kind = "physics-solve"
            else:
                rest = user_input[len("/math") :].strip()
                kind = "deep-explain"
            if kind == "deep-explain":
                prompt = rest or (
                    "Using skill math-physics-agent procedure deep-explain, ask for a topic "
                    "if none, then produce a full bottom-up lesson. Suggest workspace/lessons/ path."
                )
                if rest:
                    prompt = (
                        "Using skill math-physics-agent procedure deep-explain and "
                        "knowledge/math/deep-explain-framework.md, produce a durable lesson on:\n\n"
                        + rest
                    )
            elif kind == "theorem":
                prompt = rest or (
                    "Using skill math-physics-agent procedure theorem, ask for a statement "
                    "if none, then formal statement + proof structure."
                )
                if rest:
                    prompt = (
                        "Using skill math-physics-agent procedure theorem and "
                        "knowledge/math/theorem-framework.md, treat this claim:\n\n" + rest
                    )
            else:
                prompt = rest or (
                    "Using skill math-physics-agent procedure physics-solve, ask for the full "
                    "problem if none. Mandatory dimensional analysis gate."
                )
                if rest:
                    prompt = (
                        "Using skill math-physics-agent procedure physics-solve and "
                        "knowledge/physics/solver-framework.md, solve:\n\n" + rest
                    )
            try:
                msys = load_system_prompt(math_mode=True)
                print(ui("\n[math / physics agent]\n"))
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": msys},
                        {"role": "user", "content": prompt},
                    ],
                    prefix="MathPhys: ",
                )
            except Exception as e:
                print(ui(f"\n❌ Math/physics mode error: {e}\n"))
            continue
        if (
            low.startswith("/prompt-gen")
            or low.startswith("/promptgen")
            or low.startswith("/prompts")
            or low.startswith("/swarm-prompt")
        ):
            if low.startswith("/prompt-gen"):
                rest = user_input[len("/prompt-gen") :].strip()
            elif low.startswith("/promptgen"):
                rest = user_input[len("/promptgen") :].strip()
            elif low.startswith("/prompts"):
                rest = user_input[len("/prompts") :].strip() or "list"
            else:
                rest = user_input[len("/swarm-prompt") :].strip()
            print(ui("\n[offline prompt generator]\n"))
            try:
                if not rest or rest.lower() in {"help", "?", "plan"}:
                    pgsys = load_system_prompt(prompt_gen_mode=True)
                    content = (
                        "Using skill prompt-generator, explain modes: quant swarm, "
                        "custom swarm (swarm: …), single agent (agent: …), list. "
                        "Show example Fable CLI and how to feed generated_prompts/ into "
                        "/hermes, /team, or agents/. Prefer strong local models."
                    )
                    stream_chat(
                        client,
                        [
                            {"role": "system", "content": pgsys},
                            {"role": "user", "content": content},
                        ],
                        prefix="PromptGen: ",
                    )
                else:
                    paths = run_prompt_generator(rest, model=MODEL_NAME)
                    if paths:
                        print(
                            ui(
                                f"Generated {len(paths)} file(s) under {prompt_gen_root()}:"
                            )
                        )
                        for p in paths:
                            print(ui(f"  ✓ {p}"))
                        print(
                            ui(
                                "\nNext: load a prompt as system/agent brief, or /team /hermes "
                                "with the swarm overview. See skill prompt-generator.\n"
                            )
                        )
                    else:
                        print(
                            ui(
                                "No files written. Try: quant | list | swarm: … | agent: …\n"
                            )
                        )
            except Exception as e:
                print(ui(f"\n❌ Prompt generator error: {e}\n"))
            continue
        if low.startswith("/pdf"):
            rest = user_input[4:].strip()
            pdf_path_s = rest
            pages = None
            if " --pages " in rest:
                pdf_path_s, pages = rest.split(" --pages ", 1)
                pdf_path_s, pages = pdf_path_s.strip(), pages.strip()
            if not pdf_path_s:
                pdf_path_s = input("Path to PDF: ").strip()
            if not pdf_path_s:
                print("No path — cancelled.\n")
                continue
            try:
                out = extract_pdf_to_markdown(Path(pdf_path_s), pages_spec=pages)
                print(ui(f"✓ Extracted → {out}\n"))
                extract = out.read_text(encoding="utf-8")[:12000]
                psys = load_system_prompt(pdf_mode=True)
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": psys},
                        {
                            "role": "user",
                            "content": (
                                "Using skill pdf-render, structure this extract. "
                                "Flag OCR gaps. Do not invent text.\n\n" + extract
                            ),
                        },
                    ],
                    prefix="PdfMode: ",
                )
            except Exception as e:
                print(ui(f"\n❌ PDF error: {e}\n"))
            continue
        if low.startswith("/scrape"):
            url = user_input[7:].strip()
            if not url:
                url = input("URL to scrape: ").strip()
            if not url:
                print("No URL — cancelled.\n")
                continue
            try:
                p = scrape_url_to_knowledge(url)
                print(ui(f"✓ Saved {p}\n"))
            except Exception as e:
                print(ui(f"\n❌ Scrape error: {e}\n"))
            continue
        if low == "/memory":
            print(read_memory_bundle(limit_chars=12000))
            print()
            continue
        if low in {"/soul", "soul"}:
            print(load_soul())
            print()
            continue
        if low.startswith("/mbti") or low.startswith("/personality"):
            messages, _ = handle_mbti_command(user_input, messages)
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
                    load_system_prompt(hermes=True, engineer_mode=True, loop_mode=True),
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
                run_loop(
                    client,
                    load_system_prompt(loop_mode=True),
                    goal,
                    hermes=False,
                )
                messages = refresh_chat_system(messages)
            except Exception as e:
                print(ui(f"\n❌ Loop error: {e}\n"))
            print("Back to chat. Type another question, /improve, /hermes, or /loop.\n")
            continue

        # Chat: store clean user text; inject smart RAG only for this call
        # Optional multi-lens MBTI framing from /mbti multi
        chat_user = user_input
        try:
            from mbti_types import build_multi_perspective_prompt, load_mbti_state, save_mbti_state

            st_m = load_mbti_state()
            multi = st_m.get("multi_lens") or []
            if multi and isinstance(multi, list) and len(multi) >= 2:
                chat_user = build_multi_perspective_prompt(multi, user_input)
                st_m["multi_lens"] = []  # one-shot unless re-armed
                save_mbti_state(st_m)
        except ImportError:
            pass

        rag = retrieve_relevant_memory(user_input, top_k=min(8, RAG_TOP_K), limit_chars=2500)
        enriched = chat_user
        if rag and "(no memory yet)" not in rag:
            enriched = (
                f"{chat_user}\n\n---\nRelevant memory (smart RAG, optional):\n{rag}"
            )
        messages.append({"role": "user", "content": user_input})
        api_messages = messages[:-1] + [{"role": "user", "content": enriched}]
        _t = None
        try:
            from mbti_types import get_active_type as _mbti_active

            _t = _mbti_active()
        except ImportError:
            pass
        prefix = f"Fable5[{_t}]: " if _t else "Fable5: "
        print(ui(f"\nThinking… (Fable 5 mode{f' · {_t}' if _t else ''})\n"))
        try:
            full = stream_chat(client, api_messages, prefix=prefix)
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
        "--commune",
        nargs="?",
        const="",
        metavar="TOPIC",
        help="Run a communicator session: agents propose, critique, refine, and synthesize",
    )
    parser.add_argument(
        "--commune-rounds",
        type=int,
        default=5,
        metavar="N",
        help="Number of critique/refinement rounds for --commune (default: 5)",
    )
    parser.add_argument(
        "--commune-agents",
        default="proposer,challenger,synthesizer",
        help="Comma-separated roster for --commune",
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
        "--broker",
        nargs="?",
        const="",
        default=None,
        metavar="PROMPT",
        help="Broker user-model + claim audit using knowledge/brokers/",
    )
    parser.add_argument(
        "--legal",
        nargs="?",
        const="",
        default=None,
        metavar="PROMPT",
        help="Legal playbook mode: contract/NDA/vendor/brief/respond (knowledge/legal/)",
    )
    parser.add_argument(
        "--education",
        nargs="?",
        const="",
        default=None,
        metavar="PROMPT",
        help="Education/credential claim audit using knowledge/education/",
    )
    parser.add_argument(
        "--privacy",
        nargs="?",
        const="",
        default=None,
        metavar="PROMPT",
        help="Privacy host map + design planner using knowledge/privacy/",
    )
    parser.add_argument(
        "--calendar",
        nargs="?",
        const="",
        default=None,
        metavar="PROMPT",
        help="Calendar / iCal / mail / meetings mode (knowledge/calendar/)",
    )
    parser.add_argument(
        "--ical",
        metavar="PATH",
        help="Parse local .ics to workspace/ markdown, then calendar-mail-meetings review",
    )
    parser.add_argument(
        "--windows",
        nargs="?",
        const="",
        default=None,
        metavar="PROMPT",
        help="Licensed Windows 11 install prep / DISM hygiene (knowledge/windows/)",
    )
    parser.add_argument(
        "--macos",
        nargs="?",
        const="",
        default=None,
        metavar="PROMPT",
        help="Apple-licensed macOS bootable installer / recovery (knowledge/macos/)",
    )
    parser.add_argument(
        "--fit",
        nargs="?",
        const="",
        default=None,
        metavar="PROMPT",
        help="Instagram selfie / fit / makeup selector (knowledge/social/)",
    )
    parser.add_argument(
        "--outfit",
        nargs="?",
        const="",
        default=None,
        metavar="PROMPT",
        help="Outfit select/create + Seamly2D plan (knowledge/fashion/; seamly.io/download)",
    )
    parser.add_argument(
        "--doc",
        nargs="?",
        const="",
        default=None,
        metavar="PROMPT",
        help="DOC ranger / Trainee Ranger pathway (knowledge/conservation/)",
    )
    parser.add_argument(
        "--tiktok-ads",
        nargs="?",
        const="",
        default=None,
        metavar="PROMPT",
        help="TikTok Ads Manager creation plan (knowledge/ads/)",
    )
    parser.add_argument(
        "--deep-explain",
        nargs="?",
        const="",
        default=None,
        metavar="TOPIC",
        help="Bottom-up math/physics lesson (math-physics-agent deep-explain)",
    )
    parser.add_argument(
        "--theorem",
        nargs="?",
        const="",
        default=None,
        metavar="CLAIM",
        help="Formal theorem + proof structure (math-physics-agent)",
    )
    parser.add_argument(
        "--physics",
        nargs="?",
        const="",
        default=None,
        metavar="PROBLEM",
        help="Physics solve with dimensional analysis (math-physics-agent)",
    )
    parser.add_argument(
        "--prompt-gen",
        nargs="?",
        const="help",
        default=None,
        metavar="SPEC",
        help=(
            "Offline prompt generator: quant | list | swarm:DESC | agent:ROLE | free-text swarm "
            "(writes generated_prompts/)"
        ),
    )
    parser.add_argument(
        "--prompt-gen-agents",
        type=int,
        default=4,
        metavar="N",
        help="Agent count for custom --prompt-gen swarm (default 4, max 12)",
    )
    parser.add_argument(
        "--pdf",
        metavar="PATH",
        help="Extract text from local PDF (pypdf) to workspace/, then structure with pdf-render",
    )
    parser.add_argument(
        "--pdf-pages",
        metavar="SPEC",
        help="With --pdf: 1-based page or range (e.g. 1 or 2-10)",
    )
    parser.add_argument(
        "--pdf-out",
        metavar="PATH",
        help="With --pdf: write extract markdown to this path",
    )
    parser.add_argument(
        "--scrape",
        metavar="URL",
        action="append",
        help="Scrape URL into knowledge/ (default brokers/; use --scrape-dir)",
    )
    parser.add_argument(
        "--scrape-dir",
        default="brokers",
        metavar="SUBDIR",
        help="knowledge/ subdir for --scrape (default: brokers; use legal for contracts)",
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
        "--mbti",
        metavar="TYPE",
        default=None,
        help="Activate MBTI personality lens (e.g. INTJ, ENFP) or 'off' to clear",
    )
    parser.add_argument(
        "--mbti-rigour",
        action="store_true",
        help="Force MBTI Fable5 rigour overlay ON",
    )
    parser.add_argument(
        "--mbti-no-rigour",
        action="store_true",
        help="Force MBTI rigour overlay OFF (stronger pure persona)",
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

    # MBTI personality customiser CLI switch (persists to mbti_state.json)
    if args.mbti is not None:
        try:
            from mbti_types import normalize_type, set_active_type, set_rigour

            raw_m = (args.mbti or "").strip()
            if raw_m.lower() in {"off", "clear", "none", "default", "soul", ""}:
                set_active_type(None)
                print(ui("[MBTI cleared]"))
            else:
                code = normalize_type(raw_m)
                if not code:
                    print(ui(f"✗ Unknown MBTI type {raw_m!r}. Use INTJ…ESFP or off."))
                    return 1
                set_active_type(code)
                print(ui(f"[MBTI → {code}]"))
            if args.mbti_rigour:
                set_rigour(True)
                print(ui("[MBTI rigour ON]"))
            elif args.mbti_no_rigour:
                set_rigour(False)
                print(ui("[MBTI rigour OFF]"))
        except ImportError:
            print(ui("✗ mbti_types.py missing"))
            return 1

    if args.scrape:
        knowledge_root()
        scrape_sub = (args.scrape_dir or "brokers").strip().strip("/\\") or "brokers"
        # Prevent path escape from knowledge root
        if ".." in scrape_sub or Path(scrape_sub).is_absolute():
            print(ui("✗ --scrape-dir must be a relative subdir under knowledge/ (e.g. brokers, legal)"))
            return 1
        out_dir = knowledge_root() / scrape_sub
        for url in args.scrape:
            try:
                p = scrape_url_to_knowledge(url, out_dir=out_dir)
                print(ui(f"✓ scraped → {p}"))
            except Exception as e:
                print(ui(f"✗ scrape failed {url}: {e}"))
                return 1
        if (
            args.broker is None
            and args.legal is None
            and args.education is None
            and args.privacy is None
            and args.calendar is None
            and args.windows is None
            and args.macos is None
            and args.fit is None
            and args.outfit is None
            and args.doc is None
            and args.tiktok_ads is None
            and args.deep_explain is None
            and args.theorem is None
            and args.physics is None
            and args.prompt_gen is None
            and not args.ical
            and not args.automate
            and not args.team
        ):
            return 0

    system = load_system_prompt()
    client = make_client()

    ok, msg = check_backend()
    if not ok:
        print(ui(f"⚠️  {msg}"))
        print("  Run with --doctor for a full multi-platform check.")
        print(f"  Then: ollama pull {MODEL_NAME}  (if using Ollama)\n")

    if args.broker is not None:
        prompt = (args.broker or "").strip() or (
            "Using broker-user-model and broker-claim-audit plus knowledge/brokers/, "
            "produce a regulation/claim audit and disciplined retail user checklist. "
            "Not financial advice."
        )
        try:
            bsys = load_system_prompt(broker_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": bsys}, {"role": "user", "content": prompt}],
                prefix="BrokerMode: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.legal is not None:
        prompt = (args.legal or "").strip() or (
            "Using skill legal-playbook and knowledge/legal/playbook.md, list procedures "
            "(review-contract, triage-nda, vendor-check, brief, respond) and how to flag "
            "GREEN/YELLOW/RED. If no document was provided, ask for text. Not legal advice. "
            "Attorney review required for real matters."
        )
        try:
            lsys = load_system_prompt(legal_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": lsys}, {"role": "user", "content": prompt}],
                prefix="LegalMode: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.education is not None:
        prompt = (args.education or "").strip() or (
            "Using skill education-claim-audit and knowledge/education/ (especially "
            "lpu-credential-claims.md), produce a credential/accreditation claim audit. "
            "Verdict first. Map accreditation types. Flag pending vs approved board pathways. "
            "Not educational or medical advice."
        )
        try:
            esys = load_system_prompt(education_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": esys}, {"role": "user", "content": prompt}],
                prefix="EduMode: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.privacy is not None:
        prompt = (args.privacy or "").strip() or (
            "Using skills privacy-host-map and privacy-design-planner with knowledge/privacy/ "
            "(host maps + DESIGN_PLANNER.md + design-privacy-agent.md), produce either: "
            "(1) a host map if the user is auditing a page, or (2) a design plan for a "
            "privacy-aware agentic AI if designing. Prefer plan-from-knowledge when maps exist. "
            "Verdict first. LOAD/CONFIG/CLICK/BUNDLE for evidence. Not legal advice."
        )
        try:
            psys = load_system_prompt(privacy_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": psys}, {"role": "user", "content": prompt}],
                prefix="PrivacyMode: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.ical:
        try:
            out = parse_ics_to_markdown(Path(args.ical))
            print(ui(f"✓ iCal parse → {out}"))
            extract = out.read_text(encoding="utf-8")
            extract_for_model = (
                extract if len(extract) <= 14000 else extract[:14000] + "\n\n…[truncated]"
            )
            csys = load_system_prompt(calendar_mode=True)
            stream_chat(
                client,
                [
                    {"role": "system", "content": csys},
                    {
                        "role": "user",
                        "content": (
                            "Using skill calendar-mail-meetings procedure parse-ical, summarise "
                            "this offline iCal extract. Flag conference links as CLICK. Suggest "
                            "meeting-prep or mail-draft next steps. Do not invent attendees or times.\n\n"
                            + extract_for_model
                        ),
                    },
                ],
                prefix="CalendarMode: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ iCal error: {e}"))
            return 1

    if args.calendar is not None:
        prompt = (args.calendar or "").strip() or (
            "Using skill calendar-mail-meetings and knowledge/calendar/ "
            "(ical-and-google.md, meetings-playbook.md), list procedures and how to use "
            "Google Calendar at https://calendar.google.com/ with local .ics offline. "
            "If the user stated a meeting, run meeting-prep. Not legal advice."
        )
        try:
            csys = load_system_prompt(calendar_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": csys}, {"role": "user", "content": prompt}],
                prefix="CalendarMode: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.windows is not None:
        prompt = (args.windows or "").strip() or (
            "Using skill windows-install-prep and knowledge/windows/ "
            "(official-media.md, dism-unattend-hygiene.md), produce an official-media-plan "
            "for licensed Windows 11 via https://www.microsoft.com/software-download/windows11. "
            "Include preflight checklist. Refuse fake Windows 12, rebrand ISO compilers, "
            "cracks, and generic product keys. Not legal advice."
        )
        try:
            wsys = load_system_prompt(windows_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": wsys}, {"role": "user", "content": prompt}],
                prefix="WindowsMode: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.macos is not None:
        prompt = (args.macos or "").strip() or (
            "Using skill macos-install-prep and knowledge/macos/ "
            "(bootable-installer.md, reinstall-and-recovery.md), produce method-chooser and "
            "bootable-installer-plan per https://support.apple.com/en-nz/101578. "
            "Warn that createinstallmedia erases MyVolume. List createinstallmedia patterns "
            "only for known Apple version names; say VERIFY LIVE. Refuse Hackintosh and "
            "cracked installers. Not legal advice."
        )
        try:
            msys = load_system_prompt(macos_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": msys}, {"role": "user", "content": prompt}],
                prefix="MacOSMode: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.fit is not None:
        prompt = (args.fit or "").strip() or (
            "Using skill instagram-selfie-selector and knowledge/social/instagram-selfie-playbook.md, "
            "explain how to run select-hero for fits/makeup/selfies and ask for labeled options. "
            "Include a sample caption-pack structure and post-safety checklist. "
            "Hype-honest, no body shame, no viral guarantees. User posts manually on Instagram."
        )
        try:
            fsys = load_system_prompt(fit_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": fsys}, {"role": "user", "content": prompt}],
                prefix="FitMode: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.outfit is not None:
        prompt = (args.outfit or "").strip() or (
            "Using skill outfit-selector-create and knowledge/fashion/ "
            "(seamly-outfit-workflow.md, outfit-selector-create.md), produce: "
            "(1) method chooser select vs create (2) create-outfit-brief template "
            "(3) seamly-download-guide for https://seamly.io/download/ "
            "(4) seamly-project-plan phases (5) hand-off to Instagram skill. "
            "FOSS apparel CAD. No body shame. No pattern piracy. Not medical advice."
        )
        try:
            osys = load_system_prompt(outfit_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": osys}, {"role": "user", "content": prompt}],
                prefix="OutfitMode: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.doc is not None:
        prompt = (args.doc or "").strip() or (
            "Using skill doc-ranger-pathway and knowledge/conservation/doc-ranger-pathway.md "
            "(DOC Conservation blog seed: Becoming a DOC ranger, Jan 2020), produce pathway-map. "
            "L4 Conservation Operations / Trainee Ranger is one path; vacancies limited; "
            "VERIFY LIVE https://www.doc.govt.nz/careers/ . Not careers advice."
        )
        try:
            dsys = load_system_prompt(doc_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": dsys}, {"role": "user", "content": prompt}],
                prefix="DocMode: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.tiktok_ads is not None:
        prompt = (args.tiktok_ads or "").strip() or (
            "Using skill tiktok-ads-create and knowledge/ads/tiktok-ads-create.md, produce "
            "create-campaign-plan for a legitimate TikTok Ads Manager campaign: hierarchy, "
            "measurement-setup, audience-plan, creative-brief, launch-checklist. "
            "Official: https://ads.tiktok.com/ . Refuse fraud. VERIFY LIVE. Not financial advice."
        )
        try:
            tsys = load_system_prompt(tiktok_ads_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": tsys}, {"role": "user", "content": prompt}],
                prefix="TikTokAds: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.deep_explain is not None:
        topic = (args.deep_explain or "").strip()
        prompt = (
            "Using skill math-physics-agent procedure deep-explain and "
            "knowledge/math/deep-explain-framework.md, produce a full bottom-up lesson"
            + (f" on:\n\n{topic}" if topic else ". Ask for a topic if none was given.")
            + "\n\nSuggest saving to workspace/lessons/. Not course credit."
        )
        try:
            msys = load_system_prompt(math_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": msys}, {"role": "user", "content": prompt}],
                prefix="MathPhys: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.theorem is not None:
        claim = (args.theorem or "").strip()
        prompt = (
            "Using skill math-physics-agent procedure theorem and "
            "knowledge/math/theorem-framework.md, produce formal statement + proof structure"
            + (f" for:\n\n{claim}" if claim else ". Ask for the claim if none was given.")
            + "\n\nMark OPEN gaps. Suggest workspace/lessons/ path."
        )
        try:
            msys = load_system_prompt(math_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": msys}, {"role": "user", "content": prompt}],
                prefix="MathPhys: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.physics is not None:
        problem = (args.physics or "").strip()
        prompt = (
            "Using skill math-physics-agent procedure physics-solve and "
            "knowledge/physics/solver-framework.md, solve with mandatory dimensional analysis gate"
            + (f":\n\n{problem}" if problem else ". Ask for the full problem statement.")
            + "\n\nNot professional engineering sign-off."
        )
        try:
            msys = load_system_prompt(math_mode=True)
            stream_chat(
                client,
                [{"role": "system", "content": msys}, {"role": "user", "content": prompt}],
                prefix="MathPhys: ",
            )
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

    if args.prompt_gen is not None:
        spec = (args.prompt_gen or "help").strip()
        try:
            if spec.lower() in {"help", "?", "plan", ""}:
                pgsys = load_system_prompt(prompt_gen_mode=True)
                stream_chat(
                    client,
                    [
                        {"role": "system", "content": pgsys},
                        {
                            "role": "user",
                            "content": (
                                "Using skill prompt-generator, explain how to generate "
                                "quant / custom swarm / single-agent system prompts offline. "
                                "CLI examples and handoff to Hermes/team/agents."
                            ),
                        },
                    ],
                    prefix="PromptGen: ",
                )
                return 0
            paths = run_prompt_generator(
                spec,
                model=MODEL_NAME,
                num_agents=int(getattr(args, "prompt_gen_agents", 4) or 4),
            )
            if paths:
                print(ui(f"\n✓ {len(paths)} file(s) → {prompt_gen_root()}"))
                for p in paths:
                    print(ui(f"  {p}"))
                return 0
            # list with empty dir is success; other empty results are usage errors
            if spec.strip().lower() in {"list", "ls", "show"}:
                return 0
            print(ui("No files written. Spec: quant | list | swarm:… | agent:…"))
            return 1
        except Exception as e:
            print(ui(f"\n❌ Prompt generator error: {e}"))
            return 1

    if args.pdf:
        try:
            out = extract_pdf_to_markdown(
                Path(args.pdf),
                pages_spec=args.pdf_pages,
                out_path=Path(args.pdf_out) if args.pdf_out else None,
            )
            print(ui(f"✓ PDF extract → {out}"))
            extract = out.read_text(encoding="utf-8")
            # Cap context for local models
            extract_for_model = extract if len(extract) <= 14000 else extract[:14000] + "\n\n…[truncated]"
            psys = load_system_prompt(pdf_mode=True)
            stream_chat(
                client,
                [
                    {"role": "system", "content": psys},
                    {
                        "role": "user",
                        "content": (
                            "Using skill pdf-render procedure structure-doc, review this extract. "
                            "Verdict on text-layer quality, outline, key claims, OCR gaps, "
                            "next domain skill. Do not invent text.\n\n" + extract_for_model
                        ),
                    },
                ],
                prefix="PdfMode: ",
            )
            return 0
        except SystemExit:
            raise
        except Exception as e:
            print(ui(f"\n❌ PDF error: {e}"))
            return 1

    if args.commune is not None:
        try:
            from fable5_communicators import run_communicator_session

            topic = (args.commune or "").strip() or "How should our agents learn from each other?"
            result = run_communicator_session(
                topic,
                client=client,
                rounds=args.commune_rounds,
                agent_names=[n.strip() for n in args.commune_agents.split(",") if n.strip()],
                system_core=system,
                self_improve=DEFAULT_SELF_IMPROVE and not args.no_self_improve,
                hitl=HITL,
            )
            print(ui("\n" + result.transcript_markdown()))
            if result.memory_path:
                print(ui(f"\nTranscript saved: {result.memory_path}"))
            if result.skill_path:
                print(ui(f"New skill written: {result.skill_path}"))
            return 0
        except Exception as e:
            print(ui(f"\n❌ Error: {e}"))
            return 1

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
                load_system_prompt(hermes=True, engineer_mode=True, loop_mode=True),
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
                load_system_prompt(hermes=True, loop_mode=True),
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
                load_system_prompt(loop_mode=True),
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
