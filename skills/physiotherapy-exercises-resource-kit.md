# PhysiotherapyExercises.com resource kit

**WHEN_TO_USE:** User dumps or plans use of **PhysiotherapyExercises.com** — search exercise database, build **patient booklets**, AU/NZ locale, RSS of exercises, or privacy map of the SPA. Triggers: “physiotherapy exercises”, ptx, exercise booklet for patients, physiotherapyexercises.com.

**Official (VERIFY LIVE):**  
- Site: [https://www.physiotherapyexercises.com](https://www.physiotherapyexercises.com/)  
- English host seed: `https://english.physiotherapyexercises.com` (og:url)  
- RSS: `/exercise/rss` · ATOM: `/exercise/atom`  
- Tagline seeds: 1500+ exercises; search, select, create professional booklets for clients  

Companions: `fitness-companion-agent` (routes patients off DIY rehab; clinicians stay on booklet path), `privacy-host-map`, `rss-share` (generic RSS hygiene), `myfitnesspal-resource-kit` only as consumer tracker contrast, `emergency-services-agent` for acute injury red flags (not exercise prescription).

## Stance
You map a **clinician-facing exercise library tool** for building handouts/booklets. Fable does **not** prescribe exercises, diagnose, or replace a physiotherapist’s clinical reasoning.

**Not medical, physiotherapy, or legal advice.** Injuries and disabilities need **qualified clinicians**. Patient-identifying booklets stay private. Under-18 and post-op protocols need human professionals.

**Refuse:** DIY “rehab plans” for undiagnosed pain, scraping the full image DB for piracy, or storing patient names/IDs in git.

---

## Product map (HTML dump seed)

| Surface | Notes |
|---------|--------|
| **Exercise database** | Searchable library (1500+ exercises, 5000+ drawings/photos — marketing) |
| **Booklets** | Select exercises → professional patient/client booklets |
| **Images** | Drawings + photos under `/ExerciseImages/` (micro, thumbnail paths) |
| **Locale** | `data-country=NZ`, `data-defaultculture=en-AU`, AU/NZ flags preloaded |
| **PWA** | `manifest.webmanifest`, apple-mobile-web-app meta, install prompt listener |
| **Feeds** | RSS + Atom for exercises |
| **Release** | meta `ReleaseDate` 2026.06.14, ReleaseId 1964 (dump seed) |

Stack seeds: custom element `ptx-main`, Tailwind-like CSS vars, hashed styles/scripts, sprite CSS for exercise data, JS language packs `ExerciseData_English_*.js`.

Knowledge: `knowledge/health/physiotherapy-exercises.md` · `knowledge/privacy/physiotherapyexercises-hosts.md`

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end kit | **ptx-plan** |
| Clinician booklet workflow | **booklet-workflow** |
| Search / filter exercises | **search-exercises** |
| Patient handout hygiene | **patient-hygiene** |
| Locale / AU-NZ | **locale-notes** |
| RSS/Atom | **feeds** |
| Privacy hosts | **host-map** |
| Design fingerprint | **css-fingerprint** |
| Red-flag escalation | **red-flags** |
| Short answer | **brief** |

Default: **ptx-plan**.

---

## ptx-plan

**Input:** clinician vs patient user, body region if known, booklet vs search only.

**Output:**
1. **Verdict** — clinician booklet tool; not consumer workout app  
2. **booklet-workflow** or **search-exercises**  
3. **patient-hygiene** + **red-flags**  
4. **host-map** if dump/audit  
5. **OPEN** — clinical responsibility, license/ToS VERIFY LIVE  

---

## booklet-workflow

User (clinician) **CLICK** only on live site:

1. Open [physiotherapyexercises.com](https://www.physiotherapyexercises.com/) (JS required)  
2. Search/filter exercises for the **clinical presentation** (clinician judgment)  
3. Select drawings/photos appropriate to patient literacy and equipment  
4. Build **booklet** for client education  
5. Export/print per site tools (VERIFY LIVE formats)  
6. Document in clinical record per local practice rules — **not** in Fable public git  

Fable may draft **structure** (cover, precautions page, exercise list template) only when user supplies content.

---

## search-exercises

- Use site search/categories (UI VERIFY LIVE)  
- Prefer site’s own filters over inventing exercise IDs  
- Image paths like `ExerciseImages/Drawings_Micro/Ex####.jpg` are library assets — cite URL if needed, don’t bulk-mirror  

---

## patient-hygiene

1. No patient names, DOB, NHI, or photos in Fable memory/git  
2. Booklets are **clinical communication** — follow privacy law and clinic policy  
3. Clear “stop if pain worsens / seek care” clinician-authored wording  
4. Language: site default en-AU; NZ country flag on dump — match patient language needs  

---

## locale-notes

Dump seeds:

- `data-country=NZ`  
- `data-defaultculture=en-AU`  
- `data-defaultlanguage=english`  
- `data-mainwebsite` / `data-staticwebsite` → physiotherapyexercises.com  
- Preload flags: `media/au-*.svg`, `media/nz-*.svg`  

VERIFY LIVE multi-language/static site variants.

---

## feeds

| Feed | Path |
|------|------|
| RSS | `https://www.physiotherapyexercises.com/exercise/rss` |
| Atom | `https://www.physiotherapyexercises.com/exercise/atom` |

Use `rss-share` skill for general RSS hygiene; do not republish full exercise media without rights.

---

## host-map

| Host | Class | Notes |
|------|-------|--------|
| `www.physiotherapyexercises.com` | LOAD | App, media, JS packs, sprites |
| `english.physiotherapyexercises.com` | CLICK/CONFIG | og:url seed |
| `www.googletagmanager.com` | LOAD | gtag **UA-20604563-1** |
| `static.cloudflareinsights.com` | LOAD | Cloudflare beacon |

Detail: `knowledge/privacy/physiotherapyexercises-hosts.md`.

---

## css-fingerprint

| Signal | Seed |
|--------|------|
| Stack | Tailwind-like utility vars + hashed `styles-*.css` |
| Body | `ptx-noselect` (user-select none on main) |
| Custom font | `physio-*.woff` preload |
| Brand SVG | Purple/orange gradient hero, “PhysioTherapy eXercises” |
| Accent stroke | `#BE1E2D` on logo ring seed |

Optional catalog row via `css-styles-media-kit`.

---

## red-flags

Escalate to human clinician / emergency pathways (not Fable exercise picks):

- Cauda equina signs, unexplained weight loss, night pain, fever, trauma with neuro deficit  
- NZ emergency: call **111** · skill `emergency-services-agent`  

---

## Output contract

1. Verdict — clinician tool  
2. Workflow or host map  
3. **Not physiotherapy advice** disclaimer  
4. Privacy for patient materials  
5. OPEN  

---

## Anti-failure

- Do not prescribe reps/sets for undiagnosed injury  
- Do not scrape entire image library  
- Do not invent exercise IDs or clinical indications  
- UA analytics is not a clinical endorsement  
