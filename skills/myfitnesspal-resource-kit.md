# MyFitnessPal resource kit (nutrition · tracking · privacy)

**WHEN_TO_USE:** User dumps **MyFitnessPal** HTML/env, plans nutrition/calorie tracking workflows, Premium features, partner offers, or a **third-party host map** for myfitnesspal.com. Triggers: “MyFitnessPal”, MFP, calorie tracker, macro calculator, BMR, food diary web.

**Official (VERIFY LIVE):**  
- Site: [myfitnesspal.com](https://www.myfitnesspal.com/)  
- Blog: [blog.myfitnesspal.com](https://blog.myfitnesspal.com)  
- Community: [community.myfitnesspal.com](https://community.myfitnesspal.com)  
- API host (public env seed): `https://api.myfitnesspal.com`  
- Brand accent seed: `#0066EE` · font **Inter**  

Companions: `fitness-companion-agent` (habit/process companion over this product map), `privacy-host-map`, `privacy-design-planner`, `css-styles-media-kit` (Inter + MUI emotion shell), `healthnz-find-a-service` / `emergency-services-agent` only for real medical routing — **not** for diet coaching.

## Stance
You map **product surfaces + privacy evidence** from HTML/`window.__ENV`. Fable does **not** log into MFP, scrape private diaries, or give medical/diet prescriptions.

**Not medical, nutrition, or legal advice.** Weight, macros, fasting, and medication-partner offers are **user-operated** features — licensed clinicians decide clinical use. Under-18 and ED-sensitive contexts need human judgment; do not push extreme deficits.

**Refuse:** selling scraped food DBs, bypassing paywalls, storing session cookies / Stripe customer secrets / private journal data in git.

---

## Product map (homepage seed)

| Surface | Notes |
|---------|--------|
| **Calorie / macro tracker** | Core diary logging |
| **BMR / goals calculator** | Goal setup marketing |
| **Food tracker** | Database + barcode / meal scan / voice log (Premium feature list seed) |
| **Exercise tracking** | Workouts + device integrations (40+ apps claim) |
| **Intermittent fasting** | Premium feature seed |
| **Premium** | Ad-free, custom macros, insights, net carbs, multi-day logging, etc. |
| **Partner offers** | e.g. medication-maker Premium promo copy in i18n (VERIFY LIVE eligibility) |
| **Locales** | Many `hrefLang` locales under myfitnesspal.com/{lang} |

Stack seed: **Next.js** (`data-next-head`), release **v21.9.1**, Emotion CSS, Inter typeface, asset CDN `web-assets.myfitnesspal.com`.

Knowledge: `knowledge/health/myfitnesspal.md` · `knowledge/privacy/myfitnesspal-hosts.md`

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end kit | **mfp-plan** |
| Product / feature map | **product-map** |
| Privacy / third-party hosts | **host-map** |
| Design fingerprint (CSS) | **css-fingerprint** |
| User goals hygiene (non-clinical) | **goals-hygiene** |
| Premium / partner offer notes | **premium-notes** |
| Public env key hygiene | **env-hygiene** |
| Scaffold knowledge note | **write-knowledge** |
| Short answer | **brief** |

Default: **mfp-plan**. Audit dump: **host-map** + **env-hygiene**.

---

## mfp-plan

**Input:** user goal (track food / privacy audit / Premium question / partner code).

**Output:**
1. **Verdict** — product + page type (logged-out homepage v2 seed)  
2. **product-map**  
3. **goals-hygiene** if tracking  
4. **host-map** if dump/audit  
5. **env-hygiene** if `__ENV` present  
6. **OPEN** — medical disclaimer, ToS, regional offers  

---

## product-map

From marketing meta + i18n seeds (VERIFY LIVE in-app):

- Nutrition tracking, exercise, barcode, meal scan, voice log  
- Multi-day logging, ad-free, custom macros/goals, fasting, food insights, net carbs  
- Integrations with apps/devices (Trainerize / GymEngine widget origins in env)  

Do not invent clinical efficacy claims.

---

## host-map

Classify every host **LOAD / CONFIG / CLICK / BUNDLE**. Full table: `knowledge/privacy/myfitnesspal-hosts.md`.

Priority families:

| Family | Examples from dump |
|--------|-------------------|
| First-party | `www.myfitnesspal.com`, `web-assets.myfitnesspal.com`, `api.myfitnesspal.com`, blog, community |
| Consent | TrustArc/Truste, Sourcepoint (`cdn.privacy-mgmt.com`, init-sourcepoint.js) |
| Analytics | GTM `GTM-NR6RNVL`, GA, Amplitude, AppsFlyer, Datadog RUM/CSP |
| Ads / social | Google Ads path, Facebook SDK, `fb:app_id` |
| Payments | Stripe publishable key (public) |
| Bot | reCAPTCHA v3 site key |
| Widgets | `*.trainerize.com`, `*.gymengine.com` origins |

---

## css-fingerprint

Homepage emotion/global seeds:

- `font-family: "Inter", Helvetica, Arial, -apple-system, sans-serif`  
- Brand link/blue `#0066EE`  
- Body `rgba(0,0,0,0.87)` on white  
- Fixed header ~60px, blur mobile nav, breakpoint **992px**  

Optional: add row under `css-styles-media-kit` catalog if building a dedicated fingerprint file.

---

## goals-hygiene

Non-clinical process only:

1. User states goal in their words (energy, strength, habit) — not “ideal BMI” from Fable  
2. Prefer sustainable logging over extreme targets  
3. Re-derive numbers only when user supplies data  
4. Escalation: medical conditions → real clinician; NZ emergency → `emergency-services-agent` / 111  

---

## premium-notes

- Partner copy (e.g. Lilly/medication-maker 6-month Premium) has **eligibility and expiry** in marketing strings — VERIFY LIVE email/code terms  
- Fable does not redeem codes or verify subscriptions  

---

## env-hygiene

`window.__ENV` on the dump is **public page config**, still treat carefully:

| Do | Don't |
|----|--------|
| List key **names** + purpose | Paste live keys into public repos as “secrets to use” |
| Note sample rates (Datadog session 40%) | Claim private API access with publishable keys |
| Flag Stripe `pk_live_*` as **publishable** only | Confuse with secret `sk_live_*` |

If writing knowledge notes, prefer **redacted** examples (`pk_live_…[REDACTED]`).

---

## Output contract

1. Verdict first  
2. Product map or host table  
3. Medical disclaimer  
4. OPEN / VERIFY LIVE  
5. No diary data, no session tokens  

---

## Anti-failure

- Not medical advice  
- Do not invent calorie needs  
- Do not scrape private food logs  
- Do not treat GTM/Amplitude IDs as “hacks”  
- Separate Trainerize widget embeds from core MFP  
