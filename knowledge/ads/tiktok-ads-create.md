# TikTok Ads creation — knowledge pack

**Skill:** `tiktok-ads-create`  
**Official entry:** [TikTok Ads Manager](https://ads.tiktok.com/) · Help: [Ads structure](https://ads.tiktok.com/help/article/tiktok-ads-structure), [Create an ad](https://ads.tiktok.com/help/article/ad-set-up)  
**UI fingerprint:** `knowledge/web/css-design-fingerprint-tiktok-ui.md` (TikTok Text, `#fe2c55`, TTAM)  
**Pixel method:** `knowledge/privacy/tiktok-analytics.md`  
**Not financial or legal advice.** VERIFY LIVE all UI labels, limits, and policies (help pages update often; structure note last seen mid-2026 in public help).

---

## 1. What you are building

Paid distribution of video/image ads on TikTok (and related placements the account enables). Organised as:

| Level | Responsibility |
|-------|----------------|
| **Campaign** | Business **objective** (what success means to the algorithm) |
| **Ad group** | **Who** sees it, **where**, **when**, **how much**, **how optimised** |
| **Ad** | **What** they see (creative + copy + CTA + destination) |

Official help: campaigns → ad groups → ads; create ad after campaign + ad group exist.  
**Ad limit:** often **50 ads per ad group** (not always for every buying type / Smart Creative / split tests — VERIFY LIVE).

---

## 2. End-to-end creation flow

```text
1. Account & billing ready
2. Measurement (pixel ± Events API) if optimising to site/app events
3. Campaign objective
4. Ad group: audience, placement, budget, schedule, bid/optimisation
5. Ads: creatives + copy + CTA + URL
6. Review → publish (HITL)
7. Learning period → creative/audience iteration
```

### Official “before ad” note
Advertising **objective** and **ad group** settings change which fields appear on the ad creation module — plan hierarchy top-down.

---

## 3. Account setup checklist

| Step | Notes |
|------|--------|
| Open Ads Manager | ads.tiktok.com |
| Business / ad account | Permissions for spenders |
| Payment | Valid method; tax/entity match |
| Verification | Complete if required — no bypass coaching |
| Assets | Pixel, catalogue, app, audience library as needed |

**UI cue (from Fable CSS data):** product shells use **TikTok Text/Display**, brand **`#fe2c55`**, `--ttam-*` tokens — distinguishes Ads Manager from a random publisher site.

---

## 4. Measurement (from Fable analytics data)

### Browser pixel
| Signal | Role |
|--------|------|
| `ttq` / `TiktokAnalyticsObject` | JS API |
| `ttq.load(PIXEL_ID)` | CONFIG |
| `analytics.tiktok.com` | LOAD host (beacon) |
| Cookie `_ttp` | Browser ID-style |
| Headers `x-tt-*` | Trace (redact in notes) |

**Publisher example (not your brand site unless it is):** VUW home fired TikTok analytics — `knowledge/privacy/wgtn-ac-nz-hosts.md`.

### Events (funnel — names VERIFY LIVE)
Typical commerce hierarchy for setup planning:

1. ViewContent / PageView family  
2. AddToCart  
3. InitiateCheckout  
4. CompletePayment / Purchase  

Plus lead events for non-ecommerce. Prefer **pixel + Events API** when browsers block tags (industry practice; implement per current TikTok docs).

### Consent
Marketing tags should respect cookie/consent regime of the landing site jurisdiction. Map with `privacy-host-map` + `tiktok-analytics`.

---

## 5. Campaign level

| Decision | Guidance |
|----------|----------|
| Objective | Match real KPI: awareness vs traffic vs conversions vs app, etc. |
| Naming | `{date}_{objective}_{product}_{geo}` |
| Budget at campaign | Optional CBO-style settings if offered — VERIFY LIVE product name |

Wrong objective → wrong optimisation signal.

---

## 6. Ad group level

| Setting | Notes |
|---------|--------|
| Audience | Demographics, interests, behaviours, custom, exclusions |
| Placement | Automatic vs manual (inventory changes over time) |
| Schedule | Start/end; dayparting if available |
| Budget | Daily vs lifetime; enough for learning |
| Optimisation goal | Aligns with pixel events / delivery goal |
| Bid | Lowest cost / cost cap / etc. — VERIFY LIVE |

**Structure habit (common practice, not a hard law):** multiple ad groups for distinct audiences; 3–5 creatives to test inside groups.

---

## 6b. Creative supply: TikTok Creative Exchange (TTCX)

When the team cannot produce enough native video in-house:

| Step | Notes |
|------|--------|
| Portal | [Creative Exchange](https://ads.tiktok.com/creativeexchange) (TTCX); migrating toward **TikTok One Partner Exchange** |
| Who | Advertisers (often **managed** — VERIFY LIVE) |
| Flow | Brief → match creative partner → collaborate → deliver assets → use in Ads Manager |
| Packages | VCP Net New / Remix · CLP Fixed / Customized · add-ons · subscription · funded (case-by-case) |
| Detail | `knowledge/ads/tiktok-creative-exchange.md` |

TTCX produces **assets**; Ads Manager still runs **spend**.

---

## 7. Ad level (creative)

| Element | Notes |
|---------|--------|
| Media | Video preferred; image supported per help |
| Aspect | Vertical-first for in-feed |
| Text | Short primary text; CTA button |
| Identity | Display name + profile image |
| Destination | Landing URL or app store; mobile-ready |
| Tools | In-platform creative tools may exist — VERIFY LIVE |

### Creative hygiene
- Hook in first seconds  
- Captions for sound-off  
- Claim = landing page  
- No copyrighted music/assets without rights  
- Spark / organic boost products: separate checklist if used  

Cross-skills: `instagram-selfie-selector`, `outfit-selector-create` for UGC-style fashion creatives.

---

## 8. Launch & optimise

### Pre-flight
- [ ] Pixel events tested for conversion goals  
- [ ] Audience size sanity  
- [ ] Policy self-review  
- [ ] Budget cap known to spender  
- [ ] Landing privacy disclosure if tracking  

### After go-live
- Allow learning; avoid hourly panic edits  
- Prefer creative iteration  
- Watch frequency and CPA trends with **edge-vs-luck** humility on small samples  
- Re-check Events Manager health  

---

## 9. Policy & brand safety (high level)

| Do | Don’t |
|----|--------|
| Follow TikTok advertising policies | Restricted/prohibited goods |
| Honest claims | Before/after health miracles without basis |
| Proper age targeting | Target minors where disallowed |
| Disclose material connections where required | Fake reviews / bot traffic |

Always open current **TikTok Advertising Policies** before launch.

---

## 10. Templates

### Campaign brief
```markdown
# TikTok campaign — [name] — [date]
## Objective
## KPI / success metric
## Geo / language
## Budget & dates
## Measurement events
## Ad groups (audience hypotheses)
## Creatives (3–5 concepts)
## Landing URL
## Risks & HITL
```

### Ad group card
```markdown
## AG — [label]
- Audience:
- Placements:
- Budget:
- Optimisation:
- Ads:
```

---

## 11. Related Fable assets

| Path | Use |
|------|-----|
| `skills/tiktok-ads-create.md` | Procedures (incl. **ttcx-brief**) |
| `skills/tiktok-analytics.md` | Evidence of pixels |
| `knowledge/ads/tiktok-creative-exchange.md` | TTCX marketplace |
| `knowledge/privacy/ttcx-hosts.md` | TTCX shell hosts / pumbaa rules |
| `knowledge/web/css-design-fingerprint-tiktok-ui.md` | Confirm Ads UI |
| `knowledge/privacy/wgtn-ac-nz-hosts.md` | Third-party pixel LOAD example |

---

## Gaps (always re-verify)

- Exact objective list and Smart+ / ASC-style products  
- Current minimum budgets by market  
- Placement inventory (Feed, Search, Pangle, etc.)  
- API automation (Marketing API) — out of scope unless user has official access  
