# OpenStreetMap — contribute map data (pipelines)

**Skill:** `openstreetmap-contribute-kit`  
**Primary page:** [Contribute map data](https://wiki.openstreetmap.org/wiki/Contribute_map_data)  
**Permalink seed:** revision **3050449** (dump)  
**Privacy:** `knowledge/privacy/openstreetmap-wiki-hosts.md`  

**Not legal, surveying, or aviation advice.** VERIFY LIVE wiki before contributing.

---

## Page framing (dump seed)

- Title: **Contribute map data**  
- Project scale seed: **10M+ contributors**  
- Help tab context: How to contribute family (Get help, About, Browsing, Contribute map data, Editors, Glossary, Beginners' guide)  
- Stack: MediaWiki **1.43.9**, Vector legacy skin  
- Wiki licence footer seed: **CC BY-SA 2.0** (wiki text; map data is **ODbL**)  
- Last edited seed: **16 June 2026**, 20:33  

---

## Topic index (from wiki sections)

### General
- [Getting Involved](https://wiki.openstreetmap.org/wiki/Getting_Involved#Working_on_the_map)  
- [Scope](https://wiki.openstreetmap.org/wiki/Scope) · [How We Map](https://wiki.openstreetmap.org/wiki/How_We_Map)  
- [Beginners' guide](https://wiki.openstreetmap.org/wiki/Beginners%27_guide)  
- [Elements](https://wiki.openstreetmap.org/wiki/Elements) · [Tags](https://wiki.openstreetmap.org/wiki/Tags)  
- [Hardware Guide](https://wiki.openstreetmap.org/wiki/Hardware_Guide)  
- [Contact channels](https://wiki.openstreetmap.org/wiki/Contact_channels)  

### Mapping
- Mapping projects · techniques · data collection techniques  
- Rapid Address Collection · Mappers' guide · Good practice  

### Editing
- [Notes](https://wiki.openstreetmap.org/wiki/Notes)  
- Editors: many; popular **iD**, **JOSM** · [Comparison of editors](https://wiki.openstreetmap.org/wiki/Comparison_of_editors)  
- Aerial imagery · transparent windows  

### Tagging
- Map Features · country tagging guidelines · Features / Proposed features  
- Taginfo · Editing standards · Proposal process  

### GPS
- Recording GPS tracks · **Upload GPS tracks**  

### Advanced
- Data sources · Automated Edits code of conduct · **Import**  

### QA & conflicts
- Accuracy · Completeness · Vandalism  
- Disputes · Data working group  

### Legal
- [Contributor Terms](https://wiki.osmfoundation.org/wiki/Licence/Contributor_Terms)  
- [Open Database License](https://wiki.openstreetmap.org/wiki/Open_Database_License)  
- [openstreetmap.org/copyright](https://www.openstreetmap.org/copyright)  

---

## Fable pipeline portal (official surfaces only)

| Pipeline | Device / data | Primary tools | Upload target |
|----------|---------------|---------------|---------------|
| **pipeline-ios** | iPhone/iPad field | iOS OSM editors (VERIFY LIVE Editors list), optional GPX | OSM API via app + GPS traces |
| **pipeline-android** | Android field | StreetComplete-class, Vespucci-class, etc. | OSM API via app |
| **pipeline-3d-cad** | CAD/Blender/GIS prep | Local simplify → JOSM/iD | Changeset (tags + footprints) |
| **pipeline-drone** | UAV imagery + tracks | Licensed orthophoto background + JOSM/iD | Changeset + optional GPX |
| **pipeline-upload** | Any | Account → edit/GPS/Notes | [openstreetmap.org](https://www.openstreetmap.org/) |

### Decision tree

```text
New contributor, small fix?
  → iD on openstreetmap.org OR Notes
Field attributes on phone?
  → pipeline-ios / pipeline-android
Have GPX only?
  → gps-pipeline → draw in editor
Have drone orthophoto or CAD mass geometry?
  → rights check → pipeline-drone / pipeline-3d-cad
  → if city-scale bulk → import-gate (do not silent dump)
```

---

## What OSM is not (pipeline boundaries)

| Not this | Instead |
|----------|---------|
| Free dump of Google/Bing imagery traces | Only permitted imagery layers / your survey |
| Full BIM/CAD model host | Footprints + tags (+ simple 3D tags where documented) |
| Auto-bot without CoC | Import process + community |
| Private property indoor secrets by default | Good practice + local norms |

---

## Scaffold

```text
workspace/geo/osm-contribute/
  plan.md
  sources.md
  changesets.md
```

Sensitive GPX / tokens → keep local; see `.gitignore` patterns.

---

## Related Fable skills

- `inaturalist-flora-fauna-kit` — native flora/fauna **observations** (iNaturalist); pair with OSM for habitat/access only  
- `urban-planner-competencies` — GIS / spatial literacy  
- `3d-animation-dev-kit` — local 3D prep only  
- `privacy-host-map` — host classification  
