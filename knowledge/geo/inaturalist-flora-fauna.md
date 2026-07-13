# iNaturalist — native flora & fauna collection

**Skill:** `inaturalist-flora-fauna-kit`  
**Platform:** [https://www.inaturalist.org/](https://www.inaturalist.org/)  
**Source (MIT Rails):** [https://github.com/inaturalist/inaturalist](https://github.com/inaturalist/inaturalist)  
**Privacy:** `knowledge/privacy/inaturalist-hosts.md`  
**Local mirror:** `third_party/inaturalist/` (optional, gitignored) · `third_party/README.md`  

**Not taxonomic or conservation-law advice.** VERIFY LIVE.

---

## Why this pack exists

Fable Offline can **plan and record process** for collecting **native flora/fauna information** via iNaturalist, and **hand off** geographic mapping to OpenStreetMap without confusing the two systems.

| System | Holds |
|--------|--------|
| iNaturalist | Observations, media, community IDs, places/projects |
| OpenStreetMap | Map geometry + tags (trails, reserves, landuse) |
| Fable | Offline checklists, redacted observation logs |

---

## Upstream repo seeds (sparse clone)

| Item | Seed |
|------|------|
| Role | Rails app behind iNaturalist.org |
| Licence | MIT (`MIT-LICENSE`, copyright iNaturalist) |
| Ruby | `~> 3.3.7` (`.ruby-version` / Gemfile) |
| Rails | `6.1.7.9` (Gemfile seed) |
| Docker services | Redis 6, Elasticsearch 8.15, memcached, PostGIS 17 |
| Make targets | `services`, `services-api`, `services-vision-api`, `build`, `clean`, `stop` |
| API sibling default | `../iNaturalistAPI` |
| Vision sibling default | `../inatVisionAPI` |
| Product bugs | **Forum**, not GitHub issues |
| Prefer | [iNaturalist Network](https://www.inaturalist.org/sites/network) over forking community |
| Translations | Crowdin |
| Commit seed (sparse pull) | `46ab9e1` era main (re-check after pull) |

Windows: full clone may fail on long `spec/fixtures/...` paths — use sparse checkout or long-path support.

---

## Collection model

```text
Observe (photo + place + optional ID)
  → Upload (HITL iNat)
  → Community identification
  → Optional Research Grade
  → Export / project membership
  → Fable notes (IDs + nativeness process)
  → Optional OSM for habitat/access only
```

### Native focus hygiene

- Mark **captive/cultivated** correctly  
- Prefer wild, naturalised status from evidence + community  
- “Native” is **region-specific** — VERIFY LIVE taxon/place annotations  
- Sensitive taxa → geoprivacy  

---

## Incorporate with OSM kit

See skill **incorporate-biota** and `openstreetmap-contribute-kit`:

- Same field day can run **pipeline-ios/android** for trails **and** iNat for species  
- Do **not** bulk-import iNat points into OSM  
- Licences differ: OSM **ODbL** vs iNat observation/media terms  

---

## API / data access

- Developers hub + API reference + **recommended practices** (VERIFY LIVE)  
- Large data: prefer **observation exports** over abusive pagination  
- OAuth for authenticated app features — no secrets in git  

---

## Scaffold

```text
workspace/geo/flora-fauna/
  plan.md
  observations.md
  sources.md
```

---

## Related Fable knowledge

- `knowledge/geo/openstreetmap-contribute.md`  
- `knowledge/conservation/doc-ranger-pathway.md`  
- `knowledge/animals/animal-compliance-framework.md`  
