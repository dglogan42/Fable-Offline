# FABLE 5 OFFLINE AGENT — SETUP GUIDE
**By Dazza, straight from the outer suburbs**

G'day legend,

You wanted an offline version of that deadly Fable 5 reasoning prompt from the X post. Here it is — no cloud, no usage limits, no Claude tax. Just pure local rigour on your own hardware.

## What you got here

- `Fable5_Operating_Manual.md` → The full system prompt (the brains)
- `fable5_offline_agent.py` → A dead-simple CLI chat agent that loads it

## Quick Start (5 minutes)

### 1. Install Ollama (if you haven't)

```bash
# Mac / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows → download from https://ollama.com
```

### 2. Pull a strong reasoning model

```bash
ollama serve          # run this in one terminal
ollama pull qwen2.5:72b     # best balance right now (or llama3.1:70b, command-r-plus, deepseek-r1)
```

Bigger model = better reasoning. 70B+ recommended for this style of prompt.

### 3. Install the Python bit

```bash
pip install openai
```

### 4. Run the agent

```bash
python fable5_offline_agent.py
```

That's it. You're now chatting with a local model that thinks like a paranoid accountant crossed with a tradie who double-checks every measurement.

## How to use it properly

- This agent is **deliberately thorough**. It will:
  - Re-derive every number
  - Call out its own assumptions
  - Attack its own answers
  - Lead with the verdict, not the essay

- Use it when accuracy actually matters (code reviews, financials, technical decisions, writing contracts, debugging gnarly bugs).

- For casual yapping, just use normal chat. This mode is heavy on tokens and brainpower.

## Pro tips from Dazza

- Put both files in the same folder. The script auto-loads the .md if it's there.
- Want to tweak the rules? Edit `Fable5_Operating_Manual.md` — the agent reads it fresh every time you start.
- Temperature is set low (0.3) on purpose. Higher = more creative but more likely to bullshit.
- If you want this in VS Code / Cursor, just paste the contents of the .md into your custom instructions or Continue.dev config.

## Alternative frontends (no Python needed)

- **Open WebUI** (best looking): Point it at Ollama and paste the .md as system prompt
- **LM Studio**: Load model → Chat → System Prompt → paste the whole manual
- **SillyTavern** or **AnythingLLM**: Same deal

## Why this exists

The original prompt from @sairahul1 is bloody powerful but designed for Claude (which costs real money and has rate limits). This version runs 100% offline on your rig. You own it forever.

Just remember: with great reasoning power comes great responsibility. Don't use it to write your resignation letter in one go without reading it twice.

## Need help?

If it doesn't work:
1. Is Ollama running? (`ollama list`)
2. Did you pull the model?
3. Is the model name in the script matching what you pulled?

Otherwise hit me up... well, you're on your own now, this is offline mate.

---

**Stay rigorous. Stay local. Stay dangerous.**

*Built with no AI slop — just a bogan who likes things that actually work.*