# Fable 5 Offline Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.md)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](#platforms)
[![Python](https://img.shields.io/badge/python-3.10%2B-yellow.svg)](#requirements)

Local, **no-cloud** agent for **reasoning**, **loops**, **multi-agent teams**, **Hermes**, **self-improving skills**, **build/automate**, and an **offline prompt generator** — plus domain skills for **privacy**, **planning**, **trade**, **property**, **animals**, **emergency routing (NZ)**, **arts**, **AEM**, **PDF**, **calendar / Zoom / iCal**, **Windows / macOS / ChromeOS Flex install prep**, **Google for Education**, **Steam SIM soak**, **math/physics**, **creative pipelines**, and **2D / stop-motion / 3D animation kits** (Krita · Stop Motion Studio · [Cloud Stop Motion](https://cloudstopmotion.com/) · Blender), plus a **6-month agentic engineer roadmap**.  
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
| **Education** | Credential claim audit · **UC Arts PG** · **Google for Education** map (`knowledge/education/`) |
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
| **Windows install prep** | Licensed **Windows 11** media + DISM/unattend hygiene (`knowledge/windows/`) |
| **macOS install prep** | Apple **bootable installer** / recovery hygiene (`knowledge/macos/`) |
| **ChromeOS Flex install prep** | Install Flex on PC/Mac via USB ([product](https://chromeos.google/products/chromeos-flex/)) |
| **Google for Education** | Workspace · Classroom · Chromebooks map ([edu.google.com](https://edu.google.com/intl/ALL_us/)) |
| **Instagram fit / selfie** | Pick hero fits, makeup, slay shots + captions (`knowledge/social/`) |
| **Outfit select / create** | Wardrobe picks + **Seamly2D** pattern plans (`knowledge/fashion/`) |
| **DOC ranger pathway** | NZ Trainee Ranger / conservation career map (`knowledge/conservation/`) |
| **TikTok Ads create** | Ads Manager campaign plan + pixel hygiene (`knowledge/ads/`) |
| **Snapchat Web feed** | Desktop Chat feed protocol (`web.snapchat.com`) |
| **RSS share** | Build/share **RSS 2.0** feeds (`scripts/rss_share.py`) |
| **YouTube Live encoder** | Studio + RTMP/encoder protocol ([Help 2907883](https://support.google.com/youtube/answer/2907883?hl=en)) |
| **Creative pipeline builds** | Adobe CC + CapCut + LR/PS + Resolve export recipes (`knowledge/media/`) |
| **Animation dev kit (Krita)** | Frame-by-frame plan · walk cycle · render/FFmpeg ([Krita manual](https://docs.krita.org/en/user_manual/animation.html)) |
| **Stop / motion dev kit** | Studio + **Cloud Stop Motion** (Chromebook cloud) ([cloudstopmotion.com](https://cloudstopmotion.com/)) |
| **3D animation dev kit** | Blender-first CG pipeline · optional VFX study map ([MDS seed](https://www.mediadesignschool.com/courses/3d-animation-vfx-courses-degrees)) |
| **Math / physics agent** | `/deep-explain` · `/theorem` · `/physics` · durable lessons |
| **Prompt generator** | Offline swarm/agent system prompts → `generated_prompts/` |

Once a local model is loaded, everything stays offline — no API keys, no usage meters.  
The *system* around the model improves (soul, memory, skills, workflows), not the model weights.

**Prompt vs loop:** a prompt is one instruction. A loop is a goal the agent keeps working toward — discover, plan, do, verify, feed back — until success or a hard limit. Three make-or-break parts: **verifier**, **state**, **stop**.

**Edge vs luck:** the market manufactures convincing hot streaks and backtests by chance. Default verdict on small samples is *insufficient evidence* — treat skill claims as guilty of luck until large, out-of-sample, honestly tested numbers force otherwise.

**Broker mode:** entity-first CFD/forex client model — verify licences on primary registers, distrust “0 pip / 1:300” marketing, no live-order automation without explicit consent. **Not financial advice.**

**Legal mode:** offline playbook-driven contract review, NDA triage, vendor checks, briefs, and templated responses (GREEN/YELLOW/RED). Configure `knowledge/legal/playbook.md`. **Not legal advice** — licensed attorney review required before any real-matter use.

**Education mode:** audits school/degree marketing (who issues the diploma, ASIC vs regional accreditation, state operate licenses, NBHWC/IBLM pathways). Snapshots: LPU (`lpu-credential-claims.md`) and **UC Arts postgraduate** hub (`uc-arts-postgraduate-study.md`). **Not educational or medical advice.**

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
├── auto_prompt_generator.py     # Offline swarm/agent system-prompt generator
├── Fable5_Operating_Manual.md   # System prompt (full method)
├── SOUL.md                      # Identity / steering
├── program.md                   # Loop-engineer constraints
├── ROADMAP.md                   # 6-month agentic engineer curriculum
├── requirements.txt             # openai + pypdf
├── fable5 / fable5.cmd          # Launchers
├── agents/                      # Offline loop briefs for Hermes + Fable loops
├── scripts/                     # install, pdf_extract, ical_parse, rss_share, steam_*
├── skills/                      # Agentic skill library (see skills/INDEX.md)
├── workflows/                   # Public automation recipes (*.json)
├── knowledge/                   # Curated offline data (see knowledge/INDEX.md)
│   ├── INDEX.md                 # Data catalog
│   ├── aem/ animals/ brokers/ climate/ culture/
│   ├── calendar/ education/ health/ legal/ pdf/ privacy/
│   ├── ads/ conservation/ fashion/ macos/ property/ public-safety/
│   ├── social/ steam/ swarm/ trade/ urban-planning/ windows/
├── generated_prompts/           # Prompt-gen output (gitignored bulk)
├── workspace/                   # Runtime builds/extracts (gitignored)
├── memory/                      # Runtime memory (gitignored)
├── LICENSE · LICENSE.md         # MIT © 2026 David Logan + domain notices
├── .gitignore                   # Secrets, school PII, Flex images, creative/anim masters
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
| Windows product keys (`knowledge/windows/_local/`) | Licensing secrets |
| macOS `Install *.app`, `.ipsw`, recovery / FileVault keys | Huge binaries + secrets |
| ChromeOS Flex `.bin` images, enrollment tokens | Binary dumps + fleet secrets |
| Student rosters, school admin tokens, GfE secrets | Child/student privacy |
| Stream keys; Adobe passwords; creative `00_inbox` / `04_exports` media | Secrets + bulk binaries |
| Krita `.kra` / `03_krita/` / render sequences | Local 2D animation masters |
| Stop Motion Studio / Cloud SM dumps (`02_sms_project/`, `02_cloud_exports/`) | Local project libraries |
| Blender `.blend` / EXR / `03_shots/` / caches / FBX·USD·VDB dumps | Local 3D/CG weight |
| `generated_prompts/` bulk dumps | Local LLM prompt-gen output |
| Empty AEM `clientlib-dependencies…d41d8cd9…js` | Forensic noise |

Ship only **curated markdown** under `knowledge/` and shared skills/workflows. Full policy: [`.gitignore`](.gitignore) · data index: [`knowledge/INDEX.md`](knowledge/INDEX.md).

## Knowledge data

Offline **domain data** for skills and modes. Always re-verify primary sources before real decisions.

| Domain | Path | Skill(s) |
|--------|------|----------|
| Privacy host maps | `knowledge/privacy/` | `privacy-host-map`, `privacy-design-planner`, `tiktok-analytics` |
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
| Education claims / UC Arts PG / GfE | `knowledge/education/` | `education-claim-audit`, `uc-arts-postgraduate`, `google-for-education` |
| Legal playbook | `knowledge/legal/` | `legal-playbook` |
| PDF extract hygiene | `knowledge/pdf/` | `pdf-render` |
| Steam SIM launch / soak | `knowledge/steam/` | `steam-sim-launch` |
| Calendar / iCal / meetings | `knowledge/calendar/` | `calendar-mail-meetings` |
| Windows install (licensed) | `knowledge/windows/` | `windows-install-prep` |
| macOS install (Apple) | `knowledge/macos/` | `macos-install-prep` |
| ChromeOS Flex | `knowledge/chromeos/` | `chromeos-flex-install-prep` |
| Instagram fits / selfies | `knowledge/social/` | `instagram-selfie-selector` |
| Snapchat for Web | `knowledge/social/` | `snapchat-web-feed` |
| YouTube Live / creative / 2D / stop-mo / 3D | `knowledge/media/` | `youtube-live-encoder`, `creative-pipeline-builds`, `animation-dev-kit`, `stop-motion-dev-kit`, `3d-animation-dev-kit` |
| Math / physics lessons | `knowledge/math/`, `physics/` | `math-physics-agent` |
| Swarm / prompt generator | `knowledge/swarm/` | `prompt-generator` |
| Outfit / Seamly CAD | `knowledge/fashion/` | `outfit-selector-create` |
| DOC ranger careers | `knowledge/conservation/` | `doc-ranger-pathway` |
| TikTok Ads creation | `knowledge/ads/` | `tiktok-ads-create` |

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
| `/windows [prompt]` | Licensed Windows 11 install / DISM hygiene |
| `/macos [prompt]` | Apple-licensed macOS bootable installer / recovery |
| `/fit` · `/slay` · `/ootd` | Instagram selfie / fit / makeup selector |
| `/outfit` · `/seamly` | Outfit select/create + Seamly2D plan |
| `/doc` · `/ranger` | DOC ranger / Trainee Ranger pathway |
| `/tiktok-ads` · `/ttads` | TikTok Ads Manager creation plan |
| `/deep-explain [topic]` | Bottom-up math/physics lesson (durable md) |
| `/theorem [claim]` | Formal theorem + proof structure |
| `/physics [problem]` | Physics solve + dimensional analysis gate |
| `/prompt-gen [spec]` | Offline swarm/agent prompt generator → `generated_prompts/` |
| `/prompts` | List generated prompts (`/prompt-gen list`) |
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
./fable5 --prompt-gen quant
./fable5 --automate prompt-gen-quant
```

| Recipe (seeded) | What it does |
|-----------------|--------------|
| `hello-project` | Build a tiny multi-file hello CLI |
| `daily-review` | Compress memory → self-improve skills |
| `rigor-check` | Short Hermes loop on a numeric claim |
| `engineer-memo` | Loop-engineer a decision memo to score ≥ 8 |
| `edge-audit` | Edge-vs-luck audit (streaks, backtests, “system works” claims) |
| `prompt-gen-quant` | Generate 6-agent quant research system prompts offline |
| `prompt-gen-custom` | Generate a custom multi-agent swarm |
| `prompt-gen-plan` | Chat architect plan for swarm prompts (no files) |
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
| `tiktok-analytics-map` | TikTok Analytics / pixel HTML + Network evidence map |
| `tiktok-ads-create` | Full Ads Manager campaign plan (structure, pixel, creative, launch) |
| `snapchat-web-session` | Snapchat for Web login + Chat feed + call/snap protocol |
| `rss-share-build` | Compose channel JSON + RSS 2.0 feed.xml share pack |
| `youtube-live-encoder-plan` | YouTube Live encoder first-stream plan (Help 2907883) |
| `creative-pipeline-build` | Adobe CC + CapCut + LR/PS + Resolve export pipeline plan |
| `animation-dev-kit` | Krita frame-by-frame animation plan (storyboard → render) |
| `stop-motion-dev-kit` | Stop-motion plan (Studio and/or Cloud SM) |
| `stop-motion-cloud-chromebook` | Chromebook browser app + cloud project save + export |
| `chromeos-flex-install-prep` | ChromeOS Flex USB install plan for existing PC/Mac |
| `google-for-education` | Google for Education hub map (Workspace · Classroom · devices) |
| `3d-animation-dev-kit` | Blender-first 3D/VFX plan (+ optional formal study map) |
| `math-deep-explain` | Bottom-up durable math/physics lesson |
| `physics-solve` | Physics problem with dimensions gate |
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
| `windows-install-prep` | Licensed Win11 media plan + optional DISM/unattend outline |
| `macos-install-prep` | Apple bootable installer (101578) + recovery method chooser |
| `instagram-fit-select` | Hero fit/selfie pick + caption pack + post-safety |
| `outfit-seamly-plan` | Outfit brief + Seamly2D project plan ([download](https://seamly.io/download/)) |
| `doc-ranger-pathway` | DOC Trainee Ranger / L4 conservation pathway map |
| `uc-arts-pg-map` | UC Arts postgraduate pathways + apply navigation |

## Math & physics agent (deep-explain · theorem · solver)

Offline STEM skills for coding/AI agents: structured lessons, proofs, and dimensional analysis — saved as **markdown artifacts** (not lost in chat).

| Command | Procedure |
|---------|-----------|
| `/deep-explain` · `--deep-explain` | Bottom-up lesson |
| `/theorem` · `--theorem` | Statement + proof structure |
| `/physics` · `--physics` | Solve with **dimensions gate** |

```bash
python fable5_offline_agent.py --deep-explain "Fourier series intuition"
python fable5_offline_agent.py --theorem "intermediate value theorem"
python fable5_offline_agent.py --physics "projectile with air resistance neglected"
python fable5_offline_agent.py --automate math-deep-explain
python fable5_offline_agent.py --automate physics-solve
# Hermes: section-per-cycle durable lesson
python fable5_offline_agent.py --hermes "deep-explain Lagrange multipliers into workspace/lessons/"
```

| Resource | Path |
|----------|------|
| Skill | `skills/math-physics-agent.md` |
| Knowledge | `knowledge/math/`, `knowledge/physics/` |
| Agent brief | `agents/math-physics-agent.md` |
| Workflows | `math-deep-explain`, `physics-solve` |

Lessons: `workspace/lessons/` or `memory/lessons/` for Hermes RAG.

## Creative pipeline builds (Adobe · CapCut · Resolve)

Repeatable **export builds** with licensed apps — not cracked installers.

| Stage | Tool |
|-------|------|
| Install / update | [Adobe Creative Cloud desktop](https://www.adobe.com/nz/creativecloud/desktop-app.html) → Photoshop, Lightroom, … |
| Stills | Lightroom develop/export presets → Photoshop actions |
| Short-form | CapCut templates → 9:16 export |
| Long-form / grade | DaVinci Resolve project + Deliver presets |
| Package | `workspace/creative/<slug>/04_exports/` + `notes.md` |

```bash
python fable5_offline_agent.py --automate creative-pipeline-build
```

| Resource | Path |
|----------|------|
| Skill | `skills/creative-pipeline-builds.md` |
| Knowledge | `knowledge/media/creative-pipeline-builds.md`, `adobe-cc-desktop.md` |
| Workflow | `workflows/creative-pipeline-build.json` |

**Refuse:** GenP/cracks. User runs apps. Hand off publish to YouTube Live / TikTok / IG / RSS skills.

## Animation dev kit (Krita)

Frame-by-frame raster animation plan from the official Krita manual: [Animation with Krita](https://docs.krita.org/en/user_manual/animation.html).

| Stage | Focus |
|-------|--------|
| Workspace | Window → Workspace → **Animation** (Timeline, Onion Skin, Curves, Storyboard) |
| Plan | Script → storyboard → animatic (external NLE) → clips ≤ ~10s @ ~12 fps for beginners |
| Produce | Keyframes, holds, inbetweens; pin layers; watch **RAM** |
| Export | File → **Render Animation** (PNG sequence ± video/FFmpeg) |
| Package | `workspace/creative/<slug>/` (`03_krita/`, `04_renders/`, `notes.md`) |

```bash
python fable5_offline_agent.py --automate animation-dev-kit
```

| Resource | Path |
|----------|------|
| Skill | `skills/animation-dev-kit.md` |
| Knowledge | `knowledge/media/krita-animation.md` |
| Workflow | `workflows/animation-dev-kit.json` |
| Render docs | [Render Animation](https://docs.krita.org/en/reference_manual/render_animation.html) |

**Notes:** Krita keeps frames in memory — split long work. User installs Krita (+ optional FFmpeg). Large `.kra` / sequences stay local (gitignored).

## Stop / motion dev kit (Studio · Cloud · Chromebook)

Physical stop-motion with two official paths:

| Path | Best for | Entry |
|------|----------|--------|
| **Stop Motion Studio** | Native Win/Mac/mobile, offline projects | [Download](https://www.stopmotionstudio.com/download/index.html) |
| **Cloud Stop Motion** | **Chromebook** / browser, **cloud-stored** projects, schools | [cloudstopmotion.com](https://cloudstopmotion.com/) · [app](https://app.cloudstopmotion.com) |

| Stage | Focus |
|-------|--------|
| Choose tool | Cloud SM if Chromebook/classroom cloud; Studio if local offline |
| Chromebook | Chrome → app.cloudstopmotion.com → camera permission → sign-in |
| Cloud “upload” | Project saves in vendor cloud; confirm on 2nd device; export finished work |
| School | Org console: users/groups, review, **export finished work** |
| Rig / FPS | Tripod; start ~**6** FPS, **12+** smoother |
| Package | `02_cloud_exports/` · `02_sms_project/` · `04_exports/` · `notes.md` |

```bash
python fable5_offline_agent.py --automate stop-motion-dev-kit
python fable5_offline_agent.py --automate stop-motion-cloud-chromebook
```

| Resource | Path |
|----------|------|
| Skill | `skills/stop-motion-dev-kit.md` |
| Knowledge | `knowledge/media/stop-motion-studio.md`, `cloud-stop-motion.md` |
| Workflows | `stop-motion-dev-kit.json`, `stop-motion-cloud-chromebook.json` |

**Notes:** Official products only. Fable does **not** auto-upload. User HITL for sign-in, cloud save, export. No student PII in git. Hybrid draw → `animation-dev-kit` (Krita). Need ChromeOS on a PC/Mac first? → `chromeos-flex-install-prep`.

## ChromeOS Flex install prep

Install Google’s **ChromeOS Flex** on existing **PCs and Macs** (cloud-first OS; not a Chromebook purchase). Product: [chromeos.google/products/chromeos-flex](https://chromeos.google/products/chromeos-flex/).

| Stage | Focus |
|-------|--------|
| Compat | x86-64, 4 GB RAM, 16 GB storage; [certified models](https://support.google.com/chromeosflex/answer/11513094) only guaranteed |
| Backup | Full install **erases** the disk |
| USB | Chromebook Recovery Utility; stick ≥ 8 GB **wiped** ([create installer](https://support.google.com/chromeosflex/answer/11541904)) |
| Install | [Prepare for installation](https://support.google.com/chromeosflex/answer/11552529) — try USB then install |
| Fleet | Enterprise/Education Upgrade for Admin enrollment (VERIFY LIVE) |
| After | Cloud Stop Motion / browser classroom apps on Flex |

```bash
python fable5_offline_agent.py --automate chromeos-flex-install-prep
```

| Resource | Path |
|----------|------|
| Skill | `skills/chromeos-flex-install-prep.md` |
| Knowledge | `knowledge/chromeos/chromeos-flex.md` |
| Workflow | `workflows/chromeos-flex-install-prep.json` |

**Refuse:** third-party “Flex ISO” mirrors. Official Google Recovery Utility / Help only.

## Google for Education

School/education stack map from the official hub: [edu.google.com](https://edu.google.com/intl/ALL_us/).

| Pillar | Focus |
|--------|--------|
| **Workspace for Education** | Fundamentals (often no-cost) vs paid editions — [compare](https://edu.google.com/intl/ALL_us/workspace-for-education/editions/compare-editions/) |
| **Classroom** | Courses & assignments — [classroom.google.com](https://classroom.google.com) |
| **Chromebooks** | Managed devices — [overview](https://edu.google.com/intl/ALL_us/chromebooks/overview/) |
| **Flex / convert PC** | `chromeos-flex-install-prep` |
| **Creative class** | Cloud Stop Motion + `stop-motion-dev-kit` |

```bash
python fable5_offline_agent.py --automate google-for-education
```

| Resource | Path |
|----------|------|
| Skill | `skills/google-for-education.md` |
| Knowledge | `knowledge/education/google-for-education.md` |
| Workflow | `workflows/google-for-education.json` |

**Notes:** Not legal/compliance advice. No student PII in git. Editions/prices VERIFY LIVE.

## 3D animation dev kit (CG · Blender-first)

CG pipeline plan: model → rig → animate → light → render → deliver. Default DCC: [Blender](https://www.blender.org/download/) (FOSS). Education seed from public [MDS 3D Animation & VFX courses](https://www.mediadesignschool.com/courses/3d-animation-vfx-courses-degrees) (map only — not enrollment advice).

| Track | Focus |
|-------|--------|
| **A · Production** | Scaffold, shot budget, Blender hello-shot → asset/anim/render/finish |
| **B · Education map** | Bachelor / GDCT / foundation certificate overview (VERIFY LIVE fees & entry) |
| Engines | EEVEE lookdev · Cycles finals · prefer image sequences then encode |
| Package | `workspace/creative/<slug>/` (`03_shots/`, `04_renders/`, `06_exports/`) |

```bash
python fable5_offline_agent.py --automate 3d-animation-dev-kit
```

| Resource | Path |
|----------|------|
| Skill | `skills/3d-animation-dev-kit.md` |
| Knowledge | `knowledge/media/3d-animation-pipeline.md` |
| Workflow | `workflows/3d-animation-dev-kit.json` |

**Notes:** No cracked Maya/Houdini/C4D. Not careers advice. Huge caches/renders stay local (gitignored). Hybrid with Krita 2D / stop-motion skills as needed.

## YouTube Live with an encoder

Official protocol: [Create a YouTube live stream with an encoder](https://support.google.com/youtube/answer/2907883?hl=en).

| Step | Action |
|------|--------|
| 1 | Enable live (first time up to **24 hours**) |
| 2 | Install encoder (OBS, Streamlabs, hardware, … — third-party) |
| 3 | Connect cams/mics |
| 4 | Studio → CREATE → Go live → Stream URL + **stream key** → encoder → start |

```bash
python fable5_offline_agent.py --automate youtube-live-encoder-plan
```

| Resource | Path |
|----------|------|
| Skill | `skills/youtube-live-encoder.md` |
| Knowledge | `knowledge/media/youtube-live-encoder.md` |
| Workflow | `workflows/youtube-live-encoder-plan.json` |

**Never commit stream keys.** Defaults for privacy (public/private) depend on age band — set deliberately.

## RSS share

Produce an **RSS 2.0** feed for pull-based sharing (readers subscribe; you don’t spam-push).

```bash
python scripts/rss_share.py --demo -o workspace/demo-feed.xml
python scripts/rss_share.py path/to/items.json -o workspace/feed.xml
python fable5_offline_agent.py --automate rss-share-build
```

| Resource | Path |
|----------|------|
| Skill | `skills/rss-share.md` |
| Knowledge | `knowledge/social/rss-share.md` |
| Script | `scripts/rss_share.py` |
| Workflow | `workflows/rss-share-build.json` |

Add to site HTML: `<link rel="alternate" type="application/rss+xml" title="…" href="https://…/feed.xml" />`.

## Snapchat for Web feed protocol

Desktop Snapchat via **[web.snapchat.com](http://web.snapchat.com/)** (official client).

| Step | Protocol |
|------|----------|
| Browser | Chrome, Edge, or Safari (latest) |
| Login | Credentials + mobile app push confirm; same account on phone |
| Session | **One computer at a time** |
| Feed | Chat feed → open friend → message / Snap / call |
| Snap | Camera → click lens (photo) · hold lens (video) |
| Limits | Subset of Lenses/tools vs mobile; screenshots still possible |

```bash
python fable5_offline_agent.py --automate snapchat-web-session
# Chat after skills load: "Snapchat web feed protocol"
```

| Resource | Path |
|----------|------|
| Skill | `skills/snapchat-web-feed.md` |
| Knowledge | `knowledge/social/snapchat-web-feed.md` |
| Privacy | `knowledge/privacy/snapchat-web-hosts.md` |
| Workflow | `workflows/snapchat-web-session.json` |

**User operates the browser.** No credential storage, no feed scraping.

## TikTok Ads creation

Legitimate **TikTok Ads Manager** planning from Fable data (structure + pixel + UI fingerprint). Official: [ads.tiktok.com](https://ads.tiktok.com/).

| Layer | Content |
|-------|---------|
| Hierarchy | **Campaign → Ad group → Ad** |
| Measurement | Pixel / Events (`tiktok-analytics` + VUW publisher LOAD example) |
| Creative supply | **TTCX** / Partner Exchange marketplace (`tiktok-creative-exchange.md`) |
| UI | TikTok Text/Display, `#fe2c55`, TTAM CSS fingerprint |
| In-house creative | Fit/outfit skills as alternative to TTCX partners |

```bash
python fable5_offline_agent.py --tiktok-ads
python fable5_offline_agent.py --tiktok-ads "conversions campaign for NZ fashion DTC"
python fable5_offline_agent.py --automate tiktok-ads-create
# Chat: /tiktok-ads  /ttads
```

| Resource | Path |
|----------|------|
| Skill | `skills/tiktok-ads-create.md` |
| Knowledge | `knowledge/ads/tiktok-ads-create.md`, `tiktok-creative-exchange.md` |
| Pixel method | `knowledge/privacy/tiktok-analytics.md` |
| TTCX privacy seed | `knowledge/privacy/ttcx-hosts.md` |
| UI fingerprint | `knowledge/web/css-design-fingerprint-tiktok-ui.md` |
| Workflow | `workflows/tiktok-ads-create.json` |

**Refuse:** ad fraud, fake engagement, policy evasion. User publishes and spends in Ads Manager. **VERIFY LIVE** objectives and limits. Not financial advice.

## UC Arts postgraduate study

Hub snapshot: [Arts postgraduate study \| UC](https://www.canterbury.ac.nz/study/academic-study/arts/study-arts/arts-postgraduate-study) (AEM site; meta ~17 Mar 2026 in dump).

| Layer | Content |
|-------|---------|
| Awards | Grad/PG certs & diplomas, BA(Hons)/MusB(Hons), named Masters, research/thesis routes |
| Faculty | Te Kaupeka Toi Tangata \| Faculty of Arts |
| Apply | myUC · eligibility · contact Arts · scholarships |
| Stack | AEM + dual GTM, Adobe Launch, ClickDimensions, Lucky Orange, Monsido, Sentry |

```bash
python fable5_offline_agent.py --education
python fable5_offline_agent.py --education "map UC Arts postgraduate pathways"
python fable5_offline_agent.py --automate uc-arts-pg-map
```

| Resource | Path |
|----------|------|
| Skill | `skills/uc-arts-postgraduate.md` |
| Knowledge | `knowledge/education/uc-arts-postgraduate-study.md` |
| Privacy | `knowledge/privacy/uc-arts-pg-hosts.md` |
| Workflow | `workflows/uc-arts-pg-map.json` |

**VERIFY LIVE** each qualification page for fees and entry. Not admissions advice.

## DOC ranger pathway (NZ)

Curated from DOC’s Conservation blog: [Becoming a DOC ranger](https://blog.doc.govt.nz/2020/01/29/becoming-a-doc-ranger-2/) (Jan 2020).

| Theme | Snapshot |
|-------|----------|
| Formal start | NZ Certificate in **Conservation Operations L4** (NMIT Kaitiaki Whenua / Toi Ohomai cited in 2020) |
| DOC entry | Limited **Trainee Ranger** vacancies after graduation — not guaranteed |
| Other paths | Volunteer, community groups, science, comms, education, policy |
| Careers hub | [doc.govt.nz/careers](https://www.doc.govt.nz/careers/) — **VERIFY LIVE** |

```bash
python fable5_offline_agent.py --doc
python fable5_offline_agent.py --doc "pathway-map: how do I become a DOC ranger?"
python fable5_offline_agent.py --automate doc-ranger-pathway
# Chat: /doc  /ranger
```

| Resource | Path |
|----------|------|
| Skill | `skills/doc-ranger-pathway.md` |
| Knowledge | `knowledge/conservation/doc-ranger-pathway.md` |
| Privacy | `knowledge/privacy/doc-blog-hosts.md` |
| Workflow | `workflows/doc-ranger-pathway.json` |

**Not careers advice.** Re-check providers and vacancies before applying.

## Outfit selector / create (Seamly2D)

Wardrobe **select** or sew **create**, with open-source pattern CAD **Seamly** / Seamly2D.

| Step | Action |
|------|--------|
| Download CAD | User **CLICK** [seamly.io/download](https://seamly.io/download/) (form → email link) |
| Select | Rank closet combos for occasion / vibe |
| Create | Outfit brief → measurements → Seamly project phases → muslin |
| Show | Hand off to `--fit` / Instagram selfie selector |

```bash
python fable5_offline_agent.py --outfit
python fable5_offline_agent.py --outfit "select-outfit: dinner, cool weather, black trousers + ?"
python fable5_offline_agent.py --outfit "seamly-project-plan: A-line skirt first draft"
python fable5_offline_agent.py --automate outfit-seamly-plan
# Chat: /outfit  /seamly  /wardrobe
```

| Resource | Path |
|----------|------|
| Skill | `skills/outfit-selector-create.md` |
| Knowledge | `knowledge/fashion/seamly-outfit-workflow.md`, `outfit-selector-create.md` |
| Workflow | `workflows/outfit-seamly-plan.json` |
| Instagram hand-off | `skills/instagram-selfie-selector.md` |

FOSS apparel CAD (Windows / Linux / macOS). No body shame; no pirated commercial patterns; measurements stay in `knowledge/fashion/_local/`.

## Instagram selfie selector (fits · makeup · slay)

Hype-honest creative direction: rank selfies and OOTDs, check makeup cohesion, draft captions. **You** post in the Instagram app — Fable does not auto-publish.

```bash
python fable5_offline_agent.py --fit
python fable5_offline_agent.py --fit "A blazer mirror fit vs B soft glam close-up — feed hero?"
python fable5_offline_agent.py --automate instagram-fit-select
# Chat: /fit  /slay  /ootd  /selfie
```

| Resource | Path |
|----------|------|
| Skill | `skills/instagram-selfie-selector.md` |
| Knowledge | `knowledge/social/instagram-selfie-playbook.md` |
| Workflow | `workflows/instagram-fit-select.json` |

Procedures: **select-hero**, **fit-check**, **makeup-check**, **slay-score**, **caption-pack**, **post-safety**. No body shame, no fake viral claims, privacy crops for IDs/other people.

## Windows install prep (licensed)

Legal **Windows 11** install and image-hygiene coaching — not a piracy or “Windows 12” rebrand tool.

| Path | What |
|------|------|
| **1. Official media** | [microsoft.com/software-download/windows11](https://www.microsoft.com/software-download/windows11) + genuine key / digital license |
| **2. Enterprise image** | ADK / DISM / `unattend.xml` for **your** machines and licenses (still Windows 11) |
| **3. Fable skill** | Checklists, refuse cracks/rebrand, no keys in git |

```bash
python fable5_offline_agent.py --windows
python fable5_offline_agent.py --windows "official-media-plan for Pro reinstall"
python fable5_offline_agent.py --automate windows-install-prep
# Chat: /windows
```

| Resource | Path |
|----------|------|
| Skill | `skills/windows-install-prep.md` |
| Knowledge | `knowledge/windows/official-media.md`, `dism-unattend-hygiene.md` |
| Workflow | `workflows/windows-install-prep.json` |

**Refuse:** fake Windows 12 ISOs, activators, generic keys. Keep product keys out of the repo (`knowledge/windows/_local/`).

## macOS install prep (Apple-licensed)

Legal **macOS** install hygiene: recovery vs **bootable USB** via Apple’s `createinstallmedia`. Primary doc: [support.apple.com/en-nz/101578](https://support.apple.com/en-nz/101578).

| Path | What |
|------|------|
| **A. Often enough** | Upgrade / reinstall without USB (Software Update, Recovery) |
| **B. Bootable installer** | Full `Install macOS <Name>.app` → USB named `MyVolume` → Terminal `createinstallmedia` (**erases USB**) |
| **C. Fleet** | ADE/MDM on owned Macs; download installers from **Apple** |

```bash
python fable5_offline_agent.py --macos
python fable5_offline_agent.py --macos "bootable-installer-plan for Sequoia"
python fable5_offline_agent.py --automate macos-install-prep
# Chat: /macos
```

| Resource | Path |
|----------|------|
| Skill | `skills/macos-install-prep.md` |
| Knowledge | `knowledge/macos/bootable-installer.md`, `reinstall-and-recovery.md` |
| Workflow | `workflows/macos-install-prep.json` |

**Warn:** target Mac needs **internet** during install; silicon vs Intel boot steps differ. **Refuse:** Hackintosh, torrents, Activation Lock bypass without ownership. VERIFY LIVE Apple’s command table after new macOS releases.

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
| **`tiktok-analytics`** | TikTok pixel: `scan-html` · `confirm-network` · `map-tiktok` · `policy-tension` |

```bash
python fable5_offline_agent.py --privacy
python fable5_offline_agent.py --privacy "design-agent: offline privacy mapper"
python fable5_offline_agent.py --privacy "map-hosts: [paste HTML head/footer]"
python fable5_offline_agent.py --privacy "map-tiktok: Network dump for analytics.tiktok.com"
python fable5_offline_agent.py --automate privacy-host-map
python fable5_offline_agent.py --automate privacy-design-plan
python fable5_offline_agent.py --automate tiktok-analytics-map
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
| [`knowledge/privacy/tiktok-analytics.md`](knowledge/privacy/tiktok-analytics.md) | TikTok Analytics method (HTML + Network) |
| [`knowledge/privacy/wgtn-ac-nz-hosts.md`](knowledge/privacy/wgtn-ac-nz-hosts.md) | VUW: `analytics.tiktok.com` LOAD seed |

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

Workflow step types: `build` · `engineer` · `hermes` · `loop` · `improve` · `compress` · `llm` · `shell` · `note` · `broker` · `legal` · `education` · `privacy` · `calendar` · `windows` · `macos` · `fit` · `outfit` · `doc` · `tiktok_ads` · `math` · `pdf` · `scrape` · `hitl` · `team`.

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
| **agents/** | Offline loop briefs (`hermes-agent.md`, protocol, goals, state) |
| **Smart RAG** | Top-K (`FABLE5_RAG_TOP_K`, default **20**) relevant memory chunks |
| **Self-stop** | Success / retry ceiling / cycle budget |
| **Live repair** | On verifier FAIL → strategy patch for the next unit only |
| **Memory compress** | After multi-cycle Hermes runs → `memory/lessons/compressed-*.md` |
| **Skills** | Optional self-improve writes reusable procedures |

Edit `SOUL.md` to change persona and stop ethics. Edit **`agents/`** to change shared loop protocol for Hermes + Fable + `offline_goal_loop.py`. Quality of soul ≈ quality of compounding.

### Offline loop agents pack

| File | Feeds |
|------|--------|
| `agents/offline-loop-protocol.md` | All loops — verifier · state · stop |
| `agents/hermes-agent.md` | Hermes |
| `agents/fable-loop-agent.md` | `/loop` · `/engineer` |
| `agents/goal-quality.md` | Goal writing |
| `agents/shared-state.md` | `LOOP_STATE` vs `loop_state.json` |
| `agents/math-physics-agent.md` | STEM deep-explain / theorem / physics loops |

Also: `python offline_goal_loop.py --goal "…"` loads the same pack when present.

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
| `FABLE5_AGENTS` | `agents` | Offline loop agent briefing directory |

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

**CLI flags:** `--model` · `--roadmap` · `--team` · `--broker` · `--legal` · `--education` · `--privacy` · `--calendar` · `--ical` · `--windows` · `--macos` · `--fit` · `--outfit` · `--doc` · `--tiktok-ads` · `--deep-explain` · `--theorem` · `--physics` · `--pdf` · `--pdf-pages` · `--pdf-out` · `--scrape` · `--scrape-dir` · `--format` · `--build` · `--automate` · `--engineer` · `--criteria` · `--min-score` · `--loop` · `--hermes` · `--improve` · `--compress-memory` · `--doctor` · `--ascii`

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
| Need Windows install media | `--windows` / `/windows`; official [software-download/windows11](https://www.microsoft.com/software-download/windows11) only |
| Need macOS install USB | `--macos` / `/macos`; Apple [101578 createinstallmedia](https://support.apple.com/en-nz/101578) (USB erased) |

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
- **Education mode** — credential/accreditation claim audit + UC Arts PG pathway map + Google for Education hub map (not educational or medical advice).
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
- **Windows install prep** — licensed Win11 media + DISM/unattend hygiene (not piracy; no fake Windows 12).
- **macOS install prep** — Apple bootable installer / recovery (101578; not Hackintosh or cracked media).
- **Instagram selfie selector** — fits, makeup, slay picks + captions (not auto-post; not body-shame).
- **Outfit / Seamly** — wardrobe select + create briefs + Seamly2D pattern plan ([seamly.io/download](https://seamly.io/download/)).
- **DOC ranger pathway** — Trainee Ranger / L4 conservation map from DOC blog seed (not careers advice).
- **TikTok Ads create** — Ads Manager campaign planning + pixel hygiene (not fraud; not ROAS guarantees).
- **Snapchat Web feed** — official web.snapchat.com Chat/call/snap protocol (not a scraper).
- **RSS share** — RSS 2.0 feed build/share (`scripts/rss_share.py`; pull syndication).
- **YouTube Live encoder** — Studio + encoder setup from Help 2907883 (not stream-key storage).
- **Creative pipeline builds** — Adobe CC + CapCut + Resolve export recipes (licensed apps only).
- **Animation dev kit** — Krita frame-by-frame plan from [docs.krita.org animation manual](https://docs.krita.org/en/user_manual/animation.html) (walk cycle, RAM budget, render/FFmpeg).
- **Stop / motion dev kit** — Stop Motion Studio + [Cloud Stop Motion](https://cloudstopmotion.com/) Chromebook/browser cloud upload/export (automate recipes).
- **ChromeOS Flex install prep** — official Flex on PC/Mac ([product](https://chromeos.google/products/chromeos-flex/)); USB Recovery Utility; certified models.
- **Google for Education** — Workspace · Classroom · Chromebooks map ([edu.google.com](https://edu.google.com/intl/ALL_us/)).
- **3D animation dev kit** — Blender-first CG pipeline + optional [MDS 3D Animation & VFX](https://www.mediadesignschool.com/courses/3d-animation-vfx-courses-degrees) study map (not careers advice).
- **Math / physics agent** — deep-explain, theorem, dimensional solver; durable lessons for Hermes/Fable.
- **Offline prompt generator** — `auto_prompt_generator.py` + `/prompt-gen` → swarm/agent system prompts in `generated_prompts/` (handoff to Hermes/team).

## License

This project is free software under the **[MIT License](LICENSE.md)** ([`LICENSE`](LICENSE) is identical).

Copyright © **2026 David Logan**.

You may use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, provided the copyright and permission notice are included in all copies or substantial portions of the Software. The Software is provided **“AS IS”**, without warranty of any kind, express or implied.

See **[LICENSE.md](LICENSE.md)** (and plain [`LICENSE`](LICENSE)) for the full MIT text plus **additional notices** on:

1. Domain knowledge / skills (not professional advice)  
2. Third-party website and policy snapshots  
3. Emergency routing (**call 111** in NZ emergencies)  
4. Steam / games (ownership required; not a bot or DRM bypass)  
5. Calendar / mail / Zoom (local iCal + drafts; user CLICK join only)  
6. Windows install (licensed Win11 media / DISM only; no rebrand/piracy)  
7. macOS install ([101578](https://support.apple.com/en-nz/101578) `createinstallmedia` only; no Hackintosh/piracy)  
8. Social / RSS / Snapchat Web (no scrape; user-owned feeds only)  
9. Creative apps / pipeline builds (licensed Adobe·CapCut·Resolve only; no cracks)  
10. ChromeOS Flex / Google for Education (official install & hub map; no student PII)  
11. Animation toolkits — Krita 2D, Stop Motion Studio / Cloud SM, Blender 3D  
12. Automatic prompt generator / swarm prompts (not investment advice; review before use)  
13. Contribution licensing  

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
| Windows install prep | Piracy, fake “Windows 12” ISOs, cracks, or free product keys |
| macOS install prep | Hackintosh, cracked installers, or Activation Lock theft |
| ChromeOS Flex / Google for Education | Third-party ISOs, student PII in git, invented edition prices, or compliance guarantees |
| Snapchat Web / RSS | Feed scrape, credential theft, or tokenized private feed URLs in git |
| Creative pipeline builds | Cracked Adobe/CapCut/Resolve, GenP, or committing raw media masters |
| Animation dev kit (Krita) | Auto-running Krita, cracked apps, or committing huge `.kra`/PNG sequences |
| Stop / motion dev kit | Cracked apps, Fable auto-upload, school passwords/PII, or full SMS/cloud libraries in git |
| 3D animation dev kit | Cracked Maya/Houdini/C4D, invented school fees/jobs, or multi-GB EXR/blend caches in git |
| Prompt generator / swarms | Investment advice, live trading, or unreviewed production agents |
| Math / physics agent | Course credit or professional engineering sign-off |

Outputs require **human verification** (and licensed professionals where required) before real-world use.
