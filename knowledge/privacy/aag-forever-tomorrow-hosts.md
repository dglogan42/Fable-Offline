# Auckland Art Gallery — Forever Tomorrow exhibition page host map

**Compiled:** 2026-07-12  
**URL:** https://www.aucklandartgallery.com/visit/exhibitions/forever-tomorrow-chinese-art-now  
**Title:** Forever Tomorrow: Chinese Art Now | 2 May 2026 – 23 Aug 2026 | Auckland Art Gallery Toi o Tāmaki  
**Operator:** Auckland Art Gallery Toi o Tāmaki (Tātaki Auckland Unlimited family; CDN `cdn.aucklandunlimited.com`)  
**Skill:** `privacy-host-map`  
**Not legal advice.** Stack differs from Auckland Council AEM pages (React SPA + consent SDK + Meta pixel).

---

## Verdict first

**Map only (static HTML)** — major exhibition marketing page with **timed tickets**, rich media, and a **dense marketing/ops stack**: GTM **GTM-KCGVLXLM**, **Meta Pixel** `2180569876087694`, **Google reCAPTCHA v3**, **Securiti** cookie-consent SDK, **Sentry** browser tracing, **YouTube** + **Vimeo** players, **Stackla** social UGC widget, first-party fonts/assets, and ticketing/shop subdomains. Meta **`robots: noindex, nofollow`** on this capture (may be pre-launch/staging control — re-check live).

Exhibition substance: `knowledge/culture/aag-forever-tomorrow.md`.

---

## First-party / same org family

| Host | Role | Tag |
|------|------|-----|
| **www.aucklandartgallery.com** | Site origin, React modules under `/assets/` | **LOAD** |
| **cdn.aucklandunlimited.com** | Media CDN (heroes, carousels, sponsor logos) | **LOAD** |
| **tix.aucklandartgallery.com** | Ticketing (linked) | **CLICK** / possible embed |
| **shop.aucklandartgallery.com** | Shop | **CLICK** |
| **aagfoundation.nz** | Foundation support link | **CLICK** |

---

## A. High privacy relevance

| Host / ID | Role | Tag | Notes |
|-----------|------|-----|--------|
| **www.googletagmanager.com** | GTM **GTM-KCGVLXLM** | **LOAD** | Different container from AC `GTM-MCLW6DXF` |
| **connect.facebook.net** + **facebook.com/tr** | Meta Pixel **2180569876087694** | **LOAD** | `PageView` on load; noscript pixel |
| **www.google.com/recaptcha** | reCAPTCHA v3 site key `6LdjLpgsAAAAAHq6GB3UYyRWLJfHkEw4QE8WcxeP` | **LOAD** | Bot scoring on forms/tickets path |
| **cdn-prod.securiti.ai** + **app.securiti.ai** | Cookie consent SDK | **LOAD** | tenant `d62e2210-…`, domain `43f0df80-…` |
| **Sentry** (meta `sentry-trace` / baggage) | Error/perf monitoring | **CONFIG**/runtime | public_key `3e32099e…`, org_id `355431` |
| **www.youtube.com** | iframe API / embeds | **LOAD** |
| **player.vimeo.com** | Vimeo player API | **LOAD** |
| **assetscdn.stackla.com** / **widget-ui.stackla.com** | Stackla UGC/social wall | **LOAD** |
| **schema.org** JSON-LD | SEO structured data | **BUNDLE**/inline | Not a network tracker |

---

## B. Comparison vs Auckland Council AEM pages

| | AC Compliance / Sports field | AAG Forever Tomorrow |
|--|------------------------------|----------------------|
| CMS | AEM `etc.clientlibs` | React Router SPA (`entry.client-*.js`) |
| GTM | MCLW6DXF / TDX29C | **KCGVLXLM** |
| Session replay | Hotjar/Clarity on some AC pages | Not seen in this dump |
| Ads pixel | Usually via GTM | **Explicit Meta fbq init** |
| Consent | Policy links | **Securiti** consent SDK |
| Search | Coveo | First-party search route |

---

## Purpose diagram

```text
[Browser] → aucklandartgallery.com (Forever Tomorrow)
              ├─ GTM-KCGVLXLM
              ├─ Meta Pixel 2180569876087694
              ├─ reCAPTCHA v3
              ├─ Securiti consent (cdn-prod.securiti.ai)
              ├─ Sentry (browser)
              ├─ YouTube + Vimeo APIs
              ├─ Stackla social widget
              └─ cdn.aucklandunlimited.com media
                    └─ tickets → tix.aucklandartgallery.com
```

---

## One concrete risk

Assuming a **cultural exhibition** page is “just content”: this capture still runs **ad/retargeting (Meta)**, **bot scoring (reCAPTCHA)**, **consent tooling (Securiti)**, and **error telemetry (Sentry)** before any ticket purchase. `noindex` may limit search discovery but does **not** remove on-page trackers for visitors who open the URL.

**Related:** AC host maps under `knowledge/privacy/ac-*.md` for stack contrast.
