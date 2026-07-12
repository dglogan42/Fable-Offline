# Legal playbook (offline contract / NDA / compliance)

**WHEN_TO_USE:** Contract review, NDA pre-screening, vendor agreement status, legal briefings, templated responses to common legal ops inquiries (DSAR, discovery hold, standard pushback). Inspired by in-house legal automation patterns (clause flags, playbook positions) — **not a substitute for a licensed attorney**.

## Hard rules (always)
1. **Not legal advice.** Output is a triage / draft aid for human counsel.
2. **Licensed attorney review required** before signing, sending, or relying on any output in a real matter.
3. **Do not invent case law, statutes, jurisdiction rules, or party facts.** Mark unknowns as **UNKNOWN**.
4. Prefer the local playbook in `knowledge/legal/playbook.md` (and any `knowledge/legal/*.md`) over generic guesses.
5. If playbook is missing or silent on a clause, flag **YELLOW** and say playbook gap — do not invent “standard market” as policy.

## Commands (map user intent)

| Intent | Procedure |
|--------|-----------|
| Review a contract clause-by-clause | **review-contract** |
| Fast NDA screen | **triage-nda** |
| Vendor / MSA / DPA status | **vendor-check** |
| Daily / topic / incident brief | **brief** |
| Templated reply (DSAR, hold, pushback) | **respond** |

---

## Flag system (required on review-contract, triage-nda, vendor-check)

| Flag | Meaning |
|------|---------|
| **GREEN** | Aligns with playbook standard position (or clearly favorable and within acceptable range) |
| **YELLOW** | Negotiable / borderline; needs counsel judgment or playbook gap |
| **RED** | Escalation trigger — outside acceptable range, missing critical protection, or high-risk clause |

Every flagged item must include:
- Clause / topic name
- What the text says (quote or tight paraphrase)
- Playbook position (or “no playbook entry”)
- Flag + reason
- Specific redline or ask (concrete language when possible)

---

## review-contract

**Input:** full or partial contract text (user paste), optional counterparty / deal type, optional playbook overrides.

**Process:**
1. Identify document type, parties, governing law, term, commercial core (if present).
2. Walk high-risk buckets against playbook: liability, indemnity, IP, confidentiality, data/privacy, termination, payment, non-compete/non-solicit, dispute resolution, assignment, audit, SLAs, auto-renewal, exclusivity.
3. Score each material clause GREEN / YELLOW / RED.
4. Propose redlines only where playbook or risk analysis supports them; label speculative edits.

**Output shape:**
1. **Verdict first** — overall readiness: *Approve path / Negotiate / Escalate / Insufficient text*
2. Party / law / term summary table
3. Clause table: Topic | Flag | Issue | Redline / ask
4. Top 3 RED items (detail)
5. Missing sections the playbook expects but text lacks
6. **Counsel gate:** “Attorney must review before signature.”

---

## triage-nda

**Input:** NDA text (mutual / one-way / form).

**Categories (pick one primary):**
- **Standard approval path** — aligns with playbook; minor or no issues (mostly GREEN)
- **Counsel review** — YELLOW items or unusual structure; not auto-approve
- **Full review** — RED items, one-sided overreach, wrong party entity, perpetual overbreadth, missing residual rights balance, or unreadable/incomplete text

**Checklist gates:**
| Gate | Question |
|------|----------|
| Mutuality | Mutual vs one-way; definition of Confidential Information fair? |
| Purpose | Purpose limited and clear? |
| Term | Disclosure period + survival reasonable per playbook? |
| Residuals / reverse engineer | Residual knowledge; no unfair reverse-eng ban if needed? |
| Non-solicit / non-compete | Hidden restraint of trade? |
| Residuals of liability | Cap / unlimited on breach of conf? |
| Return/destroy | Practical and timely? |
| Governing law / venue | Acceptable jurisdiction? |

**Output:** category first → flag table → 3 concrete next steps → counsel gate.

---

## vendor-check

**Input:** vendor MSA / order form / DPA / security addendum (any subset) + optional prior notes in `knowledge/legal/`.

**Assess:**
1. Contract stack completeness (MSA, SOW, DPA, SLA, BAA if health data)
2. Data processing roles (controller/processor), sub-processors, transfer mechanisms (flag if claimed but not evidenced)
3. Security commitments vs playbook minimums
4. Liability / insurance / indemnities
5. Exit: data return, deletion, transition assistance
6. Auto-renewal and price uplift traps

**Output:** status (**Clear / Conditional / Block**) → gaps table → RED/YELLOW list → counsel gate.

---

## brief

**Modes:**
- **daily** — open items, deadlines, escalations (from user-provided notes/memory only)
- **topic** — research brief from pasted sources + playbook (no invented law)
- **incident** — facts known / unknown, legal hold checklist, comms discipline, who to escalate

**Output:** 5–10 bullets max for daily; structured memo for topic/incident; always list sources used and unknowns.

---

## respond

**Templates (draft only):**
- Data subject / privacy request acknowledgment
- Legal hold / preservation notice (internal)
- Standard NDA / MSA pushback on a RED clause
- “We need more time / more information” status reply

**Rules:**
- Neutral professional tone
- No admissions of liability
- No fake deadlines or fake policy citations
- Mark placeholders as `[PARTY]`, `[DATE]`, `[MATTER]`

---

## Playbook file

Load and prefer:
- `knowledge/legal/playbook.md` — standard positions, acceptable ranges, escalation triggers
- Other `knowledge/legal/*.md` — matter notes, prior reviews (secondary)

If empty: still run review with **generic risk flags** labeled as non-playbook, and urge user to fill playbook.

---

## Forbidden
- Claiming to be a lawyer or giving jurisdiction-specific legal conclusions as fact
- Approving signature without human counsel
- Inventing statutes, case names, or “this is unenforceable in X”
- Silently skipping RED issues to be agreeable

## Note
This skill is **legal operations hygiene**, not representation. All outputs require licensed attorney review for real matters.
