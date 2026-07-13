# Privacy host map seed — MyFitnessPal (myfitnesspal.com)

**Skill:** `privacy-host-map` · `myfitnesspal-resource-kit`  
**Page:** Logged-out homepage HTML dump (`release-version` v21.9.1)  
**URL:** https://www.myfitnesspal.com  
**Evidence class:** LOAD / CONFIG from head + `window.__ENV`  

Not a compliance certification. Not legal advice. VERIFY LIVE after deploys.

---

## First-party / CDN

| Host | Class | Notes |
|------|-------|--------|
| `www.myfitnesspal.com` | LOAD | Site origin, NextAuth URL |
| `web-assets.myfitnesspal.com` | LOAD | Next static CSS/JS/fonts (`ASSET_PREFIX`, scripts) |
| `web-main-assets.myfitnesspal.com` | LOAD | Preconnect assets |
| `api.myfitnesspal.com` | CONFIG | `MFP_PUBLIC_API_HOST` |
| `blog.myfitnesspal.com` | CONFIG/CLICK | `BLOG_HOST` |
| `community.myfitnesspal.com` | CONFIG/CLICK | Community + `COMMUNITY_CLIENT_ID` |
| `www.prodmyfitnesspal.com` | CONFIG | Sourcepoint property href |

---

## Consent / privacy management

| Host / vendor | Class | Notes |
|---------------|-------|--------|
| `consent.truste.com` | LOAD | TrustArc/Truste preconnect |
| `consent.trustarc.com` | LOAD | TrustArc |
| `cdn.privacy-mgmt.com` | LOAD | Sourcepoint unified messaging wrapper |
| Sourcepoint init | LOAD | `…/scripts/latest/init-sourcepoint.js` + XSS hardening for `_sp_version` |

---

## Analytics / RUM / product analytics

| Host / vendor | Class | Notes |
|---------------|-------|--------|
| `www.googletagmanager.com` | LOAD | GTM enabled; container **GTM-NR6RNVL** |
| `www.google-analytics.com` | LOAD | Preconnect |
| `www.google.com` / `www.gstatic.com` | LOAD | Google stack / reCAPTCHA |
| Amplitude | CONFIG | `AMPLITUDE_*` keys in `__ENV` (public page config) |
| AppsFlyer | CONFIG | `APPSFLYER_ENABLED` |
| Datadog | CONFIG | Client tokens, RUM app id, CSP token, sample rates (session 40%) |
| Cloudflare Insights | LOAD | `static.cloudflareinsights.com` beacon |

---

## Ads / social / growth

| Host / vendor | Class | Notes |
|---------------|-------|--------|
| Facebook | CONFIG/LOAD | `fb:app_id` **186796388009496**; `connect.facebook.net` preconnect |
| Google Ads | CONFIG | `GOOGLE_AD_KEY` path `/17729925/UACF_W/MFP/` |

---

## Security / payments / widgets

| Host / vendor | Class | Notes |
|---------------|-------|--------|
| reCAPTCHA v3 | CONFIG | Site key in `__ENV` (`CAPTCHA_ENABLED`) |
| Stripe | CONFIG | **Publishable** `pk_live_*` + API version (not secret key) |
| Trainerize / GymEngine | CONFIG | `WIDGET_PARENT_DOMAIN_OR_ORIGIN` list (embed parents) |

---

## Public env key hygiene

Keys in `window.__ENV` are **exposed to every browser** on that page. Still:

- Prefer documenting **purpose**, not copying full secrets into public forks  
- Stripe `pk_live_` ≠ `sk_live_`  
- Do not use page keys to impersonate private APIs  

---

## OPEN

- Cookie list after consent accept/reject  
- Authenticated diary endpoints (not in homepage dump)  
- Regional CMP behaviour  
