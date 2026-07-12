# Urban planner — core competencies framework

**Compiled:** 2026-07-12  
**Skill:** `urban-planner-competencies`  
**Purpose:** Offline coaching framework for Fable (study paths, skill audits, planning-assistant agent design).  
**Not legal, planning, or engineering advice.**

---

## Role definition

Urban planners require a blend of **spatial analysis**, **policy knowledge**, and **stakeholder management** to design and implement community **land-use strategies**.

Core competencies range from technical work in mapping software to soft skills: **negotiation**, **empathy**, and **creative problem-solving**.

---

## 1. Technical & analytical skills

| Skill | Why it matters |
|-------|----------------|
| **Geographic Information Systems (GIS)** | Critical for mapping infrastructure, analysing land use, visualising spatial data |
| **Data analysis & statistics** | Interpret demographic, economic, and environmental data; discern trends; forecast community needs |
| **CAD & 3D modelling** | Create spatial plans and architectural / urban layouts |
| **Regulatory knowledge** | Local zoning, building codes, environmental regulations, resource management policies |
| **Freight & goods data** | HGV volumes, freight generators (ports, logistics), first/last-mile constraints; observed vs modelled |

**Practice notes**
- Always bind regulation to a **named jurisdiction** and document version.  
- Label forecasts as scenarios with uncertainty.  
- GIS outputs need metadata (source, date, CRS).  
- Freight metrics: never invent counts; cite year and method.  

---

## 2. Communication & interpersonal skills

| Skill | Why it matters |
|-------|----------------|
| **Stakeholder engagement** | Involve community members, business owners, environmental groups in decisions |
| **Freight stakeholders** | Ports, logistics operators, industrial landowners, RCAs, rail, corridor communities |
| **Public speaking & presentation** | Translate technical concepts for boards and the public |
| **Mediation & negotiation** | Facilitate when developers, policymakers, and residents conflict (incl. freight amenity vs access) |
| **Team collaboration** | Multidisciplinary work with architects, civil engineers, economists, transport/freight planners |

**Practice notes**
- Engagement without feedback loops is theatre — record what changed.  
- In Aotearoa NZ contexts, plan for appropriate engagement with **mana whenua** (process depends on project; do not invent protocols).  
- Freight corridors need **both** industry and residential voices.  

---

## 3. Design & strategic capabilities

| Skill | Why it matters |
|-------|----------------|
| **Creative vision** | Visualise untapped potential; envision alternative social and physical environments |
| **Master planning & revitalisation** | Spatial structure, functional public space, sustainable transit systems |
| **Multimodal strategic networks** | Integrate passenger modes **and freight**; hierarchy of strategic vs supporting links |
| **Freight network planning** | Mode split, land-use fit, first/last mile, time horizons, intermodal nodes |
| **Project evaluation** | Feasibility, sustainability, and social impact of proposals (incl. freight reliability, noise, severance) |

**Practice notes**
- Vision without constraints is fantasy; constraints without vision is stagnation.  
- Evaluate with explicit criteria (access, housing, hazard, cost, equity, ecology, **freight access/safety**).  
- Full freight module: `knowledge/urban-planning/freight-plan.md`.  

---

## 4. Management & organisation

| Skill | Why it matters |
|-------|----------------|
| **Decision making** | Choose viable, safe plans under budgets and land constraints |
| **Leadership & organisation** | Multiple projects, staff oversight, alignment with government mandates |
| **Programme alignment** | Link local freight actions to regional transport / port / investment pathways |

**Practice notes**
- Decision logs beat undocumented “professional judgment.”  
- Align to higher-order plans (regional policy, district plan, transport strategy, **freight network plans**).  

---

## Self-audit rubric (1–5)

| Score | Meaning |
|-------|---------|
| 1 | No experience |
| 2 | Course exposure only |
| 3 | Contributed under supervision |
| 4 | Led work with review |
| 5 | Can mentor others / set methods |

Audit all four areas → pick **one technical + one interpersonal** growth focus per quarter.

---

## Fable Offline usage

```bash
# Coach against the framework
python fable5_offline_agent.py --privacy  # if analysing programme marketing pages
# Prefer chat / engineer with skill loaded automatically:
# "Audit my urban planner competencies: [paste CV]"
# "Plan 6 months growth toward council junior planner"
# "Map Master of Urban Design webinar to competencies"
# "Draft a freight plan issues note for [area] using Future Connect freight mode"
python fable5_offline_agent.py --automate urban-planner-checkpoint
python fable5_offline_agent.py --automate freight-plan-review
```

### Related knowledge
- Freight module: `knowledge/urban-planning/freight-plan.md`  
- AT Future Connect portal: `knowledge/urban-planning/at-future-connect-portal.md`  
- Future Connect privacy: `knowledge/privacy/at-future-connect-hosts.md`  
- UoA PG webinar marketing: `knowledge/privacy/uoa-eloqua-pg-webinar-hosts.md` — **privacy map**, not curriculum endorsement.  
- Education claims: skill `education-claim-audit`.  
- Privacy-aware tools: skills `privacy-host-map`, `privacy-design-planner`.  
- PDFs/reports: skill `pdf-render`.  

---

## Agent assist boundaries

A Fable agent may:
- Structure option appraisals and engagement plans  
- Summarise user-supplied plan text  
- Score draft memos against this framework  

A Fable agent must not:
- Issue planning consent or invent zone rules  
- Fabricate hazard or demographic data  
- Replace registered professionals where law requires them  

---

## Source basis

User-supplied competency synthesis (technical, communication, design, management clusters). Treat as a **practice learning framework**, not a statutory competency standard for any single country.
