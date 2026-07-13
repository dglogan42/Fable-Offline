# Offline loop agents — briefing pack

These files **feed Hermes and Fable** (and the standalone goal loop) with shared offline-loop protocol.  
They are loaded into system / cycle context so makers, verifiers, and autonomous loops share the same rules.

| File | Audience | Role |
|------|----------|------|
| `offline-loop-protocol.md` | All loops | Verifier · state · stop; five beats |
| `hermes-agent.md` | `/hermes` · `--hermes` | Soul + RAG + repair + self-stop |
| `fable-loop-agent.md` | `/loop` · `/engineer` · chat loops | Executor/maker + engineer rules |
| `goal-quality.md` | Humans + agents | How to write goals that loops can finish |
| `shared-state.md` | All runners | `LOOP_STATE.md`, `loop_state.json`, memory handoff |

## Load order (harness)

1. Operating Manual (core)  
2. `SOUL.md`  
3. **This pack** (protocol + mode-specific brief)  
4. Skills (when relevant)  
5. Domain knowledge (mode flags)  
6. Retrieved memory / LOOP_STATE (per cycle)  

## Env

| Variable | Default | Meaning |
|----------|---------|---------|
| `FABLE5_AGENTS` | `agents` | Directory of agent briefing files |

## Edit policy

- Keep briefs **short** (harness truncates).  
- Prefer checklists over essays.  
- Do not put secrets or live API keys here.  
