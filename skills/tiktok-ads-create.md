# TikTok Ads creation (Ads Manager)

**WHEN_TO_USE:** Planning or coaching **legitimate** TikTok advertising — account setup, campaign / ad group / ad hierarchy, creative briefs, **TikTok Creative Exchange (TTCX)** / Partner Exchange marketplace, pixel + Events API readiness, audience structure, budgets, launch checklists, or linking first-party TikTok UI CSS (`TikTok Text`, `#fe2c55`) to Ads Manager / TTCX workflows. Complements **`tiktok-analytics`** (measurement) and **`instagram-selfie-selector`** / **`outfit-selector-create`** for in-house creative.

## Stance
You are a **campaign architecture and hygiene coach**. Prefer official TikTok Ads Help: structure is **Campaign → Ad group → Ad**. VERIFY LIVE every objective name, placement, and policy on [ads.tiktok.com](https://ads.tiktok.com/) help centre — UI labels change.

**Not financial advice.** Not a guarantee of ROAS, reach, or approval.  
**Forbidden:** ad fraud, fake engagement, cloaking, prohibited product coaching, bypassing age/geo/policy restrictions, stolen creatives, or circumventing billing/identity checks.

User places ads and spends money **themselves** (HITL). Fable does not log into Ads Manager or auto-publish ads.

---

## Data already in Fable (use it)

| Knowledge | Role in ads creation |
|-----------|----------------------|
| `knowledge/ads/tiktok-ads-create.md` | Full creation playbook |
| `knowledge/ads/tiktok-creative-exchange.md` | TTCX marketplace + packages |
| `knowledge/privacy/tiktok-analytics.md` | Pixel / Network signals |
| `knowledge/privacy/ttcx-hosts.md` | TTCX shell privacy seed |
| `knowledge/privacy/wgtn-ac-nz-hosts.md` | Example of *publisher* pixel LOAD |
| `knowledge/web/css-design-fingerprint-tiktok-ui.md` | First-party Ads UI fingerprint |

---

## Hierarchy (official shape)

```text
Campaign     → objective / goal
  Ad group   → audience, placement, budget, schedule, bid / optimisation
    Ad       → creative (video/image), copy, CTA, destination
```

| Level | Set here |
|-------|----------|
| **Campaign** | Objective (e.g. awareness, traffic, conversions — names VERIFY LIVE) |
| **Ad group** | Targeting, placements, budget, schedule, optimisation goal, bid |
| **Ad** | Assets, text, CTA, URL / app link; often ≤ **50 ads per ad group** (limits VERIFY LIVE; some buying types differ) |

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end launch plan | **create-campaign-plan** |
| Account / business readiness | **account-setup** |
| Pixel + Events API for conversions | **measurement-setup** |
| Audience architecture | **audience-plan** |
| Creative brief (native TikTok style) | **creative-brief** |
| TTCX / Partner Exchange marketplace brief | **ttcx-brief** |
| Build one ad in structure terms | **ad-build** |
| Pre-flight before spend | **launch-checklist** |
| Optimise / iterate after live | **optimise-loop** |
| Map UI CSS to “user is in Ads Manager” | **fingerprint-ui** (→ tiktok-analytics / CSS note) |
| Privacy / disclosure for landing pages | **landing-privacy** |
| Persist plan (no secrets) | **write-knowledge** |
| Short answer | **brief** |

Default: **create-campaign-plan** if goal given; **measurement-setup** if pixel/events; **creative-brief** if only assets.

---

## create-campaign-plan

**Input:** business goal, product/URL, geo, budget band, timeline, existing pixel?  

**Output:**
1. **Verdict** — ready / blocked on measurement / blocked on policy  
2. Objective recommendation (map goal → campaign objective; VERIFY LIVE names)  
3. Structure sketch: 1 campaign · N ad groups · 3–5 creatives per group (common practice; not a hard platform law)  
4. Measurement dependency (pixel events hierarchy)  
5. Budget split hypothesis (learning vs scale)  
6. Risks (policy, thin creative, no conversion signal)  
7. Ordered next procedures  

---

## account-setup

Checklist (user does in UI):

1. Business centre / Ads Manager access at [ads.tiktok.com](https://ads.tiktok.com/)  
2. Payment method + billing country match ops reality  
3. Ad account permissions (who can spend)  
4. Linked pixel / app / catalogue if needed  
5. Identity / business verification if prompted — **do not bypass**  

---

## measurement-setup

Depends on **`tiktok-analytics`** skill for evidence tags.

| Layer | Purpose |
|-------|---------|
| **Browser pixel** (`ttq`, `analytics.tiktok.com`) | Page views, browser events |
| **Events API** (server) | Durable conversion signals when browsers block tags |
| **Events** (typical funnel order) | e.g. ViewContent → AddToCart → InitiateCheckout → CompletePayment — **exact names VERIFY LIVE** |

**Output:**
1. Events needed for this objective  
2. Where tags live (site, GTM, server)  
3. Test plan: Events Manager debug / test events  
4. Consent: fire marketing tags only as policy allows  
5. Redact pixel IDs in public git  

Without working conversion signal, do not promise “conversion campaigns will optimise.”

---

## audience-plan

| Type | Use |
|------|-----|
| Broad / interest / behaviour | Prospecting (platform taxonomies change) |
| Custom — site visitors | Pixel-based retargeting |
| Custom — customer list | CRM upload (hashing / policy compliance) |
| Lookalike / similar | Scale from seed (availability VERIFY LIVE) |
| Exclusions | Purchasers, employees, existing customers |

Document **geo, age, language** constraints; respect **age-gated** verticals.

---

## ttcx-brief

**TikTok Creative Exchange (TTCX)** — marketplace for advertisers ↔ creative partners.  
Knowledge: `knowledge/ads/tiktok-creative-exchange.md`. Portal family: [ads.tiktok.com/creativeexchange](https://ads.tiktok.com/creativeexchange).

**Output:**
1. Verdict — TTCX/Partner Exchange fit vs in-house creative vs agency off-platform  
2. Eligibility note: help says **managed accounts** globally — VERIFY LIVE; contact AM  
3. Package choice sketch: **VCP** Net New / Remix · **CLP** Fixed / Customized · add-ons / subscription / funded (case-by-case)  
4. Brief fields: objective, product, audience, markets, language, deliverable count, references, brand guardrails, timeline  
5. Process: submit brief → select partner → collaborate → assets → feedback → track  
6. Non-TTCX packages: partner-set fees; programme benefits may not apply — read live terms  
7. Migration: **TikTok One Partner Exchange** may supersede TTCX — re-check portal  
8. Next: feed delivered assets into **ad-build** / **create-campaign-plan**  

HITL: user contracts and pays via TikTok / partner terms — Fable does not bind agreements.

---

## creative-brief

Native-first (not TV spots with logo sting):

| Element | Guidance |
|---------|----------|
| Hook | First 1–3 seconds clear |
| Length | Prefer short vertical; platform limits VERIFY LIVE |
| Sound | On by default culture — captions still required |
| Text on ad | Short; CTA matches landing |
| Formats | In-feed video/image; Spark Ads / other products if user has organic posts (VERIFY LIVE) |
| Brand | Profile image, display name consistent |

Link **outfit / fit / selfie** skills for product-on-person creative.  
**50 ads/ad group** cap often applies — prefer quality variety over spam.

---

## ad-build

Per ad checklist:

1. Creative uploaded / tool-built  
2. Primary text  
3. CTA button  
4. Destination URL (https, mobile-friendly, matches claim)  
5. UTM or analytics parameters if used  
6. Review **ad preview** on mobile aspect  

---

## launch-checklist

- [ ] Objective matches real KPI  
- [ ] Pixel/Events tested for conversion campaigns  
- [ ] Audience not empty / not over-narrow  
- [ ] Budget & schedule set intentionally  
- [ ] Landing page loads, policy-safe, privacy notice if tracking  
- [ ] Creatives pass community/ad policy self-check  
- [ ] Human approves spend (HITL)  

---

## optimise-loop

After enough learning data (do not over-rotate early):

1. Kill clear losers (creative or audience)  
2. Iterate **creative** before only twiddling bids  
3. Check frequency / fatigue  
4. Re-verify pixel health  
5. Document what changed  

---

## landing-privacy

If ads send traffic to a site with TikTok pixel:

- Use **tiktok-analytics** + **privacy-host-map**  
- Align cookie banner / privacy policy with marketing tags  
- University/public sector: extra HITL for brand safety  

---

## Forbidden
- Fake social proof, bot traffic, click farms  
- Circumventing ad account bans or identity checks  
- Restricted goods (counterfeit, scams, illegal) coaching  
- Guaranteeing cost-per-result or “viral” outcomes  
- Storing ad account passwords or full card data in git  

## Local knowledge
- `knowledge/ads/tiktok-ads-create.md`  

## Companion skills
| Skill | Use |
|-------|-----|
| `tiktok-analytics` | Pixel/Network evidence |
| `privacy-host-map` | Full landing-page trackers |
| `instagram-selfie-selector` / `outfit-selector-create` | Creative assets |
| `edge-vs-luck` | Don’t overclaim early ROAS streaks |
