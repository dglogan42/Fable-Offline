# Fable 5 Offline Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](#platforms)
[![Python](https://img.shields.io/badge/python-3.10%2B-yellow.svg)](#requirements)

Local, **no-cloud** agent for **reasoning**, **loops**, **multi-agent teams**, **Hermes**, **self-improving skills**, and **build/automate** — plus a **6-month agentic engineer roadmap**.  
Runs on **Windows · macOS · Linux** against any OpenAI-compatible API (default: [Ollama](https://ollama.com)).

| Mode | What it does |
|------|----------------|
| **Chat** | Fable 5 Operating Manual: re-derive numbers, label guesses, attack your own answer, verdict first |
| **Loop** | Goal cycles: executor → **fresh-context verifier** → memory → stop rules (**maker ≠ grader**) |
| **Self-improve** | Reflect → propose **skills** → grade in fresh context → write `skills/` (system compounds; **weights do not**) |
| **Hermes** | Soul-steered loop: **SOUL.md** · smart RAG (top-K memory) · self-stop · live repair · memory compress |
| **Build** | Multi-file project scaffold under `workspace/build-*/` (PLAN + FILE blocks) |
| **Automate** | Multi-step JSON recipes in `workflows/` (build → hermes → improve → …) |
| **Engineer** | **Loop like an engineer**: purpose once · PLAN→DO→VERIFY · **LOOP_STATE** · stop gates · optional bilevel |
| **Team** | Multi-agent supervisor: **research → write → critic** (HITL optional) |
| **Roadmap** | 6-month agentic engineer path (`ROADMAP.md`) — build real things, order matters |
| **Edge audit** | **Fooled by Randomness** protocol: separate real edge from luck |
| **Broker** | Scrape reg/marketing pages · **broker user model** · claim audit (`knowledge/brokers/`) |
| **Legal** | Contract / NDA / vendor playbook · GREEN/YELLOW/RED flags · briefs & draft responds (`knowledge/legal/`) |
| **Education** | Credential claim audit · accreditation type map · board pathway hygiene (`knowledge/education/`) |

Once a local model is loaded, everything stays offline — no API keys, no usage meters.  
The *system* around the model improves (soul, memory, skills, workflows), not the model weights.

**Prompt vs loop:** a prompt is one instruction. A loop is a goal the agent keeps working toward — discover, plan, do, verify, feed back — until success or a hard limit. Three make-or-break parts: **verifier**, **state**, **stop**.

**Edge vs luck:** the market manufactures convincing hot streaks and backtests by chance. Default verdict on small samples is *insufficient evidence* — treat skill claims as guilty of luck until large, out-of-sample, honestly tested numbers force otherwise.

**Broker mode:** entity-first CFD/forex client model — verify licences on primary registers, distrust “0 pip / 1:300” marketing, no live-order automation without explicit consent. **Not financial advice.**

**Legal mode:** offline playbook-driven contract review, NDA triage, vendor checks, briefs, and templated responses (GREEN/YELLOW/RED). Configure `knowledge/legal/playbook.md`. **Not legal advice** — licensed attorney review required before any real-matter use.

**Education mode:** audits school/degree marketing (who issues the diploma, ASIC vs regional accreditation, state operate licenses, NBHWC/IBLM pathways). Example snapshot: Lifestyle Prescriptions® University in `knowledge/education/lpu-credential-claims.md`. **Not educational or medical advice.**

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
├── fable5_offline_agent.py      # CLI: chat, team, broker, legal, scrape, build, automate…
├── Fable5_Operating_Manual.md   # System prompt (full method)
├── SOUL.md                      # Identity / steering
├── program.md                   # Loop-engineer constraints (Karpathy-style)
├── ROADMAP.md                   # 6-month agentic engineer curriculum
├── requirements.txt
├── fable5 / fable5.cmd          # Launchers
├── scripts/                     # install + platform wrappers
├── skills/                      # Skill library (broker, legal, edge, loops…)
├── workflows/                   # Automation recipes (*.json)
├── knowledge/brokers/           # Curated reg notes (scrapes gitignored)
├── knowledge/legal/             # playbook.md shipped; matters/_local gitignored
├── knowledge/education/         # Credential claim notes (e.g. LPU)
├── workspace/                   # Build + team outputs (gitignored; .gitkeep)
├── memory/                      # Runtime memory / HITL logs (gitignored; .gitkeep)
├── LICENSE                      # MIT — Copyright (c) 2026 David Logan
├── .gitignore                   # Secrets, memory, scrapes, private legal
└── README.md
```

**Do not commit secrets:** `.env`, keys, tokens, raw contract PDFs, and `knowledge/legal/matters/` are gitignored. Ship only the public playbook template and curated notes.


## Requirements

- **Python 3.10+** on `PATH`
- **Ollama** (or any OpenAI-compatible server, default `http://localhost:11434/v1`)
- A local chat model — larger models produce better loops, builds, and skills

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
.\fable5.cmd --build "minimal Python CLI that greets and exits"
.\fable5.cmd --automate daily-review
.\fable5.cmd --engineer "Ship a decision memo" --criteria "Verdict first,Three risks,Numbers checked"
.\fable5.cmd --hermes "Re-derive: revenue $4.0M to $4.2M is a 20% gain"

# macOS / Linux
./fable5
./fable5 --doctor
./fable5 --build "minimal Python CLI that greets and exits"
./fable5 --automate engineer-memo
./fable5 --engineer "Ship a decision memo" --min-score 8
./fable5 --hermes "Re-derive: revenue $4.0M to $4.2M is a 20% gain"
```

## Chat commands

| Input | Action |
|-------|--------|
| *(any question)* | One-shot rigorous answer (+ light smart RAG) |
| `/roadmap` | Show 6-month agentic engineer roadmap |
| `/team <task>` | Multi-agent: research → write → critic |
| `/broker [prompt]` | Broker user-model + claim audit (local knowledge) |
| `/legal [prompt]` | Legal playbook: contract / NDA / vendor / brief / respond |
| `/education [prompt]` | Education/credential claim audit (local knowledge) |
| `/scrape <url>` | Fetch page text into `knowledge/brokers/` |
| `/build <goal>` | Scaffold multi-file project under `workspace/` |
| `/automate <name>` | Run workflow recipe |
| `/workflows` | List automation recipes |
| `/loop <goal>` | Multi-cycle loop (+ self-improve after, by default) |
| `/hermes <goal>` | Hermes loop: soul + smart RAG + live repair + self-stop |
| `/engineer <goal>` | Loop engineer: PLAN→DO→VERIFY · LOOP_STATE · score gates |
| `/improve [focus]` | Self-improve: write verified skills from memory |
| `/skills` | List / show skill library |
| `/soul` | Show SOUL.md |
| `/compress [focus]` | Compress memory into a durable note |
| `/memory` | Show loop memory index |
| `/doctor` | OS / Python / backend check |
| `/help` | Command list |
| `quit` · `exit` · `q` | Leave |

## Build and automate

```bash
./fable5 --build "minimal Python CLI that greets and exits"
./fable5 --automate daily-review
./fable5 --automate rigor-check
./fable5 --automate hello-project
```

| Recipe (seeded) | What it does |
|-----------------|--------------|
| `hello-project` | Build a tiny multi-file hello CLI |
| `daily-review` | Compress memory → self-improve skills |
| `rigor-check` | Short Hermes loop on a numeric claim |
| `engineer-memo` | Loop-engineer a decision memo to score ≥ 8 |
| `edge-audit` | Edge-vs-luck audit (streaks, backtests, “system works” claims) |
| `agentic-checkpoint` | Biweekly: compress → improve → coach next roadmap stage |
| `broker-full-audit` | Scrape EC Markets pages → broker audit + user model + HITL |
| `broker-user-session` | Disciplined retail CFD user coaching |
| `broker-claim-audit` | Engineer scored claim audit |
| `legal-contract-review` | Clause flags GREEN/YELLOW/RED vs playbook + HITL |
| `legal-nda-triage` | NDA pre-screen categories + HITL |
| `legal-vendor-check` | Vendor stack Clear / Conditional / Block |
| `legal-brief` | Daily / topic / incident brief |
| `legal-respond` | Draft DSAR / hold / pushback templates + HITL |
| `education-claim-audit` | Engineer scored school/credential claim audit |
| `lpu-full-audit` | Scrape LPU pages → education claim audit + HITL |

## Broker scrape, user model & audit

```bash
# Scrape regulation / legal pages into knowledge/brokers/
python fable5_offline_agent.py --scrape https://www.ecmarkets.com/legal/
python fable5_offline_agent.py --scrape https://www.ecmarkets.co.nz/regulations-licences/

# Broker user-model + claim audit (uses knowledge/brokers/*.md)
python fable5_offline_agent.py --broker
python fable5_offline_agent.py --automate broker-full-audit
python fable5_offline_agent.py --automate broker-user-session
```

Curated snapshot: `knowledge/brokers/ec-markets-regulation.md` (entity **EC Markets Financial Limited**, co. **2446590**, FSPR **FSP197465**, claimed AFSL **414198**, multi-regulator marketing, leverage inconsistencies 1:30/1:100 vs 1:300). **Re-verify on official registers** before any real decision. Not financial advice.

## Legal playbook (contract / NDA / vendor)

Offline counterpart to playbook-driven legal ops: clause review, NDA triage, vendor checks, briefs, and draft responses. Configure positions in `knowledge/legal/playbook.md`.

```bash
# Edit your standard positions, ranges, and escalation triggers
# knowledge/legal/playbook.md

# Legal mode (paste contract/NDA in the prompt or chat)
python fable5_offline_agent.py --legal "triage-nda: [paste NDA text]"
python fable5_offline_agent.py --legal "review-contract: [paste MSA sections]"

# Workflows
python fable5_offline_agent.py --automate legal-contract-review
python fable5_offline_agent.py --automate legal-nda-triage
python fable5_offline_agent.py --automate legal-vendor-check
python fable5_offline_agent.py --automate legal-brief
python fable5_offline_agent.py --automate legal-respond

# Optional: scrape a public policy page into knowledge/legal/
python fable5_offline_agent.py --scrape https://example.com/terms --scrape-dir legal
```

| Procedure | Output |
|-----------|--------|
| **review-contract** | Verdict + GREEN/YELLOW/RED clause table + redlines |
| **triage-nda** | Standard approval path · Counsel review · Full review |
| **vendor-check** | Clear / Conditional / Block + gaps |
| **brief** | daily / topic / incident memo (sources + unknowns) |
| **respond** | Draft DSAR ack, hold notice, or clause pushback |

**Not legal advice.** All real-matter outputs require licensed attorney review before signature or send.

## Education & credential claim audit

Audits “accredited degree / certification” marketing the same way broker mode audits licences: **type of recognition first**, logos second.

```bash
# Curated LPU snapshot already in repo
python fable5_offline_agent.py --education

# Scrape + full audit workflow
python fable5_offline_agent.py --scrape https://www.lifestyleprescription.tv/accreditation --scrape-dir education
python fable5_offline_agent.py --automate education-claim-audit
python fable5_offline_agent.py --automate lpu-full-audit
```

Example: **Lifestyle Prescriptions® University** (`knowledge/education/lpu-credential-claims.md`) — homepage markets accredited M.A./Ph.D. and IBLM/NBHWC paths; accreditation page cites **ASIC UK**, **Wyoming** proprietary license, **EIU-Paris** degree validation, NBHWC program approval, and **IBLM approval pending**. Snapshot verdict: marketing / insufficient evidence for US-regional-equivalent PhD claims. **Re-verify on primary registers.** Not educational or medical advice.

## Multi-agent team & roadmap

```bash
./fable5 --roadmap
./fable5 --team "Research offline agent evals and write a one-page brief" --format brief
./fable5 --automate agentic-checkpoint
```

Supervisor pattern: **research** → **writer** → **critic** (separate grader, max 3 revisions). HITL prompts on start/ship when `FABLE5_HITL=1` (default).

## Edge audit

```bash
# Chat: describe the strategy, then
./fable5 --automate edge-audit
# or
./fable5 --engineer "Audit this system for edge vs luck: [paste rules + stats]" \
  --criteria "Verdict label correct,Sample/OOS honest,Multiple testing named,Survivorship/costs,What would change mind,Risk of belief now"
```

Workflow step types: `build` · `engineer` · `hermes` · `loop` · `improve` · `compress` · `llm` · `shell` · `note` · `broker` · `legal` · `scrape` · `hitl` · `team`.

Add your own recipes as `workflows/my-job.json`. Private experiments can go in `workflows/_local/` (gitignored).

**Shell automation** is **off by default**. Enable carefully:

```bash
# macOS / Linux
export FABLE5_ALLOW_SHELL=1

# Windows cmd
set FABLE5_ALLOW_SHELL=1
```

Only allowlisted commands run (python/pip/ollama, limited git, simple `ls`/`dir`/`echo`). Builds cannot write outside `workspace/`.

## Loop like an engineer

```bash
./fable5 --engineer "Rewrite this decision memo until it is shippable" \
  --criteria "Verdict first,Three concrete risks,Numbers re-derived or labeled" \
  --min-score 8 --max-cycles 6

# Chat: /engineer <goal>  then optional comma-separated criteria
```

| Piece | Offline implementation |
|-------|------------------------|
| **Verifier** | Fresh-context sub-agent scores each criterion 1–10 (maker ≠ grader) |
| **State** | `memory/LOOP_STATE.md` — tried, failed, next (resume tomorrow) |
| **Stop** | All scores ≥ min **or** hard limit (cycles / retry ceiling) |
| **program.md** | Constraints the loop must respect (human-written purpose) |
| **Bilevel** | Every `FABLE5_BILEVEL_EVERY` cycles, outer loop breaks stuck search patterns |
| **Preflight** | Printed checklist: only run heavy loops when they earn the cost |

Inspired by loop-engineering practice (Karpathy-style experiment loops, Cherny-style “write loops not prompts”) — adapted fully offline. The loop does not delete thinking; it removes you as the bottleneck on measurable work.

## Hermes mode

```bash
./fable5 --hermes "Re-derive every claim and stop when verified"
```

| Behavior | Offline implementation |
|----------|------------------------|
| **SOUL.md** | Identity + boundaries loaded every turn |
| **Smart RAG** | Top-K (`FABLE5_RAG_TOP_K`, default **20**) relevant memory chunks |
| **Self-stop** | Success / retry ceiling / cycle budget |
| **Live repair** | On verifier FAIL → strategy patch for the next unit only |
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

Runtime artifacts: `memory/` — **gitignored**.

## Configuration

| Variable | Default | Meaning |
|----------|---------|---------|
| `FABLE5_MODEL` | `qwen2.5:7b` | Model name (`ollama list`) |
| `FABLE5_BASE_URL` | `http://localhost:11434/v1` | OpenAI-compatible base URL |
| `FABLE5_MEMORY` | `memory` | Memory directory (`~` allowed) |
| `FABLE5_SKILLS` | `skills` | Skill library directory |
| `FABLE5_SOUL` | `SOUL.md` | Identity / steering file |
| `FABLE5_PROGRAM` | `program.md` | Loop-engineer constraints |
| `FABLE5_ROADMAP` | `ROADMAP.md` | 6-month curriculum file |
| `FABLE5_KNOWLEDGE` | `knowledge` | Scraped research (brokers, etc.) |
| `FABLE5_HITL` | `1` | Human approval gates (`0` = off) |
| `FABLE5_ENGINEER_MIN_SCORE` | `8` | Min 1–10 score per criterion |
| `FABLE5_BILEVEL_EVERY` | `3` | Outer meta-loop period (`0` = off) |
| `FABLE5_WORKFLOWS` | `workflows` | Automation recipe directory |
| `FABLE5_WORKSPACE` | `workspace` | Build output directory |
| `FABLE5_ALLOW_SHELL` | unset | `1` = run allowlisted shell steps |
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
.\fable5.cmd --build "your scaffold goal"
```

```powershell
# Windows PowerShell
$env:FABLE5_MODEL = "qwen2.5:7b"
.\scripts\fable5.ps1 --automate daily-review
```

```bash
# macOS / Linux
export FABLE5_MODEL=qwen2.5:7b
./fable5 --hermes "your goal"
```

**CLI flags:** `--model` · `--roadmap` · `--team` · `--broker` · `--legal` · `--education` · `--scrape` · `--scrape-dir` · `--format` · `--build` · `--automate` · `--engineer` · `--criteria` · `--min-score` · `--loop` · `--hermes` · `--improve` · `--compress-memory` · `--doctor` · `--ascii`

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
| Shell steps dry-run only | Set `FABLE5_ALLOW_SHELL=1` (allowlisted commands only) |
| Slow first reply / cycle | Model loading into RAM/VRAM — expected |

## When to use it

| Prefer | For |
|--------|-----|
| **Chat** | Single decisions, code review, re-deriving a figure |
| **Build** | New scripts, CLIs, small multi-file apps |
| **Automate** | Daily review, chained build → hermes → improve |
| **Loop** | Multi-step goals, graded multi-claim work |
| **Hermes** | Long goals needing selective memory, live repair, self-stop |
| **Self-improve** | Encoding durable procedures after loops or failures |

Skip this stack for casual chat when speed matters more than rigor.

## Credits

- **Reasoning rules** — Fable 5–style rigorous operating manual (community prompt lineage).
- **Loop engineering** — Verifier · state · stop; PLAN→DO→VERIFY; Karpathy-style `program.md`; optional bilevel meta-search.
- **Self-improvement** — Memory + skills compound around a frozen local model.
- **Hermes behaviors** — Soul file, smart RAG, self-stopping loops, live repair, memory compression.
- **Build & automate** — Multi-file scaffolds and multi-step offline workflow recipes.
- **Edge vs luck** — Fooled-by-Randomness style checklist (LLN, OOS, multiple testing, survivorship, regression to the mean).
- **Agentic engineer path** — 6-month / 12-stage roadmap; multi-agent supervisor; HITL.
- **Broker mode** — regulation scrapes, claim audit, disciplined retail user model (not advice).
- **Legal mode** — playbook-driven contract/NDA/vendor triage (not legal advice; attorney review required).
- **Education mode** — credential/accreditation claim audit (not educational or medical advice).

## License

This project is free software under the **[MIT License](LICENSE)**.

Copyright © **2026 David Logan**.

You may use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, provided the copyright and permission notice are included in all copies or substantial portions of the Software. The Software is provided **“AS IS”**, without warranty of any kind, express or implied.

**Disclaimer:** Broker mode is **not financial advice**. Legal mode is **not legal advice** and does not create an attorney–client relationship. Education mode is **not educational, career, or medical advice**. Outputs require human verification (and licensed counsel for legal matters) before real-world use.
