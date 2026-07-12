# Privacy design planner — template & playbook

**Skill:** `privacy-design-planner` (`skills/privacy-design-planner.md`)  
**Evidence skill:** `privacy-host-map`  
**Not legal advice.** Copy sections into `design-<slug>.md` for each product or agent.

---

## When to use this template

1. Designing a **privacy-aware agentic AI** (tools, memory, HITL).  
2. Planning a **multi-step privacy review** of a site or app.  
3. Turning host maps in this folder into a **roadmap of artifacts**.  

---

## Design brief (fill once)

| Field | Value |
|-------|--------|
| **Purpose (one sentence)** | |
| **Users / data subjects** | |
| **Data categories** | e.g. contact, auth, health, location, ads IDs |
| **Jurisdictions (if known)** | e.g. NZ, AU, EU — mark UNKNOWN if not |
| **Online surface** | URL(s) or “offline agent only” |
| **Agentic?** | Y/N — goal loop, tools, multi-agent |
| **Non-goals** | What we refuse to build/claim |
| **Owner** | |
| **Date** | |

---

## Phase plan (default)

| Phase | Goal | Exit criteria | Default artifacts |
|-------|------|---------------|-------------------|
| **P0 Evidence** | Know what loads and what is collected | All LOAD/CONFIG hosts tagged; form fields listed | `*-third-party-hosts.md` via host-map |
| **P1 Risks** | Name tensions and top risks | Risk register ≥ 3 items with verify-how | Section in `design-<slug>.md` |
| **P2 Controls** | Mitigations + HITL gates | Each high risk has a control | Controls table |
| **P3 Automate** | Repeatable offline agent runs | Workflow runs map/plan | `workflows/privacy-*.json` |
| **P4 Compound** | System gets smarter | Skill/INDEX update if reusable | skill patch proposal |

---

## Agentic AI privacy design checklist

### Agent that **analyzes** privacy
- [ ] Goal cannot be “declare legal compliance”  
- [ ] Tools: read/scrape allowlist, write knowledge — no live form POST of real PII  
- [ ] Verifier separate from mapper  
- [ ] BUNDLE hosts never reported as confirmed LOAD  
- [ ] Stop rules + cycle budget  
- [ ] Output path under `knowledge/privacy/`  

### Agent that **processes** personal data
- [ ] Data minimisation stated  
- [ ] Tool least privilege (network/shell default off)  
- [ ] Memory redaction rules  
- [ ] Third-party processors listed before enable  
- [ ] HITL: export / delete / external share / marketing send  
- [ ] Eval cases: injection + exfil  

### Fable Offline mapping
| Need | Mechanism |
|------|-----------|
| Evidence map | `--privacy` / skill `privacy-host-map` |
| Design plan | skill `privacy-design-planner` |
| Execute plan steps | `--engineer` + criteria |
| Multi-role critique | `--team` research → write → critic |
| Human gates | HITL on workflows |
| Durable learning | `/improve` after two successful maps |

---

## Data-flow skeleton

```text
[Data subject]
    → [UI / form / agent chat]
        → [First-party app or landing host]
            → [Tag manager / pixel / search SaaS]
            → [CRM / email / ads / analytics]
        → [LLM provider or local model]
            → [memory/ skills/ logs]   ← redaction rules here
```

---

## Trust boundaries skeleton

| Zone | Components | PII? | Third parties |
|------|------------|------|---------------|
| Browser | | | |
| First-party server | | | |
| Marketing cloud | | | |
| LLM / agent runtime | | | |
| Human operator | | | |

---

## Risk register skeleton

| ID | Risk | L | I | Mitigation | Verify how |
|----|------|---|---|------------|------------|
| R1 | | | | | |
| R2 | | | | | |
| R3 | | | | | |

---

## Engineer criteria block (copy-paste)

```
Purpose one sentence,
Data categories listed or UNKNOWN,
Processors first- vs third-party,
Data-flow diagram present,
HITL gates for high-risk actions,
Verification steps concrete,
No invented legal conclusions,
Artifact paths under knowledge/privacy or workflows specified
```

Min score: 8 · max cycles: 5 · skill: privacy-design-planner

---

## Seed maps in this folder

| File | Stack pattern |
|------|----------------|
| `akl-libraries-third-party-hosts.md` | AEM + GTM + Adobe Launch + Coveo + Shielded iframe |
| `uoa-eloqua-pg-webinar-hosts.md` | Eloqua LP + lead form + Ads gclid/utm + first-party cookie domain |

**Pattern lesson:** government **service** pages often mix **analytics + safety widgets**; university **recruitment** pages often mix **marketing automation + paid media IDs + PII forms**. Plans should treat these as different archetypes.

---

## Write path

New design docs: `knowledge/privacy/design-<slug>.md`  
New host maps: `knowledge/privacy/<slug>-third-party-hosts.md`  
Keep raw HTML/JS out of git (see root `.gitignore`).
