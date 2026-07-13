# OpenStreetMap contribute kit (pipelines · mobile · 3D/CAD · drone · upload)

**WHEN_TO_USE:** User pastes **OpenStreetMap Wiki** contribute pages, wants to **add map data**, pick **editors** (iD / JOSM / mobile), run **iOS or Android** mapping pipelines, prepare **drone / aerial** or **3D/CAD-derived** features for OSM, or design an **upload portal checklist** (GPS traces, Notes, changeset publish). Triggers: “Contribute map data”, OSM wiki, openstreetmap.org edit, StreetComplete, Vespucci, Go Map, drone orthophoto → OSM, CAD building footprints, ODbL.

**Official (VERIFY LIVE):**  
- Contribute hub: [wiki.openstreetmap.org/wiki/Contribute_map_data](https://wiki.openstreetmap.org/wiki/Contribute_map_data)  
- The map / edit: [www.openstreetmap.org](https://www.openstreetmap.org/)  
- Beginners: [Beginners' guide](https://wiki.openstreetmap.org/wiki/Beginners%27_guide)  
- Editors: [Editors](https://wiki.openstreetmap.org/wiki/Editors) · [Comparison](https://wiki.openstreetmap.org/wiki/Comparison_of_editors)  
- Popular desktop/web: [iD](https://wiki.openstreetmap.org/wiki/ID) · [JOSM](https://wiki.openstreetmap.org/wiki/JOSM)  
- GPS: [Recording GPS tracks](https://wiki.openstreetmap.org/wiki/Recording_GPS_tracks) · [Upload GPS tracks](https://wiki.openstreetmap.org/wiki/Upload_GPS_tracks)  
- Legal: [Contributor Terms](https://wiki.osmfoundation.org/wiki/Licence/Contributor_Terms) · [ODbL](https://wiki.openstreetmap.org/wiki/Open_Database_License) · [Copyright](https://www.openstreetmap.org/copyright)  
- Import / bots: [Import](https://wiki.openstreetmap.org/wiki/Import) · [Automated Edits code of conduct](https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct)  
- Foundation privacy: [OSMF Privacy Policy](https://www.osmfoundation.org/wiki/Privacy_Policy)  

Companions: `inaturalist-flora-fauna-kit` (**native flora/fauna** occurrences — iNat first; do not spam OSM with species nodes), `urban-planner-competencies` (GIS literacy), `3d-animation-dev-kit` / Blender only as **local geometry prep** (not OSM replace), `privacy-host-map`, `rss-share` (wiki Atom recent changes if used carefully).

## Stance
You coach **community contribution pipelines** to OpenStreetMap using **official wiki + map site** paths. Fable does **not** hold OSM account passwords, auto-upload changesets, bulk-import without Import guidelines, or copy **copyrighted** maps/aerials/CAD into OSM.

**Not legal, surveying, aviation, or cadastral advice.** OSM data is under **ODbL** once contributed; users must accept **Contributor Terms**. Local laws (drone flights, privacy of private property, military sites) always win over “map everything.”

**Refuse:** scraping Google/Bing/Apple/HERE proprietary basemaps into OSM; uploading private personal tracks with people/home patterns without consent hygiene; automated vandalism; committing OSM session cookies / OAuth secrets.

---

## Wiki map (HTML dump seed — Contribute map data)

Page seed: **Contribute map data** · revision **3050449** · MediaWiki **1.43.9** · last edit seed **16 June 2026** · category **Contribute**.

Help menu neighbours: Get help · About OSM · Browsing · How to contribute · **Contribute map data** · Editors · Glossary · Beginners' guide.

| Section (wiki) | Links / focus |
|----------------|---------------|
| **General** | Get Involved, Scope / How We Map, Beginners' guide, Elements, Tags, Hardware Guide, Contact channels |
| **Mapping** | Mapping projects, techniques, data collection techniques, Rapid Address Collection, Mappers' guide, Good practice |
| **Editing** | Notes, many editors (iD + JOSM most popular), transparent windows, Aerial imagery |
| **Tagging** | Map Features, country guidelines, Features, proposed tags, Taginfo, standards, proposal process |
| **GPS / satnav** | Record traces · **Upload traces** |
| **Advanced** | Data sources · Automated Edits CoC · **Import** |
| **QA** | Accuracy, Completeness, Vandalism |
| **Conflicts** | Disputes · Data working group |
| **Legal** | Contributor Terms · ODbL · free licence for reuse |

Framing quote seed: *“More than ten million contributors make OpenStreetMap possible.”*

Knowledge: `knowledge/geo/openstreetmap-contribute.md` · Privacy: `knowledge/privacy/openstreetmap-wiki-hosts.md`

---

## Pipeline portal (what Fable means by “upload portal”)

Not a proprietary Fable host — a **HITL checklist** routing data into **official OSM surfaces**:

| Portal surface | Use |
|----------------|-----|
| [openstreetmap.org](https://www.openstreetmap.org/) **Edit** (iD) | Interactive map edits + publish changeset |
| OSM.org **GPS traces** upload | GPX from phone / drone / logger |
| OSM.org **Notes** | Quick “something here” without full edit |
| **JOSM** (desktop) upload | Complex CAD/drone-derived geometry |
| Mobile apps (Android/iOS) | Field survey → direct API edit (per app) |
| Wiki + community | Import proposals, tagging questions |

Fable **plans** the pipeline; user **CLICK**s login, review, and upload.

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end kit | **osm-plan** |
| iOS field pipeline | **pipeline-ios** |
| Android field pipeline | **pipeline-android** |
| 3D / CAD → OSM features | **pipeline-3d-cad** |
| Drone / aerial → OSM | **pipeline-drone** |
| Upload portal checklist | **pipeline-upload** |
| Pick editor | **editor-pick** |
| Tagging hygiene | **tag-hygiene** |
| GPS record + upload | **gps-pipeline** |
| Import / bulk risk gate | **import-gate** |
| QA / conflict | **qa-conflict** |
| Legal / licence brief | **licence-brief** |
| Privacy hosts | **host-map** |
| Scaffold local notes | **write-knowledge** |
| Short answer | **brief** |

Default: **osm-plan**. Field phone: **pipeline-ios** or **pipeline-android**. Photogrammetry/CAD: **pipeline-drone** or **pipeline-3d-cad** then **pipeline-upload**.

---

## osm-plan

**Input:** platform (iOS / Android / desktop), data type (field / GPS / drone / CAD / 3D), area, experience level.

**Output:**
1. **Verdict** — contribute path + complexity (Note / mobile edit / iD / JOSM / import)  
2. **licence-brief**  
3. Chosen **pipeline-***  
4. **editor-pick**  
5. **pipeline-upload** steps  
6. **import-gate** if bulk or automated  
7. **OPEN** — VERIFY LIVE wiki + local law + imagery licence  

---

## pipeline-ios

Field contribution on **iPhone/iPad** (HITL app install from App Store — names VERIFY LIVE on [Editors](https://wiki.openstreetmap.org/wiki/Editors)):

```text
1. Create OSM account (openstreetmap.org) → accept Contributor Terms
2. Install a maintained iOS OSM editor (e.g. Go Map!! / similar — VERIFY LIVE wiki Editors list)
3. Optional: GPX logger or watch for tracks
4. Survey: observe on ground; do not invent from memory alone for critical attributes
5. Edit POIs / ways / notes in-app OR export GPX
6. pipeline-upload: publish small changesets with clear comments
7. Review on openstreetmap.org after tile refresh delay
```

| Do | Don't |
|----|--------|
| Ground-truth names, access, barriers | Trace Google Maps satellite into OSM |
| Small focused changesets | Mass unreviewed AI geometry dumps |
| Use Notes if unsure | Map private interior plans without consent |

---

## pipeline-android

Field contribution on **Android**:

```text
1. OSM account + Contributor Terms
2. Install maintained Android editor(s) — common community tools (VERIFY LIVE Editors wiki):
   StreetComplete (quest-style), Vespucci, Every Door, Organic Maps edit paths, etc.
3. Offline areas if needed for survey
4. Capture attributes (surface, access, opening hours) per Map Features + country guidelines
5. Upload when online; fix conflicts carefully
6. Optional GPX → GPS traces upload
```

StreetComplete-style apps are excellent for **incremental QA**, not full CAD imports.

---

## pipeline-3d-cad

OSM is **not** a general 3D CAD repository. Use CAD/Blender as **prep**, then map to **OSM elements + tags** (2D footprint primary; height / levels / simple 3D tags where accepted).

```text
1. Confirm data rights — you own survey OR ODbL-compatible source (never proprietary CAD of unknown origin)
2. Local prep (HITL): CAD/GIS/Blender → clean 2D footprints / roof outlines in local CRS → WGS84
3. Simplify: remove interior furniture, MEP, non-mappable detail
4. Map to Elements (node/way/relation) + Tags (building=*, height, building:levels, …) via Map Features
5. Prefer manual JOSM / iD upload of reviewed geometry over blind Import
6. Large datasets → import-gate (community consultation)
7. Do not upload full 3D mesh libraries as OSM “data” — use accepted Simple 3D Building practices (VERIFY LIVE wiki)
```

Cross-link: `3d-animation-dev-kit` only for local mesh cleanup; **publish path is OSM tags**, not glTF to osm.org.

---

## pipeline-drone

Drone / UAV → OSM:

```text
1. Legal flight + privacy: local aviation rules, no-fly zones, neighbour privacy (user responsibility)
2. Capture: geotagged imagery / orthomosaic / GPS track
3. Licence check: only use imagery you may use as mapping reference (or official open aerial layers listed for OSM)
4. Process offline: orthophoto + GCPs if needed; export GPX of flight path optional
5. Edit: load licensed imagery as background in JOSM/iD (where allowed) OR survey-grade digitise footprints
6. Upload: geometry + tags via editor; optional GPX to GPS traces
7. Never claim military / sensitive restricted sites against community/local rules
```

Wiki anchors: [Aerial imagery](https://wiki.openstreetmap.org/wiki/Aerial_imagery), [Hardware Guide](https://wiki.openstreetmap.org/wiki/Hardware_Guide), [Recording GPS tracks](https://wiki.openstreetmap.org/wiki/Recording_GPS_tracks).

Bulk automated tracing of entire cities → **import-gate**.

---

## pipeline-upload

**Upload portal checklist** (official OSM, user HITL):

| Step | Surface | Action |
|------|---------|--------|
| A | Account | Log in at openstreetmap.org |
| B | Licence | Confirm Contributor Terms understanding |
| C1 | Map edit | Edit with iD/JOSM/mobile → **Upload** / Save with changeset comment |
| C2 | GPS | My GPS traces → upload GPX (visibility settings intentional) |
| C3 | Notes | Drop Note if not ready to map fully |
| D | QA | Check for overlaps, tagging mistakes, good practice |
| E | Community | Respond to changeset discussions; use contact channels if stuck |
| F | Advanced only | Import wiki process + Automated Edits CoC |

Changeset comments: **what + where + why** (good practice).

---

## editor-pick

| Need | Prefer (VERIFY LIVE) |
|------|----------------------|
| First edit in browser | **iD** on openstreetmap.org |
| Complex relations, CAD layers, plugins | **JOSM** |
| Quick report | **Notes** |
| Android quests / attributes | StreetComplete-class tools |
| Full mobile edit | Vespucci / Go Map!! class tools |
| Bulk / scripted | Only with **import-gate** + CoC |

Wiki: popular editors are **iD** and **JOSM**.

---

## tag-hygiene

1. Prefer established tags on [Map Features](https://wiki.openstreetmap.org/wiki/Map_Features)  
2. Country/territory rules: Tagging guidelines by country  
3. Discover usage: [Taginfo](https://wiki.openstreetmap.org/wiki/Taginfo)  
4. New concepts: proposal process — don’t invent silent one-off keys for major features  
5. Editing standards and conventions  

---

## gps-pipeline

1. Record traces (phone / dedicated GNSS / drone log) — [Recording GPS tracks](https://wiki.openstreetmap.org/wiki/Recording_GPS_tracks)  
2. Clean outliers offline if needed  
3. Upload — [Upload GPS traces](https://wiki.openstreetmap.org/wiki/Upload_GPS_tracks)  
4. Use tracks as **background** while drawing ways in editor  
5. Privacy: prefer non-identifying visibility for home/work commute patterns when appropriate  

---

## import-gate

Hard stop before bulk load:

| Question | If no → stop |
|----------|----------------|
| Compatible licence? | No import |
| Documented on wiki Import guidelines? | No silent dump |
| Local community consulted? | Pause |
| Automated Edits CoC followed? | No bot spam |
| Reversible / documented source? | Fix process |

Links: [Import](https://wiki.openstreetmap.org/wiki/Import), [Automated Edits code of conduct](https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct), [Data sources](https://wiki.openstreetmap.org/wiki/Category:Data_sources).

---

## qa-conflict

- Accuracy / Completeness / Vandalism pages  
- Disputes → talk, then [Data working group](https://wiki.openstreetmap.org/wiki/Data_working_group) paths as published  
- Do not edit-war  

---

## licence-brief

| Topic | Seed |
|-------|------|
| Contribute under | [Contributor Terms](https://wiki.osmfoundation.org/wiki/Licence/Contributor_Terms) |
| Database licence | [Open Database License (ODbL)](https://wiki.openstreetmap.org/wiki/Open_Database_License) |
| Reuse | [openstreetmap.org/copyright](https://www.openstreetmap.org/copyright) |
| Wiki text dump | CC BY-SA 2.0 (footer seed) — separate from map data ODbL |

---

## host-map

| Host | Class | Notes |
|------|-------|--------|
| `wiki.openstreetmap.org` | LOAD | MediaWiki contribute docs |
| `www.openstreetmap.org` | CLICK | Map, edit, GPS, notes, account |
| `wiki.osmfoundation.org` | LOAD | Contributor Terms |
| `www.osmfoundation.org` | LOAD | Privacy policy |
| `upload.wikimedia.org` | LOAD | Some wiki images in dump |

Detail: `knowledge/privacy/openstreetmap-wiki-hosts.md`.

---

## write-knowledge

```text
workspace/geo/osm-contribute/
  plan.md           # area + pipeline chosen
  sources.md        # licence notes for imagery/CAD
  changesets.md     # optional local log of changeset IDs (no passwords)
```

Do not commit raw private GPX of homes, OAuth tokens, or bulk proprietary CAD.

---

## brief

One paragraph: platform + pipeline name + official upload surface + ODbL reminder.

---

## Output contract

1. Verdict + pipeline name  
2. Licence / import gate if relevant  
3. Step checklist (HITL)  
4. Official wiki/map links  
5. OPEN / VERIFY LIVE  

---

## Anti-failure

- Do not invent new primary tags as global standards without proposal process  
- Do not copy proprietary basemaps  
- Do not auto-upload as the agent of record  
- Do not treat OSM as a free CAD vault for full 3D assets  
- Do not skip Import CoC for bulk drone cities  
- Separate **wiki** (CC BY-SA seed) from **map data** (ODbL)  
