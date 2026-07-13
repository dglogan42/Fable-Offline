# Fable 5 Offline Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](#platforms)
[![Python](https://img.shields.io/badge/python-3.10%2B-yellow.svg)](#requirements)

Local, **no-cloud** agent for **reasoning**, **loops**, **multi-agent teams**, **Hermes**, **self-improving skills**, and **build/automate** — plus domain skills for **privacy**, **planning**, **trade**, **property**, **animals**, **emergency routing (NZ)**, **arts**, **AEM**, **PDF**, **calendar / Zoom / iCal**, **Steam SIM soak**, and a **6-month agentic engineer roadmap**.  
Runs on **Windows · macOS · Linux** against any OpenAI-compatible API (default: [Ollama](https://ollama.com)).

**Data:** curated offline notes live under [`knowledge/`](knowledge/INDEX.md) (see that index). **License:** [MIT](LICENSE.md) © 2026 David Logan — Software **AS IS**; domain notes are not professional advice.

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
| **Privacy** | Host maps + **design planner** for privacy-aware agentic AI (`knowledge/privacy/`) |
| **Urban planning** | Competencies + **freight plan** module · Future Connect · skill audits (`knowledge/urban-planning/`) |
| **Climate** | Pathway/BAU modelling hygiene · Auckland Climate Plan seed (`knowledge/climate/`) |
| **Export / forwarder** | Export readiness · Incoterms · doc packs · MPI path (`knowledge/trade/`) |
| **Property manager** | Rates · tenancy ops · maintenance · consents navigation (`knowledge/property/`) |
| **Animal compliance** | Dogs/animals bylaws · complaints · pets in rentals (`knowledge/animals/`) |
| **Emergency services (NZ)** | 111/105 routing · FENZ · Health NZ finder (`knowledge/public-safety/`) |
| **Arts & culture** | Exhibition briefs · visitor ops · content warnings (`knowledge/culture/`) |
| **AEM site agent** | Adobe AEM fingerprints · clientlibs · AC privacy patterns (`knowledge/aem/`) |
| **PDF** | Offline extract (pypdf) · structure · PDF.js identification (`knowledge/pdf/`) |
| **Steam SIM soak** | Launch SimCity 4 (etc.) + **measure Ollama latency** under load (`knowledge/steam/`) |
| **Calendar / mail / meetings** | Google Calendar + **Zoom** web join + **iCal** + meeting prep (`knowledge/calendar/`) |

Once a local model is loaded, everything stays offline — no API keys, no usage meters.  
The *system* around the model improves (soul, memory, skills, workflows), not the model weights.

**Prompt vs loop:** a prompt is one instruction. A loop is a goal the agent keeps working toward — discover, plan, do, verify, feed back — until success or a hard limit. Three make-or-break parts: **verifier**, **state**, **stop**.

**Edge vs luck:** the market manufactures convincing hot streaks and backtests by chance. Default verdict on small samples is *insufficient evidence* — treat skill claims as guilty of luck until large, out-of-sample, honestly tested numbers force otherwise.

**Broker mode:** entity-first CFD/forex client model — verify licences on primary registers, distrust “0 pip / 1:300” marketing, no live-order automation without explicit consent. **Not financial advice.**

**Legal mode:** offline playbook-driven contract review, NDA triage, vendor checks, briefs, and templated responses (GREEN/YELLOW/RED). Configure `knowledge/legal/playbook.md`. **Not legal advice** — licensed attorney review required before any real-matter use.

**Education mode:** audits school/degree marketing (who issues the diploma, ASIC vs regional accreditation, state operate licenses, NBHWC/IBLM pathways). Example snapshot: Lifestyle Prescriptions® University in `knowledge/education/lpu-credential-claims.md`. **Not educational or medical advice.**

**Privacy mode:** third-party host maps (`privacy-host-map`) plus **agentic design planner** (`privacy-design-planner`) for review programmes and privacy-aware agents. Knowledge: host maps, `DESIGN_PLANNER.md`, `design-privacy-agent.md`. **Not legal advice.**

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
├── fable5_offline_agent.py      # CLI harness (all modes)
├── Fable5_Operating_Manual.md   # System prompt (full method)
├── SOUL.md                      # Identity / steering
├── program.md                   # Loop-engineer constraints
├── ROADMAP.md                   # 6-month agentic engineer curriculum
├── requirements.txt             # openai + pypdf
├── fable5 / fable5.cmd          # Launchers
├── scripts/                     # install, pdf_extract, ical_parse, steam_launch, steam_sim_soak
├── skills/                      # Agentic skill library (see skills/INDEX.md)
├── workflows/                   # Public automation recipes (*.json)
├── knowledge/                   # Curated offline data (see knowledge/INDEX.md)
│   ├── INDEX.md                 # Data catalog
│   ├── aem/ animals/ brokers/ climate/ culture/
│   ├── calendar/ education/ health/ legal/ pdf/ privacy/
│   ├── property/ public-safety/ steam/ trade/ urban-planning/
├── workspace/                   # Runtime builds/extracts (gitignored)
├── memory/                      # Runtime memory (gitignored)
├── LICENSE · LICENSE.md         # MIT © 2026 David Logan + domain notices
├── .gitignore                   # Secrets, scrapes, PDFs, private knowledge, soak junk
└── README.md
```

### What not to commit

| Keep out of git | Why |
|-----------------|-----|
| `.env`, keys, tokens, `secrets/` | Credentials |
| `memory/*`, `workspace/*` | Runtime / local experiments |
| `knowledge/**/scrape-*`, `*-raw.*`, `*.pdf` | Bulky / sensitive dumps |
| `knowledge/**/_local/`, `legal/matters/` | Private matter files |
| `**/*.ics`, Zoom passcodes, secret calendar feeds | Private invites / join secrets |
| Empty AEM `clientlib-dependencies…d41d8cd9…js` | Forensic noise |

Ship only **curated markdown** under `knowledge/` and shared skills/workflows. Full policy: [`.gitignore`](.gitignore) · data index: [`knowledge/INDEX.md`](knowledge/INDEX.md).

## Knowledge data

Offline **domain data** for skills and modes. Always re-verify primary sources before real decisions.

| Domain | Path | Skill(s) |
|--------|------|----------|
| Privacy host maps | `knowledge/privacy/` | `privacy-host-map`, `privacy-design-planner` |
| Urban planning / freight | `knowledge/urban-planning/` | `urban-planner-competencies` |
| Climate pathways | `knowledge/climate/` | `climate-modeling` |
| Trade / MPI / export | `knowledge/trade/` | `freight-forwarder-exporter` |
| Property management | `knowledge/property/` | `property-manager-agent` |
| Animals / dogs | `knowledge/animals/` | `animal-compliance-agent` |
| Emergency / safety | `knowledge/public-safety/` | `emergency-services-agent` |
| Health directory | `knowledge/health/` | `emergency-services-agent` |
| Arts / exhibitions | `knowledge/culture/` | `arts-culture-agent` |
| AEM patterns | `knowledge/aem/` | `aem-site-agent` |
| Brokers | `knowledge/brokers/` | `broker-claim-audit` |
| Education claims | `knowledge/education/` | `education-claim-audit` |
| Legal playbook | `knowledge/legal/` | `legal-playbook` |
| PDF extract hygiene | `knowledge/pdf/` | `pdf-render` |
| Steam SIM launch / soak | `knowledge/steam/` | `steam-sim-launch` |
| Calendar / iCal / meetings | `knowledge/calendar/` | `calendar-mail-meetings` |

Full file list: **[`knowledge/INDEX.md`](knowledge/INDEX.md)**.


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
| `/privacy [prompt]` | Third-party host / privacy map (local knowledge) |
| `/calendar [prompt]` | Calendar / iCal / mail / meetings (`calendar-mail-meetings`) |
| `/meetings` · `/mail` | Aliases for `/calendar` |
| `/pdf <path>` | Extract PDF text (pypdf) + structure with `pdf-render` |
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
| `privacy-host-map` | Engineer scored third-party host / privacy map |
| `privacy-design-plan` | Design planner: architecture, risks, P0–P3, HITL |
| `urban-planner-checkpoint` | Four-area competency audit + 90-day growth task |
| `freight-plan-review` | Freight network / freight plan structured review (urban scale) |
| `freight-export-checkpoint` | Export readiness + forwarder/exporter doc checklist |
| `property-manager-checkpoint` | Property intake + tenancy/maintenance checklist |
| `animal-compliance-checkpoint` | Animal/dog compliance checklist + routing |
| `emergency-route-check` | 111/105/Healthline/FENZ/Health NZ routing (min score 9) |
| `arts-exhibition-brief` | Exhibition/visitor brief (arts-culture-agent) |
| `aem-page-audit` | AEM fingerprint + clientlibs + privacy map |
| `climate-plan-review` | Climate plan + emissions modelling audit |
| `pdf-extract-review` | Structure/review a PDF text extract (skill pdf-render) |
| `steam-sim-perf-check` | Plan Steam SIM launch + model perf notes (SC4 app 24780) |
| `calendar-meeting-prep` | Meeting prep + Google Calendar / Zoom join / iCal / mail drafts |

## Calendar · mail · meetings (Google / Zoom / iCal)

Offline help for **Google Calendar**, **Zoom Web Client**, **iCalendar (.ics)**, **mail invites**, and **meeting prep/notes**.

| Surface | User CLICK | Agent |
|---------|------------|--------|
| Google Calendar | [calendar.google.com](https://calendar.google.com/) | Prep, drafts, no auth scrape |
| Zoom web join | [app.zoom.us/wc/join](https://app.zoom.us/wc/join) | **join-zoom** checklist; never auto-join |
| Google Meet | `meet.google.com/…` | Flag as CLICK from invites |

```bash
# Mode
python fable5_offline_agent.py --calendar
python fable5_offline_agent.py --calendar "join-zoom: checklist for web client"
python fable5_offline_agent.py --calendar "meeting-prep: design review Fri 10:00 NZST"
# Chat: /calendar  /meetings  /mail

# Parse a local invite export (flags zoom.us / meet.google.com links)
python scripts/ical_parse.py path/to/invite.ics
python fable5_offline_agent.py --ical path/to/invite.ics
python fable5_offline_agent.py --automate calendar-meeting-prep
```

| Resource | Path |
|----------|------|
| Skill | `skills/calendar-mail-meetings.md` |
| Knowledge | `knowledge/calendar/ical-and-google.md`, `zoom-web-join.md`, `meetings-playbook.md` |
| Privacy seeds | `knowledge/privacy/google-calendar-hosts.md`, `zoom-hosts.md` |
| Parser | `scripts/ical_parse.py` |
| Workflow | `workflows/calendar-meeting-prep.json` |

**Draft only** — user sends mail, creates events, and joins Zoom/Meet. Keep secret iCal feeds, OAuth tokens, and Zoom passcodes out of git (`knowledge/calendar/_local/`, `.ics` ignored).

## Steam SIM launch & Ollama soak

Launch an **owned, installed** SIM/city-builder via Steam and measure local LLM latency under concurrent load.

**Seed:** SimCity 4 Deluxe — `steam://rungameid/24780`

```bash
# Launch only
python scripts/steam_launch.py 24780
python scripts/steam_launch.py steam://rungameid/24780 --dry-run

# Full A/B soak: latency WITH game → stop → baseline WITHOUT → relaunch
python scripts/steam_sim_soak.py --appid 24780
python scripts/steam_sim_soak.py --appid 24780 --no-stop          # load-only sample
python scripts/steam_sim_soak.py --appid 24780 --skip-relaunch    # do not restart game after baseline

# Doctor + planned workflow notes
python fable5_offline_agent.py --doctor
python fable5_offline_agent.py --automate steam-sim-perf-check
```

| Resource | Path |
|----------|------|
| Skill | `skills/steam-sim-launch.md` |
| Knowledge | `knowledge/steam/sim-games-launch.md` |
| Launch script | `scripts/steam_launch.py` |
| Soak / latency | `scripts/steam_sim_soak.py` |
| Workflow | `workflows/steam-sim-perf-check.json` |

**Soak metrics:** time-to-first-token (TTFT), total generate time, rough tok/s for a short fixed prompt (`qwen2.5:7b` by default; override with `--model`). Optional env: `FABLE5_STEAM` or `STEAM_EXE` → path to `steam.exe`.

**Not a game bot** — launch and measure only; no in-game automation, no DRM bypass. Close heavy games before long engineer/Hermes loops if latency or VRAM is tight.

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

## Privacy / third-party host maps + design planner

| Skill | Role |
|-------|------|
| **`privacy-host-map`** | Evidence: `map-hosts` · `map-tags` · `map-tension` · `key-hygiene` · `write-knowledge` |
| **`privacy-design-planner`** | Design/plan: `design-system` · `plan-review` · `plan-from-knowledge` · **`design-agent`** · `plan-compound` · `brief` |

```bash
python fable5_offline_agent.py --privacy
python fable5_offline_agent.py --privacy "design-agent: offline privacy mapper"
python fable5_offline_agent.py --privacy "map-hosts: [paste HTML head/footer]"
python fable5_offline_agent.py --automate privacy-host-map
python fable5_offline_agent.py --automate privacy-design-plan
```

| Tag | Meaning |
|-----|---------|
| **LOAD** | Script/iframe/img load on page |
| **CONFIG** | API/config endpoint in page |
| **CLICK** | User-initiated outbound link |
| **BUNDLE** | String in minified JS only — not a confirmed call |

**Agentic stack:** purpose → design planner → host map → engineer verify → write `knowledge/privacy/` → HITL.

Curated knowledge:

| Note | Scope |
|------|--------|
| [`knowledge/privacy/DESIGN_PLANNER.md`](knowledge/privacy/DESIGN_PLANNER.md) | Template, phases P0–P4, engineer criteria block |
| [`knowledge/privacy/design-privacy-agent.md`](knowledge/privacy/design-privacy-agent.md) | Seed design for Fable privacy agentic AI |
| [`knowledge/privacy/akl-libraries-third-party-hosts.md`](knowledge/privacy/akl-libraries-third-party-hosts.md) | Auckland Libraries: GTM, Adobe, Coveo, Shielded |
| [`knowledge/privacy/uoa-eloqua-pg-webinar-hosts.md`](knowledge/privacy/uoa-eloqua-pg-webinar-hosts.md) | UoA Eloqua webinar LP: pixel, lead form, Ads gclid |

**Not legal advice.** Re-verify with live Network capture and the published privacy policy before decisions.

## Urban planner competencies (incl. freight)

Four-area practice framework for study and career coaching (not professional registration advice):

1. **Technical & analytical** — GIS, data/stats, CAD/3D, regulatory knowledge, **freight & goods data**  
2. **Communication & interpersonal** — engagement, **freight stakeholders**, presentation, mediation, teams  
3. **Design & strategic** — vision, master planning, **multimodal + freight networks**, project evaluation  
4. **Management & organisation** — decisions, leadership, programme alignment  

**Freight module:** strategic vs supporting freight networks, generators, first/last mile, mode split, evaluation criteria (access, safety, equity, environment, resilience, land use, deliverability). Procedures: `plan-freight`, `future-connect-freight` (AT Future Connect portal).

```bash
python fable5_offline_agent.py --automate urban-planner-checkpoint
python fable5_offline_agent.py --automate freight-plan-review
# Chat: "Draft a freight plan issues note for [area]"
# Chat: "Future Connect freight walkthrough for Current vs First Decade"
```

| Resource | Path |
|----------|------|
| Skill | `skills/urban-planner-competencies.md` |
| Framework | `knowledge/urban-planning/competencies.md` |
| Freight module | `knowledge/urban-planning/freight-plan.md` |
| Future Connect | `knowledge/urban-planning/at-future-connect-portal.md` |
| Workflows | `urban-planner-checkpoint`, `freight-plan-review` |

Cross-links: programme marketing → `education-claim-audit` / privacy maps; PDFs → `pdf-render`; portal privacy → `knowledge/privacy/at-future-connect-hosts.md`.

**Not legal or planning consent advice.**

## Freight forwarder & exporter agent

Skill **`freight-forwarder-exporter`**: commercial **shipment** scale (vs urban **strategic freight networks**).

| Procedure | Use |
|-----------|-----|
| **export-readiness** | Product → destination gap analysis |
| **shipment-checklist** | Pre-book through POD phases |
| **incoterms-coach** | Risk/cost split (state Incoterms® year) |
| **doc-pack** | Invoice, packing list, B/L/AWB, certificates matrix |
| **cost-build** | Landed skeleton from **user quotes only** |
| **mpi-export-path** | NZ food & fibre → MPI Exporter Help |
| **role-split** | Exporter / forwarder / broker / MPI / carrier |
| **design-export-agent** | Offline agent architecture |

```bash
python fable5_offline_agent.py --automate freight-export-checkpoint
# Chat: "export-readiness: honey to Japan, FOB Auckland, no HS yet"
# Chat: "mpi-export-path for dairy powder"
```

| Resource | Path |
|----------|------|
| Skill | `skills/freight-forwarder-exporter.md` |
| Framework | `knowledge/trade/freight-forwarder-exporter.md` |
| MPI Exporter Help | `knowledge/trade/mpi-exporter-help.md` |
| Workflow | `workflows/freight-export-checkpoint.json` |

**Not customs, biosecurity, or freight brokerage advice.** No invented HS codes or rates.

## Property manager agent

Skill **`property-manager-agent`**: property intake, rates/valuations navigation, tenancy ops checklists, maintenance, consents/compliance handoffs, incident routing.

```bash
python fable5_offline_agent.py --automate property-manager-checkpoint
```

| Resource | Path |
|----------|------|
| Skill | `skills/property-manager-agent.md` |
| Framework | `knowledge/property/property-manager-framework.md` |
| Workflow | `workflows/property-manager-checkpoint.json` |

**Not legal, valuation, or real-estate agency advice.**

## Animal compliance agent

Skill **`animal-compliance-agent`**: owner checklists, complaint routing, attack/incident routing (111 when danger), pets in property, council bylaw navigation, MPI animal/export adjacency.

```bash
python fable5_offline_agent.py --automate animal-compliance-checkpoint
```

| Resource | Path |
|----------|------|
| Skill | `skills/animal-compliance-agent.md` |
| Framework | `knowledge/animals/animal-compliance-framework.md` |
| Workflow | `workflows/animal-compliance-checkpoint.json` |

**Danger from animal → call 111.** Not legal or veterinary advice.

## Emergency services agent (NZ)

Skill **`emergency-services-agent`**: hard-gate routing to official channels.

| Procedure | Use |
|-----------|-----|
| **route-emergency** | 111 first when danger/unclear |
| **police-105** | Non-emergency Police |
| **fenz-guide** | Fire incidents + escape plan education |
| **health-find-service** | Health NZ directory / Healthline |
| **escape-plan** | FENZ 3-step home fire plan |
| **map-safety-privacy** | Trackers on safety sites |

```bash
python fable5_offline_agent.py --automate emergency-route-check
# Chat: "Is 105 or 111 for a car broken into yesterday?"
```

| Resource | Path |
|----------|------|
| Skill | `skills/emergency-services-agent.md` |
| Framework | `knowledge/public-safety/emergency-services-framework.md` |
| Seeds | `nz-police-105.md`, `fenz-incident-reports.md`, `health/healthnz-find-a-service.md` |
| Workflow | `workflows/emergency-route-check.json` |

**In emergency call 111.** Not medical/legal advice. Agents do not take reports.

## Arts & culture agent

Skill **`arts-culture-agent`**: exhibition structure, visitor ops, content warnings, institution map, arts-site privacy handoff.

```bash
python fable5_offline_agent.py --automate arts-exhibition-brief
# Chat: "structure-exhibition for Forever Tomorrow at AAG"
```

| Resource | Path |
|----------|------|
| Skill | `skills/arts-culture-agent.md` |
| Framework | `knowledge/culture/arts-culture-framework.md` |
| Seed | `knowledge/culture/aag-forever-tomorrow.md` |
| Workflow | `workflows/arts-exhibition-brief.json` |

**Not ticketing advice.**

## AEM site agent

Skill **`aem-site-agent`**: fingerprint Adobe AEM (`etc.clientlibs`, data layer, Experience Fragments), inventory clientlibs (including empty `d41d8cd9` stubs), Coveo/Launch/GTM/Shielded patterns used on Auckland Council properties.

```bash
python fable5_offline_agent.py --automate aem-page-audit
# Chat: "fingerprint this HTML for AEM and map privacy"
```

| Resource | Path |
|----------|------|
| Skill | `skills/aem-site-agent.md` |
| Patterns | `knowledge/aem/aem-patterns.md` |
| Workflow | `workflows/aem-page-audit.json` |
| Example maps | `knowledge/privacy/ac-*.md`, `akl-libraries-*.md` |

**Not a penetration test.**

## Climate modeling (Auckland Climate Plan)

Skill **`climate-modeling`**: inventories vs **illustrative pathways**, BAU vs action packages, residual emissions, uncertainty. Seed knowledge from [Te Tāruke-ā-Tāwhiri: Auckland’s Climate Plan](https://www.aucklandcouncil.govt.nz/content/dam/ac/docs/plans/climate-plan/auckland-climate-plan.pdf) (PDF extract; plan claims include **CURB** World Bank/C40 modelling, **−50% by 2030** and **net zero 2050** vs **2016** baseline).

```bash
python fable5_offline_agent.py --pdf path/to/auckland-climate-plan.pdf
python fable5_offline_agent.py --automate climate-plan-review
```

| Resource | Path |
|----------|------|
| Skill | `skills/climate-modeling.md` |
| Plan snapshot | `knowledge/climate/auckland-climate-plan.md` |
| Modelling hygiene | `knowledge/climate/climate-modeling.md` |
| Workflow | `workflows/climate-plan-review.json` |

Crosswalks to urban/freight/transport via `urban-planner-competencies` procedure **plan-climate**. **Not climate or investment advice.**

## PDF render & extract

Offline text extract + structure (Mozilla **PDF.js** is the common browser viewer — not committed as a bundle).

```bash
python -m pip install pypdf   # also in requirements.txt
python fable5_offline_agent.py --pdf path/to/file.pdf
python fable5_offline_agent.py --pdf path/to/file.pdf --pdf-pages 1-5
python scripts/pdf_extract.py path/to/file.pdf -o workspace/extract.md
python fable5_offline_agent.py --automate pdf-extract-review
```

| Resource | Path |
|----------|------|
| Skill | `skills/pdf-render.md` |
| Knowledge | `knowledge/pdf/pdfjs-and-offline-render.md` |
| CLI helper | `scripts/pdf_extract.py` |
| Workflow | `workflows/pdf-extract-review.json` |

Image-only/scanned pages need OCR (skill procedure **ocr-gap**). Hand off extracts to legal / education / urban skills as needed. **Do not commit** `.pdf` binaries or multi‑MB `pdf.js` dumps.

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

Workflow step types: `build` · `engineer` · `hermes` · `loop` · `improve` · `compress` · `llm` · `shell` · `note` · `broker` · `legal` · `education` · `privacy` · `calendar` · `pdf` · `scrape` · `hitl` · `team`.

Add your own recipes as `workflows/my-job.json`. Private experiments go in `workflows/_local/` (gitignored).

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
| `FABLE5_STEAM` / `STEAM_EXE` | unset | Path to `steam.exe` (SIM launch / soak scripts) |

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

**CLI flags:** `--model` · `--roadmap` · `--team` · `--broker` · `--legal` · `--education` · `--privacy` · `--calendar` · `--ical` · `--pdf` · `--pdf-pages` · `--pdf-out` · `--scrape` · `--scrape-dir` · `--format` · `--build` · `--automate` · `--engineer` · `--criteria` · `--min-score` · `--loop` · `--hermes` · `--improve` · `--compress-memory` · `--doctor` · `--ascii`

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
| Slow chat while a SIM runs | Expected under load; run `python scripts/steam_sim_soak.py` for A/B TTFT |
| Steam not found | Set `FABLE5_STEAM` / `STEAM_EXE`, or install Steam; default also checks `D:\Steam\steam.exe` |
| Need Zoom / calendar help | `--calendar` / `/calendar`; web join [app.zoom.us/wc/join](https://app.zoom.us/wc/join); parse invites with `--ical` |

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
- **Privacy mode** — host maps + design planner for privacy-aware agentic AI (not legal advice).
- **Urban planner competencies** — GIS-to-stakeholder framework for learning and skill audits (not professional advice).
- **PDF render** — offline pypdf extract + PDF.js identification (not a cloud document API).
- **Climate modeling** — pathway/BAU hygiene; Auckland Climate Plan seed (not climate advice).
- **Freight forwarder / exporter** — readiness, docs, Incoterms, MPI path (not customs advice).
- **Property manager** — tenancy/ops checklists (not legal or valuation advice).
- **Animal compliance** — dog/animal bylaw navigation (not veterinary or legal advice).
- **Emergency services (NZ)** — 111/105/Healthline/FENZ routing (not emergency response).
- **Arts & culture** — exhibition briefs and visitor ops (not ticketing).
- **AEM site agent** — public AEM fingerprints and clientlib hygiene (not pen-test).
- **Knowledge data** — curated offline notes; see [`knowledge/INDEX.md`](knowledge/INDEX.md).
- **Steam SIM soak** — launch owned Steam SIMs + measure Ollama latency (not a game bot; no DRM bypass).
- **Calendar / mail / meetings** — Google Calendar + Zoom web join + iCal parse + meeting prep (not a mail/Zoom client; draft + checklist only).

## License

This project is free software under the **[MIT License](LICENSE.md)** ([`LICENSE`](LICENSE) is identical).

Copyright © **2026 David Logan**.

You may use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, provided the copyright and permission notice are included in all copies or substantial portions of the Software. The Software is provided **“AS IS”**, without warranty of any kind, express or implied.

See **[LICENSE.md](LICENSE.md)** for the full MIT text plus **additional notices** on:

1. Domain knowledge / skills (not professional advice)  
2. Third-party website and policy snapshots  
3. Emergency routing (**call 111** in NZ emergencies)  
4. Steam / games (ownership required; not a bot or DRM bypass)  
5. Calendar / mail / Zoom (local iCal + drafts; user CLICK join only)  
6. Contribution licensing  

### Domain disclaimers (summary)

| Area | Not… |
|------|------|
| Broker | Financial advice |
| Legal | Legal advice / attorney–client relationship |
| Education | Educational or career advice |
| Privacy / AEM | Legal advice, pen-test, or compliance certification |
| Planning / climate | Planning consent or climate-science consultancy |
| Export / freight | Customs, biosecurity, or brokerage advice |
| Property / animals | Legal, valuation, veterinary, or agency advice |
| Emergency / health | Medical advice or emergency response (call **111**) |
| Arts | Ticketing or rights clearance |
| Steam SIM soak | Game automation, multiplayer cheating, or DRM bypass |
| Calendar / mail / Zoom | Mailbox control, silent send, auto-join, or account takeover |

Outputs require **human verification** (and licensed professionals where required) before real-world use.
