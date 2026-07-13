# MPI Exporter Help page — host / stack map

**Compiled:** 2026-07-12  
**URL:** https://www.mpi.govt.nz/export/get-help-with-exporting  
**Title:** Exporter Help | NZ Government  
**Skill:** `privacy-host-map`  
**Not legal advice.** HTML dump was largely **CSS branch theming + Swiftype keyword meta**; network inventory may be incomplete vs live browser.

---

## Verdict first

**Map only / incomplete dump** — NZ Government **MPI** Silverstripe site. First-party base `https://www.mpi.govt.nz`. SEO enrichment via **Swiftype** meta tags (`class="swiftype"`). No GTM/Meta/Hotjar IDs found in this truncated dump — **do not assume zero analytics** until Network tab on live page. Service content: `knowledge/trade/mpi-exporter-help.md`.

---

## First-party

| Asset | Role | Tag |
|-------|------|-----|
| **www.mpi.govt.nz** | Origin, Silverstripe CMS 5.4 | **LOAD** |
| `/_resources/client/…` | Site images/CSS/JS (typical) | **LOAD** |

---

## Observed in dump

| Signal | Role | Tag |
|--------|------|-----|
| **Silverstripe CMS 5.4** | Generator meta | CONFIG |
| **Swiftype** keyword metas | Search/index enrichment (`data-type="enum"`) | CONFIG (on-page) |
| **robots** | `index, follow` | CONFIG |
| **theme-color** | `#95c11f` | — |
| Branch CSS (`.branch-mpi` / multi-branch) | Multi-site theming on shared platform | BUNDLE |

Hosts extracted from dump were essentially **www.mpi.govt.nz** only (incomplete body).

---

## Expected follow-ups (verify on live Network — not confirmed in dump)

Government Silverstripe sites often load some of:

- Google Analytics / GTM  
- Siteimprove / other accessibility crawlers  
- Consent banners  
- Form POST endpoints for contact  

Re-scan live page before claiming a full processor list.

---

## Comparison

| Site family | Stack flavour |
|-------------|----------------|
| Auckland Council AEM | GTM + Coveo + Adobe + often Hotjar/Clarity |
| AAG React | GTM + Meta + Securiti + reCAPTCHA |
| **MPI Silverstripe** (this dump) | First-party + Swiftype meta; analytics **unconfirmed** here |

---

## One concrete risk

Treating a **large HTML save that is mostly CSS** as a complete privacy audit. This capture under-represents scripts; always validate with DevTools Network on `mpi.govt.nz`.

**Related:** `knowledge/trade/mpi-exporter-help.md`.
