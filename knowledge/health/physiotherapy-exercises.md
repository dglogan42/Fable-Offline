# PhysiotherapyExercises.com — offline notes

**Skill:** `physiotherapy-exercises-resource-kit`  
**Companion agent:** `fitness-companion-agent` (patients → injury-route; clinicians → booklet path)  
**Site:** [https://www.physiotherapyexercises.com](https://www.physiotherapyexercises.com/)  
**Privacy:** `knowledge/privacy/physiotherapyexercises-hosts.md`  

**Not medical or physiotherapy advice.** For clinicians building education materials; patients should follow their treating professional.

---

## Product summary (HTML dump seed)

| Field | Value |
|-------|--------|
| Title | PhysiotherapyExercises.com |
| Description | Search exercise database and make booklets for patients |
| OG | 1500+ exercises for people with injuries and disabilities |
| Positioning | Search, select, create professional booklets for clients |
| Assets claim | 1500+ exercises, 5000+ drawings and photos |
| ReleaseDate meta | 2026.06.14 (seed) |
| ReleaseId | 1964 (seed) |
| Country seed | `data-country=NZ` |
| Culture seed | `en-AU` / English |
| Feeds | `/exercise/rss`, `/exercise/atom` |
| PWA | manifest.webmanifest, install prompt hook |

### Paths of interest

| Path | Role |
|------|------|
| `/ExerciseImages/Drawings_Micro/Ex*.jpg` | Micro drawings |
| `/ExerciseImages/Drawings_Thumbnail/` | Thumbnails |
| `/Js/ExerciseData_Common_*.js` | Common exercise data pack |
| `/Js/ExerciseData_English_*.js` | English strings/data |
| `/Sprite/ExerciseData-Style-*.css` | Sprite styles |
| `/media/physio-*.woff` | Brand font |
| `/media/au-*.svg`, `/media/nz-*.svg` | Locale flags |

### Shell tech seeds

- Custom element `ptx-main`  
- Tailwind-like CSS custom properties  
- Hashed Angular/Vite-style `main-*.js`, `polyfills-*.js`, `styles-*.css`  
- `data-staticwebsite` / `data-mainwebsite` both physiotherapyexercises.com  

---

## Clinician workflow seed

```text
Search library → select exercises → build booklet → give to patient
  → document in clinical notes (clinic systems, not public git)
```

---

## Contrast

| Tool | Audience |
|------|----------|
| PhysiotherapyExercises.com | Clinician booklet builder |
| MyFitnessPal | Consumer nutrition tracker |

---

## Scaffold

```text
workspace/health/physiotherapy-exercises/
  notes.md          # process only — no patient IDs
```
