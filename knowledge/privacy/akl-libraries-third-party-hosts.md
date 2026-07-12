# Auckland Libraries — third-party host / privacy map

**Compiled:** 2026-07-12  
**Page reviewed:** https://www.aucklandlibraries.govt.nz/en/guide-to-using-the-library/search-library-catalogue.html  
**Title:** Searching the library catalogue  
**Stack:** Adobe AEM (`etc.clientlibs`), Coveo Atomic search, Adobe Launch, GTM, Shielded Site footer widget  
**Purpose:** Offline privacy / host hygiene note for Fable.  
**Skill:** `privacy-host-map` (`skills/privacy-host-map.md`) — use this file as local knowledge when running `/privacy` or `--automate privacy-host-map`.  
**Not legal advice.** Re-check live Network tab and current privacy notices before relying on this map.

---

## Method

1. Static HTML dump of the guide page (head scripts, footer, search config).  
2. Live fetch of first-party clientlibs (sizes as of compile date):  
   - `clientlib-dependencies…d41d8cd9…js` → **0 bytes** (empty AEM stub)  
   - `clientlib-site…` → ~446 KB (UI + Shielded modal)  
   - `clientlib-coveosearch…` → ~572 KB (Coveo Atomic bootstrap)  
   - `clientlib-base…`, Granite CSRF, TOC clientlibs  
3. Host strings classified as **LOAD / CONFIG / CLICK / BUNDLE** (see legend).

### Legend

| Tag | Meaning |
|-----|---------|
| **LOAD** | Browser can load resource on this page (script, iframe, img, stylesheet link) |
| **CONFIG** | Endpoint in page config (e.g. search API) |
| **CLICK** | Outbound link or secondary product path (user-initiated) |
| **BUNDLE** | Host string inside minified vendor JS (docs/examples) — **not proof of a live call** |

### First-party (excluded from third-party list)

- `www.aucklandlibraries.govt.nz` / `aucklandlibraries.govt.nz`  
- `www.aucklandcouncil.govt.nz` / `aucklandcouncil.govt.nz` (same organisation family)  
- Relative paths: `/etc.clientlibs/…`, `/content/…`, `/.rum/…` (Helix RUM is Adobe code **served from** the library host)

---

## A. High privacy relevance (active or likely on page load)

| Host | Role | Tag | Notes |
|------|------|-----|--------|
| **www.googletagmanager.com** | Google Tag Manager `GTM-TDX29C` | LOAD | Can inject further tags/pixels; cookie behaviour depends on container config (not in HTML alone). |
| **assets.adobedtm.com** | Adobe Experience Platform Launch | LOAD | Tag manager; page calls `_satellite.pageBottom()`. Path under `db549a90b710/…`. |
| **platform-au.cloud.coveo.com** | Coveo Search API (AU region) | CONFIG | `orgId=aucklandcouncilproductionv7ckem2o`; **public search access key** in HTML `data-config` (must be search-scoped only). |
| **static.cloud.coveo.com** | Coveo Atomic UI assets | LOAD | Loaded via coveo clientlib (`atomic.esm.js`). |
| **analytics.cloud.coveo.com** | Coveo analytics | BUNDLE / likely runtime | Common Coveo beacon host; confirm in Network on live visit. |
| **shielded.co.nz** | Shielded Site branding | LOAD | Footer logo: “Activate Shielded on this website”. |
| **staticcdn.co.nz** | Shielded Site widget | LOAD (iframe) | `310×455` iframe; `sandbox="allow-forms allow-scripts allow-same-origin allow-popups"`. Safety content runs in **this origin**, not the library origin. |
| **First-party `/.rum/@adobe/helix-rum-js@^2/…`** | Adobe Helix RUM | LOAD | Performance beacons; same-site path, Adobe vendor code. |

### Adobe data layer (first-party JS)

Inline + ACDL clientlibs push to `adobeDataLayer` / `adobeDataLayer`: page title, description, repo path (`/content/aclib/en/...`), template, language, `cmp:show` events. Launch/GTM may forward events off-site.

### Empty clientlib stub

`/etc.clientlibs/aucklandcouncil/clientlibs/clientlib-dependencies.lc-d41d8cd98f00b204e9800998ecf8427e-lc.min.js`  
Hash `d41d8cd98f00b204e9800998ecf8427e` = MD5 of empty string. **No code, no privacy impact** beyond an extra request.

---

## B. Product / research ecosystems (mostly click or secondary)

| Host | Role | Tag |
|------|------|-----|
| **aucklandcouncil.syd1.qualtrics.com** | Qualtrics feedback (Sydney AU) | CLICK / embed candidate |
| **aucklandlibraries.idm.oclc.org** | OCLC identity / library login ecosystem | CLICK |
| **search.ebscohost.com** | EBSCO databases | CLICK / site JS |
| **research.ebsco.com**, **support.ebsco.com** | EBSCO product / support | CLICK |
| **www.worldbookonline.com** | World Book e-resource | CLICK |
| **www.clarityenglish.com** | Clarity English | CLICK |
| **documentation.iii.com** | Innovative / ILS vendor docs | CLICK |
| **heritageetal.blogspot.com** | Content blog link | CLICK |

---

## C. Social / media

| Host | Role | Tag |
|------|------|-----|
| **www.facebook.com** | Social | CLICK / site bundle |
| **twitter.com** | Social (X) | site bundle |
| **www.linkedin.com** | Social | CLICK / bundle |
| **www.tiktok.com** | Social | site bundle |
| **www.youtube.com** | Video | CLICK / bundle |
| **soundcloud.com** | Audio | CLICK |

Presence in `clientlib-site` often means shared chrome or share widgets — not always first-paint loads.

---

## D. Government / policy (usually not commercial trackers)

| Host | Role | Tag |
|------|------|-----|
| **www.govt.nz** | NZ Government portal | CLICK |
| **www.aucklandcouncil.govt.nz** | Privacy policy, T&Cs | CLICK |

Official privacy pointer from footer: https://www.aucklandcouncil.govt.nz/en/privacy-policy.html  

---

## E. Bundle noise (do not treat as confirmed trackers)

Strings only inside minified vendor JS (docs, licenses, examples) unless Network proves a request:

- `docs.coveo.com` · `github.com` · `bit.ly` · `day.js.org` · `redux-toolkit.js.org` · `stenciljs.com` · `www.w3.org` · `stuk.github.io` · `acrobatservices.adobe.com` · `schema.org`

---

## Host map (purpose view)

```text
[Browser] → aucklandlibraries.govt.nz  (AEM HTML + clientlibs + Helix RUM path)
              │
              ├─→ assets.adobedtm.com          Adobe Launch tags
              ├─→ www.googletagmanager.com     GTM-TDX29C → (dynamic children)
              │
              ├─→ platform-au.cloud.coveo.com  Search queries / tokens
              ├─→ static.cloud.coveo.com       Atomic UI
              ├─→ analytics.cloud.coveo.com    Search analytics (likely)
              │
              ├─→ shielded.co.nz               Logo asset
              └─→ staticcdn.co.nz              Shielded safety iframe (sandboxed)

Optional / on interaction:
              ├─→ Qualtrics (syd1)             Feedback
              ├─→ OCLC idm / EBSCO / …         Research & account ecosystems
              └─→ Social (FB, X, LI, TT, YT)   Share / follow
```

---

## Shielded Site integration (privacy tension)

| Aspect | Detail |
|--------|--------|
| **UI** | Footer `#shielded-logo` opens `.shielded-modal` with iframe → `https://staticcdn.co.nz` |
| **Site JS** | `clientlib-site` adds `.open` on click; listens for `postMessage` `data === "closeModal"` (**no `event.origin` check** — low impact: closes modal only) |
| **Isolation** | Sandboxed iframe; parent tags do **not** automatically see iframe DOM |
| **Residual risk** | Parent-page GTM/Launch/Coveo still observe the **library page visit**; may log modal clicks if containers listen for `#shielded-logo` events (config not in HTML) |
| **Iframe storage** | `allow-same-origin` allows the widget origin its own cookies/storage inside the frame |

For a strict reading of a domestic-violence safety affordance: **third-party tag managers on the parent page** are the main systemic tension; the Shielded iframe is a separate, intentional third party.

---

## Storage / cookies (signals only — not a live capture)

| Mechanism | Where |
|-----------|--------|
| GTM / Adobe Launch | Typically first- and third-party cookies (config-dependent) |
| Coveo | `localStorage` / `sessionStorage` / cookies referenced in bundle |
| AEM CSRF | Cookie/header pattern for authenticated POSTs |
| Shielded iframe | Own-origin storage possible under sandbox |

Definitive cookie table requires DevTools → Network / Application on a live visit.

---

## Coveo public search key (hygiene)

Embedded in search form `data-config` (example observed in dump):

- `platformURL`: `https://platform-au.cloud.coveo.com`  
- `accessKey`: `xx691cbe06-…` (public page source — treat as **semi-public**)  
- `orgId`: `aucklandcouncilproductionv7ckem2o`  
- Atomic: `pipeline="ac-lib"`, `search-hub="ac-lib"`

**Required hygiene:** key must be search-only (no admin/index write), rate-limited, sources restricted. Not a “leaked password” pattern if correctly scoped — still rotate if privileges are wrong.

---

## Practical checklist

1. Review GTM `GTM-TDX29C` and Adobe Launch for consent gating vs fire-on-all-pages.  
2. Confirm Coveo key privileges and query-log retention.  
3. Prefer not attaching analytics goals to `#shielded-logo` if avoiding “safety tool opened” signals.  
4. Verify cookie/consent UX against NZ Privacy Act practice and Auckland Council privacy policy.  
5. Processors to document for users (as used): **Google, Adobe, Coveo, Shielded/staticcdn, Qualtrics, OCLC/EBSCO** (and social destinations if linked).

---

## Related Fable artifacts

- Empty clientlib review: AEM stub hash `d41d8cd9…` = empty body.  
- Shielded CSS class pattern (`.shielded-page` 310×420-class widget) matches iframe dimensions used here.  
- Real UI logic lives in **`clientlib-site`** and **`clientlib-coveosearch`**, not the empty dependencies file.

---

## Sources

- HTML snapshot of catalogue search guide page (user-supplied dump, 2026-07-12 session).  
- Live GETs of AEM clientlibs from `www.aucklandlibraries.govt.nz`.  
- Public footer links: Shielded logo, Council privacy/terms, govt.nz.

**Not legal advice. Not a penetration test. Snapshot may drift as tags and clientlib hashes change.**
