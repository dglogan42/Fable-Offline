# NZ Police 105 (use-105) — third-party host map

**Compiled:** 2026-07-12  
**URL:** https://www.police.govt.nz/use-105  
**Title:** 105 Police Non-Emergency Online Reporting  
**Skill:** `privacy-host-map`  
**Not legal advice.** Reporting flows often continue on `forms.police.govt.nz` / `webforms.police.govt.nz` — scan those separately when dumping forms.

---

## Verdict first

**Map only** — Drupal 11 Police site page for **105 non-emergency** reporting. Analytics: **Google Analytics 4 `G-D3P3CRCCXE`** (gtag + Drupal `google_analytics` module settings: outbound/mailto/tel/download tracking). Commented legacy **GTM-KXS4K6P** in HTML. Facebook domain verification + **fb:app_id 537614739774441**. Bootstrap 5.2 from **jsdelivr**. First-party police assets; form hosts under police.govt.nz subdomains.

Service content: `knowledge/public-safety/nz-police-105.md`.

---

## First-party

| Host | Role | Tag |
|------|------|-----|
| **www.police.govt.nz** | Main site | **LOAD** |
| **forms.police.govt.nz** | Online forms (linked) | **CLICK**/LOAD if used |
| **webforms.police.govt.nz** | Webforms (linked) | **CLICK**/LOAD if used |
| **www.newcops.govt.nz** | Recruitment related | **CLICK** |
| Theme `bs_barrio_police` | Custom Drupal theme | **LOAD** |

---

## A. High privacy relevance

| Host / ID | Role | Tag | Notes |
|-----------|------|-----|--------|
| **www.googletagmanager.com/gtag** | GA4 **G-D3P3CRCCXE** | **LOAD** | `allow_ad_personalization_signals: false` in gtag config |
| Drupal `google_analytics` | Module settings | **CONFIG** | trackOutbound, trackMailto, trackTel, trackDownload + extension list |
| **GTM-KXS4K6P** | GTM | commented out in dump | May still exist elsewhere |
| **Facebook** | `fb:app_id` **537614739774441**, domain verification | **CONFIG** | Meta platform association; full pixel load not confirmed in head snippet alone |
| **cdn.jsdelivr.net** | Bootstrap 5.2.0 bundle | **LOAD** |
| jQuery 4.0.0 | Drupal core vendor | **LOAD** first-party path |

### Sensitive context

Users may enter **crime/incident details** on linked forms. Analytics on the **landing page** still fires for page views; form destinations need separate DPIA-style review by Police (not invent outcomes here).

---

## B. Comparison (public sector)

| Site | Analytics | Notes |
|------|-----------|--------|
| Health NZ Find a service | GTM-NQDRN6WT + Hotjar + Mapbox | Health + location |
| Auckland Council | GTM-MCLW6DXF etc. | Coveo/Hotjar on some pages |
| **Police 105** | **GA4 G-D3P3CRCCXE** | Drupal 11; forms subdomains |

---

## Purpose diagram

```text
[Browser] → police.govt.nz/use-105
              ├─ gtag G-D3P3CRCCXE (ad personalization off)
              ├─ Bootstrap (jsdelivr)
              ├─ Facebook app_id meta
              └─ report flows → forms.police.govt.nz / webforms / call 105
                    emergency → 111 (not this page)
```

---

## One concrete risk

Assuming non-emergency reporting is “offline/private”: the landing page still uses **Google Analytics** (with download/tel/mailto tracking enabled in module config). Sensitive reports should use **official** 105/online channels; agents must not collect report narratives into Fable memory by default.

**Related:** Health NZ, Shielded/WR patterns for safety-adjacent UX.
