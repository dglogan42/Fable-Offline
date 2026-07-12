# Te Tāruke-ā-Tāwhiri: Auckland’s Climate Plan — knowledge snapshot

**Document:** Auckland Climate Plan (PDF)  
**URL:** https://www.aucklandcouncil.govt.nz/content/dam/ac/docs/plans/climate-plan/auckland-climate-plan.pdf  
**Cover date in extract:** December 2020  
**Pages:** 179 (text layer extracted 2026-07-12 via pypdf)  
**Skills:** `climate-modeling`, `urban-planner-competencies`, `pdf-render`  
**Not legal, planning, or climate-science advice.** Figures below are **plan claims** from the PDF extract — re-verify against the live PDF and any updated council publications.

---

## Identity

| Field | Value (from extract) |
|-------|----------------------|
| Māori title | **Te Tāruke-ā-Tāwhiri** |
| English title | Auckland’s Climate Plan |
| Publisher | Auckland Council (public PDF) |
| Framing | Tāmaki Makaurau response to climate change; mana whenua acknowledged as first peoples |

---

## Core goals (plan claims)

| Goal | Claimed target |
|------|----------------|
| Emissions | **50%** reduction in greenhouse gas emissions by **2030** against a **2016 baseline** |
| Long-term | **Net zero emissions by 2050** |
| Adaptation | Plan for impacts under the **current emissions pathway** (adapt even while reducing) |

Illustrative pathway table (plan, MtCO₂e net):

| | 2016 | 2030 | 2050 |
|--|------|------|------|
| Population (est.) | 1,614,400 | 2,040,100 | 2,464,100 |
| **BAU projection** | 10.1 | 11.5 | **12.4** |
| **Decarbonisation pathway** | 10.1 | **5.1** (−50%) | **0.6** (−94% vs 2016) |
| BAU tCO₂e per capita | 6.3 | 5.6 | 5.0 |
| Pathway tCO₂e per capita | 6.3 | 2.5 | 0.3 |

**Residual emissions:** illustrative pathway ~**6%** remaining in 2050 → plan notes need for further strategies, technology, **sequestration** to reach net zero (shared C40-city issue).

---

## Climate / emissions modelling (plan claims)

| Element | Detail from extract |
|---------|---------------------|
| Purpose | **Illustrative decarbonisation pathway** — one possible path, not a prediction of the future |
| Primary tool | **CURB Tool** (World Bank in partnership with **C40 Cities**) |
| Plus | **Supplementary modelling** across Auckland GHG profile sectors |
| Intentional asymmetry | **Not all sectors modelled** to the same reduction depth — reflects different challenges/opportunities |
| BAU | Business-as-usual projection without the modelled package of actions |
| Graph logic | Coloured bands = sector reductions subtracted from BAU; grey residual under bands |
| Certainty | **Assumptions**; certainty **decreases over time** |
| Policy takeaway in plan | Bold action **across every sector** required for commitments |

### Modelling hygiene (for Fable agents)

1. Label outputs **illustrative pathway** vs **forecast** vs **observation**.  
2. State **baseline year (2016)** and units (**MtCO₂e**).  
3. Separate **inventory/accounting** from **projection models**.  
4. Do not invent sectoral Mt figures not in the extract.  
5. Re-run or cite updates if council publishes a newer inventory/pathway.  
6. Full practice rules: `knowledge/climate/climate-modeling.md` + skill `climate-modeling`.

---

## Structure (priority action areas in plan)

From table of contents / narrative (bilingual sections):

1. Why we need to act now  
2. Reducing our emissions  
3. Adapting to climate change  
4. **Natural environment** (Taiao māori)  
5. **Built environment** (Taiao hanga)  
6. **Transport** (Ikiiki)  
7. **Economy** (Ōhanga)  
8. **Communities and coast**  
9. **Food**  
10. **Energy and industry**  
11. Implementation, roles/partnerships, indicators, glossary  

Plan states **eight priorities for action** for greatest impact on mitigation and adaptation (collaborate across Tāmaki Makaurau; no single actor delivers alone).

---

## Crosswalk to urban / transport / freight practice

| Climate plan theme | Related Fable module |
|--------------------|----------------------|
| Transport decarbonisation | Freight plan (mode shift, HGV), Future Connect networks |
| Built environment / net-zero operations | Urban design, density, energy |
| Communities and coast | Adaptation, equity, coastal hazard literacy |
| Natural environment | Blue-green networks, sequestration language (plan-level) |
| Implementation / indicators | Programme alignment, M&E |

Do **not** treat Future Connect GIS layers as a substitute for this climate plan’s emissions model — different products.

---

## PDF extract hygiene

| Item | Note |
|------|------|
| Local extract | `workspace/climate/auckland-climate-plan-extract.md` (gitignored workspace) |
| Binary | Do not commit the ~8MB PDF |
| Tool | pypdf; 179 pages; text layer present |
| Re-extract | `python fable5_offline_agent.py --pdf workspace/climate/auckland-climate-plan.pdf` |

---

## What to verify next

1. Live PDF still matches Dec 2020 claims (or superseded version).  
2. Latest Auckland GHG **inventory** year and MtCO₂e.  
3. Sector charts (2016–2030 modelled actions) — re-read pages ~44–50 in PDF.  
4. Legal status of plan vs statutory RMA/district plan instruments.  
5. Alignment with national emissions reduction plans (date-sensitive).  

---

## One concrete risk of misuse

Treating the **illustrative CURB pathway** as a guaranteed future or as detailed project-level carbon accounting. The plan itself frames it as **one pathway under assumptions**, with **residual emissions** and **declining certainty** over time.

**Not climate, planning, or investment advice.**
