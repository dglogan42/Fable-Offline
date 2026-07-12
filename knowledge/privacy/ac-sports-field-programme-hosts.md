# Auckland Council Sports field capacity development programme — host map

**Compiled:** 2026-07-12  
**URL:** https://www.aucklandcouncil.govt.nz/en/plans-policies-bylaws-reports-projects/our-projects/auckland-wide-projects/sports-field-capacity-development-programme.html  
**Title:** Sports field capacity development programme  
**Skill:** `privacy-host-map`  
**Not legal advice.** This dump is **richer** in session-replay / UX analytics than the Compliance Policy HTML snapshot.

---

## Verdict first

**Map only / partially verified** — AEM project page with standard AC stack (**GTM-MCLW6DXF**, Adobe Launch, Coveo Atomic, Helix RUM, Shielded) **plus** Microsoft **Clarity**, **Hotjar** (site id **2128290**), **GA4 gtag G-PNKQX5MDKC**, **YouTube** iframe API, and **Qualtrics** feedback button / Site Intercept. Programme substance: `knowledge/urban-planning/ac-sports-field-capacity-programme.md`.

---

## A. High privacy relevance (LOAD / CONFIG)

| Host / ID | Role | Tag | Notes |
|-----------|------|-----|--------|
| **www.googletagmanager.com** | GTM **GTM-MCLW6DXF** | **LOAD** | Same container as Compliance Policy page |
| **www.googletagmanager.com/gtag** | GA4 **G-PNKQX5MDKC** | **LOAD** | Additional gtag alongside GTM |
| **assets.adobedtm.com** | Adobe Launch + rule packages | **LOAD** | Includes extra `RC…-source.min.js` rule |
| **/.rum/@adobe/helix-rum-js@^2** | Helix RUM | **LOAD** | First-party path |
| **static.cloud.coveo.com** | Coveo Atomic v2 ESM | **LOAD** | Search UI |
| **platform-au.cloud.coveo.com** | Coveo Search API | **CONFIG** | Via header search (typical AC) |
| **www.clarity.ms** / **scripts.clarity.ms** | Microsoft Clarity | **LOAD** | Project tag **`lri629brr9`** — session heatmaps/replay class |
| **static.hotjar.com** / **script.hotjar.com** | Hotjar | **LOAD** | **hotjar-2128290** — session recording / surveys class |
| **www.youtube.com** | YouTube iframe API / widgetapi | **LOAD** | Video embed capability |
| **siteintercept.qualtrics.com** / **community.qualtrics.com** | Qualtrics feedback | **LOAD** | Side “Feedback” tab UI in dump |
| **shielded.co.nz** / **staticcdn.co.nz** | Shielded Site | **LOAD** | Footer pattern (if present in full page) |
| Empty `clientlib-dependencies…d41d8cd9…` | AEM stub | **LOAD** | 0-byte pattern |

### Sensitive-class tools

| Tool | Privacy class |
|------|----------------|
| **Hotjar** | Session replay / funnels — higher sensitivity than pageviews alone |
| **Clarity** | Session replay / heatmaps — similar class |
| **Qualtrics** | Explicit feedback capture when opened |
| **YouTube** | Third-party cookies/player when embeds play |

---

## B. Comparison with other AC pages in Fable knowledge

| Page | GTM | Extra UX analytics |
|------|-----|--------------------|
| Libraries catalogue | GTM-TDX29C | Coveo ac-lib focus |
| Compliance Policy | GTM-MCLW6DXF | Coveo ac-web |
| **Sports field programme** | GTM-MCLW6DXF | **+ Clarity + Hotjar + GA4 gtag + YouTube + Qualtrics** |

---

## Purpose diagram

```text
[Browser] → aucklandcouncil.govt.nz (sports field programme)
              ├─ GTM-MCLW6DXF + gtag G-PNKQX5MDKC
              ├─ Adobe Launch + Helix RUM
              ├─ Coveo Atomic (static.cloud.coveo.com)
              ├─ Clarity (lri629brr9)
              ├─ Hotjar (2128290)
              ├─ YouTube iframe API
              ├─ Qualtrics Feedback button
              └─ Shielded (staticcdn.co.nz) when footer present
```

---

## One concrete risk

A routine **open-space / sports infrastructure** project page can still load **session-replay vendors (Hotjar, Clarity)** and feedback intercepts. Topic (sports fields) does not imply low tracking.

**Related:** `ac-compliance-policy-hosts.md`, `akl-libraries-third-party-hosts.md`.
