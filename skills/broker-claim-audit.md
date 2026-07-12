# Broker claim audit (marketing vs evidence)

**WHEN_TO_USE:** Evaluating a broker website, “0 pip spreads”, multi-regulated claims, leverage tables, account comparisons, partner funnels — especially after pasting site HTML or a URL summary.

## Stance
Marketing pages are **unverified claims**, not ground truth. Apply Section 4 (re-derive) and Section 13 (edge vs luck): treat impressive numbers as **guilty of being sales copy** until primary evidence is checked.

## What to extract from a site
1. Legal entity name(s) and jurisdictions claimed  
2. Account types, spreads “from”, leverage, margin call / stop out  
3. Products (CFDs on FX, metals, energy, indices, crypto)  
4. Platforms (e.g. MT5) and deposit/fee claims  
5. Risk warnings (presence/absence and specificity)  
6. What is **missing**: licence numbers, FSPR/FMA IDs, entity that holds client money, complaint path  

## Checklist (score each 1–10 honesty of disclosure, not “broker quality”)
| Gate | Question |
|------|----------|
| Entity clarity | Which company contracts with the client? Where is it registered? |
| Regulation | Named regulator + licence/FSPR number verifiable on **official** register? |
| Product truth | CFDs clearly labeled? Retail leverage vs professional disclosed? |
| Cost completeness | Spreads “from” vs typical; commissions; swap; deposit/withdrawal fees |
| Leverage realism | Matches local retail caps (e.g. NZ/AU/EU retail limits) or only offshore entity? |
| Risk disclosure | Loss of capital, leverage risk, not investment advice — specific, not buried |
| Conflicts | Market maker vs STP/ECN claims consistent with pricing model |
| Missing evidence | What cannot be verified from the page alone? |

## Verdict labels (required)
- **Insufficient evidence** — cannot verify licences/entity/costs from material given  
- **Marketing only** — claims present, primary sources not checked  
- **Partially verified** — some claims match public registers  
- **Red flags** — inconsistent leverage, missing licence IDs, pressure CTAs without risk, contradictory account tables  

## Forbidden
- Recommending a broker as “safe” or “best” from a homepage alone  
- Treating “spreads from 0.0” as average trading cost  
- Treating multi-licence banners as proof without register lookup  
- Inventing licence numbers or regulatory status  

## Output shape
1. **Verdict first**  
2. Table of claims vs evidence status (stated / missing / needs register check)  
3. Account/leverage inconsistencies if any  
4. What the user must verify next (specific URLs: FMA, Companies Office, ASIC, etc.)  
5. One concrete risk of trusting the page as-is  

## Local knowledge
If `knowledge/brokers/` contains scraped notes (e.g. `ec-markets-regulation.md`), **use them** and cite filenames. Still mark primary-register checks as required for live decisions.

## Note
This skill does **not** provide financial advice. It audits **claims**.
