# Privacy host map seed — Heart of the City (Health & Wellbeing)

**Skill:** `privacy-host-map` · `hotc-wellness-retreat-kit`  
**URL:** https://heartofthecity.co.nz/health-wellbeing  
**Evidence:** Public page fetch (Drupal-style listings, social links). VERIFY LIVE for full tracker stack.

Not legal advice.

---

## Host inventory

| Host | Class | Notes |
|------|-------|--------|
| `heartofthecity.co.nz` | LOAD/CLICK | Directory, articles, favourites, search |
| `www.facebook.com` | CLICK | heartofaklcity |
| `twitter.com` / `x.com` | CLICK | HeartOfAklCity |
| `instagram.com` | CLICK | heartofaklcity |
| Venue third-party sites | CLICK | Booking after leaving HOTC (per listing) |

### First-party path families

- `/health-wellbeing` — category grid  
- `/health-wellbeing/*` — venue detail  
- `/article/*` — editorial (e.g. healthy habits)  
- `/explore/*` — precinct pages  
- `/flag/flag/favourite/*` — favourites (auth-ish)  
- `/sites/default/files/*` — images  

---

## Notes

- Favourites / accounts may set cookies — user HITL  
- Brochure curation does not require login  
- Do not scrape full business DBs into git  

## OPEN

- Full analytics (GTM/Hotjar/etc.) on live Network tab  
- Payment/booking hosts per venue  
