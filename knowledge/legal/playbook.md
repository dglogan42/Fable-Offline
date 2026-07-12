# Organization legal playbook (offline defaults)

Edit this file to match your real negotiation positions. Fable Legal mode loads it as the source of truth for GREEN / YELLOW / RED flags.

**Not legal advice.** Defaults are conservative templates for a small/mid company buying SaaS and signing mutual NDAs. Replace with counsel-approved positions before production use.

## Meta
- **Playbook owner:** [YOUR COUNSEL / GC]
- **Last reviewed:** [DATE]
- **Default governing law preference:** [e.g. New Zealand / California / England & Wales]
- **Default venue:** courts of that law (arbitration only if playbook says so)
- **Signature authority:** only after licensed attorney review for non-standard deals

---

## NDA — standard positions

| Topic | Standard (GREEN) | Acceptable range (YELLOW) | Escalate (RED) |
|-------|------------------|---------------------------|----------------|
| Mutuality | Mutual NDA preferred | One-way if we only receive info | One-way where we only disclose and counterparty has broad use rights |
| Definition of CI | Reasonable incl. oral if confirmed in writing in 30 days | Slightly broader defs | Unlimited “all information” with no exclusions |
| Exclusions | Public, prior known, independent develop, third-party rightfully received | Minor wording diffs | No standard exclusions |
| Purpose | Specific project / evaluation | Broader “business discussions” | No purpose limitation |
| Term (disclosure) | 1–3 years | Up to 5 years | Perpetual disclosure period |
| Survival | 3–5 years; trade secrets while secret | Up to 7 years | Perpetual for all CI including non-secrets |
| Residuals | Residual knowledge clause OK if no source-code dump | Omitted residuals | Residuals that gut confidentiality |
| Non-solicit | None or employees only, ≤12 months, limited | Soft non-solicit | Customer non-solicit / non-compete buried in NDA |
| Return/destroy | 30 days on request + certify | 60 days | No return obligation |
| Liability | Consequential damages carve-outs mutual; uncapped for confidentiality breach often requested — push for cap if possible | Uncapped conf breach only | Unlimited liability for ordinary breach + conf |
| Law/venue | Our preferred law | Neutral third law | Hostile exclusive foreign courts with no connection |

**NDA triage categories:**
- **Standard approval path** — all GREEN or only cosmetic YELLOW
- **Counsel review** — any material YELLOW or unusual structure
- **Full review** — any RED, incomplete text, wrong entity, or one-sided overreach

---

## Commercial / vendor MSA — standard positions

| Topic | Standard (GREEN) | Acceptable (YELLOW) | Escalate (RED) |
|-------|------------------|---------------------|----------------|
| Liability cap | ≤12 months fees paid (or fixed $) | 24 months fees | Unlimited liability for ordinary performance |
| Consequential damages | Mutual exclusion | One-sided exclusion against us | We waive consequential; they do not |
| Indemnity | IP infringement from vendor; our misuse carve-out | Mutual IP indemnity | We indemnify their IP claims broadly |
| IP ownership | We own our data/pre-existing; vendor owns platform; work product negotiated | Ambiguous work product | Vendor owns our data or outputs we paid for without license back |
| Data / DPA | DPA present; processor limits; no sale of data; deletion on exit | DPA light but fixable | No DPA when personal data in scope; unrestricted sub-processors |
| Security | SOC2/ISO claim + breach notice ≤72h | Longer notice with justification | No security schedule; silent on breach |
| Term / renewal | Clear term; opt-out of auto-renew ≥30 days notice | Auto-renew with 60-day notice | Evergreen auto-renew + silent price uplift >10% |
| Termination for convenience | Us: 30 days; them: match or for cause only | Both 30 days | Only they can terminate for convenience mid-term after we prepaid |
| SLA credits | Credits as sole remedy for uptime (cap ≤ monthly fees) | Weak credits | Sole remedy + broad waiver of all other claims with no real SLA |
| Audit | Annual reasonable audit / questionnaire | On-site rare | Unlimited invasive audit at our cost |
| Assignment | Assignment with consent (not unreasonably withheld); free on change of control with notice | Free assignment by vendor only | Vendor free assign to competitor without notice |
| Publicity | No use of our name without consent | Logo in customer list OK | Forced case study / press without approval |

---

## Privacy / DSAR / holds (respond templates)

| Situation | Position |
|-----------|----------|
| DSAR / data subject request | Acknowledge receipt promptly; do not admit scope until verified; route to privacy owner; never invent identity verification outcome |
| Legal hold | Preserve broadly once litigation/investigation reasonably anticipated; do not delete; loop counsel before interviews |
| Regulator inquiry | Escalate immediately; no informal substantive answers without counsel |

---

## Escalation triggers (always RED → counsel)

1. Unlimited liability or uncapped indemnity for ordinary performance  
2. Perpetual non-compete or broad customer non-solicit in NDA/MSA  
3. Transfer of our IP or exclusive license of core IP without separate deal  
4. Personal data processing without DPA / transfer safeguards when required  
5. Governing law/venue we cannot practically litigate  
6. Security / breach silence when we send regulated or sensitive data  
7. Any “you warrant compliance with all laws worldwide” overbroad warranty on us as customer  
8. Missing party legal name / wrong entity signing  

---

## review-contract output expectations

Counsel expects:
1. Overall verdict first  
2. Flag table with concrete redlines  
3. Explicit **playbook gap** where this file is silent  
4. Final line: attorney review required before signature  

---

## Notes for editors

- Tighten numbers (caps, days, % uplifts) to match your real paper.  
- Add industry modules (healthcare BAA, finance confidentiality, government flow-downs) as extra sections.  
- Keep matter-specific notes in separate files under `knowledge/legal/` (e.g. `matter-acme-msa.md`).  
