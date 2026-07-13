# Offline automatic prompt generator — framework

Local tool to generate **elite system prompts** for multi-agent swarms using Ollama (or any OpenAI-compatible endpoint). Part of Fable Offline: Fable5 rigour → loop execution → swarm orchestration → **prompt generation**.

## Entry points

| Surface | Example |
|---------|---------|
| Script | `python auto_prompt_generator.py` (interactive) |
| Script CLI | `python auto_prompt_generator.py --quant` |
| Fable CLI | `python fable5_offline_agent.py --prompt-gen quant` |
| Chat | `/prompt-gen quant` · `/prompt-gen list` · `/prompts` |
| Automate | `--automate prompt-gen-quant` |
| Skill | `skills/prompt-generator.md` |
| Agent brief | `agents/prompt-generator-agent.md` |

## Modes

### 1. Quant research swarm (built-in)

Six agents (sequential handoff):

1. `01_Idea_Generator` — research tickets from papers  
2. `02_Feature_Engineer` — clean features, no look-ahead  
3. `03_Backtester` — costs, Sharpe, drawdown  
4. `04_Validator` — statistical rigor; **never generated the signal**  
5. `05_Regime_Auditor` — multi-regime survival  
6. `06_Factor_Decomposer` — residual alpha vs known factors  

Also writes `00_Swarm_Overview.md` + `swarm_config.json`.

### 2. Custom swarm

Describe the swarm in one sentence; model proposes N roles (2–12), then generates one `.md` prompt each under `generated_prompts/swarm_<slug>_<timestamp>/`.

### 3. Single agent

One specialized role → `Single_Agent_<name>.md`.

## Prompt structure (meta template)

Every generated file should contain:

- **Role** · **Core Responsibilities**  
- **Input Contract** · **Output Contract**  
- **Rigour Rules** (Fable5)  
- **Self-Verification**  
- **Stopping Conditions**  
- **Anti-Failure Rules**  

## Model quality

- Larger local models (e.g. 70B-class) produce better prompts.  
- Default Fable model may be smaller (`qwen2.5:7b`) — acceptable for structure, review/edit after.  
- Override: `FABLE5_MODEL` or `PROMPT_GEN_MODEL` or `--model` on the script.

## Output location

| Env | Default |
|-----|---------|
| `FABLE5_PROMPT_GEN_DIR` / `PROMPT_GEN_OUT` | `generated_prompts/` |

Local bulk output is typically **gitignored** — ship the generator + skill/knowledge, not every swarm dump.

## Handoff into Fable

1. Generate → open `00_Swarm_Overview.md`  
2. Run agents in order; each Output Contract feeds the next Input  
3. Prefer `/hermes` or `/engineer` with LOOP_STATE for multi-cycle work  
4. Use `/team` for research→write→critic on a single deliverable  
5. Optional: copy stable prompts into `agents/` or `skills/` after human edit  

See `agents/shared-state.md`.

## Related files

- `auto_prompt_generator.py`  
- `README_Automatic_Prompt_Generator.md`  
- `skills/prompt-generator.md`  
- `agents/prompt-generator-agent.md`  
- `workflows/prompt-gen-quant.json`  

## Disclaimer

Quant swarm prompts are for **research process design** offline. Not investment advice. Not a live trading system.
