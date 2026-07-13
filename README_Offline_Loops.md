# OFFLINE LOOPS — Autonomous Goal Agent for Local LLMs
**By Dazza — straight from the outer suburbs, no cloud tax**

G'day legend,

This is the offline version of that "Loops" idea from the Raytar post. Instead of babysitting Claude one prompt at a time, you give it a clear **goal** and it keeps working, checking itself, remembering where it left off, and only stops when the job is actually done.

No Claude Code required. Runs 100% local with Ollama (or any OpenAI-compatible local server).

## What this actually is

A **loop** is smarter than a normal chat because it has:

- A clear finish line (the goal)
- Self-checking after every step ("Is this done yet? If not, why?")
- Memory / state so it doesn't forget or repeat work
- The ability to keep going autonomously until it's satisfied the goal

The post was about Claude's built-in `/goal` command. This is the same concept, but running locally on your machine with zero limits and zero cost.

## Files included

- `offline_goal_loop.py` — The actual agent. Give it a goal and watch it work.
- `Fable5_Operating_Manual.md` (from previous) — Optional but recommended. The loop agent can use this for ultra-rigorous thinking.
- `SOUL.md` — Identity / Hermes ethics (loaded when present).
- **`agents/`** — Offline loop briefing pack shared with Fable Hermes/loops:
  - `offline-loop-protocol.md` — verifier · state · stop
  - `hermes-agent.md` · `fable-loop-agent.md` — mode briefs
  - `goal-quality.md` · `shared-state.md` — goals + state handoff
  - `INDEX.md` — load order

Prefer **`python fable5_offline_agent.py --hermes "…"`** or **`--engineer "…"`** when you want maker≠grader + skills + smart RAG. Use `offline_goal_loop.py` for a simple JSON-resume autonomous loop that still loads `agents/`.

## Quick Start

```bash
# 1. Ollama running with a strong model
ollama serve
ollama pull qwen2.5:72b   # or your best reasoning model

# 2. Install deps
pip install openai

# 3. Run the loop agent
python offline_goal_loop.py
```

Then just type your goal when it asks, e.g.:

> "Write a complete, well-tested Python script for a todo list app with FastAPI + SQLite. Include tests and README."

It will start working, check its own output, fix issues, and keep going until it believes the goal is met.

## How the loop works (the five beats)

Every cycle the agent does:

1. **Find the work** — Looks at current state + goal, decides the next concrete task
2. **Do it** — Produces the output / code / research / fix
3. **Check itself** — A separate evaluation: "Is the overall goal actually satisfied right now?"
4. **Remember** — Saves what was done + current plan to `loop_state.json`
5. **Go again** — If not done, repeats. If done, stops and shows final summary.

This is exactly what the post described — except it runs on your local model forever.

## Pro tips from Dazza

- Use **strong models** (70B+). Weaker models get lost in long loops.
- Be **specific** with your goal. "Make a good app" is vague. "Build a FastAPI todo app with user auth, tests, and Docker" is a proper goal.
- The agent saves `loop_state.json` in the same folder. Delete it to start fresh.
- You can interrupt with Ctrl+C and it will resume from where it left off next time (thanks to state).
- For coding tasks, run it in a project folder — it can create/edit files if you give it the right instructions.
- Combine with the Fable5 manual (previous agent) for even more rigorous self-checking.

## When to use loops vs normal chat

**Use a loop when:**
- The job has many small pieces
- It needs verification or fixing (tests, sources, consistency)
- You want it to keep going overnight or while you do other things
- The task is repeatable or has a clear "done" state

**Don't use a loop when:**
- It's a one-shot question
- The goal is vague ("make my life better")
- You want creative brainstorming (normal chat is better)

## Advanced: Running on a schedule

Once you're happy with a loop, you can wrap the script in a simple cron job or systemd timer so it wakes up, does its thing, and goes back to sleep.

Example (Linux):
```bash
# Run every morning at 7am
0 7 * * * cd /path/to/agent && python offline_goal_loop.py --goal "Triage my inbox notes and update the priority list" --auto
```

## Why this matters

The post's big point: prompting is doing the work yourself.  
Loop engineering is **managing the worker**.

With this offline version, you now have a tireless local employee that never gets bored checking links, running tests, or fixing its own mistakes.

Download the script, give it a real goal, and watch what happens.

First time you come back and it's finished something properly while you were at the pub... that's the moment you stop typing one prompt at a time.

Stay dangerous. Stay local.

**Dazza** 🦘

---

*Built for legends who want their AI to actually finish the bloody job.*