# Design: privacy-aware agentic AI (Fable Offline)

**Date:** 2026-07-12  
**Skill used:** `privacy-design-planner`  
**Evidence:** `akl-libraries-third-party-hosts.md`, `uoa-eloqua-pg-webinar-hosts.md`, `DESIGN_PLANNER.md`  
**Status:** Seed design (ready to engineer refinements)  
**Not legal advice.**

---

## Purpose (one sentence)

Build an **offline-first agentic system** that maps third-party processors from public HTML, plans privacy reviews, and compounds durable notes under `knowledge/privacy/` — **without** claiming legal compliance or submitting real personal data to external forms.

---

## Non-goals

- Acting as a lawyer, DPIA author of record, or certified auditor  
- Attacking systems, bypassing auth, or scraping behind logins without permission  
- Auto-sending marketing email or posting lead forms with user PII  
- Declaring “Privacy Act / GDPR compliant”  

---

## Data inventory (the agent itself)

| Category | In scope? | Notes |
|----------|-----------|--------|
| User-pasted HTML | Yes | Treat as potentially sensitive; do not push secrets to git |
| Host maps / design docs | Yes | Curated markdown in `knowledge/privacy/` |
| Live scrape text | Optional | `knowledge/` scrapes gitignored when matching patterns |
| End-user PII from third-party forms | No (analysis only) | Describe fields; do not fill/submit |
| Model prompts / memory | Yes | Redact tokens, gclid full values, emails in examples when possible |

---

## Architecture

```text
[User] → Fable CLI (/privacy, --automate, /engineer)
            │
            ├─ skill privacy-host-map     → evidence tables (LOAD/CONFIG/CLICK/BUNDLE)
            ├─ skill privacy-design-planner → plans, risks, phases, agent design
            ├─ knowledge/privacy/*        → durable maps + DESIGN_PLANNER template
            ├─ workflows/privacy-*.json   → repeatable recipes
            └─ loop-engineer / team       → verify plans; critic pass

Trust boundary: local model (Ollama) + local disk. Network only for allowlisted scrape/fetch.
```

### Trust boundaries

| Zone | Components | Third parties |
|------|------------|---------------|
| Operator machine | Fable, Ollama, files | None required |
| Optional network | `--scrape` URLs | Target site only |
| Memory/skills | Local markdown | Do not sync secrets |
| Human | HITL approvals | Final authority |

---

## Agent loop design

| Stage | Behavior |
|-------|----------|
| Goal | Map or plan for a named surface |
| Plan | Single next evidence or design step |
| Tools | Read knowledge, write curated md, scrape if allowed |
| Verify | Fresh-context: tags correct, no invented law, paths exist |
| Stop | Criteria ≥ min score OR budget OR blocked on user input |
| Compound | After ≥2 maps, propose taxonomy skill tweak only if reusable |

---

## HITL gates (required)

1. Before treating a scrape as authoritative for a real decision  
2. Before any workflow that would contact external humans or submit forms  
3. Before publishing design claims as organisational policy  
4. Before enabling shell (`FABLE5_ALLOW_SHELL`) for anything privacy-related  

---

## Risk register (seed)

| ID | Risk | L | I | Mitigation | Verify |
|----|------|---|---|------------|--------|
| R1 | BUNDLE hosts reported as LOAD | M | M | Legend enforced in skill + verifier criteria | Critic pass |
| R2 | Invented legal compliance | M | H | Forbidden in skills; criteria ban | Critic pass |
| R3 | Committing raw HTML/PII | M | H | gitignore scrapes; curated md only | `git status` |
| R4 | Operator pastes secrets into chat | M | H | Redaction guidance in output shape | Human review |
| R5 | Over-automation of marketing sites | L | M | Scrape allowlist + HITL on full audits | Workflow design |

---

## Phased roadmap

| Phase | Goal | Exit criteria | Artifacts |
|-------|------|---------------|-----------|
| **P0** | Evidence skill + two seed maps | Maps exist for AKL + UoA | host map md files |
| **P1** | Design planner skill + template | Skills + DESIGN_PLANNER.md | this design doc |
| **P2** | Automate plan + map | workflows run offline | `privacy-host-map`, `privacy-design-plan` |
| **P3** | Compound | INDEX + manual § privacy design | skill INDEX, Operating Manual |

**P0–P1 delivered in repo.** P2–P3 = wiring/docs polish and operator use.

---

## Verification plan

1. `--privacy` produces tagged host tables on seed knowledge.  
2. `--automate privacy-design-plan` yields purpose + phases + HITL.  
3. Critic checklist: no compliance claims; artifact paths valid.  
4. `git status` shows no raw HTML clientlibs committed.  

---

## First engineer cycle (if refining this design)

**Single step:** Add one eval-style criteria string to `workflows/privacy-design-plan.json` for “cites at least one knowledge/privacy file by name” and re-run automate once.

---

## Related commands

```bash
python fable5_offline_agent.py --privacy
python fable5_offline_agent.py --automate privacy-host-map
python fable5_offline_agent.py --automate privacy-design-plan
python fable5_offline_agent.py --engineer "Refine design-privacy-agent.md" --criteria "Purpose,Data inventory,Trust boundaries,HITL,Risks,Phases,No legal invention,Artifact paths"
```
