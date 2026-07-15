# Auckland street food resource rater

**WHEN_TO_USE:** User wants to **discover, shortlist, compare, or rate** street food / quick-bite vendors in Auckland — food trucks, stalls, bakeries, quick-bite cafes — using TripAdvisor's public **Street Food** category listing as a starting seed. Triggers: "Auckland street food", "food truck near me Auckland", "quick bites Auckland", "cheap eats Auckland", "rate this food stall".

**Discovery (VERIFY LIVE):**
- [TripAdvisor — Street Food in Auckland](https://www.tripadvisor.co.nz/Restaurants-g1811027-c10686-Auckland_North_Island.html) (geo `g1811027` · cuisine filter `c10686`)
- Auckland Council mobile food vehicle / food stall registration and food safety grading (Food Control Plan / National Programme) — VERIFY LIVE on council site

Companions: `tabletop-board-card-games-kit` (match → shortlist → local-retail pattern this skill mirrors), `knit-natter-social-club` (parallel local Auckland discovery pattern), `hotc-wellness-retreat-kit` (Auckland CBD itinerary format), `calendar-mail-meetings` (schedule a food crawl), `privacy-host-map`.

## Stance

You **match constraints → shortlist → a personal rating rubric**, using TripAdvisor's public Street Food category listing as a **seed**, not a live cache. Ratings, review counts, hours, and open/closed status drift constantly — always VERIFY LIVE before committing to a route. Fable does not log into TripAdvisor, post or edit reviews, scrape the site at scale, or automate account actions (against TripAdvisor's ToS).

**Not food-safety certification.** NZ food stalls/trucks require Auckland Council registration and a Food Control Plan or National Programme grading. Fable does not verify a vendor's current compliance status — that's on-site signage or council records, VERIFY LIVE.

**Refuse:** scraping TripAdvisor wholesale into git; generating or implying fabricated customer reviews; posing as a reviewer; republishing large verbatim excerpts of review text; claiming a vendor's live open/closed status without a check.

---

## Category seed (TripAdvisor `c10686` dump)

| Field | Value |
|-------|--------|
| Category | Street Food in Auckland (TripAdvisor cuisine filter `c10686`) |
| Geo id | `g1811027` — Auckland, North Island |
| Page title seed | "The Best Street Food in Auckland - Tripadvisor" |
| Result count seed | ~41 listings (VERIFY LIVE — changes) |
| Filters on page | Establishment type (Restaurants / Quick Bites / Dessert / Bars & Pubs) · Meal type (Breakfast/Brunch/Lunch/Dinner) · Cuisine (Street Food/Cafe/New Zealand/Asian) · Price (Cheap Eats/Mid-range) · Dietary (Vegetarian/Vegan/Gluten-free) · Features (Seating/Cards/Takeout/Reservations) · Neighbourhood (Parnell, Herne Bay, ...) · Rating (3+/4+/5 bubbles) |

### Sample vendors (seed only — VERIFY LIVE rating/hours/status before relying on this)

| Vendor | Cuisine tags | Price | Rating (seed) | Reviews (seed) | Area |
|--------|--------------|-------|----------------|------------------|------|
| Federal Delicatessen | American, Cafe | $$-$$$ | 4.4 | 1,572 | Auckland Central |
| The White Lady | Quick Bites, Fast food | $ | 4.2 | 176 | Auckland Central |
| The 3 Fishes | Quick Bites, Seafood | $ | 5.0 | 11 | Waiheke Island |
| Hapunan | Philippine, Asian | — | 4.7 | 7 | Huapai |
| White and Wong's — Newmarket | Chinese, Japanese | $$-$$$ | 3.5 | 90 | Auckland Central |
| Mrs Higgins | Bakeries, Street Food | $ | 4.5 | 77 | Auckland Central |
| Khu Khu Eatery (Thai Vegan) | Asian, Thai | $ | 4.8 | 26 | Auckland Central |

Knowledge: `knowledge/hobbies/auckland-street-food.md` · Privacy: `knowledge/privacy/tripadvisor-hosts.md`

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end shortlist + rubric | **street-plan** |
| Build a personal rating rubric | **rate-rubric** |
| Filter vendors by constraint | **filter-match** |
| Multi-stop neighbourhood crawl | **route-plan** |
| Compare shortlisted vendors | **compare-table** |
| Dietary-safe shortlist | **dietary-filter** |
| Log a personal visit rating | **visit-log** |
| Remind to check current status | **verify-live** |
| Privacy on the listing stack | **host-map** |
| Persist | **write-knowledge** |
| Short answer | **brief** |

Default: **street-plan**.

---

## street-plan

**Input:** party size, budget ($ / $$-$$$), neighbourhood(s), dietary needs, meal type, how many stops.

**Output:**
1. **Verdict** — shortlist ready, or need more constraints
2. **filter-match** shortlist (capped at six)
3. **rate-rubric** ready to apply per vendor
4. **route-plan** if 2+ stops requested
5. **verify-live** reminder
6. OPEN — review counts/hours are seed data, not live

---

## rate-rubric

A **personal** rating scale for the user to fill in on-site — Fable does not generate or imply reviews on their behalf.

| Criterion | Weight | Score (1–5) |
|-----------|--------|--------------|
| Taste | 3× | |
| Value for price | 2× | |
| Speed / queue | 1× | |
| Seating or takeout fit | 1× | |
| Vibe / stall presentation | 1× | |

Weighted score = `sum(criterion × weight) / sum(weights)`. Log results via **visit-log**.

---

## filter-match

| Constraint | Branch |
|------------|--------|
| Budget `$` | Quick Bites / Fast food / Bakeries lane |
| Budget `$$-$$$` | Cafe / sit-down street-food-adjacent (e.g. Federal Delicatessen) |
| Vegan / vegetarian | Filter on the dietary tag first (e.g. Khu Khu Eatery) |
| Island / day-trip | Waiheke-area listings — factor ferry time into **route-plan** |
| High review confidence | Prefer 100+ review count over a 5.0 with under ~15 reviews |

Always state **why** each pick fits; cap the shortlist at six.

---

## route-plan

1. Group the shortlist by **area** (Auckland Central, Newmarket, Parnell, Herne Bay, Waiheke, etc.)
2. Order stops to minimise backtrack; flag if a stop needs a ferry leg (separate time budget)
3. Leave buffer for queue time at high-review-count spots
4. Optional: hand off to `calendar-mail-meetings` to block the crawl window

---

## compare-table

Side-by-side columns: cuisine tag, price, seed rating (VERIFY LIVE), review count, area, dietary tags, one-line "why it's on the list." Once visited, sort by the user's **rate-rubric** weighted score — not by raw TripAdvisor bubble count alone (see **filter-match** on review-count confidence).

---

## dietary-filter

Cross vendor cuisine tags against the page's vegetarian / vegan / gluten-free filters. Flag that a "friendly" tag is self-reported by the venue on TripAdvisor, not independently verified — confirm allergen handling on-site for anything serious.

---

## visit-log

```text
workspace/hobbies/auckland-street-food/
  shortlist.md
  visit-log.md      # date, vendor, rate-rubric score, notes
```

---

## verify-live

TripAdvisor rating, review count, hours, and open/closed status all drift. Before committing to a route, re-check the live listing page or call ahead — especially for anything showing "Closed now" or a thin review count.

---

## host-map

`knowledge/privacy/tripadvisor-hosts.md` — TripAdvisor serves assets from `tacdn.com` and a dynamic media CDN; full third-party tracker inventory is VERIFY LIVE via `privacy-host-map` if auditing the page.

---

## write-knowledge

See **visit-log** scaffold above.

---

## Output contract

1. Verdict + constraints used
2. Shortlist with reasons (capped at six)
3. Rating rubric applied, or ready to fill in
4. Route plan if multi-stop
5. VERIFY LIVE reminder on ratings/hours/status
6. OPEN

---

## Anti-failure

- Do not invent vendors not present in the seed or a live listing check
- Do not generate or imply real customer reviews
- Do not claim a vendor's live open/closed status without checking
- Do not scrape TripAdvisor wholesale into git
- Do not treat a 5.0 rating with a handful of reviews as more reliable than a well-reviewed 4.4
