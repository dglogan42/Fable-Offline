# Shared state — how the agent surfaces actually talk to each other

Offline loops and multi-agent modes share **intent** (finish the goal with
verification) but not one single state file. This doc has two parts: the
stores each surface reads/writes, and the four concrete channels agents use
to pass information to each other.

## Communication channels between agents

| Channel | Scope | Used by | Mechanic |
|---------|-------|---------|----------|
| **In-session transcript** | One run, ephemeral | `--commune`, `--team`, `--mbti-feedback` | Each turn's prompt includes the full prior transcript; the next agent/persona reads what came before as its user message. Dies with the process — nothing persists unless written out (see stores below). |
| **Skills bundle (cross-session)** | Persistent, all modes | Everything | `skills/*.md` is loaded into *every* mode's system prompt (12 most-recently-modified files — see `agents/INDEX.md`). A lesson one `--commune` session writes to `skills/commune-*.md` is the newest file on disk, so it's in the top-12 the very next run of `--loop`, `--hermes`, `--team`, or `--commune`. This is the actual "agents learn from each other" mechanism — not a live message bus, a filesystem handoff. |
| **Auto-injection bridge** | Per-cycle, opt-out | `--loop` / `--hermes` / `--engineer` ← `--mbti-feedback` | `AUTO_MBTI_FEEDBACK` (default on) makes `maybe_append_mbti_feedback_prompt()` append an MBTI multi-lens critique block to the loop's own prompt each cycle — the loop agent gets a second, differently-typed perspective folded into its own turn rather than a separate agent call. Disable with `--no-mbti-feedback` or `FABLE5_AUTO_MBTI_FEEDBACK=0`. |
| **Sequential handoff files** | Persistent, one goal | `fable5_offline_agent.py` engineer mode, `offline_goal_loop.py`, prompt-generator swarms | Cycle *n* writes tried/failed/next to a state file; cycle *n+1* (same or different agent instance) reads it before acting. See stores table below. |

None of these are a live inter-process bus — every cross-agent or
cross-session handoff in this repo is either "read the growing transcript
in this call" or "read a file the previous call wrote."

## Stores — Fable 5 (`fable5_offline_agent.py`)

| Store | Path | Role | Written by |
|-------|------|------|------------|
| Loop state (engineer) | `memory/LOOP_STATE.md` | Tried / failed / next | `--engineer` cycles |
| Memory lessons | `memory/`, `memory/lessons/` | RAG corpus | Self-improve / compress paths |
| Commune transcripts | `memory/communicator_sessions/{timestamp}-{topic-slug}.md` (via `result.memory_path`) | Full `--commune` session record | `run_communicator_session()` |
| Skills | `skills/*.md` | Reusable procedures, loaded into every mode | `--commune` synthesizer (`skills/commune-*.md`), self-improve, manual authoring |
| MBTI state | `mbti_state.json` | Active MBTI type + rigour mode, shared between `mbti_personality_agent.py` (standalone) and `--mbti` / `--mbti-feedback` in Fable 5 | `mbti_types.py` (`set_active_type`, `set_rigour`) |
| Program | `program.md` | Engineer constraints | Manual |
| Soul | `SOUL.md` | Identity / Hermes ethics | Manual |
| Agent briefs | `agents/*.md` | See `agents/INDEX.md` for the three loading mechanisms | Manual |
| Generated prompts | `generated_prompts/` | Auto prompt generator output; next swarm agent reads the prior agent's Output Contract as its user message (`FABLE5_PROMPT_GEN_DIR`) | `auto_prompt_generator.py` / `--prompt-gen` |
| Robotics eval artifacts | `workspace/robotics/evals/{suite,detectors,failsafe,report}.md` | Frozen task suite, F1/F2 detector specs, crisis ladder, eval report | `skills/robotics-functionality-tester.md` `write-knowledge` procedure |
| Workspace | `workspace/` | Build artifacts | `--build` and other scaffolders |

## Stores — standalone goal loop (`offline_goal_loop.py`)

| Store | Path | Role |
|-------|------|------|
| JSON state | `loop_state.json` (cwd) | Goal, steps, conversation, iteration |
| Manual | `Fable5_Operating_Manual.md` | Optional rigor core |
| Agent briefs | `agents/*.md` | Loaded when present |

## Handoff tips

1. Prefer **Fable** `/hermes` or `/engineer` for maker≠grader + skills + RAG.
2. Prefer **offline_goal_loop** for simple "keep going on a goal" with JSON resume.
3. Do not assume both share one state file — copy conclusions into `memory/lessons/` if you want Fable RAG to see them.
4. Delete `loop_state.json` or clear `LOOP_STATE` to start clean.
5. **Prompt generator:** `auto_prompt_generator.py` / `--prompt-gen` writes system prompts under `generated_prompts/`. Load each agent `.md` as system (or agent brief); pass prior agent Output Contract as the next user message. Overview + `swarm_config.json` describe order.
6. **Commune → skills:** if you want a `--commune` lesson to influence a *specific* upcoming run rather than "whatever's newest," read `skills/commune-*.md` and reference it explicitly in the goal/topic — don't rely solely on mtime ordering when more than 12 skill files churn between the write and the read.
7. **MBTI feedback is a lens, not a second agent:** `--mbti-feedback` output is a prompt block, not an agent that runs independently — it only has effect once it's appended into a real loop call (automatically via `AUTO_MBTI_FEEDBACK`, or manually by pasting its output into a prompt).

## Privacy

Never put passwords, API keys, Snap/TikTok session cookies, or private feed tokens into state or agent briefs.
