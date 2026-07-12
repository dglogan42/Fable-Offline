# Fable 5 Offline Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](#platforms)
[![Python](https://img.shields.io/badge/python-3.10%2B-yellow.svg)](#requirements)

Local, **no-cloud** reasoning agent with **loop engineering**, **self-improving skills**, and **Hermes-style behaviors**.  
Runs on **Windows · macOS · Linux** against any OpenAI-compatible API (default: [Ollama](https://ollama.com)).

| Mode | What it does |
|------|----------------|
| **Chat** | Fable 5 Operating Manual: re-derive numbers, label guesses, attack your own answer, verdict first |
| **Loop** | Goal cycles: executor → **fresh-context verifier** → memory → stop rules (**maker ≠ grader**) |
| **Self-improve** | Reflect → propose **skills** → grade in fresh context → write `skills/` (system compounds; **weights do not**) |
| **Hermes** | Soul-steered loop: **SOUL.md** · smart RAG (top-K memory) · self-stop · live repair · memory compress |

Once a local model is loaded, everything stays offline — no API keys, no usage meters.

The *system* around the model improves (soul, memory, skills), not the model weights.

**Repository:** [github.com/dglogan42/Fable-Offline](https://github.com/dglogan42/Fable-Offline)

## Platforms

| OS | Install | Run |
|----|---------|-----|
| **Windows** | `powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1` | `.\fable5.cmd` |
| **macOS** | `chmod +x fable5 scripts/*.sh && ./scripts/install.sh` | `./fable5` |
| **Linux** | `chmod +x fable5 scripts/*.sh && ./scripts/install.sh` | `./fable5` |
| **Any** | `python -m pip install -r requirements.txt` | `python fable5_offline_agent.py` |

Cross-platform: UTF-8 consoles, `pathlib` paths, `~` expansion, LF memory files, Python discovery (`python` / `python3` / `py -3`), `--doctor` health checks.

## Repository layout

```
Fable-Offline/
├── fable5_offline_agent.py      # CLI: chat, loop, hermes, self-improve, doctor
├── Fable5_Operating_Manual.md   # System prompt (reasoning + loops + hermes + skills)
├── SOUL.md                      # Hermes-style identity / steering
├── requirements.txt
├── fable5                       # Unix launcher
├── fable5.cmd                   # Windows launcher
├── scripts/
│   ├── install.sh / install.ps1
│   └── fable5.sh / fable5.ps1
├── skills/                      # Skill library (seeds + self-improved)
│   ├── INDEX.md
│   ├── hermes-loop.md
│   └── rederive-numbers.md
├── memory/                      # Runtime only (gitignored; .gitkeep kept)
├── LICENSE                      # MIT — Copyright (c) 2026 David Logan
├── .gitignore
├── .gitattributes
└── README.md
```

## Requirements

- **Python 3.10+** on `PATH`
- **Ollama** (or any OpenAI-compatible server, default `http://localhost:11434/v1`)
- A local chat model — larger models produce better loops and skills

```bash
python -m pip install -r requirements.txt
```

## Quick start

### 1. Install Ollama and a model

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh   # or: brew install ollama
ollama serve
ollama pull qwen2.5:7b      # ~12 GB RAM
# ollama pull qwen2.5:72b   # 48 GB+ RAM
```

Windows: [ollama.com/download](https://ollama.com/download), start the app, then `ollama pull qwen2.5:7b`.

### 2. Install the agent

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1

# macOS / Linux
./scripts/install.sh
```

### 3. Run

```bash
# Windows
.\fable5.cmd
.\fable5.cmd --doctor
.\fable5.cmd --hermes "Re-derive: revenue $4.0M to $4.2M is a 20% gain"
.\fable5.cmd --improve

# macOS / Linux
./fable5
./fable5 --doctor
./fable5 --hermes "Re-derive: revenue $4.0M to $4.2M is a 20% gain"
./fable5 --improve
```

## Chat commands

| Input | Action |
|-------|--------|
| *(any question)* | One-shot rigorous answer (+ light smart RAG) |
| `/loop <goal>` | Multi-cycle loop (+ self-improve after, by default) |
| `/hermes <goal>` | Hermes loop: soul + smart RAG + live repair + self-stop |
| `/improve [focus]` | Self-improve: write verified skills from memory |
| `/skills` | List / show skill library |
| `/soul` | Show SOUL.md |
| `/compress [focus]` | Compress memory into a durable note |
| `/memory` | Show loop memory index |
| `/doctor` | OS / Python / backend check |
| `/help` | Command list |
| `quit` · `exit` · `q` | Leave |

## Hermes mode

```bash
./fable5 --hermes "Re-derive every claim and stop when verified"
# Windows: .\fable5.cmd --hermes "…"
```

| Behavior | Offline implementation |
|----------|------------------------|
| **SOUL.md** | Identity + boundaries loaded every turn |
| **Smart RAG** | Top-K (`FABLE5_RAG_TOP_K`, default **20**) relevant memory chunks — not the whole archive |
| **Self-stop** | Success / retry ceiling / cycle budget |
| **Live repair** | On verifier FAIL → strategy patch for the **next unit only** |
| **Memory compress** | After multi-cycle Hermes runs → `memory/lessons/compressed-*.md` |
| **Skills** | Optional self-improve writes reusable procedures |

Edit `SOUL.md` to change persona and stop ethics. Quality of soul ≈ quality of compounding.

## Self-improvement (skills)

```bash
./fable5 --improve
./fable5 --improve "numeric and financial claims"
./fable5 --compress-memory
```

Flow: memory + cycles → improver proposes skills → fresh-context skill verifier → write `skills/*.md` → next run loads them into the system prompt.

Disable post-loop improve: `--no-self-improve` or `FABLE5_SELF_IMPROVE=0`.

## Loop mode

```
Trigger → Rules + memory (+ RAG if Hermes) → Executor (1 unit) → Verifier (fresh)
        → [on FAIL + Hermes: live repair] → stop or continue
        → optional compress + self-improve
```

```bash
./fable5 --loop "One-page risk memo on shipping feature X" --max-cycles 6
```

Runtime artifacts: `memory/` (`INDEX.md`, `cycle_*.md`, `lessons/`) — **gitignored**.

## Configuration

| Variable | Default | Meaning |
|----------|---------|---------|
| `FABLE5_MODEL` | `qwen2.5:7b` | Model name (`ollama list`) |
| `FABLE5_BASE_URL` | `http://localhost:11434/v1` | OpenAI-compatible base URL |
| `FABLE5_MEMORY` | `memory` | Memory directory (`~` allowed) |
| `FABLE5_SKILLS` | `skills` | Skill library directory |
| `FABLE5_SOUL` | `SOUL.md` | Identity / steering file |
| `FABLE5_RAG_TOP_K` | `20` | Smart RAG chunk count |
| `FABLE5_SELF_IMPROVE` | `1` | Self-improve after loops (`0` to disable) |
| `FABLE5_MAX_CYCLES` | `6` | Loop cycle budget |
| `FABLE5_RETRY_CEILING` | `3` | Stop after N similar failures |
| `FABLE5_TEMPERATURE` | `0.3` | Sampling temperature |
| `FABLE5_ASCII` | unset | `1` = ASCII-only UI |
| `FABLE5_PYTHON` | unset | Force Python executable path |
| `FABLE5_MANUAL` | `Fable5_Operating_Manual.md` | System prompt path |
| `FABLE5_API_KEY` | `ollama` | API key (ignored by Ollama) |

```bat
REM Windows cmd
set FABLE5_MODEL=qwen2.5:7b
.\fable5.cmd --hermes "your goal"
```

```powershell
# Windows PowerShell
$env:FABLE5_MODEL = "qwen2.5:7b"
.\scripts\fable5.ps1 --hermes "your goal"
```

```bash
# macOS / Linux
export FABLE5_MODEL=qwen2.5:7b
./fable5 --hermes "your goal"
```

**CLI flags:** `--model` · `--loop` · `--hermes` · `--improve` · `--compress-memory` · `--self-improve` · `--no-self-improve` · `--max-cycles` · `--retry-ceiling` · `--success` · `--doctor` · `--ascii`

## Troubleshooting

```bash
python fable5_offline_agent.py --doctor
```

| Symptom | Fix |
|---------|-----|
| `No module named openai` | `python -m pip install -r requirements.txt` |
| Backend unreachable | Start Ollama; `ollama list`; confirm port `11434` |
| Garbled box characters | `--ascii` or `FABLE5_ASCII=1` |
| `python` not found (Windows) | Use `py -3` or reinstall with PATH enabled |
| `Permission denied: ./fable5` | `chmod +x fable5 scripts/*.sh` |
| Slow first reply / cycle | Model loading into RAM/VRAM — expected |

## When to use it

| Prefer | For |
|--------|-----|
| **Chat** | Single decisions, code review, re-deriving a figure |
| **Loop** | Multi-step goals, graded multi-claim work |
| **Hermes** | Long goals needing selective memory, live repair, self-stop |
| **Self-improve** | Encoding durable procedures after loops or failures |

Skip this stack for casual chat when speed matters more than rigor.

## Credits

- **Reasoning rules** — Fable 5–style rigorous operating manual (community prompt lineage).
- **Loop engineering** — Goals, boundaries, verification, fresh-context graders, stop rules.
- **Self-improvement** — Memory + skills compound around a frozen local model.
- **Hermes behaviors** — Soul file, smart RAG, self-stopping loops, live repair, memory compression (offline adaptation of self-building agent practice).

## License

This project is free software under the **[MIT License](LICENSE)**.

Copyright © **2026 David Logan**.

You may use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, provided the copyright and permission notice are included. The Software is provided **“AS IS”**, without warranty of any kind.
