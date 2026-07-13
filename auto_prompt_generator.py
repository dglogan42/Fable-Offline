#!/usr/bin/env python3
"""
Automatic Prompt Generator for Agent Swarms (offline)

Generates high-quality, specialized system prompts for multi-agent systems
using a local OpenAI-compatible LLM (default: Ollama).

Inspired by the quant research swarm post + Fable5 rigour + Loop principles.

Standalone:
    python auto_prompt_generator.py
    python auto_prompt_generator.py --quant
    python auto_prompt_generator.py --swarm "4-agent technical blog swarm" --agents 4
    python auto_prompt_generator.py --agent "Rigorous code reviewer"

Fable integration:
    python fable5_offline_agent.py --prompt-gen quant
    python fable5_offline_agent.py --prompt-gen "swarm: blog writer team"
    /prompt-gen in chat · /automate prompt-gen-quant

Env (shared with Fable when set):
    FABLE5_BASE_URL / FABLE5_MODEL / FABLE5_PROMPT_GEN_DIR
    or PROMPT_GEN_BASE_URL / PROMPT_GEN_MODEL / PROMPT_GEN_OUT
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

# ==================== CONFIG ====================
LOCAL_LLM_BASE_URL = os.environ.get(
    "PROMPT_GEN_BASE_URL",
    os.environ.get("FABLE5_BASE_URL", "http://localhost:11434/v1"),
)
MODEL_NAME = os.environ.get(
    "PROMPT_GEN_MODEL",
    os.environ.get("FABLE5_MODEL", "qwen2.5:7b"),
)
OUTPUT_DIR = os.environ.get(
    "PROMPT_GEN_OUT",
    os.environ.get("FABLE5_PROMPT_GEN_DIR", "generated_prompts"),
)
# Prefer stronger model for prompt quality when user has one pulled
DEFAULT_STRONG_HINT = "qwen2.5:72b"
# ===============================================


def get_client(base_url: Optional[str] = None, api_key: Optional[str] = None):
    try:
        from openai import OpenAI
    except ImportError as e:
        print("Missing dependency: openai")
        print("  python -m pip install openai")
        raise SystemExit(1) from e
    return OpenAI(
        base_url=(base_url or LOCAL_LLM_BASE_URL).rstrip("/"),
        api_key=api_key or os.environ.get("FABLE5_API_KEY", "ollama"),
    )


def call_model(
    client,
    system_prompt: str,
    user_prompt: str,
    *,
    model: Optional[str] = None,
    temperature: float = 0.5,
    max_tokens: int = 8192,
) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    response = client.chat.completions.create(
        model=model or MODEL_NAME,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return (response.choices[0].message.content or "").strip()


def get_meta_system_prompt() -> str:
    return """You are an elite prompt engineer who specializes in creating system prompts for specialized AI agents in swarms.

Your generated prompts must be:
- Extremely clear about the agent's single responsibility
- Include strong self-verification and stopping conditions (loop style)
- Incorporate Fable5-level rigour: re-derive facts, label guesses, attack own conclusions
- Define clean input/output contracts so agents can pass work to each other
- Include maker-checker principles where appropriate (never let the generator validate its own output)
- Be concise but complete — no fluff
- Written so the agent knows it is part of a larger swarm and must produce output the next agent can use
- Suitable for offline runners: Fable5 (/hermes, /loop, /team), offline_goal_loop.py, Slate, LM Studio

Always structure the output as a clean Markdown file with these sections:
# [Agent Name]

## Role
[One sentence]

## Core Responsibilities
- Bullet list

## Input Contract
What this agent receives

## Output Contract
What this agent must produce (format it expects the next agent to consume)

## Rigour Rules
- Specific rules for accuracy and self-checking (Fable5 style)

## Self-Verification
How this agent checks its own work before handing off

## Stopping Conditions
When this agent should consider its job complete for this cycle

## Anti-Failure Rules
Specific instructions to avoid common swarm failure modes

Do not add extra commentary outside this structure."""


def _safe_filename(name: str, max_len: int = 60) -> str:
    s = re.sub(r"[^\w.\-]+", "_", name.strip(), flags=re.U)
    s = re.sub(r"_+", "_", s).strip("._")
    return (s or "Agent")[:max_len]


def _parse_roles_json(text: str, num_agents: int, fallback_desc: str) -> list[dict[str, str]]:
    """Extract a JSON array of {name, description} from model output."""
    raw = text.strip()
    # Strip markdown fences
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", raw, re.I)
    if fence:
        raw = fence.group(1).strip()
    # Find first [ ... ]
    start = raw.find("[")
    end = raw.rfind("]")
    if start >= 0 and end > start:
        raw = raw[start : end + 1]
    try:
        roles = json.loads(raw)
        if isinstance(roles, list) and roles:
            out = []
            for i, r in enumerate(roles):
                if isinstance(r, dict):
                    name = str(r.get("name") or f"{i+1:02d}_Agent")
                    desc = str(r.get("description") or fallback_desc)
                    out.append({"name": _safe_filename(name), "description": desc})
            if out:
                return out[:num_agents]
    except (json.JSONDecodeError, TypeError, ValueError):
        pass
    return [
        {
            "name": f"{i+1:02d}_Agent",
            "description": fallback_desc,
        }
        for i in range(num_agents)
    ]


def _ensure_out(out_dir: str | Path) -> Path:
    p = Path(out_dir)
    p.mkdir(parents=True, exist_ok=True)
    return p


def _write_prompt(out: Path, name: str, content: str) -> Path:
    path = out / f"{_safe_filename(name)}.md"
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return path


def generate_quant_swarm(
    client,
    *,
    model: Optional[str] = None,
    out_dir: Optional[str | Path] = None,
    quiet: bool = False,
) -> list[Path]:
    """Generate the full 6-agent quant research swarm. Returns written paths."""
    if not quiet:
        print("\n🔨 Generating the full 6-agent Quant Research Swarm...")

    agents = [
        {
            "name": "01_Idea_Generator",
            "description": (
                "Reads new research papers from arXiv, SSRN and financial journals. "
                "Extracts hypotheses, required data, and predicted signal direction. "
                "Outputs structured research tickets."
            ),
        },
        {
            "name": "02_Feature_Engineer",
            "description": (
                "Takes a hypothesis ticket. Pulls required data, engineers features, "
                "handles missing values, outliers, look-ahead bias. Outputs clean "
                "dataframe ready for backtesting."
            ),
        },
        {
            "name": "03_Backtester",
            "description": (
                "Takes feature vector. Runs historical backtest with realistic costs "
                "and slippage. Outputs Sharpe, max drawdown, turnover, capacity estimates."
            ),
        },
        {
            "name": "04_Validator",
            "description": (
                "Takes backtest results. Runs statistical rigor (Newey-West, bootstrap). "
                "Flags overfitting and weak signals. Uses strongest model. "
                "Never validates its own generation."
            ),
        },
        {
            "name": "05_Regime_Auditor",
            "description": (
                "Takes validated signals. Segments performance by market regime "
                "(HMM on volatility). Kills signals that only work in one regime."
            ),
        },
        {
            "name": "06_Factor_Decomposer",
            "description": (
                "Takes regime-robust signals. Regresses against Fama-French + Carhart + "
                "low-vol factors. Reports residual alpha and whether it is genuine new alpha."
            ),
        },
    ]

    out = _ensure_out(out_dir or OUTPUT_DIR)
    written: list[Path] = []

    for agent in agents:
        if not quiet:
            print(f"   → Generating {agent['name']}...")
        user_prompt = f"""Create an elite system prompt for this specialized agent in a quant research swarm:

Agent Name: {agent['name']}
Description: {agent['description']}

The swarm runs daily. Each agent must produce output the next agent can directly consume. The Validator and Factor Decomposer must be especially rigorous."""

        prompt_content = call_model(
            client, get_meta_system_prompt(), user_prompt, model=model
        )
        path = _write_prompt(out, agent["name"], prompt_content)
        written.append(path)
        if not quiet:
            print(f"     Saved to {path}")

    overview = f"""# Quant Research Alpha Swarm — Generated {datetime.now().strftime('%Y-%m-%d')}

This swarm replaces a traditional quant research team with 6 specialized agents.

## Architecture
1. **Idea Generator** → produces research tickets from papers
2. **Feature Engineer** → builds clean features
3. **Backtester** → runs historical tests with costs
4. **Validator** → statistical rigor + anti-overfitting (strongest model)
5. **Regime Auditor** → checks performance across market regimes
6. **Factor Decomposer** → checks if alpha is real or repackaged factors

## Key Principles Built In
- Maker-checker split (Validator never generated the signal it checks)
- Strong self-verification in every agent
- Clear input/output contracts between agents
- Fable5-level rigour applied throughout
- Explicit stopping conditions

## How to Use with Fable Offline
1. Copy or symlink prompts into a swarm run folder, or load as skill/agent briefs.
2. Feed each agent prompt as the system message (or `/team` role) in order.
3. Prefer Fable `/hermes` or `/engineer` for maker≠grader + LOOP_STATE.
4. Standalone: `offline_goal_loop.py` with goal = current ticket handoff.
5. See `agents/shared-state.md` for state handoff between runners.

Drop these prompts into Slate Programs, offline_goal_loop.py, or Fable team mode.
Run the swarm daily. Wake up to vetted alpha signals.

Generated by Fable Offline Automatic Prompt Generator.
"""
    ov = out / "00_Swarm_Overview.md"
    ov.write_text(overview, encoding="utf-8")
    written.append(ov)

    config = {
        "name": "quant_research_swarm",
        "generated": datetime.now().isoformat(timespec="seconds"),
        "model": model or MODEL_NAME,
        "agents": [a["name"] for a in agents],
        "files": [p.name for p in written],
        "handoff": "sequential 01→06; Validator is maker≠generator",
    }
    cfg = out / "swarm_config.json"
    cfg.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    written.append(cfg)

    if not quiet:
        print(f"\n✅ Full quant swarm generated in ./{out}/")
        print("   Includes all 6 agents + overview + swarm_config.json")
    return written


def generate_custom_swarm(
    client,
    description: str,
    num_agents: int = 4,
    *,
    model: Optional[str] = None,
    out_dir: Optional[str | Path] = None,
    quiet: bool = False,
) -> list[Path]:
    """Generate a custom N-agent swarm from a free-text description."""
    description = (description or "").strip()
    if not description:
        raise ValueError("Swarm description is required")
    num_agents = max(2, min(int(num_agents), 12))

    if not quiet:
        print(f"\n🔨 Generating custom {num_agents}-agent swarm for: {description}")

    breakdown_prompt = f"""Break this swarm request into exactly {num_agents} specialized agent roles.

Swarm request: {description}

Return ONLY a JSON array like this:
[
  {{"name": "01_Researcher", "description": "..."}},
  {{"name": "02_Writer", "description": "..."}}
]
"""
    roles_json = call_model(
        client,
        "You are a helpful swarm architect. Return only valid JSON.",
        breakdown_prompt,
        model=model,
        temperature=0.3,
    )
    roles = _parse_roles_json(roles_json, num_agents, description)

    out = _ensure_out(out_dir or OUTPUT_DIR)
    # Subfolder by slug for multiple swarms
    slug = _safe_filename(description[:40])
    swarm_dir = out / f"swarm_{slug}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    swarm_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    for role in roles:
        if not quiet:
            print(f"   → Generating {role['name']}...")
        user_prompt = f"""Create an elite system prompt for this agent:

Agent: {role['name']}
Description: {role['description']}

This agent is part of a larger swarm: {description}
Make sure the prompt defines clean handoff to the next agent."""

        prompt_content = call_model(
            client, get_meta_system_prompt(), user_prompt, model=model
        )
        path = _write_prompt(swarm_dir, role["name"], prompt_content)
        written.append(path)
        if not quiet:
            print(f"     Saved to {path}")

    overview = f"""# Custom Swarm — {description}

Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Agents
""" + "\n".join(
        f"- **{r['name']}**: {r['description']}" for r in roles
    ) + """

## Handoff
Sequential by numeric prefix. Each agent's Output Contract feeds the next Input Contract.
Use Fable maker≠grader: never let the same role validate its own generation.

## Use
Load each `.md` as system prompt / agent brief. See `agents/shared-state.md`.
"""
    ov = swarm_dir / "00_Swarm_Overview.md"
    ov.write_text(overview, encoding="utf-8")
    written.append(ov)

    config = {
        "name": slug,
        "description": description,
        "generated": datetime.now().isoformat(timespec="seconds"),
        "model": model or MODEL_NAME,
        "agents": [r["name"] for r in roles],
        "dir": str(swarm_dir),
    }
    cfg = swarm_dir / "swarm_config.json"
    cfg.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    written.append(cfg)

    if not quiet:
        print(f"\n✅ Custom swarm generated in ./{swarm_dir}/")
    return written


def generate_single_agent(
    client,
    role: str,
    *,
    model: Optional[str] = None,
    out_dir: Optional[str | Path] = None,
    quiet: bool = False,
) -> list[Path]:
    """Generate one high-quality agent prompt."""
    role = (role or "").strip()
    if not role:
        raise ValueError("Agent role description is required")

    if not quiet:
        print(f"\n🔨 Generating elite prompt for: {role}")

    user_prompt = f"""Create an elite system prompt for a specialized agent whose job is:

{role}

Make it extremely effective, rigorous, and suitable for running in a loop or swarm.
Include Fable5 rigour, self-verification, and clear stopping conditions."""

    prompt_content = call_model(
        client, get_meta_system_prompt(), user_prompt, model=model
    )
    out = _ensure_out(out_dir or OUTPUT_DIR)
    safe_name = _safe_filename(role[:40])
    path = _write_prompt(out, f"Single_Agent_{safe_name}", prompt_content)
    if not quiet:
        print(f"\n✅ Saved to {path}")
    return [path]


def list_generated(out_dir: Optional[str | Path] = None) -> list[Path]:
    """List .md prompt files under the output directory."""
    root = Path(out_dir or OUTPUT_DIR)
    if not root.is_dir():
        return []
    return sorted(root.rglob("*.md"))


def run_mode(
    mode: str,
    *,
    description: str = "",
    num_agents: int = 4,
    model: Optional[str] = None,
    out_dir: Optional[str | Path] = None,
    base_url: Optional[str] = None,
    quiet: bool = False,
) -> list[Path]:
    """
    Programmatic entry for Fable integration.

    mode: quant | swarm | single | list
    """
    mode = (mode or "").strip().lower()
    out = out_dir or OUTPUT_DIR
    if mode == "list":
        paths = list_generated(out)
        if not quiet:
            if not paths:
                print(f"No prompts in {out}/ yet. Run --quant or --swarm first.")
            else:
                print(f"Generated prompts under {out}/:")
                for p in paths:
                    print(f"  {p}")
        return paths

    client = get_client(base_url=base_url)
    m = model or MODEL_NAME
    if not quiet:
        print(f"Model: {m}  ·  Out: {out}")

    if mode in {"quant", "1", "quant-swarm", "quant_swarm"}:
        return generate_quant_swarm(client, model=m, out_dir=out, quiet=quiet)
    if mode in {"swarm", "custom", "2"}:
        return generate_custom_swarm(
            client,
            description or "A multi-agent research and writing swarm",
            num_agents=num_agents,
            model=m,
            out_dir=out,
            quiet=quiet,
        )
    if mode in {"single", "agent", "3"}:
        return generate_single_agent(
            client,
            description or "Specialized offline agent with Fable5 rigour",
            model=m,
            out_dir=out,
            quiet=quiet,
        )
    raise ValueError(f"Unknown mode: {mode!r} (use quant | swarm | single | list)")


def interactive_main() -> None:
    print("╔════════════════════════════════════════════════════════════╗")
    print("║     AUTOMATIC PROMPT GENERATOR — FABLE OFFLINE             ║")
    print("║   Build elite agent swarms without writing prompts by hand ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print(f"Model: {MODEL_NAME}")
    print(f"Out:   {OUTPUT_DIR}/")
    if MODEL_NAME != DEFAULT_STRONG_HINT:
        print(f"Tip: stronger prompts often come from larger models (e.g. {DEFAULT_STRONG_HINT})")

    client = get_client()

    print("\nWhat do you want to generate?")
    print("1. Full 6-agent Quant Research Swarm (from the viral post)")
    print("2. Custom swarm (describe what you need)")
    print("3. Single specialized agent prompt")
    print("4. List existing generated_prompts/")
    print("5. Exit")

    choice = input("\nChoice [1-5]: ").strip()

    if choice == "1":
        generate_quant_swarm(client)
    elif choice == "2":
        print("\nDescribe the swarm you want to build.")
        print(
            "Example: 'A 4-agent swarm for writing high-quality technical blog posts: "
            "researcher, writer, fact-checker, SEO optimizer'"
        )
        description = input("\nSwarm description: ").strip()
        if not description:
            print("No description given. Exiting.")
            return
        print("\nHow many agents? (recommended 3-6)")
        try:
            num_agents = int(input("Number of agents: ").strip() or "4")
        except ValueError:
            num_agents = 4
        generate_custom_swarm(client, description, num_agents)
    elif choice == "3":
        role = input(
            "\nWhat should this agent do? "
            "(e.g. 'Rigorous code reviewer that never lets bugs through'):\n"
        ).strip()
        if not role:
            return
        generate_single_agent(client, role)
    elif choice == "4":
        run_mode("list")
        return
    else:
        print("Righto, catch ya later.")
        return

    print("\n" + "=" * 60)
    print(f"Done! Your generated prompts are in the '{OUTPUT_DIR}' folder.")
    print("Use with: Fable /hermes · /team · offline_goal_loop.py · agents/ briefs")
    print("=" * 60)


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Automatic Prompt Generator — offline Ollama/OpenAI-compatible"
    )
    p.add_argument(
        "--quant",
        action="store_true",
        help="Generate full 6-agent quant research swarm",
    )
    p.add_argument(
        "--swarm",
        metavar="DESC",
        help="Generate custom swarm from description",
    )
    p.add_argument(
        "--agents",
        type=int,
        default=4,
        help="Number of agents for --swarm (default 4, max 12)",
    )
    p.add_argument(
        "--agent",
        metavar="ROLE",
        help="Generate a single agent prompt for this role",
    )
    p.add_argument(
        "--list",
        action="store_true",
        help="List existing generated prompts",
    )
    p.add_argument("--model", help=f"Model name (default: {MODEL_NAME})")
    p.add_argument("--out", help=f"Output directory (default: {OUTPUT_DIR})")
    p.add_argument("--base-url", help=f"API base URL (default: {LOCAL_LLM_BASE_URL})")
    p.add_argument(
        "--quiet",
        action="store_true",
        help="Less console noise (still writes files)",
    )
    return p


def main(argv: Optional[list[str]] = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    # No flags → interactive
    if not argv:
        interactive_main()
        return 0

    parser = build_arg_parser()
    args = parser.parse_args(argv)

    model = args.model or MODEL_NAME
    out = args.out or OUTPUT_DIR
    base = args.base_url
    quiet = args.quiet

    try:
        if args.list:
            run_mode("list", out_dir=out, quiet=quiet)
            return 0
        if args.quant:
            run_mode("quant", model=model, out_dir=out, base_url=base, quiet=quiet)
            return 0
        if args.swarm is not None:
            run_mode(
                "swarm",
                description=args.swarm,
                num_agents=args.agents,
                model=model,
                out_dir=out,
                base_url=base,
                quiet=quiet,
            )
            return 0
        if args.agent is not None:
            run_mode(
                "single",
                description=args.agent,
                model=model,
                out_dir=out,
                base_url=base,
                quiet=quiet,
            )
            return 0
        # Unknown empty: show help
        parser.print_help()
        return 1
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
