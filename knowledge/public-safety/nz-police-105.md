# NZ Police 105 — non-emergency reporting

**URL:** https://www.police.govt.nz/use-105  
**Title:** 105 Police Non-Emergency Online Reporting | New Zealand Police  
**Drupal node:** `/node/66454`  
**Captured:** 2026-07-12  
**CMS:** Drupal 11 (theme `bs_barrio_police`)  
**Skills:** `emergency-services-agent`, `privacy-host-map`  
**Not legal advice.** Not a substitute for emergency response.

---

## Emergency vs non-emergency (critical)

| Situation | Action |
|-----------|--------|
| **Emergency** — happening now, or someone in danger | Call **111** |
| **Non-emergency** report | Online options on this page, or call **105** (Ten-Five) **24/7** |

Page messaging (from meta/body): use online report options for non-emergency, or call 105. If it’s happening now or someone’s in danger → **111**.

---

## What 105 is for (page framing)

- **Non-emergency** crime and incident reporting  
- Phone **105** available 24/7  
- Online reporting paths (forms typically on `forms.police.govt.nz` / `webforms.police.govt.nz` — linked from police site)  

Exact report categories (theft, damage, etc.) are on the live page form selector — re-check live; do not invent report types.

---

## Site chrome (context only)

Dump also showed:

- **Amber Alert** banner component (active-alert UI when live)  
- Multilingual advice links (English, te reo Māori, Chinese, Hindi, Spanish, Arabic, Farsi, German, Japanese, Korean, Somali, Thai, Vietnamese)  
- Related advice hubs: victims, family violence, sexual assault, driving/road safety, firearms safety, etc.  

---

## Agent boundaries

| May | Must not |
|-----|----------|
| Direct users to **111** vs **105** correctly | Take crime reports as the agent of record |
| Summarise published 105 purpose | Advise “don’t call 111” in unclear emergencies |
| Link to official police.govt.nz pages | Store victim PII or full report narratives in git |
| Map privacy of the reporting page | Impersonate Police or open investigations |

---

## Privacy

Host map: `knowledge/privacy/nz-police-105-hosts.md`

---

## Related

- Health NZ Find a service — health directory, not police  
- Women’s Refuge / Shielded — family violence safety tools (different agencies)  
- For family violence help, page links Police advice; crisis support may also use independent services  

**In emergency always prioritise 111.**
