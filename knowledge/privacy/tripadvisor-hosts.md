# Privacy host map seed — TripAdvisor street food listing

**Skill:** `privacy-host-map` · `auckland-street-food-rater`
**Primary page:** https://www.tripadvisor.co.nz/Restaurants-g1811027-c10686-Auckland_North_Island.html
**Evidence:** Public listing page dump (partially JS-rendered). VERIFY LIVE for full tracker inventory.

Not legal advice.

---

## Host inventory

| Host | Class | Notes |
|------|-------|--------|
| `tripadvisor.co.nz` / `.com` | CLICK/LOAD | Listing pages, search, reviews, filters |
| `tacdn.com` | LOAD | Static asset CDN (icons, scripts, styles) |
| Dynamic media CDN (image host) | LOAD | Listing photos — exact hostname VERIFY LIVE |
| Analytics / ad tech | LOAD (assumed) | Not confirmed in the fetched excerpt — large listing sites typically run tag managers and ad partners; confirm via a live `privacy-host-map` pass before treating as exhaustive |

---

## Notes

- Page appeared partially JS-rendered on fetch — placeholder image SVGs and dynamic-content loading indicators present, so a full network trace (not just the HTML dump) is needed for a complete host list
- TripAdvisor accounts (for posting reviews, saving lists) are user CLICK/HITL only — Fable does not log in or post on the user's behalf
- Do not scrape the full listings database into git; treat sample vendor tables in `knowledge/hobbies/auckland-street-food.md` as a small dated seed, not a live mirror

## OPEN

- Full third-party tag/analytics/ad-tech inventory (needs live network trace, not static HTML)
- Explicit copyright/trademark footer text (truncated in the fetched excerpt)
