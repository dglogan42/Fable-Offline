# Offline prompt generator (swarm / agent system prompts)

**WHEN_TO_USE:** User wants **system prompts for multi-agent swarms** or a specialized agent without writing them by hand — **`/prompt-gen`**, **`--prompt-gen`**, `/automate prompt-gen-*`, or “generate agent prompts offline.”

Companion: `auto_prompt_generator.py` (Ollama/OpenAI-compatible). Output: `generated_prompts/` (or `FABLE5_PROMPT_GEN_DIR`).  
Creative writing prompts: skill **`manga-anime-fanfic-prompt-kit`** + `scripts/manga_fanfic_prompt.py` (offline scaffolds; no novel piracy).

## Stance
You design **specialized, handoff-ready** agent prompts. Each agent has **one job**, clear **I/O contracts**, **self-verification**, **stopping conditions**, and **Fable5 rigour** (re-derive, label guesses, attack conclusions). Prefer **maker ≠ checker** across the swarm.

Not financial advice when shipping the quant research swarm. Generated prompts are starting points — human review before production trading or safety-critical use.

---

## Slash / intent map

| User intent | Action |
|-------------|--------|
| `/prompt-gen` · help | **plan** — explain modes + CLI |
| `/prompt-gen quant` | Run generator: 6-agent quant swarm |
| `/prompt-gen swarm: …` | Custom swarm from description |
| `/prompt-gen agent: …` | Single elite agent prompt |
| `/prompt-gen list` · `/prompts` | List files under `generated_prompts/` |
| Design-only (no files) | **architect** — role breakdown + contracts (chat) |
| After files exist | **handoff** — how to wire into Hermes/team |

---

## Procedures

### plan
Explain:
1. **quant** — fixed 6-agent alpha research pipeline  
2. **swarm:** free-text → N specialized roles (default 4)  
3. **agent:** one role  
4. Prefer a **strong local model** for generation quality  
5. Artifacts land in `generated_prompts/` (+ optional `swarm_*/` subfolders)  

### architect
When the user wants design without calling the generator yet:
1. Split the goal into 3–6 agents (specialization)  
2. Name them `01_…` … `0N_…`  
3. For each: Role · Input · Output · Maker vs checker  
4. Draw sequential handoff; mark who validates  
5. Suggest exact `/prompt-gen swarm: …` string  

### generate (runtime — harness)
Harness runs `auto_prompt_generator.py` via `run_prompt_generator()`:
- `--prompt-gen quant`
- `--prompt-gen "swarm: blog team"` + optional `--prompt-gen-agents 4`
- `--prompt-gen "agent: code reviewer"`
- Standalone: `python auto_prompt_generator.py --quant`

### handoff
After generation:
| Target | How |
|--------|-----|
| Fable `/team` | Paste role prompts into research/write/critic or sequential goals |
| Fable `/hermes` · `/engineer` | Goal = “run agent 0k with ticket from previous output”; use LOOP_STATE |
| `agents/*.md` | Copy curated prompts into briefs (do not commit secrets) |
| `offline_goal_loop.py` | Goal + load generated `.md` as system context |
| Slate / LM Studio / Open WebUI | Import `.md` as system prompt |

See `agents/shared-state.md` and `agents/prompt-generator-agent.md`.

### review-prompt
User pastes a generated prompt: check sections (Role, I/O, Rigour, Self-Verification, Stopping, Anti-Failure), tighten fluff, enforce maker≠checker.

---

## Output contract (architect / plan)

1. **Verdict** — which mode to run  
2. **Agent list** (if swarm) with one-line jobs  
3. **Exact CLI / slash** to run next  
4. **Handoff** path into Fable loops  
5. **Risks** — weak model → weak prompts; quant swarm is research hygiene not live trading  

---

## Env

| Variable | Default | Meaning |
|----------|---------|---------|
| `FABLE5_PROMPT_GEN_DIR` | `generated_prompts` | Output root |
| `FABLE5_MODEL` | (agent model) | Used for generation unless overridden |
| `PROMPT_GEN_MODEL` | — | Override model for generator only |

---

## Automation recipes

- `prompt-gen-quant` — full quant swarm files  
- `prompt-gen-custom` — custom swarm from workflow prompt/spec  
- `prompt-gen-plan` — chat plan only (skill guidance)  

---

## Anti-failure

- Do not invent “already generated” files — list or generate  
- Do not put API keys or live trading credentials into prompts  
- Quant Validator must remain **separate** from Idea Generator  
- Generated content is local; prefer gitignore for bulk runs  
