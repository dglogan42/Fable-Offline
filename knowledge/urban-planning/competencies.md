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

**Practice notes**
- Always bind regulation to a **named jurisdiction** and document version.  
- Label forecasts as scenarios with uncertainty.  
- GIS outputs need metadata (source, date, CRS).  

---

## 2. Communication & interpersonal skills

| Skill | Why it matters |
|-------|----------------|
| **Stakeholder engagement** | Involve community members, business owners, environmental groups in decisions |
| **Public speaking & presentation** | Translate technical concepts for boards and the public |
| **Mediation & negotiation** | Facilitate when developers, policymakers, and residents conflict |
| **Team collaboration** | Multidisciplinary work with architects, civil engineers, economists |

**Practice notes**
- Engagement without feedback loops is theatre — record what changed.  
- In Aotearoa NZ contexts, plan for appropriate engagement with **mana whenua** (process depends on project; do not invent protocols).  

---

## 3. Design & strategic capabilities

| Skill | Why it matters |
|-------|----------------|
| **Creative vision** | Visualise untapped potential; envision alternative social and physical environments |
| **Master planning & revitalisation** | Spatial structure, functional public space, sustainable transit systems |
| **Project evaluation** | Feasibility, sustainability, and social impact of proposals |

**Practice notes**
- Vision without constraints is fantasy; constraints without vision is stagnation.  
- Evaluate with explicit criteria (access, housing, hazard, cost, equity, ecology).  

---

## 4. Management & organisation

| Skill | Why it matters |
|-------|----------------|
| **Decision making** | Choose viable, safe plans under budgets and land constraints |
| **Leadership & organisation** | Multiple projects, staff oversight, alignment with government mandates |

**Practice notes**
- Decision logs beat undocumented “professional judgment.”  
- Align to higher-order plans (regional policy, district plan, transport strategy).  

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
python fable5_offline_agent.py --automate urban-planner-checkpoint
```

### Related knowledge
- UoA PG webinar marketing (Urban Design among topics): `knowledge/privacy/uoa-eloqua-pg-webinar-hosts.md` — **privacy map**, not curriculum endorsement.  
- Education claims: skill `education-claim-audit`.  
- Privacy-aware tools: skills `privacy-host-map`, `privacy-design-planner`.  

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
