# Shared state — Hermes, Fable, offline goal loop

Offline loops share **intent** (finish the goal with verification) but may use different files.

## Fable 5 (`fable5_offline_agent.py`)

| Store | Path | Role |
|-------|------|------|
| Loop state (engineer) | `memory/LOOP_STATE.md` | Tried / failed / next |
| Memory lessons | `memory/`, `memory/lessons/` | RAG corpus |
| Skills | `skills/*.md` | Reusable procedures |
| Program | `program.md` | Engineer constraints |
| Soul | `SOUL.md` | Identity / Hermes ethics |
| Agent briefs | `agents/*.md` | This pack |
| Generated prompts | `generated_prompts/` | Auto prompt generator output (`FABLE5_PROMPT_GEN_DIR`) |
| Workspace | `workspace/` | Build artifacts |

## Standalone goal loop (`offline_goal_loop.py`)

| Store | Path | Role |
|-------|------|------|
| JSON state | `loop_state.json` (cwd) | Goal, steps, conversation, iteration |
| Manual | `Fable5_Operating_Manual.md` | Optional rigor core |
| Agent briefs | `agents/*.md` | Loaded when present |

## Handoff tips

1. Prefer **Fable** `/hermes` or `/engineer` for maker≠grader + skills + RAG.  
2. Prefer **offline_goal_loop** for simple “keep going on a goal” with JSON resume.  
3. Do not assume both share one state file — copy conclusions into `memory/lessons/` if you want Fable RAG to see them.  
4. Delete `loop_state.json` or clear LOOP_STATE to start clean.  
5. **Prompt generator:** `auto_prompt_generator.py` / `--prompt-gen` writes system prompts under `generated_prompts/`. Load each agent `.md` as system (or agent brief); pass prior agent Output Contract as the next user message. Overview + `swarm_config.json` describe order.  

## Privacy

Never put passwords, API keys, Snap/TikTok session cookies, or private feed tokens into state or agent briefs.