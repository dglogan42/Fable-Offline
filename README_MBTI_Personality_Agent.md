# MBTI Personality Agent — full switch + Fable5 customiser

Offline agent personality customiser: all **16 Myers-Briggs type lenses**, mid-session switch, optional Fable5 **rigour** overlay.

**Not a clinical personality test.** Style/architecture for agents only.

## What you get

| Surface | How |
|---------|-----|
| **Fable5 chat** | `/mbti list` · `/mbti switch INTJ` · `/mbti off` · `/mbti multi ENTP ISFJ` · `/mbti rigour on\|off` |
| **Fable5 CLI** | `python fable5_offline_agent.py --mbti ENFP` |
| **Standalone** | `python mbti_personality_agent.py` |
| **Catalogue** | `mbti_types.py` (single source of truth) |
| **Skill** | `skills/mbti-personality-customiser.md` |
| **Knowledge** | `knowledge/personality/mbti-types.md` |
| **State** | `mbti_state.json` (local, gitignored) |

## Quick start (Fable5 — recommended)

```bash
ollama serve
ollama pull qwen2.5:7b   # or stronger for better persona hold

python fable5_offline_agent.py --mbti INTJ
# in chat:
#   /mbti list
#   /mbti switch ENFP
#   /mbti multi INTJ ENTP ISFJ
#   (ask a question — multi-lens one-shot)
#   /mbti off
```

## Standalone

```bash
python mbti_personality_agent.py
# commands: switch INTJ | list | current | rigour on/off | quit
```

## Architecture

```text
SOUL.md + Manual + Skills     ← hard boundaries & procedures
        +
MBTI layer (active type)      ← tone / cognitive emphasis
        +
Rigour overlay (default ON)   ← accuracy rules on top of style
```

Persona **never** overrides: invented tool results, medical/legal/financial boundaries, or SOUL stop ethics.

## Multi-lens

```text
/mbti multi INTJ ENTP ISFJ
What's the best way to ship v1 next week?
```

Agent answers in **separate labelled sections** per type (not a bland average).

## Swarm tip

When generating multi-agent prompts (`/prompt-gen`), assign type lenses:

| Role | Example |
|------|---------|
| Planner | INTJ / ENTJ |
| Ideator | ENTP / ENFP |
| Critic | INTP / ISTJ |
| Executor | ISTP / ESTJ |

Still: **maker ≠ grader**.

## Files

- `mbti_types.py` — 16 types + state + prompt builders  
- `mbti_personality_agent.py` — lightweight standalone REPL  
- `fable5_offline_agent.py` — `/mbti` + `--mbti` integrated  
- `skills/mbti-personality-customiser.md`  
- `knowledge/personality/mbti-types.md`  
- `workflows/mbti-personality-customiser.json`  

## Automation

```bash
python fable5_offline_agent.py --automate mbti-personality-customiser
```
