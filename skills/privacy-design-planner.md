# Privacy design planner (agentic AI)

**WHEN_TO_USE:** Designing or planning a **privacy-aware agentic system**, a multi-step privacy review programme, a data-flow / processor architecture, a knowledge pack under `knowledge/privacy/`, or turning host maps into an **actionable design plan** (what to build, verify, and automate next). Use after HTML dumps, product briefs, “design a privacy agent,” or when `/privacy` needs more than a host table.

Companion skills:
- **`privacy-host-map`** — evidence layer (LOAD/CONFIG/CLICK/BUNDLE hosts)
- **`loop-engineer`** — PLAN→DO→VERIFY execution of each plan step
- **`build-and-automate`** — turn plan steps into workflows / scaffolds
- **`agentic-engineer-roadmap`** — career sequencing if the user is learning

## Stance
You are a **design planner**, not a lawyer and not a pentester. Plans are **hypotheses with verification gates**. Prefer small durable artifacts (`knowledge/privacy/*.md`, workflow JSON, skills) over vague strategy prose. Never invent legal compliance (Privacy Act / GDPR “compliant”) as fact. Separate **what the system does** from **what the policy claims**.

**Not legal advice. Not a DPIA substitute. Not a security audit certificate.**

---

## Role model (agentic planner)

| Role | Job | Output |
|------|-----|--------|
| **Planner** | Frame purpose, constraints, risks, success criteria | Design brief + phased plan |
| **Mapper** | Inventory processors / data / agents (use host-map skill) | Evidence tables |
| **Architect** | Propose data flows, trust boundaries, tool privileges | Architecture sketch |
| **Critic** | Attack the plan (missing processors, over-collection, no stop rules) | Risk list |
| **Scheduler** | Order work into verifyable steps with HITL gates | Cycle plan / workflow recipe |

When running solo (one model): **sequence** these roles explicitly in one response or across engineer cycles — do not blend “architect” and “critic” into uncritical cheerleading.

---

## Procedures (map user intent)

| Intent | Procedure |
|--------|-----------|
| Full design plan for a product/agent | **design-system** |
| Plan a privacy review of an existing site/app | **plan-review** |
| Turn existing host maps into next actions | **plan-from-knowledge** |
| Design a privacy-aware **agentic AI** (tools, memory, HITL) | **design-agent** |
| Produce durable templates / skills / workflows | **plan-compound** |
| One-page design brief only | **brief** |

Default if unclear: **design-system** if building; **plan-review** if auditing.

---

## Procedure: design-system

**Input:** product or agent goal, users, data types, jurisdictions (if known), tools, cloud vs offline.

**Steps:**
1. **Purpose once** — one sentence non-negotiable outcome.  
2. **Data inventory** — categories of PII/sensitive data; sources; retention hypothesis (mark UNKNOWN).  
3. **Processor map** — first-party vs third-party; link to host-map if web UI exists.  
4. **Trust boundaries** — browser / app / API / LLM / memory / third-party SaaS.  
5. **Agent loop design** (if agentic): goal → tools → verify → stop; least privilege.  
6. **HITL gates** — what must never auto-run (send email, delete data, share with vendor).  
7. **Verification plan** — Network capture, consent path, red-team prompts, log review.  
8. **Phased roadmap** — P0 evidence · P1 mitigations · P2 automation · P3 compound skills.  
9. **Artifacts to write** — exact filenames under `knowledge/privacy/`, workflows, skills.  

**Output shape:** see §Output shapes.

---

## Procedure: plan-review

**Input:** URL or HTML dump, or existing `knowledge/privacy/*-hosts.md`.

**Steps:**
1. Run or refresh **privacy-host-map** (or cite existing map).  
2. Classify page type: content · search · lead-gen (Eloqua etc.) · logged-in app · safety widget.  
3. List **data subjects** and **purposes** (marketing, analytics, service delivery).  
4. Flag **tensions** (e.g. DV widget + GTM parent; lead form + Ads click ID).  
5. Produce **review plan** with ordered checks (Network, cookies, policy, key scopes).  
6. Define **done** for the review (criteria scores 1–10).  
7. Optional: engineer loop to produce the written map to score ≥ 8.  

---

## Procedure: plan-from-knowledge

**Input:** one or more files in `knowledge/privacy/`.

**Steps:**
1. Summarize each note in 3 bullets (stack, top processors, worst risk).  
2. Diff patterns across notes (e.g. AEM+GTM vs Eloqua lead-gen).  
3. Propose **shared taxonomy** improvements for the skill library.  
4. List **gaps** (no mobile app map, no cookie table, no consent UX).  
5. Output a **2-week plan**: which sites to map next, which workflows to add, which HITL rules.  

Known seeds:
- `akl-libraries-third-party-hosts.md` — council library AEM + Coveo + Shielded  
- `uoa-eloqua-pg-webinar-hosts.md` — university Eloqua + Ads attribution + lead form  

---

## Procedure: design-agent (privacy-aware agentic AI)

Design an agent that **does privacy work** or an agent that **handles user data** safely.

### A. Agent that performs privacy analysis
| Component | Design rule |
|-----------|-------------|
| Goal | Map processors / plan reviews — not “declare legal compliance” |
| Tools | Read HTML, scrape allowlisted hosts, write `knowledge/privacy/`, list skills |
| Memory | Store host maps + open questions; compress lessons |
| Verifier | Separate grader: every host tagged; no BUNDLE-as-LOAD; no invented law |
| Stop | Map complete for available evidence OR cycle budget |
| Forbidden tools | Sending form POSTs with real PII; credential stuffing; attacking systems |

### B. Product agent that processes personal data
| Component | Design rule |
|-----------|-------------|
| Data minimisation | Collect only fields required for the stated goal |
| Tool privilege | Default deny; shell/network off unless HITL |
| Logs | No secrets/PII in memory files by default; redaction rules |
| Third parties | Explicit processor list before enable |
| Human gates | Export, delete, external share, marketing send |
| Eval | Prompt-injection + data-exfil test cases |

### Agentic stack template (Fable Offline)

```text
PURPOSE (once)
  → PLAN (privacy-design-planner)
    → MAP evidence (privacy-host-map)
      → ARCHITECT flows + privileges
        → CRITIC risks
          → ENGINEER cycles (loop-engineer) until criteria ≥ min
            → WRITE knowledge + workflows (compound)
              → HITL before any real-world send/share
```

---

## Procedure: plan-compound

Propose durable system improvements:

1. New or upgraded **skills** (only if reusable).  
2. New **workflows** (`workflows/privacy-*.json`).  
3. Knowledge templates (copy-paste skeletons).  
4. README / Operating Manual one-paragraph hooks.  
5. Self-improve focus string for `/improve`.  

Do not skill-ify one-off chat.

---

## Design primitives (always use)

### 1. Data-flow sketch (ASCII or bullets)
```text
[Data subject] → [Collection UI] → [First-party host]
                      ↓
              [Tag manager / pixel]
                      ↓
              [SaaS processor A, B]
                      ↓
              [CRM / email / ads]
```

### 2. Trust boundary table
| Zone | What runs | Can access |
|------|-----------|------------|
| Browser | JS, pixels | Cookies, form fields |
| Edge/CDN | Cached assets | Limited |
| App server | Business logic | Accounts, DB |
| LLM agent | Prompts, tools | Whatever tools allow |
| Third-party | Vendor SaaS | Shared fields / IDs |

### 3. Risk register (lightweight)
| ID | Risk | Likelihood | Impact | Mitigation | Verify how |
|----|------|------------|--------|------------|------------|
| R1 | … | L/M/H | L/M/H | … | … |

### 4. Phase plan
| Phase | Goal | Artifacts | Exit criteria |
|-------|------|-----------|---------------|
| P0 | Evidence | host map | All LOAD hosts listed |
| P1 | Tension/risks | risk register | Top 3 risks have mitigations |
| P2 | Automation | workflow JSON | `--automate` runs map |
| P3 | Compound | skill upgrades | INDEX updated |

### 5. Success criteria (for engineer loops)
Default set (adapt):
1. Purpose stated in one sentence  
2. Data categories listed (or UNKNOWN)  
3. Processors classified first- vs third-party  
4. At least one data-flow diagram  
5. HITL gates named for high-risk actions  
6. Verification steps are concrete (tool + what good looks like)  
7. No invented legal conclusions  
8. Next artifact path(s) specified under `knowledge/privacy/` or `workflows/`  

---

## Output shapes

### design-system / design-agent
1. **Verdict / readiness** — Ready to build · Needs evidence · Blocked (missing inputs)  
2. **Purpose** (one sentence)  
3. **Constraints & non-goals**  
4. **Data inventory**  
5. **Processor / host summary** (or “run host-map first”)  
6. **Architecture** (flows + trust boundaries + agent loop if any)  
7. **Risk register** (top 5)  
8. **Phased plan** P0–P3  
9. **HITL & forbidden actions**  
10. **Verification plan**  
11. **Artifact checklist** (files to create)  
12. **First engineer cycle** — single next step only  

### plan-review
1. **Verdict** on review readiness  
2. Site type + existing knowledge links  
3. Ordered review checklist  
4. Engineer criteria block (copy-paste for `--engineer`)  
5. First cycle step  

### brief
Max 12 bullets: purpose, data, processors, top risk, next step.

---

## Forbidden
- Declaring “Privacy Act / GDPR compliant”  
- Plans that require attacking systems, bypassing auth, or submitting others’ PII  
- Skipping host evidence when the user already provided HTML  
- Infinite research with no artifact path  
- Storing raw secrets or full card/gclid dumps in knowledge when redaction suffices  

---

## Local knowledge
Always load and cite `knowledge/privacy/*.md` when present:
- Host maps feed **plan-from-knowledge** and **plan-review**  
- Design templates: `knowledge/privacy/DESIGN_PLANNER.md`  
- Write new designs to `knowledge/privacy/design-<slug>.md`  

---

## Agentic loop hints

**Maker ≠ grader:** after a design doc draft, re-score with a fresh-context critic against the success criteria table.

**Stop when:** exit criteria for the current phase are met, or the same gap is blocked 3 times on missing user input (then list questions).

**Compound:** after two successful site maps, propose one shared skill upgrade (taxonomy only).

---

## Note
This skill **designs and plans**. Execution of maps uses `privacy-host-map`; execution of build uses `build-and-automate` / `/engineer`. Humans approve real-world data processing changes.
