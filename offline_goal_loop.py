#!/usr/bin/env python3
"""
Offline Goal Loop Agent
Autonomous loop runner for local LLMs (inspired by Claude Code /goal loops)

Run with a clear goal and it will keep working, self-checking, and remembering
until the goal is satisfied or max iterations reached.

Usage:
    python offline_goal_loop.py
    # then type your goal when prompted

Or with command line:
    python offline_goal_loop.py --goal "Build a complete FastAPI todo app with tests"

Requirements:
    pip install openai
    ollama running with a strong model (qwen2.5:72b recommended)
"""

import os
import json
import argparse
from datetime import datetime
from pathlib import Path
from openai import OpenAI

# ==================== CONFIG ====================
LOCAL_LLM_BASE_URL = os.environ.get("FABLE5_BASE_URL", "http://localhost:11434/v1")
MODEL_NAME = os.environ.get("FABLE5_MODEL", "qwen2.5:72b")  # Change to your strongest local model
MAX_ITERATIONS = int(os.environ.get("FABLE5_MAX_CYCLES", "20"))
STATE_FILE = "loop_state.json"
FABLE5_FILE = "Fable5_Operating_Manual.md"  # Optional - loads if present for better reasoning
SOUL_FILE = os.environ.get("FABLE5_SOUL", "SOUL.md")
AGENTS_DIR = Path(os.environ.get("FABLE5_AGENTS", "agents"))
# ===============================================


def load_fable5_prompt():
    if os.path.exists(FABLE5_FILE):
        with open(FABLE5_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        if "## 1. Read the request beneath the words" in content:
            start = content.find("## 1. Read the request beneath the words")
            return "\n\n" + content[start:]
    return ""


def load_soul_prompt() -> str:
    path = Path(SOUL_FILE)
    if path.is_file():
        try:
            return path.read_text(encoding="utf-8")
        except OSError:
            return ""
    return ""


def load_agents_brief(limit_chars: int = 5000) -> str:
    """Load offline loop agent files that inform Hermes/Fable-style autonomous work."""
    root = AGENTS_DIR if AGENTS_DIR.is_absolute() else Path(__file__).resolve().parent / AGENTS_DIR
    if not root.is_dir():
        return ""
    names = [
        "offline-loop-protocol.md",
        "hermes-agent.md",
        "fable-loop-agent.md",
        "goal-quality.md",
        "shared-state.md",
    ]
    parts: list[str] = []
    for name in names:
        path = root / name
        if not path.is_file():
            continue
        try:
            parts.append(f"### agents/{name}\n{path.read_text(encoding='utf-8').strip()}")
        except OSError:
            continue
    if not parts:
        return ""
    bundle = "\n\n---\n\n".join(parts)
    if len(bundle) > limit_chars:
        bundle = bundle[:limit_chars] + "\n\n…[agents brief truncated]…"
    return bundle


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "goal": "",
        "completed_steps": [],
        "current_plan": "",
        "conversation": [],
        "iteration": 0,
        "created_at": datetime.now().isoformat()
    }


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def get_client():
    return OpenAI(base_url=LOCAL_LLM_BASE_URL, api_key="ollama")


def call_model(client, messages, temperature=0.4, max_tokens=8192, stream=True):
    """Call the local model and return full response."""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=stream
    )
    
    if stream:
        full = ""
        print("\033[96m[Agent]\033[0m ", end="", flush=True)
        for chunk in response:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                full += content
        print()
        return full
    else:
        return response.choices[0].message.content


def run_loop(goal: str, resume: bool = True):
    client = get_client()
    state = load_state() if resume else {"goal": goal, "completed_steps": [], "current_plan": "", "conversation": [], "iteration": 0, "created_at": datetime.now().isoformat()}
    
    if not state["goal"]:
        state["goal"] = goal
    
    fable5 = load_fable5_prompt()
    soul = load_soul_prompt()
    agents = load_agents_brief()
    
    system_prompt = f"""You are an autonomous goal-oriented agent running in a loop
(aligned with Fable offline loops + Hermes-style self-stop).

Your job is to achieve the user's goal through repeated work + self-verification.

CORE RULES:
- You are running as a LOOP, not a single response. Keep working until the goal is fully satisfied.
- After every major output, you will be asked to evaluate whether the OVERALL GOAL is achieved.
- Be extremely honest in self-evaluation. Do not claim success until the goal is genuinely met.
- Use the state to remember what you've already done.
- Never repeat work you've already completed successfully.
- If something fails or is incomplete, diagnose why and fix it in the next iteration.
- Verifier · state · stop (see offline loop agent briefs). Maker ≠ final grader when possible.
- One bounded unit of progress per iteration preferred.

{fable5}

{"--- SOUL ---\n" + soul if soul else ""}

{"--- OFFLINE LOOP AGENTS ---\n" + agents if agents else ""}

CURRENT GOAL:
{state['goal']}

CURRENT STATE:
Completed steps: {state['completed_steps']}
Current plan: {state['current_plan']}

You must respond in this exact format for every turn:

**Next Action:**
[One clear concrete thing you will do right now]

**Output / Work:**
[Do the actual work here — write code, research, fix, create files, etc. Be thorough.]

**Self-Check Question:**
[What question will you ask yourself to verify progress?]

Then stop and wait for the next cycle where you will be told if the goal is met.
"""

    messages = [
        {"role": "system", "content": system_prompt}
    ]
    
    # Restore previous conversation if resuming
    if state["conversation"]:
        messages.extend(state["conversation"])
        print(f"\n🔄 Resuming from iteration {state['iteration']} | Goal: {state['goal'][:80]}...")
    else:
        print(f"\n🚀 Starting new goal loop")
        print(f"Goal: {state['goal']}")
        print(f"Max iterations: {MAX_ITERATIONS}")
        print("-" * 60)
    
    iteration = state["iteration"]
    
    while iteration < MAX_ITERATIONS:
        iteration += 1
        state["iteration"] = iteration
        print(f"\n{'='*60}")
        print(f"ITERATION {iteration} / {MAX_ITERATIONS}")
        print(f"{'='*60}")
        
        # Get next action from model
        response = call_model(client, messages)
        
        # Save this turn
        state["conversation"].append({"role": "assistant", "content": response})
        
        # Self-evaluation turn
        eval_messages = messages + [
            {"role": "assistant", "content": response},
            {"role": "user", "content": f"""Now do a strict self-evaluation.

GOAL: {state['goal']}

Based on everything done so far, answer ONLY in this format:

**Goal Achieved?** YES or NO

**Evidence:**
[Specific evidence from what was just produced that supports your answer]

**What's Still Missing:**
[Be brutally honest — list concrete gaps]

**Next Step Recommendation:**
[If NO, what should happen in the next iteration?]
"""}
        ]
        
        print("\n\033[93m[Self-Check]\033[0m ", end="", flush=True)
        eval_response = call_model(client, eval_messages, temperature=0.2, stream=True)
        
        state["conversation"].append({"role": "user", "content": eval_messages[-1]["content"]})
        state["conversation"].append({"role": "assistant", "content": eval_response})
        
        # Parse the evaluation
        if "**Goal Achieved?** YES" in eval_response or "**Goal Achieved?**  YES" in eval_response:
            print("\n✅ GOAL ACHIEVED — Loop complete!")
            state["completed_steps"].append(f"Iteration {iteration}: Goal met")
            save_state(state)
            print(f"\nFinal state saved to {STATE_FILE}")
            print("You can now review the work. Delete the state file to start a new goal.")
            return
        
        # Update state summary
        state["completed_steps"].append(f"Iteration {iteration}: Work + self-check performed")
        save_state(state)
        
        print(f"\n📝 State saved. Continuing loop...")
    
    print(f"\n⚠️ Reached max iterations ({MAX_ITERATIONS}). Goal may not be fully complete.")
    print("You can resume by running the script again (it will continue from current state).")
    save_state(state)


def main():
    parser = argparse.ArgumentParser(description="Offline Goal Loop Agent")
    parser.add_argument("--goal", type=str, help="Goal to achieve (if not provided, will prompt)")
    parser.add_argument("--fresh", action="store_true", help="Start fresh (ignore existing state)")
    args = parser.parse_args()
    
    print("╔════════════════════════════════════════════════════════════╗")
    print("║           OFFLINE GOAL LOOP AGENT — POWERED BY DAZZA       ║")
    print("║   Local • Autonomous • Self-Checking • No Cloud Limits     ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    if args.goal:
        goal = args.goal
    else:
        print("\nWhat goal do you want the loop to achieve?")
        print("Be as specific as possible (e.g. 'Build and test a complete FastAPI todo app with auth')")
        goal = input("\nGoal: ").strip()
        if not goal:
            print("No goal provided. Exiting.")
            return
    
    resume = not args.fresh
    run_loop(goal, resume=resume)


if __name__ == "__main__":
    main()