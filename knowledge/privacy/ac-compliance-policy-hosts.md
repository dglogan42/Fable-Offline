# Auckland Council Compliance Policy page — third-party host map

**Compiled:** 2026-07-12  
**URL:** https://www.aucklandcouncil.govt.nz/en/plans-policies-bylaws-reports-projects/our-policies/compliance-policy.html  
**Title:** Compliance Policy (Kaupapa Here Tautukunga)  
**Stack:** Adobe AEM (`etc.clientlibs`), Coveo Atomic search, Adobe Launch, GTM, Shielded Site  
**Skill:** `privacy-host-map`  
**Not legal advice.** Compare with Libraries site map (`akl-libraries-third-party-hosts.md`) — same family, different GTM container and richer Coveo key set.

---

## Verdict first

**Map only (static HTML)** — standard Auckland Council **AEM policy page** with **GTM-MCLW6DXF**, Adobe Launch, Helix RUM, Coveo search (org `aucklandcouncilproductionv7ckem2o`, pipeline `ac-web`), empty AEM clientlib stub, and **Shielded Site** footer iframe. Page content is a **principles-based compliance policy** summary (under review as of site text). Policy substance: `knowledge/urban-planning/ac-compliance-policy.md`.

---

## First-party

- `www.aucklandcouncil.govt.nz` / relative `/etc.clientlibs/…`, `/content/…`, `/.rum/…`  
- Sister CCO links in chrome (AT, Libraries, Watercare, etc.) — **CLICK** when used  

---

## A. High privacy relevance

| Host / ID | Role | Tag |
|-----------|------|-----|
| **www.googletagmanager.com** | GTM **`GTM-MCLW6DXF`** | **LOAD** |
| **assets.adobedtm.com** | Adobe Launch `launch-cfce880f62ba.min.js` | **LOAD** |
| **platform-au.cloud.coveo.com** | Coveo Search API (AU) | **CONFIG** |
| **static.cloud.coveo.com** | Atomic UI (via clientlib) | **LOAD** (typical) |
| **First-party `/.rum/@adobe/helix-rum-js@^2/…`** | Adobe Helix RUM | **LOAD** |
| **shielded.co.nz** | Shielded logo | **LOAD** |
| **staticcdn.co.nz** | Shielded widget iframe 310×455 | **LOAD** |
| Empty `clientlib-dependencies…d41d8cd9…js` | AEM empty stub | **LOAD** (0 bytes) |

### Coveo config (public search keys in HTML)

| Field | Value (from dump) |
|-------|-------------------|
| `orgId` | `aucklandcouncilproductionv7ckem2o` |
| `platformURL` | `https://platform-au.cloud.coveo.com` |
| `accessKey` | `xx9f4cd9d0-…` (main web) |
| Scoped keys | parks accommodation, submissions, paths, cemeteries, featured paths, etc. |
| Atomic | `pipeline="ac-web"`, `search-hub="ac-web"` |

Treat keys as **semi-public search tokens** — verify least privilege in Coveo console.

### Diff vs Libraries catalogue page

| Item | Libraries dump | This Compliance Policy page |
|------|----------------|------------------------------|
| GTM | `GTM-TDX29C` | **`GTM-MCLW6DXF`** |
| Search pipeline | `ac-lib` (libraries) | **`ac-web`** (council web) |
| Coveo keys | Single access key in dump | **Multiple scoped** keys |
| Shielded | Present | Present (same pattern) |
| Adobe Launch path | Same container family | Same `db549a90b710/…` launch |

---

## B. Social / footer CLICK

Facebook, X/Twitter, LinkedIn, TikTok, Instagram (aklcouncil) — user-initiated.

---

## C. Shielded tension

Same as other AC properties: parent-page **GTM + Launch + Coveo** while DV safety widget loads in sandboxed iframe. Agreement not required to load tags on this page.

---

## Purpose diagram

```text
[Browser] → aucklandcouncil.govt.nz (Compliance Policy HTML)
              ├─ GTM-MCLW6DXF
              ├─ Adobe Launch + Helix RUM
              ├─ Coveo ac-web (platform-au + Atomic)
              └─ Shielded → staticcdn.co.nz
```

---

## One concrete risk

Assuming a **policy/compliance** page is “low tracking” because the topic is regulatory: the **same marketing/analytics stack** as other AC pages still loads; search keys and GTM fire independently of reading the Compliance Policy text.

**Related:** `knowledge/privacy/akl-libraries-third-party-hosts.md`, skill `privacy-host-map`.
