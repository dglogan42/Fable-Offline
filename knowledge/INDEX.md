# Fable Offline — knowledge data index

Curated **offline notes** loaded into domain modes and skills.  
Prefer these over inventing figures. Re-verify live sources before real decisions.

**Do not commit:** secrets, raw scrapes (`scrape-*`, `*-raw.*`), PDFs, private matters (`**/_local/`, `legal/matters/`). See root `.gitignore`.

---

## Domains

| Folder | Purpose | Key files |
|--------|---------|-----------|
| **ads/** | TikTok Ads Manager + Creative Exchange (TTCX) | `tiktok-ads-create.md`, `tiktok-creative-exchange.md` |
| **aem/** | Adobe AEM public-site patterns | `aem-patterns.md` |
| **animals/** | Animal/dog compliance framework | `animal-compliance-framework.md` |
| **brokers/** | Broker claim snapshots | `ec-markets-regulation.md` |
| **calendar/** | Google Calendar · Zoom · iCal · mail · meetings | `ical-and-google.md`, `zoom-web-join.md`, `meetings-playbook.md` |
| **chromeos/** | ChromeOS Flex install on PC/Mac | `chromeos-flex.md` |
| **climate/** | Climate plan + modelling hygiene | `auckland-climate-plan.md`, `climate-modeling.md` |
| **conservation/** | DOC ranger / Trainee Ranger pathways | `doc-ranger-pathway.md` |
| **culture/** | Arts/exhibitions | `arts-culture-framework.md`, `aag-forever-tomorrow.md` |
| **education/** | Credential claims · UC Arts PG · GfE · Minecraft Edu · Book Creator · TEDx pathways | `lpu-credential-claims.md`, `uc-arts-postgraduate-study.md`, `google-for-education.md`, `minecraft-education.md`, `book-creator-comics.md`, `tedx-learning-pathways.md` |
| **fashion/** | Outfit select/create + Seamly2D CAD | `seamly-outfit-workflow.md`, `outfit-selector-create.md` |
| **geo/** | OpenStreetMap · iNaturalist flora/fauna | `openstreetmap-contribute.md`, `inaturalist-flora-fauna.md` |
| **health/** | Health NZ · fitness companion · MyFitnessPal · PhysiotherapyExercises.com | `fitness-companion-framework.md`, `healthnz-find-a-service.md`, `myfitnesspal.md`, `physiotherapy-exercises.md` |
| **legal/** | Org negotiation playbook | `playbook.md` |
| **macos/** | Apple macOS bootable installer + recovery | `bootable-installer.md`, `reinstall-and-recovery.md` |
| **math/** | Deep-explain + theorem frameworks | `deep-explain-framework.md`, `theorem-framework.md` |
| **media/** | YouTube Live · Adobe · CapCut/Resolve · Krita · Stop Motion · Cloud SM · 3D/CG · Roblox Studio | `youtube-live-encoder.md`, `adobe-cc-desktop.md`, `creative-pipeline-builds.md`, `krita-animation.md`, `stop-motion-studio.md`, `cloud-stop-motion.md`, `3d-animation-pipeline.md`, `roblox-studio.md` |
| **physics/** | Solver + dimensional analysis | `solver-framework.md` |
| **pdf/** | PDF.js + extract hygiene | `pdfjs-and-offline-render.md` |
| **personality/** | MBTI agent personality customiser catalogue | `mbti-types.md` |
| **privacy/** | Third-party host maps + privacy design | See table below |
| **property/** | Property manager framework | `property-manager-framework.md` |
| **public-safety/** | Emergency / Police / FENZ | `emergency-services-framework.md`, `nz-police-105.md`, `fenz-incident-reports.md` |
| **social/** | Instagram fits · Snapchat Web · RSS share | `instagram-selfie-playbook.md`, `snapchat-web-feed.md`, `rss-share.md` |
| **trade/** | Export + freight forwarder | `freight-forwarder-exporter.md`, `mpi-exporter-help.md` |
| **urban-planning/** | Planner competencies, freight, AC programmes | `competencies.md`, `freight-plan.md`, … |
| **steam/** | Steam SIM launch for model soak tests | `sim-games-launch.md` |
| **swarm/** | Offline prompt generator / multi-agent swarm design | `prompt-generator.md` |
| **windows/** | Licensed Win11 media + DISM/unattend hygiene | `official-media.md`, `dism-unattend-hygiene.md` |
| **web/** | CSS media kit · fingerprints · Inkstone SPA | `css-styles-media-kit.md`, `css-design-fingerprint-*.md`, `inkstone-app.md` |

---

## Privacy host maps (`knowledge/privacy/`)

| File | Site / topic |
|------|----------------|
| `DESIGN_PLANNER.md` | Privacy design planner template |
| `design-privacy-agent.md` | Seed privacy-aware agent design |
| `akl-libraries-third-party-hosts.md` | Auckland Libraries catalogue (AEM) |
| `ac-compliance-policy-hosts.md` | AC Compliance Policy page |
| `ac-sports-field-programme-hosts.md` | AC sports field programme (+ Hotjar/Clarity) |
| `at-future-connect-hosts.md` | AT Future Connect portal |
| `uoa-eloqua-pg-webinar-hosts.md` | UoA Eloqua PG webinar LP |
| `aag-forever-tomorrow-hosts.md` | Auckland Art Gallery exhibition |
| `mpi-exporter-help-hosts.md` | MPI Exporter Help |
| `healthnz-find-a-service-hosts.md` | Health NZ Find a service |
| `nz-police-105-hosts.md` | NZ Police 105 |
| `fenz-incident-reports-hosts.md` | FENZ incident reports |
| `google-calendar-hosts.md` | Google Calendar / Meet / mail seed map |
| `zoom-hosts.md` | Zoom Web Client join (`app.zoom.us/wc/join`) seed map |
| `doc-blog-hosts.md` | DOC Conservation blog (WordPress/Jetpack) |
| `uc-arts-pg-hosts.md` | UC Arts postgraduate hub (AEM + multi-analytics) |
| `wgtn-ac-nz-hosts.md` | Victoria University of Wellington — TikTok Analytics seed |
| `tiktok-analytics.md` | TikTok pixel/analytics method (HTML + Network) |
| `ttcx-hosts.md` | TikTok Creative Exchange shell (pumbaa-rule seed) |
| `snapchat-web-hosts.md` | Snapchat for Web (web.snapchat.com) seed |
| `inkstone-hosts.md` | Inkstone SPA (yueimg.com/inkstone) + HiBridge + CF Insights |
| `myfitnesspal-hosts.md` | MyFitnessPal.com homepage third-party map (GTM, CMP, RUM, ads) |
| `physiotherapyexercises-hosts.md` | PhysiotherapyExercises.com (GA, Cloudflare, first-party media) |
| `openstreetmap-wiki-hosts.md` | OpenStreetMap Wiki + map contribute surfaces (MediaWiki seed) |
| `inaturalist-hosts.md` | iNaturalist.org / API / forum / static (flora-fauna kit) |
| `tedx-youtube-hosts.md` | TEDx Talks / TED / TED-Ed YouTube + web watch surfaces |

---

## Urban planning data (`knowledge/urban-planning/`)

| File | Topic |
|------|--------|
| `competencies.md` | Four-area + freight + climate literacy |
| `freight-plan.md` | Strategic freight module |
| `at-future-connect-portal.md` | AT Future Connect UI |
| `ac-compliance-policy.md` | AC Compliance Policy summary |
| `ac-sports-field-capacity-programme.md` | Sports field capacity programme |

---

## Counts (shipped curated markdown)

- Skills: see `skills/INDEX.md`  
- Workflows: `workflows/*.json` (public recipes)  
- Knowledge: curated `.md` under this tree only  

**Disclaimer:** Knowledge notes are research snapshots, not official government or institutional publications. Not financial, legal, medical, planning, customs, or emergency-response advice.
