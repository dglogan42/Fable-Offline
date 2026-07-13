# AUTOMATIC PROMPT GENERATOR — Build Elite Agent Swarms in Minutes
**By Dazza — no more manually writing 2000-word system prompts like a mug**

G'day legend,

The last post was about building a **six-agent quant research swarm** that hunts alpha while you sleep.

The hard part isn't the architecture — it's writing **excellent, specialized system prompts** for each agent so they actually do their job properly without babysitting.

Writing good prompts for Idea Generator, Validator, Regime Auditor etc. is painful and time-consuming.

So I built you this: an **Automatic Prompt Generator** that does it for you.

## What this tool actually does

You tell it what kind of swarm or agent you want (or pick from the built-in quant research swarm), and it spits out:

- High-quality, detailed system prompts for every agent in the swarm
- Ready-to-use .md files you can drop straight into Slate, the offline_goal_loop.py, LM Studio, Open WebUI, etc.
- Prompts that incorporate:
  - Fable 5 rigour (re-derive, self-attack, label guesses)
  - Loop best practices (self-checking, clear stopping conditions, state awareness)
  - Swarm principles (specialization, maker-checker split, no one agent doing everything)

It can generate prompts for **any domain**, not just quant finance.

## Files included

- `auto_prompt_generator.py` — The generator itself (runs offline with your local LLM)
- `skills/prompt-generator.md` — Fable skill (plan / architect / handoff)
- `knowledge/swarm/prompt-generator.md` — Framework notes
- `agents/prompt-generator-agent.md` — Loop brief for Hermes/Fable
- `workflows/prompt-gen-*.json` — Automate recipes
- This README

## Quick Start

```bash
# Make sure Ollama is running
ollama serve
ollama pull qwen2.5:7b      # or a stronger model for better prompts
# ollama pull qwen2.5:72b

pip install openai

# Interactive
python auto_prompt_generator.py

# Non-interactive
python auto_prompt_generator.py --quant
python auto_prompt_generator.py --swarm "4-agent technical blog team" --agents 4
python auto_prompt_generator.py --agent "Rigorous code reviewer"
python auto_prompt_generator.py --list
```

### Fable Offline integration

```bash
python fable5_offline_agent.py --prompt-gen quant
python fable5_offline_agent.py --prompt-gen "swarm: research + write + fact-check"
python fable5_offline_agent.py --prompt-gen "agent: strict PR reviewer"
python fable5_offline_agent.py --prompt-gen list
python fable5_offline_agent.py --automate prompt-gen-quant

# In chat
# /prompt-gen quant
# /prompt-gen swarm: 4-agent blog team
# /prompts
```

Then choose (interactive menu):

1. Generate the **full 6-agent Quant Research Swarm** (from the post)
2. Generate prompts for a **custom swarm** you describe
3. Generate a single specialized agent prompt
4. List existing `generated_prompts/`

It writes clean `.md` files under `generated_prompts/` (configurable via `FABLE5_PROMPT_GEN_DIR`).

## Example: The Quant Research Swarm it can generate

Running option 1 gives you ready-made prompts for:

- `01_Idea_Generator.md`
- `02_Feature_Engineer.md`
- `03_Backtester.md`
- `04_Validator.md` (the rigorous one — uses strongest model)
- `05_Regime_Auditor.md`
- `06_Factor_Decomposer.md`
- `swarm_overview.md` + `swarm_config.json`

Each prompt already includes:
- Clear role + responsibilities
- Input/output contracts
- Self-verification rules
- Anti-hallucination / rigour instructions (Fable5 style)
- How to handle state and pass work to the next agent
- Stopping conditions

## Why this is bloody useful

Before: You spend 2-3 hours writing one good agent prompt.

Now: You describe the swarm in one sentence and get 6 elite prompts in under a minute.

Then you can feed those prompts straight into:
- Fable Offline: `/hermes`, `/engineer`, `/team`
- `agents/*.md` briefs (after human edit)
- The `offline_goal_loop.py` runner
- Slate Programs, LM Studio, Open WebUI, or any local agent runner

This closes the loop on the whole series:
Fable5 rigour → Loop execution → Swarm orchestration → Automatic prompt generation for the swarm

## Pro tips from Dazza

- Use a strong model (70B+) when generating prompts — better prompts come from better models.
- After it generates the swarm, you can go back and say "make the Validator even stricter on overfitting" and it will regenerate just that one with improvements.
- The generated prompts are designed to work together — outputs of one become clean inputs for the next.
- For non-quant use cases, just describe what you want, e.g. "Build a 4-agent swarm for writing high-quality technical blog posts with research + editing + fact-checking + SEO optimization"

## Failure modes this generator helps you avoid

The original post listed 5 failure modes. This tool bakes in protections against most of them by default:
- Maker-checker split (different agents for generation vs validation)
- Strong self-verification in every prompt
- Clear stopping conditions
- State awareness instructions
- Specialization (each agent gets one job only)

## Next level

Once you have the generated prompts, you can drop them into the `offline_goal_loop.py` and have a fully autonomous local swarm running on your machine.

Or use them in Slate if you want the fancy terminal UI and parallel execution.

Either way — you stop writing prompts by hand.

You become the architect.

---

**Download the generator, run it, and in 60 seconds you'll have better agent prompts than most people write in a week.**

Stay dangerous. Stay building.

**Dazza** 🦘

*This one was cooked up after reading that quant swarm post at 3am. You're welcome.*