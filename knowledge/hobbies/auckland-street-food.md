# Auckland street food — discovery map

**Skill:** `auckland-street-food-rater`
**Discovery hub:** [TripAdvisor — Street Food in Auckland](https://www.tripadvisor.co.nz/Restaurants-g1811027-c10686-Auckland_North_Island.html)
**Not product endorsement.** Ratings, review counts, hours, and stock/menu items **VERIFY LIVE**. Trademarks and business names remain with their respective owners.

---

## Scope

Auckland "street food" spans food trucks, market stalls, bakeries, and quick-bite cafes across Auckland Central and outer suburbs/islands (e.g. Waiheke, Huapai). Pick by **budget**, **area**, **dietary need**, and **review confidence** (review count, not just star rating).

---

## Category seed (TripAdvisor `c10686`, geo `g1811027`)

| Field | Value |
|-------|--------|
| Category label | Street Food in Auckland |
| Result count seed | ~41 listings (VERIFY LIVE) |
| Establishment types | Restaurants, Quick Bites, Dessert, Bars & Pubs |
| Meal types | Breakfast, Brunch, Lunch, Dinner |
| Cuisine filters | Street Food, Cafe, New Zealand, Asian |
| Price bands | Cheap Eats (`$`), Mid-range (`$$-$$$`) |
| Dietary filters | Vegetarian friendly, Vegan options, Gluten free options |
| Feature filters | Seating, Accepts Credit Cards, Takeout, Reservations |
| Neighbourhood filters seen | Parnell, Herne Bay (VERIFY LIVE for full list) |
| Rating filters | 3+, 4+, 5 bubbles |

### Sample vendors (seed — VERIFY LIVE before relying on rating/hours/status)

| Vendor | Cuisine | Price | Rating | Reviews | Area |
|--------|---------|-------|--------|---------|------|
| Federal Delicatessen | American, Cafe | $$-$$$ | 4.4 | 1,572 | Auckland Central |
| The White Lady | Quick Bites, Fast food | $ | 4.2 | 176 | Auckland Central |
| The 3 Fishes | Quick Bites, Seafood | $ | 5.0 | 11 | Waiheke Island |
| Hapunan | Philippine, Asian | — | 4.7 | 7 | Huapai |
| White and Wong's — Newmarket | Chinese, Japanese | $$-$$$ | 3.5 | 90 | Auckland Central |
| Mrs Higgins | Bakeries, Street Food | $ | 4.5 | 77 | Auckland Central |
| Khu Khu Eatery (Thai Vegan) | Asian, Thai | $ | 4.8 | 26 | Auckland Central |

**Review-confidence hygiene:** a 5.0 average built on ~10 reviews is a weaker signal than a 4.4 built on 1,500+. Prefer the latter for a first-time visit; use small-sample high scorers as adventurous picks, not anchor choices.

---

## Rating rubric (personal, not a scraped review)

| Criterion | Weight | Score (1–5) |
|-----------|--------|--------------|
| Taste | 3× | |
| Value for price | 2× | |
| Speed / queue | 1× | |
| Seating or takeout fit | 1× | |
| Vibe / stall presentation | 1× | |

Weighted score = `sum(criterion × weight) / sum(weights)`.

---

## Session matchmaker (quick)

| Constraint | Prefer |
|------------|--------|
| Tight budget | `$` Quick Bites / bakeries |
| Sit-down mid-range | Cafe-tagged spots (e.g. Federal Delicatessen) |
| Vegan/vegetarian | Filter dietary tag first |
| Day trip | Waiheke listings — add ferry time |
| First-time visit | High review-count spots over thin-sample 5.0s |

---

## Auckland Council food-safety context (general, VERIFY LIVE)

Mobile food vehicles and stalls operating in Auckland must register with **Auckland Council** and operate under either a **Food Control Plan** (template or custom) or a **National Programme**, per the NZ Food Act 2014. TripAdvisor listings do not surface current compliance/grading status — check on-site signage or council records if that matters to the user.

---

## Scaffold

```text
workspace/hobbies/auckland-street-food/
  shortlist.md
  visit-log.md      # date, vendor, rate-rubric score, notes
```

---

## Related Fable skills

| Skill | Overlap |
|-------|---------|
| `tabletop-board-card-games-kit` | Same match → shortlist → local-retail pattern, different hobby |
| `knit-natter-social-club` | Parallel local Auckland discovery pattern |
| `hotc-wellness-retreat-kit` | Auckland CBD itinerary format |
| `calendar-mail-meetings` | Schedule a food crawl |

---

## OPEN

- Current TripAdvisor result count, ratings, hours, and open/closed status
- Full neighbourhood filter list
- Auckland Council's current registered mobile-vendor list
