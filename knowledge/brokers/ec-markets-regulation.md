# EC Markets — regulation scrape snapshot

**Scraped / compiled:** 2026-07-12  
**Purpose:** Offline claim material for Fable broker-claim-audit and broker-user-model.  
**Not financial advice.** Verify every licence on **official** registers before relying on it.  
**Sources are marketing sites unless marked primary.**

---

## Entities (as claimed in public materials)

| Entity | Claimed details | Source type |
|--------|-----------------|-------------|
| **EC Markets Financial Limited** | NZ company **2446590**; FSPR **FSP197465**; address Level 1, 1 Albert Street, Auckland 1010, NZ | Broker sites (ecmarkets.com / .sc / about) |
| | Authorised/regulated by NZ **FMA**, FSPR No. FSP197465 | Broker + third-party directories |
| | **ASIC** AFSL **414198**; foreign co ARBN **152 535 085** | Broker sites |
| | **FSCA** (South Africa) Licence **51886** | Broker / directory |
| **EC Markets Limited** | **Seychelles FSA** Licence **SD009** | Directory / broker footnotes |
| **EC Markets Securities & Financial Promotion L.L.C** | UAE **SCA** Category 5, Licence **20200000281** | Directory |
| Site brands | ecmarkets.co.nz, .com, .com.au, .sc | Observed |

**FMA primary note (govt):** FMA licensed providers page lists *EC Markets Financial Limited*, previously CTRL Investments Limited / MahiFX Limited, **FSP197465**, as a **licensed derivatives issuer** (fma.govt.nz business/licensed-providers). Treat as stronger than logo bars; still re-check live register.

**Important NZ nuance:** FSPR registration alone is not “FMA licensed.” This firm is separately described as a licensed derivatives issuer — confirm current status on FMA/FSPR tools.

---

## NZ site marketing (ecmarkets.co.nz homepage / reg page)

### Account tables (homepage)

| | ECN | STD |
|--|-----|-----|
| Spreads from | 0.0 pips | From 1.0 on Forex |
| Leverage up to | **1:100** | **1:30** |
| Min order | 0.01 lot | 0.01 lot |
| Max order | 50 | Unlimited |
| Margin call | 50% | 100% |
| Stop out | 50% | 100% |

### Hero / stats bar
- $0 deposit fee  
- **7** regulatory licences  
- Support 9am–6pm Mon–Fri (local team claim)  
- 80+ instruments  
- Spreads as low as **0.0**  
- 2 account types (homepage) — .com legal also mentions **PRO** account  

### Products
CFDs: Forex, precious metals, energies, indices, cryptocurrencies. Platforms: MetaTrader 5 (+ app).

### Regulation page claims
- Seven authorities named: **FSC, FCA, CMA, FSCA, ASIC, FMA, FSA** (logos)  
- “Spreads starting from 0 pips, leverage **up to 1:300**” — **conflicts** with homepage ECN 1:100 / STD 1:30  
- Fast deposits/withdrawals (no schedule detail on page)

### Risk copy
- “Trading is risky. Proceed wisely.” (minimal on hero)

---

## .com legal page (scraped text)

- Brand **EC Markets Limited** legal pack links: Client Agreement, Privacy Policy, Risk Disclosure, Complaints Handling, Client Onboarding  
- Funnel: Register → Deposit → Start Trading  
- Account types in nav: STD, ECN, **PRO**  
- Platforms: MT4, MT5, EC Markets App  

Raw extract file: `ec-markets-com-legal-raw.txt` (generated from HTML scrape).

---

## Inconsistencies / gaps (for audit)

1. **Leverage:** 1:30 / 1:100 (homepage tables) vs **1:300** (reg marketing).  
2. **Licence IDs** often missing on NZ reg marketing page; better detail on global footers/directories.  
3. **Which entity** a NZ retail client contracts with is not proven by homepage alone.  
4. **FCA** appears in logo list; confirm exact FCA firm reference number on register.fca.org.uk.  
5. Live prices on HTML dump were not populated (JS).  

---

## Register check list (human / online)

| Claim | Primary check |
|-------|----------------|
| Co. 2446590 | companies-register.companiesoffice.govt.nz |
| FSP197465 | fsp-register.companiesoffice.govt.nz |
| Derivatives issuer | fma.govt.nz licensed providers |
| AFSL 414198 | connectonline.asic.gov.au |
| FSCA 51886 | fsca.co.za |
| FSA SD009 | Seychelles FSA public list |
| SCA 20200000281 | UAE SCA |

---

## Scraped file inventory

| File | Content |
|------|---------|
| `ec-markets-regulation.md` | This synthesis |
| `ec-markets-com-legal-raw.html` / `.txt` | Legal page scrape |
| (optional) further scrapes via `--scrape` | Added by harness |

**Last synthesis:** 2026-07-12. Re-scrape before high-stakes decisions.
