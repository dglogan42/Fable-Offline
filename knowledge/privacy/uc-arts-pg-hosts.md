# Privacy host map — UC Arts postgraduate hub (seed)

**Skill:** `privacy-host-map`  
**Page:** [Arts postgraduate study](https://www.canterbury.ac.nz/study/academic-study/arts/study-arts/arts-postgraduate-study)  
**Org:** University of Canterbury (`canterbury.ac.nz`)  
**Not legal advice.** Static HTML + head tags; re-verify Network tab.

---

## Verdict

Heavy **marketing + accessibility + error monitoring** stack on an **AEM** site. Multiple parallel analytics vendors (double GTM containers, Adobe Launch, ClickDimensions, Lucky Orange, Monsido). Folio auth token keys appear in head scripts (sessionStorage) — treat as **CONFIG** for library/auth integration, not proof of active login on this topic page.

---

## Host inventory (from dump head)

| Host / pattern | Tag | Notes |
|----------------|-----|--------|
| `www.canterbury.ac.nz` | origin **LOAD** | Main site |
| `myuc.canterbury.ac.nz` | **CLICK** | Apply / login |
| `courseinfo.canterbury.ac.nz` | **CLICK** | Courses |
| `uconline.ac.nz` | **CLICK** | UC Online |
| `www.googletagmanager.com` | **LOAD** | **GTM-TNGVT97** and **GTM-NDJ6FWD5** (two containers) |
| `assets.adobedtm.com` | **LOAD** | Adobe Launch / DTM |
| `js.sentry-cdn.com` | **LOAD** | Sentry error monitoring |
| `/.rum/@adobe/helix-rum-js` | **LOAD** | Adobe Helix RUM (relative) |
| `d10lpsik1i8c69.cloudfront.net` | **LOAD** | Lucky Orange (`__lo_site_id = 330545`) |
| `analytics-au.clickdimensions.com` | **LOAD** / **CONFIG** | ClickDimensions; account key present in page script; domain `canterbury.ac.nz` |
| `app-script.monsido.com` | **LOAD** | Monsido accessibility / heatmap / page assist |
| `MomentJS.com` | **LOAD** | moment.js from public CDN (third-party) |
| `shielded.co.nz` | **CLICK** / img | Shielded Site logo in footer |

### First-party / same-org

- `canterbury.ac.nz` and subdomains above  
- `/etc.clientlibs/…` AEM clientlibs (first-party path)  
- `/content/dam/uoc-…` DAM assets  

### CONFIG notes

| Item | Value (snapshot — may rotate) |
|------|-------------------------------|
| GTM IDs | `GTM-TNGVT97`, `GTM-NDJ6FWD5` |
| Lucky Orange site | `330545` |
| ClickDimensions account key | Present in page (`aOkuhWr0XXUyACa3lLtKZL` in dump — treat as sensitive config; do not reuse for attacks) |
| Monsido token | Present in `_monsido` config object |
| Folio session keys | `folio.auth`, `folio.tenant` in sessionStorage helpers |

---

## Evidence rules

| Tag | Use |
|-----|-----|
| **LOAD** | Scripts, pixels, RUM |
| **CONFIG** | GTM IDs, account keys, Folio keys |
| **CLICK** | Apply, contact, qualification links, Shielded |
| **BUNDLE** | Host strings only in minified AEM JS |

---

## Sensitive widgets

| Widget | Note |
|--------|------|
| Monsido PageAssist | Accessibility personalisation UI |
| Shielded | Family-violence safety logo — isolation notes if mapping further |
| Apply / myUC | Auth boundary — not this public topic page alone |

---

## Cross-links

- Content: `knowledge/education/uc-arts-postgraduate-study.md`  
- AEM patterns: `aem-site-agent` / `knowledge/aem/aem-patterns.md`  
