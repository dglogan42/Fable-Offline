# Health NZ Te Whatu Ora — Find a service host map

**Compiled:** 2026-07-12  
**URL:** https://www.healthnz.govt.nz/hospitals-services/services-support  
**Title:** Find a service  
**Agency:** Health New Zealand | Te Whatu Ora  
**CMS:** Silverstripe CMS 6.2  
**Skill:** `privacy-host-map`  
**Not legal or medical advice.**

---

## Verdict first

**Map only / partially verified** — national **health service directory** page with location selector, service type links (hospitals, ED, GP, dentists, pharmacies, etc.), **Mapbox** public token for maps, **GTM-NQDRN6WT**, **Hotjar** (hjid **3700571**), **Women’s Refuge Shield** CSS, **Reoako** te reo Māori API (`api.reoako.nz`), Vimeo preconnects, and first-party health apps (`my.health.nz`). Empty search API keys in inline config (`search_apiKey = ''`) suggest server-side or deferred search wiring.

Service content: `knowledge/health/healthnz-find-a-service.md`.

---

## First-party / health family

| Host | Role | Tag |
|------|------|-----|
| **www.healthnz.govt.nz** | Main public site | **LOAD** |
| **www.tewhatuora.govt.nz** | Brand / jobs related | **CLICK** |
| **my.health.nz** | My Health Record (external link) | **CLICK** |
| **workforce.identity.health.nz** | Workforce identity | **CLICK** |
| **jobs.tewhatuora.govt.nz** | Careers | **CLICK** |
| **hauoraaotearoa.sharepoint.com** | Staff intranet (linked for professionals) | **CLICK** |

---

## A. High privacy relevance

| Host / ID | Role | Tag | Notes |
|-----------|------|-----|--------|
| **www.googletagmanager.com** | GTM **GTM-NQDRN6WT** | **LOAD** | Distinct from AC/AAG containers |
| **static.hotjar.com** | Hotjar **3700571** | **LOAD** | Session analytics / UX class |
| **Mapbox** token `pk.eyJ1IjoidGV3aGF0dW9yYSIsImEiOiJjbHltZzRjMnowaWttMmlvanNndXJxbmV1In0.…` | Map tiles / geocoding for “use my location” | **CONFIG** | Public **pk.** token (browser-exposed by design); still scopes map usage to Mapbox account **tewhatuora** |
| **api.reoako.nz** | Reoako te reo translations | **LOAD**/runtime | `Authorization: Token` pattern in embedded client — API key in page bundle if configured |
| **Women’s Refuge Shield** CSS | `andrewandante/womens-refuge-shield` | **LOAD** | DV safety button pattern (related to Shielded-style tools) |
| **Vimeo** CDNs | Video preconnect | **LOAD**/potential |
| **www.gstatic.com** | Google static (often fonts/recaptcha-related) | **LOAD**/potential |
| Search config | `search_apiKey` / `search_engineName` **empty** in dump | CONFIG | Incomplete search backend in static HTML |

### Location / sensitive surface

Page offers **“Use my location”** and region pickers (Northland … Otago/Southland). Geolocation + Mapbox implies **location data** may leave the browser for map/search — higher sensitivity on a **health** site.

---

## B. Comparison

| Site | GTM | Session UX | Maps |
|------|-----|------------|------|
| Auckland Council sports field | MCLW6DXF | Hotjar + Clarity | — |
| AAG Forever Tomorrow | KCGVLXLM | Meta pixel | — |
| **Health NZ Find a service** | **NQDRN6WT** | **Hotjar 3700571** | **Mapbox pk.** + geolocation |

---

## Purpose diagram

```text
[Browser] → healthnz.govt.nz (Find a service)
              ├─ GTM-NQDRN6WT
              ├─ Hotjar 3700571
              ├─ Mapbox (tewhatuora account pk token)
              ├─ Reoako API (te reo)
              ├─ Women’s Refuge Shield CSS
              └─ Links → my.health.nz / hospitals / services
```

---

## One concrete risk

A **public service finder** combines **health intent** with **geolocation**, **Hotjar session tooling**, and **Mapbox**. Users searching for ED/GP/sexual health may not expect session analytics or map-provider processing of location queries.

**QR codes:** Page UI includes **“Get QR code”** for location-specific content (QR images may appear in captures). Treat as deep-links to the same site family unless decoded otherwise.

**Related:** Shielded/WR patterns on AC pages; do not confuse Health NZ GTM with Auckland Council GTM.
