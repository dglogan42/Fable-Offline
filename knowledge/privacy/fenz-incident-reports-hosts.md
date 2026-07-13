# FENZ Incident reports — third-party host map

**Compiled:** 2026-07-12  
**URL:** https://www.fireandemergency.nz/incidents-and-news/incident-reports/  
**Title:** Incident reports | Fire and Emergency New Zealand  
**Skill:** `privacy-host-map`  
**Not legal advice.**

---

## Verdict first

**Map only** — Silverstripe 5.4 FENZ public site. Analytics stack is **heavy**: **GTM-5CJ5CBS** + **GA4 G-BE91QQHSE8** + legacy **UA-26098074-2** (analytics.js) simultaneously. **Google Maps JavaScript API** with browser key `AIzaSyB2C5Jyx-Xakk9oT2E2gq3kp71zh7DFP8U`. **Incapsula** WAF/bot script. Facebook domain verification. Social: YouTube, Facebook, Instagram, Twitter/X. Related first-party tools: firepermit.nz, checkitsalright.nz, portal.fireandemergency.nz.

Service content: `knowledge/public-safety/fenz-incident-reports.md`.

---

## First-party / FENZ family

| Host | Role | Tag |
|------|------|-----|
| **www.fireandemergency.nz** | Main site | **LOAD** |
| **portal.fireandemergency.nz** | Staff portal / intranet | **CLICK** |
| **www.firepermit.nz** | Fire permits | **CLICK** |
| **www.checkitsalright.nz** | Outdoor burning / fire risk check | **CLICK** |
| **firehazard.nz** | Linked hazard tool | **CLICK** |
| **vr.escapemyhouse.co.nz** | Escape plan VR experience | **CLICK** |

---

## A. High privacy relevance

| Host / ID | Role | Tag | Notes |
|-----------|------|-----|--------|
| **www.googletagmanager.com** | GTM **GTM-5CJ5CBS** | **LOAD** | |
| **www.googletagmanager.com/gtag** | GA4 **G-BE91QQHSE8** | **LOAD** | |
| **www.google-analytics.com/analytics.js** | Universal Analytics **UA-26098074-2** | **LOAD** | Legacy UA still present alongside GA4 |
| **maps.googleapis.com** | Google Maps API v3 | **LOAD** | Key in page: `AIzaSyB2C5Jyx-…` (browser-exposed; restrict by HTTP referrer in GCP) |
| **Incapsula** `/_Incapsula_Resource…` | WAF / bot management | **LOAD** | Imperva family |
| Facebook domain verification | `q0hfvzs6ldp5d8x1bl7yqp4izy1m9e` | **CONFIG** | |
| Social CLICK | youtube, facebook, instagram, twitter | **CLICK** | Footer |

### Stack note

Running **GTM + GA4 + UA** on one page is redundant tracking and increases third-party surface. Map key exposure is normal for Maps JS but should be **HTTP-referrer restricted**.

---

## B. Comparison (emergency / safety sector)

| Site | Analytics | Maps |
|------|-----------|------|
| NZ Police 105 | GA4 G-D3P3CRCCXE | — |
| Health NZ Find a service | GTM-NQDRN6WT + Hotjar | Mapbox |
| **FENZ incident reports** | **GTM + GA4 + UA** | **Google Maps** |

---

## Purpose diagram

```text
[Browser] → fireandemergency.nz (incident reports)
              ├─ GTM-5CJ5CBS
              ├─ gtag G-BE91QQHSE8
              ├─ UA-26098074-2 (analytics.js)
              ├─ Google Maps API (key in page)
              ├─ Incapsula
              └─ related: firepermit.nz / checkitsalright.nz / MetService
```

---

## One concrete risk

Public **incident browsing** still loads **three Google analytics layers** plus **Maps**. Users checking fires/incidents may not expect multi-product Google measurement; map API key must not be unrestricted (quota abuse risk for FENZ).

**Related:** `nz-police-105-hosts.md`, `healthnz-find-a-service-hosts.md`.
