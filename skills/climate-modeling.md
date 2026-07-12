# Climate modeling (pathways, inventory, hazards)

**WHEN_TO_USE:** City/regional climate plans, GHG pathways, BAU vs decarbonisation curves, CURB/C40-style tools, emissions targets (e.g. 2030/2050), adaptation vs mitigation splits, or PDFs such as **Te Tāruke-ā-Tāwhiri: Auckland’s Climate Plan**. Also when urban/freight/transport plans claim “climate aligned” reductions.

## Stance
Climate **models and pathways are tools under assumptions**, not oracles. Prefer **source-cited** baselines, units, and scenario names. Apply Section 4 (**re-derive** tables). Do not invent MtCO₂e, sector shares, or RCP/SSP labels.

**Not climate science consultancy, legal, or investment advice.**

## Companion skills
| Skill | Role |
|-------|------|
| `pdf-render` | Extract plan PDFs offline |
| `urban-planner-competencies` | Land use, transport, freight co-benefits/conflicts |
| `rederive-numbers` | Check pathway arithmetic |
| `edge-vs-luck` | Avoid overclaiming from single pathways |
| `privacy-host-map` | If plan is only a web app with trackers |

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| Read/structure a climate plan PDF | **structure-plan** |
| Document emissions modelling | **map-modeling** |
| Critique a pathway/BAU chart | **audit-pathway** |
| Link climate to urban/freight/transport | **crosswalk-spatial** |
| Adaptation / hazard side | **map-adaptation** |
| Persist knowledge | **write-knowledge** |

Default: **structure-plan** if PDF/extract present; **map-modeling** if user asks about models/tools.

---

## structure-plan

1. Identity — title, date, publisher, URL  
2. Goals — mitigation targets + adaptation goals (verbatim claims)  
3. Priority action areas / sectors  
4. Modelling section summary (tool, baseline, BAU, pathway)  
5. Implementation / indicators if present  
6. Gaps / what needs live verification  
7. Hand off to domain skills  

**Auckland seed:** `knowledge/climate/auckland-climate-plan.md`  
**Source PDF:** https://www.aucklandcouncil.govt.nz/content/dam/ac/docs/plans/climate-plan/auckland-climate-plan.pdf  

---

## map-modeling

Capture:

| Field | Required |
|-------|----------|
| Tool name(s) | e.g. CURB (World Bank / C40) + supplementary |
| Purpose | Inventory / illustrative pathway / hazard |
| Baseline year | e.g. 2016 |
| Units | MtCO₂e, t/capita |
| Scenarios | BAU, pathway names |
| Sector coverage | Equal or intentional asymmetry |
| Residual | What’s left at horizon |
| Uncertainty language | From source |
| Not modelled | Explicit gaps |

**Auckland plan claim:** CURB + supplementary modelling for **illustrative** decarbonisation; not all sectors equal; residual ~6% in 2050 pathway narrative → sequestration/tech beyond package.

---

## audit-pathway

1. Re-state targets and baseline.  
2. Re-derive % reductions from absolute Mt if both given.  
3. Flag: illustrative vs forecast; declining certainty; residual.  
4. Equity / land-use / freight feedbacks present or missing.  
5. Verdict: **usable for strategy framing** / **insufficient for project carbon** / **needs update**.  

Example re-derive (Auckland table claims): 5.1/10.1 ≈ 50% reduction 2030; 0.6/10.1 ≈ 94% by 2050 — matches plan’s stated % if arithmetic holds.

---

## crosswalk-spatial

Link climate actions to:
- **Transport / freight** — mode shift, HGV, strategic networks (`freight-plan`, Future Connect)  
- **Built environment** — density, retrofit, energy  
- **Coast/communities** — adaptation equity  
- Do not invent quantified co-benefits without sources  

---

## map-adaptation

Separate from mitigation pathways:
- Hazards named (flood, heat, coastal, etc.)  
- Whether GCM/downscaled products cited  
- Planning response types (avoid, protect, accommodate, retreat)  
- Data gaps  

Auckland plan includes dedicated **Adapting to climate change** section — detail from extract/PDF, don’t invent hazard layers.

---

## write-knowledge

- `knowledge/climate/<slug>.md` curated only  
- No binary PDFs in git  
- Cite URL + extract date + tool (pypdf)  

---

## Forbidden
- Inventing emissions inventories or pathway Mt  
- Claiming “Paris-aligned” without source definition  
- Treating one city pathway as global climate science  
- Project-level carbon certification from a city illustrative curve alone  

## Local knowledge
- `knowledge/climate/climate-modeling.md`  
- `knowledge/climate/auckland-climate-plan.md`  

## Note
Models inform **decisions under uncertainty**. Planners still need statutory, equity, and delivery tests beyond the curve.
