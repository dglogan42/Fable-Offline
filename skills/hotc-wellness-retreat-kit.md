# Heart of the City wellness retreat kit (Auckland CBD self-care brochure)

**WHEN_TO_USE:** User wants an **Auckland city-centre wellness retreat**, **self-care program**, or **brochure** based on [Heart of the City Health & Wellbeing](https://heartofthecity.co.nz/health-wellbeing); spa/gym/yoga day plans; CBD precinct wellness itineraries. Triggers: “Heart of the City wellness”, HOTC health, CBD self-care, Auckland spa retreat brochure.

**Official (VERIFY LIVE):**  
- Directory: [heartofthecity.co.nz/health-wellbeing](https://heartofthecity.co.nz/health-wellbeing)  
- Habits article: [Creating healthy habits for your wellbeing](https://heartofthecity.co.nz/article/creating-healthy-habits-your-wellbeing)  
- HOTC home: [heartofthecity.co.nz](https://heartofthecity.co.nz/)  

Companions: `fitness-companion-agent`, `emergency-services-agent`, `privacy-host-map`, `myfitnesspal-resource-kit` (logging only), `physiotherapy-exercises-resource-kit` (clinician path only if injured).

## Stance
You **curate itineraries and brochures** from the public HOTC directory. Fable does **not** book venues, guarantee prices, or give medical advice.

**Not medical, physiotherapy, or mental-health advice.** Not an official HOTC package. Listings change — VERIFY LIVE. Escalate distress/emergency via **111** / Healthline.

**Refuse:** inventing closed businesses as open; scraping private favourites; storing booking credentials.

---

## Deliverables

| Asset | Path |
|-------|------|
| Knowledge | `knowledge/health/auckland-cbd-wellness-retreat.md` |
| Privacy | `knowledge/privacy/heartofthecity-hosts.md` |
| Brochure PPTX | `brochures/auckland-cbd-wellness/Auckland_CBD_Wellness_Retreat_Brochure.pptx` |
| Rebuild | `node brochures/auckland-cbd-wellness/build_brochure.js` (needs pptxgenjs) |

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end kit | **hotc-plan** |
| Build 1–3 day program | **retreat-itinerary** |
| Brochure contents map | **brochure-map** |
| Pillars / categories | **pillars** |
| Venue shortlist | **select-venues** |
| Express half-day packs | **express-packs** |
| Booking checklist | **book-hitl** |
| Habits prompts | **habits** |
| Privacy hosts | **host-map** |
| Rebuild PPTX | **rebuild-brochure** |
| Short answer | **brief** |

Default: **hotc-plan**.

---

## hotc-plan

**Input:** days (1–3), focus (restore / move / glow), precinct preference.

**Output:**
1. Verdict — curated CBD self-care; not clinical retreat  
2. **pillars** + **retreat-itinerary**  
3. **select-venues** (from knowledge seeds + VERIFY LIVE)  
4. **book-hitl**  
5. Point to brochure PPTX  
6. Disclaimer  

---

## retreat-itinerary

| Day | Theme | Blocks |
|-----|--------|--------|
| 1 | Arrive & unwind | Spa/massage · optional beauty · journal |
| 2 | Move & strengthen | Yoga/pilates · gym/PT · recovery |
| 3 | Integrate & glow | Light movement · glow · weekly habit plan |

Adapt to half-day via **express-packs**.

---

## brochure-map

| Slide | Content |
|-------|---------|
| 1 | Cover |
| 2 | Welcome |
| 3 | Six pillars |
| 4 | 3-day itinerary |
| 5 | Sample venues table |
| 6 | Express options |
| 7 | How to use HOTC + habits |
| 8 | Disclaimer + source |

---

## pillars

Move · Flow · Core · Restore · Glow · Nourish — see knowledge file.

---

## select-venues

Prefer knowledge sample table; always re-check HOTC listing status. Filter by precinct (Britomart, Queen St, Wynyard, Victoria Park…).

---

## express-packs

Half-day Restore · Morning Flow · Glow Afternoon · Active Reset.

---

## book-hitl

User only: open HOTC → filter → venue site → book. No Fable payment.

---

## habits

Non-clinical prompts: protect one appointment, phone-down blocks, hydrate & walk, sleep as recovery, rotate weekly pillars.

---

## rebuild-brochure

```bash
npm.cmd install pptxgenjs   # if needed
node brochures/auckland-cbd-wellness/build_brochure.js
```

---

## host-map

`knowledge/privacy/heartofthecity-hosts.md`

---

## Output contract

1. Verdict + itinerary  
2. Venue shortlist with VERIFY LIVE  
3. Brochure path  
4. Medical disclaimer  
5. OPEN  

---

## Anti-failure

- Do not invent prices or “HOTC official package”  
- Do not prescribe treatment for injury  
- Do not scrape full directory into git  
