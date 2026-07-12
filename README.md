# Fable 5 Offline Agent

Local, **no-cloud** reasoning agent with a **loop-engineering harness**.  
Runs on **Windows · macOS · Linux** against any OpenAI-compatible API (default: [Ollama](https://ollama.com)).

| Mode | What it does |
|------|----------------|
| **Chat** | Applies the Fable 5 Operating Manual: re-derive numbers, label guesses, attack your own answer, verdict first |
| **Loop** | Goal-directed cycles: executor → **fresh-context verifier** → memory → stop rules (**maker ≠ grader**) |

Once a local model is loaded, everything stays offline—no API keys, no usage meters.

## Platforms

| OS | Install | Run |
|----|---------|-----|
| **Windows** | `powershell -ExecutionPolicy Bypass -File .\scripts\install.ps1` | `.\fable5.cmd` |
| **macOS** | `chmod +x fable5 scripts/*.sh && ./scripts/install.sh` | `./fable5` |
| **Linux** | `chmod +x fable5 scripts/*.sh && ./scripts/install.sh` | `./fable5` |
| **Any** | `python -m pip install -r requirements.txt` | `python fable5_offline_agent.py` |

Built-in cross-platform behavior: UTF-8 consoles, `pathlib` paths, `~` expansion, LF memory files, Python discovery (`python` / `python3` / `py -3`), and `--doctor` health checks.

## Repository layout

```
Fable/
├── fable5_offline_agent.py      # CLI: chat, /loop, --doctor
├── Fable5_Operating_Manual.md   # System prompt (reasoning + loops)
├── requirements.txt
├── fable5                       # Unix launcher
├── fable5.cmd                   # Windows launcher
├── scripts/
│   ├── install.sh / install.ps1
│   └── fable5.sh / fable5.ps1
├── memory/                      # Runtime only (gitignored)
├── LICENSE                      # MIT
├── .gitignore
├── .gitattributes
└── README.md
```

## Requirements

- **Python 3.10+** on `PATH`
- **Ollama** (or any server exposing an OpenAI-compatible API, default `http://localhost:11434/v1`)
- A local chat model — larger models produce better loops

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

Windows: install from [ollama.com/download](https://ollama.com/download), start the app, then `ollama pull qwen2.5:7b`.

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
.\fable5.cmd --loop "Re-derive: revenue $4.0M to $4.2M is a 20% gain"

# macOS / Linux
./fable5
./fable5 --doctor
./fable5 --loop "Re-derive: revenue $4.0M to $4.2M is a 20% gain"
```

## Chat commands

| Input | Action |
|-------|--------|
| *(any question)* | One-shot rigorous answer |
| `/loop <goal>` | Multi-cycle loop harness |
| `/memory` | Show loop memory index |
| `/doctor` | OS / Python / backend check |
| `/help` | Command list |
| `quit` · `exit` · `q` | Leave |

## Loop mode

```
Trigger → Rules + memory → Executor (1 unit) → Verifier (fresh context)
        → Write memory → success | retry ceiling | budget | continue
```

```bash
./fable5 --loop "One-page risk memo on shipping feature X" \
  --max-cycles 6 \
  --success "Verdict, three risks, one recommendation; numbers re-derived"
```

Runtime artifacts land in `memory/` (`INDEX.md`, `cycle_*.md`, `lessons/`).

## Configuration

| Variable | Default | Meaning |
|----------|---------|---------|
| `FABLE5_MODEL` | `qwen2.5:7b` | Model name (`ollama list`) |
| `FABLE5_BASE_URL` | `http://localhost:11434/v1` | OpenAI-compatible base URL |
| `FABLE5_MEMORY` | `memory` | Memory directory (`~` allowed) |
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
.\fable5.cmd --loop "your goal"
```

```powershell
# Windows PowerShell
$env:FABLE5_MODEL = "qwen2.5:7b"
.\scripts\fable5.ps1 --loop "your goal"
```

```bash
# macOS / Linux
export FABLE5_MODEL=qwen2.5:7b
./fable5 --loop "your goal"
```

**CLI flags:** `--model` · `--max-cycles` · `--retry-ceiling` · `--success` · `--doctor` · `--ascii`

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
| **Chat** | Single decisions, code review, re-deriving a figure, careful rewrites |
| **Loop** | Multi-step goals, “keep going until…”, claim clusters that need independent grading |

Skip this stack for casual chat when speed matters more than rigor.

## Credits

- **Reasoning rules** — Fable 5–style rigorous operating manual (community prompt lineage).
- **Loop engineering** — Goals, boundaries, verification, fresh-context graders, and stop rules, adapted for fully local OpenAI-compatible runtimes.

## License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE).

Copyright © 2026 David Logan.
