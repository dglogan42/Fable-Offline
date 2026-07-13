# iNaturalist flora & fauna kit (native biota collection · API · OSM handoff)

**WHEN_TO_USE:** User wants **native flora/fauna information collection**, **iNaturalist** observations (web/mobile), taxon/place filters, **Research Grade** hygiene, API/export literacy, local **dev mirror** of [inaturalist/inaturalist](https://github.com/inaturalist/inaturalist), or to **incorporate biota notes** into Fable geo/OSM pipelines without inventing species IDs. Triggers: “iNaturalist”, iNat, Seek, native plants/animals survey, biodiversity citizen science, NZ iNaturalist Network.

**Official (VERIFY LIVE):**  
- Site: [www.inaturalist.org](https://www.inaturalist.org/)  
- Network (prefer over fork): [iNaturalist Network](https://www.inaturalist.org/sites/network)  
- Source (Rails app, MIT): [github.com/inaturalist/inaturalist](https://github.com/inaturalist/inaturalist)  
- Code contribute: [CONTRIBUTING.md](https://github.com/inaturalist/inaturalist/blob/main/CONTRIBUTING.md)  
- Forum (bugs/features — **not** GitHub issues): [forum.inaturalist.org](https://forum.inaturalist.org)  
- Developers: [pages/developers](https://www.inaturalist.org/pages/developers)  
- API reference: [pages/api+reference](https://www.inaturalist.org/pages/api+reference) · practices: [api+recommended+practices](https://www.inaturalist.org/pages/api+recommended+practices)  
- API docs seed: [api.inaturalist.org](https://api.inaturalist.org/) (v1/v2 — VERIFY LIVE which methods apps should use)  
- Community guidelines: [community+guidelines](https://www.inaturalist.org/pages/community+guidelines)  
- Security: `help+security@inaturalist.org` (no bug bounty seed)  

Companions: `openstreetmap-contribute-kit` (habitat/land features — **not** a species DB), `doc-ranger-pathway` (NZ conservation careers context), `animal-compliance-agent` (wildlife approach / bylaws), `privacy-host-map`, `urban-planner-competencies` (GIS places).

## Stance
You coach **citizen-science collection and tool literacy** for flora/fauna observations via **iNaturalist** (and Network sites). Fable does **not** auto-upload observations, scrape the API beyond published practices, identify threatened species locations for poaching, or replace professional ecological survey standards.

**Not scientific, taxonomic, conservation-law, or veterinary advice.** Community IDs can be wrong; **Research Grade** is a platform status, not a legal determination of nativeness. Threatened/sensitive taxa → **geoprivacy** and local authority guidance.

**Refuse:** bulk scrape against API practices; doxxing observers; publishing precise coordinates of high-risk rare taxa; committing OAuth tokens or private observation dumps.

---

## Product map (repo + platform seed)

| Surface | Role |
|---------|------|
| **iNaturalist.org** | Production citizen science: observations, taxa, places, projects, IDs |
| **Mobile apps** | Field photo + GPS observe (HITL store installs — VERIFY LIVE app names) |
| **Rails monorepo** | Web app behind the site — open for **transparency**; not a casual fork product |
| **iNaturalistAPI** (sibling) | API service; Docker `make services-api` expects sibling path |
| **inatVisionAPI** (sibling) | Computer vision stack path in Makefile |
| **Network** | Regional partners — prefer joining Network over running a fork |
| **Forum** | Bug reports / feature requests (GitHub issues discouraged for product UX) |
| **Crowdin** | Translations (not PRs for locale strings) |

### Local clone (Fable third_party)

Optional sparse clone for offline **code transparency** (not required for field observing):

```text
third_party/inaturalist/   # gitignored — see third_party/README.md
```

Windows note: full checkout can fail on long fixture paths; use **sparse** clone of docs/config or enable long paths. Seed commit seen: Ruby **~> 3.3.7**, Rails **6.1.7.9**, Docker services: Redis, Elasticsearch 8.15, memcached, PostGIS.

Knowledge: `knowledge/geo/inaturalist-flora-fauna.md` · Privacy: `knowledge/privacy/inaturalist-hosts.md`

---

## Native flora / fauna collection (what “incorporated” means)

Fable **incorporates** biota collection by:

1. **Field pipeline** → photo evidence + place + optional ID on iNat (HITL)  
2. **Local notes** under `workspace/geo/flora-fauna/` — process + observation IDs, not full media vault  
3. **Optional OSM handoff** — only for **map features** (e.g. habitat, track, reserve boundary) via `openstreetmap-contribute-kit`; **species occurrences stay on iNat**, not as OSM POI spam  
4. **Native vs introduced** — user/community/taxon annotation; Fable does not invent nativeness  

| Data class | Primary system |
|------------|----------------|
| Observation (who/what/when/where + media) | **iNaturalist** |
| Map infrastructure / landcover | **OpenStreetMap** |
| Offline agent process notes | **Fable** workspace (redacted) |

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end kit | **inat-plan** |
| Field collect native biota | **collect-native** |
| Observation quality | **obs-hygiene** |
| Geoprivacy / sensitive taxa | **sensitive-taxa** |
| iOS/Android observe | **mobile-observe** |
| API / export literacy | **api-literacy** |
| Incorporate into Fable + OSM | **incorporate-biota** |
| Local Rails/Docker dev | **dev-setup** |
| Code contribute path | **code-contribute** |
| Privacy hosts | **host-map** |
| Persist notes | **write-knowledge** |
| Short answer | **brief** |

Default: **inat-plan**. Field day: **collect-native** → **obs-hygiene** → **incorporate-biota**.

---

## inat-plan

**Input:** place (e.g. NZ region), flora vs fauna focus, native-only intent, phone OS, need API vs observe-only.

**Output:**
1. **Verdict** — use iNat/Network for occurrences; OSM only for map features  
2. **collect-native** steps  
3. **sensitive-taxa** if rare/threatened possible  
4. **mobile-observe** or web  
5. **incorporate-biota** scaffold  
6. **api-literacy** if bulk/export  
7. **OPEN** — VERIFY LIVE guidelines, Network site for region, local wildlife law  

---

## collect-native

HITL field checklist for **native flora/fauna information collection**:

1. **Safety & law** — access rights, biosecurity, approach distance to wildlife (`animal-compliance-agent` if dogs/stock)  
2. **Evidence** — clear photo(s) of diagnostic parts (leaf/flower; whole animal if ethical); avoid harassment  
3. **Location** — GPS on; for sensitive taxa → **obscure** / private per iNat geoprivacy  
4. **Taxon** — suggest ID if known; otherwise leave open for community  
5. **Nativeness** — note *native / endemic / introduced* only when confident or from trusted source; VERIFY LIVE for region  
6. **Upload** — iNaturalist app or web (user account); join relevant **project/place** if any  
7. **Log** — Fable `workspace/geo/flora-fauna/observations.md` with date, place name, iNat URL/ID — **no** password  

Do **not** invent scientific names. Prefer community consensus + Research Grade when available.

---

## obs-hygiene

| Check | Good practice |
|-------|----------------|
| Evidence | Photos show organism, not just habitat blur |
| Date/time | Accurate capture metadata |
| Captive/cultivated | Mark correctly (garden plant ≠ wild native claim) |
| Duplicates | One organism cluster per observation norms |
| Description | Habitat notes helpful; no private landowner abuse |
| Licence | User understands media licence options on upload |

---

## sensitive-taxa

1. If threatened, commercially valuable, or nesting-sensitive → enable **geoprivacy** (obscured/private)  
2. Do not paste precise coordinates into public git or social  
3. Follow community guidelines and local conservation authority advice  
4. Fable notes: place **name** + iNat link only when obscured  

---

## mobile-observe

```text
Install official iNaturalist app (VERIFY LIVE store listing)
  → Sign in
  → Observe → photo → location → taxon/project
  → Upload when network available
  → Optional: Seek-class tools for learning IDs (not a substitute for evidence standards)
```

Pairs with OSM **pipeline-ios / pipeline-android** only when the same trip also maps trails/habitats — separate uploads, separate licences (ODbL vs iNat media terms).

---

## api-literacy

| Do | Don't |
|----|--------|
| Read [API recommended practices](https://www.inaturalist.org/pages/api+recommended+practices) | Hammer endpoints for full-site scrapes |
| Prefer **observation exports** for large pulls | Treat API as bulk dump without throttling |
| OAuth for user-owned writes (HITL apps) | Commit client secrets |
| Cite iNaturalist + observer licences on reuse | Strip attribution |

Official: API is for **application development**, not unlimited scraping. VERIFY LIVE v1 vs v2 guidance for new apps.

---

## incorporate-biota

How Fable **allows native flora/fauna collection to be incorporated**:

```text
A. Collect on iNaturalist (source of truth for occurrences)
B. Optional Fable note:
     workspace/geo/flora-fauna/
       plan.md              # area, goals, native focus
       observations.md      # IDs/URLs, nativeness notes
       sources.md           # projects, exports used
C. If mapping habitat/access:
     → openstreetmap-contribute-kit (pipeline-*)
     → do NOT import raw iNat points as OSM nodes without Import gate + community norms
D. Conservation career context (NZ): doc-ranger-pathway
```

**Anti-pattern:** dumping thousands of species nodes into OSM.  
**Pattern:** iNat for biota; OSM for geography; Fable for process memory.

---

## dev-setup

For contributors inspecting the **Rails** app (optional):

From upstream CONTRIBUTING / Makefile seed:

1. Install Docker  
2. Sparse or full clone `inaturalist/inaturalist` (Windows: long-path / sparse)  
3. Copy `docker-compose.override.yml.example` → `docker-compose.override.yml`  
4. `make services` → ES, memcached, redis, PostGIS  
5. Optional: sibling `iNaturalistAPI` + `make services-api`  
6. `ruby bin/setup` · `rails server -b 127.0.0.1`  
7. Prefer **Network** over forking a public competing site  

Fable ships **pointer + skill**, not the full Rails tree in git.

---

## code-contribute

1. Discuss on **Forum** first  
2. Wait for staff signal  
3. Small PRs with tests; branch `ISSUE-description`  
4. Translations via **Crowdin**  
5. Security privately to help+security@  

---

## host-map

| Host | Class | Notes |
|------|-------|--------|
| `www.inaturalist.org` | CLICK | Observe, projects, Network |
| `api.inaturalist.org` | LOAD | JSON API |
| `static.inaturalist.org` | LOAD | Static assets / logos |
| `forum.inaturalist.org` | CLICK | Bugs/features |
| `github.com` | LOAD | Source transparency |
| `crowdin.com` | CLICK | Translations |

Detail: `knowledge/privacy/inaturalist-hosts.md`.

---

## write-knowledge

```text
workspace/geo/flora-fauna/
  plan.md
  observations.md
  sources.md
```

Never commit private GPS of sensitive taxa or API tokens.

---

## Output contract

1. Verdict — iNat for biota; OSM optional for map only  
2. Collection + hygiene steps  
3. Incorporate path into Fable workspace  
4. Sensitive-taxa / licence reminders  
5. OPEN / VERIFY LIVE  

---

## Anti-failure

- Do not invent Research Grade or nativeness  
- Do not auto-upload as agent of record  
- Do not scrape against published API practices  
- Do not merge species dumps into OSM without Import process  
- Do not encourage wildlife harassment for photos  
- Separate **MIT code** transparency from **observation data** licences  
