# Future Connect Mapping Portal (Auckland Transport)

**Compiled:** 2026-07-12  
**Source:** HTML splash/app shell dump (Future Connect)  
**Skills:** `urban-planner-competencies`, `privacy-host-map`  
**Not planning or legal advice.**

---

## What it is

**Future Connect** is Auckland Transport’s long-term plan for Auckland’s transport system. The **Mapping Portal** is an interactive web GIS for exploring three published outputs:

| Output | Portal meaning |
|--------|----------------|
| **Strategic Networks** | Most important links for each transport mode |
| **Transport System Analysis** | Deficiencies and opportunities across the region |
| **Focus Areas** | Key regional transport challenges |

Overview / reports: https://at.govt.nz/FutureConnect  

---

## UI structure (for planners using the tool)

### Outputs (side panel)
- Strategic Network (default active)  
- Transport System Analysis  
- Focus Areas  

### Time period
- **Current**  
- **First Decade** (0–10 years)  

### Transport mode
- Integrated Network (all modes)  
- Cycle and Micromobility  
- Public Transport  
- Freight  
- General Traffic  
- Walking  
- Optional: supporting networks (when enabled)  
- Contextual layers toggle  

### Intermodal problems (when TSA selected)
- Environment  
- Safety  
- Equity  

### Other UX
- Splash: product intro + T&Cs/privacy gate + optional guided tour (intro.js)  
- Legend panel  
- Layer visibility status in header  
- Feedback / map notes UI partially present (some controls commented out in dump)  

---

## Competency practice mapping

| Portal activity | Competence area |
|-----------------|-----------------|
| Toggle modes/periods/layers | **GIS / technical** — spatial multi-layer literacy |
| Read strategic vs supporting networks | **Design & strategic** — network hierarchy |
| **Mode = Freight** (Current / First Decade) | **Freight network planning** — strategic goods links |
| Integrated vs Freight-only compare | **Multimodal strategic networks** |
| Environment / safety / equity layers | **Project evaluation** + equity lens (freight corridor exposure) |
| Explain map to public/board | **Communication** |
| Cross-check with AT reports/PDFs | **Regulatory / policy knowledge** + `pdf-render` for downloadable reports |

### Freight walkthrough (skill procedure `future-connect-freight`)

1. Strategic Network → **Freight** → Current → note visible hierarchy/legend.  
2. Same mode → **First Decade** → differences only if observed.  
3. Transport System Analysis + Freight → Environment / Safety / Equity if enabled.  
4. Compare **Integrated Network**.  
5. Write one-page freight issues note → full structure via **plan-freight**.  
6. Module detail: `knowledge/urban-planning/freight-plan.md`.

---

## Stack (short)

- Esri **ArcGIS JS 4.21** (`js.arcgis.com`)  
- Local app `js/script.min.js` (layer config)  
- Google Analytics 4 `G-QZXSBZ5249`  
- Privacy map: `knowledge/privacy/at-future-connect-hosts.md`  

---

## Boundaries for Fable agents

- May describe portal structure and help users navigate concepts.  
- Must **not** invent corridor designations, deficiency scores, or “official” Future Connect conclusions not in user-supplied extracts/maps.  
- Network designations change; always prefer live portal + AT publications.  

**Not a substitute for AT statutory processes or professional transport planning advice.**
