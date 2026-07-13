# Freight forwarder & exporter — practice framework

**Skill:** `freight-forwarder-exporter`  
**Related:** `knowledge/trade/mpi-exporter-help.md`, `knowledge/urban-planning/freight-plan.md`  
**Not legal, customs, biosecurity, or freight brokerage advice.**

---

## Two scales of “freight”

| Scale | Skill / knowledge | Question |
|-------|-------------------|----------|
| **Strategic networks** | `urban-planner` plan-freight, Future Connect | Which corridors matter for goods in a region? |
| **Commercial shipment** | **This module** | How does *this* cargo move under contract, docs, and clearance? |

Do not mix answers without labelling the scale.

---

## Export readiness card (template)

```markdown
# Export readiness — [product] → [destination] — [date]
## Parties
## Product (description, claims, cold chain, DG?)
## Volume / frequency
## Preferred Incoterms® (year)
## Known licences / registrations
## Unknowns (blockers)
## Doc status matrix
## Mode options (qualitative)
## Official next steps (MPI / Customs / broker / NZTE)
## Non-claims
```

---

## Shipment phases

1. Pre-book → 2. Book → 3. Origin → 4. Main leg → 5. Destination → 6. Exceptions/claims  

---

## Doc pack (minimum skeleton)

- Commercial invoice  
- Packing list  
- Transport document (B/L, AWB, …)  
- Certificates as required (origin, health, phyto, organic, …)  
- Insurance if applicable  
- LC documents if applicable  

---

## NZ primary industry entry

- MPI export hub: https://www.mpi.govt.nz/export  
- Exporter Help: https://www.mpi.govt.nz/export/get-help-with-exporting  
- Query form / phones: see `mpi-exporter-help.md` (verify live)  
- Webinars: linked from Exporter Help section  

---

## Cost skeleton

Origin + main freight + surcharges + destination + duties/taxes + brokerage/fees + insurance = landed (label incomplete without quotes).

---

## HITL gates

- Sending PII or commercial terms externally  
- Choosing Incoterms for a binding contract  
- Any statement of legal compliance for a market  
- Booking or amending cargo as principal  

---

## Agent design (Fable)

```text
User goal
  → freight-forwarder-exporter (export-readiness | shipment-checklist)
    → mpi-export-path if food/fibre NZ
    → pdf-render for official PDFs
    → legal-playbook for sale/forwarder contracts
    → engineer verify: no invented codes/rates
    → write knowledge/trade/*.md
```
