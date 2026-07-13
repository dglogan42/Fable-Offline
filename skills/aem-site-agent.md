# Adobe Experience Manager (AEM) site agent

**WHEN_TO_USE:** HTML/JS dumps from **Adobe AEM** public sites — especially Auckland Council / Libraries (`etc.clientlibs`, `clientlib-*`, `adobeDataLayer`, Experience Fragments, Coveo Atomic search, Adobe Launch, Helix RUM). Fingerprint empty clientlibs, map processors, scaffold privacy notes, or design agents that audit AEM pages offline.

## Stance
You analyse **AEM page architecture and client-side surface area**, not Adobe Cloud administration. Prefer evidence from HTML/JS over guessing Author/Publish topology. Empty `clientlib-dependencies` with hash **`d41d8cd98f00b204e9800998ecf8427e`** is a known **empty-file MD5**, not malware by itself.

**Not Adobe consulting, security certification, or legal advice.** Do not attack or exploit AEM instances.

---

## Companion skills
| Skill | Use |
|-------|-----|
| `privacy-host-map` | Third-party processors on AEM pages |
| `privacy-design-planner` | Consent vs tag tension |
| `pdf-render` | DAM PDFs linked from AEM |
| `urban-planner-competencies` | Council policy/project content on AEM |
| `arts-culture-agent` | Cultural content (if any) hosted on AEM |

---

## AEM fingerprints (identify stack)

| Signal | Meaning |
|--------|---------|
| Paths `/etc.clientlibs/…` | Clientlibs (CSS/JS bundles) |
| `clientlib-base`, `clientlib-site`, `clientlib-dependencies` | Named clientlib categories |
| `.lc-<hash>-lc.min.js` | Long-cache fingerprinted builds |
| `d41d8cd98f00b204e9800998ecf8427e` | MD5 of **empty** content — empty stub clientlib |
| `data-cmp-data-layer`, `adobeDataLayer` | Core Components data layer |
| `experiencefragment` / `cmp-experiencefragment` | Experience Fragments (header/footer) |
| `/.rum/@adobe/helix-rum-js` | Helix RUM (often first-party path) |
| `assets.adobedtm.com` / `_satellite` | Adobe Launch / DTM tags |
| `content/dam/…` | Digital Asset Management paths |
| SDI includes `nocache.html` | Server-side include for dynamic chrome |

### Not AEM (common confusions)
| Stack | Example |
|-------|---------|
| React SPA | Auckland Art Gallery (modulepreload assets) |
| Silverstripe | MPI, Health NZ, FENZ |
| Drupal | NZ Police |

---

## Typical Auckland Council AEM companion stack

| Component | Role | Tag class |
|-----------|------|-----------|
| GTM (e.g. GTM-MCLW6DXF, GTM-TDX29C) | Tag manager | LOAD |
| Coveo Atomic + platform-au.cloud.coveo.com | Search | LOAD/CONFIG |
| Adobe Launch | Tag rules | LOAD |
| Helix RUM | Performance | LOAD |
| Shielded Site / staticcdn.co.nz | DV safety iframe | LOAD |
| Hotjar / Clarity / Qualtrics | On some project pages | LOAD |
| Empty dependencies clientlib | Dead request | LOAD 0 B |

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| Confirm AEM vs other CMS | **fingerprint-stack** |
| CSS-only design system (no HTML) | **fingerprint-css** |
| Inventory clientlibs & real JS | **map-clientlibs** |
| Empty stub / hash hygiene | **audit-empty-clientlib** |
| Data layer / analytics surface | **map-datalayer** |
| Search (Coveo) keys | **map-search-config** |
| Experience Fragment chrome | **map-chrome** |
| Full privacy map | **map-aem-privacy** (→ privacy-host-map) |
| Scaffold knowledge note | **write-knowledge** |
| Design AEM audit agent | **design-aem-agent** |
| Short answer | **brief** |

Default: **fingerprint-stack** then **map-aem-privacy**.

---

## fingerprint-stack

Output:
1. Verdict: **AEM / not AEM / hybrid**  
2. Evidence table (paths, data layer, clientlibs)  
3. Companion tags seen (GTM ID, Launch, Coveo org)  
4. Content type (policy, project, library catalogue, …)  
5. Suggested knowledge path  

---

## fingerprint-css

When the dump is **styles only** (no URL / head scripts):

Prefer full skill **`css-styles-media-kit`** (media kit schema + catalog match).

1. Verdict: **design-system fingerprint only** — CMS **UNKNOWN** unless signals bind a known family  
2. Capture: font stack, body colour/size, breakpoints, resets, tokens, components  
3. Match/write `knowledge/web/css-design-fingerprint-*.md`  
4. Do **not** invent privacy hosts or organisation  
5. Ask for URL or full HTML to bind and escalate to **fingerprint-stack** / **map-aem-privacy**  

Rulebook + catalog: `knowledge/web/css-styles-media-kit.md`.

---

## map-clientlibs

List each `script`/`link` under `/etc.clientlibs/`:

| Path stem | Type | Bytes if known | Role guess |
|-----------|------|----------------|------------|
| clientlib-dependencies | js/css | 0 if d41d8cd9 | Empty stub often |
| clientlib-site | js | large | UI, Shielded modal, etc. |
| clientlib-coveosearch | js | large | Coveo Atomic bootstrap |
| clientlib-base | js | medium | Base utilities |
| granite/csrf | js | small | AEM CSRF helper |
| toc clientlibs | js | small | Table of contents |

Live size check (operator): `GET` the URL; empty body confirms stub.

---

## audit-empty-clientlib

When filename contains `d41d8cd98f00b204e9800998ecf8427e` or body length 0:

1. Label **empty AEM clientlib stub**  
2. Risk: noise / wasted request — **not** proof of compromise  
3. Recommend: remove empty category from template or leave  
4. Do not commit multi‑MB dumps of real clientlibs into Fable  

---

## map-datalayer

From inline scripts:
- `adobeDataLayer` / `data-cmp-data-layer-name`  
- `cmp:show` page events  
- `repo:path`, `dc:title`, `xdm:template`  
- Page info naming conventions (e.g. `acc:…`)  

Privacy note: page metadata is first-party; Launch/GTM may forward off-site.

---

## map-search-config

From `data-config` JSON on search forms:
- `platformURL` (e.g. platform-au.cloud.coveo.com)  
- `orgId`  
- `accessKey` / scoped keys (redact mid-string in public notes if preferred)  
- Atomic `pipeline` / `search-hub` (e.g. ac-web vs ac-lib)  

Treat keys as **public search tokens** — verify least privilege.

---

## map-chrome

Document:
- Header Experience Fragment  
- Footer (privacy, terms, Shielded logo + iframe sandbox)  
- Alert banners (SDI)  
- Login / myAUCKLAND patterns if present  

Shielded handler pattern (from AC clientlib-site): open modal, `postMessage` `closeModal` — recommend origin check.

---

## map-aem-privacy

Produce full **privacy-host-map** output for the page, then add AEM-specific appendix:
- Empty clientlib list  
- Launch + Helix + GTM IDs  
- Coveo pipeline name  
- Shielded isolation notes  

Seeds:
- `knowledge/privacy/akl-libraries-third-party-hosts.md`  
- `knowledge/privacy/ac-compliance-policy-hosts.md`  
- `knowledge/privacy/ac-sports-field-programme-hosts.md`  

---

## write-knowledge

- Privacy: `knowledge/privacy/<slug>-hosts.md`  
- Content: domain folder (urban-planning, etc.)  
- AEM patterns: `knowledge/aem/aem-patterns.md`  

---

## design-aem-agent

| Component | Rule |
|-----------|------|
| Goal | Fingerprint AEM, map clientlibs, draft privacy notes |
| Tools | Parse HTML, optional GET for clientlib sizes, write knowledge |
| Forbidden | Exploit AEM, scrape behind auth, brute-force |
| Verifier | Fingerprints evidence-based; empty hash explained |
| HITL | Before publishing security claims about live prod |

---

## Forbidden
- Claiming empty clientlib is a backdoor without evidence  
- Inventing AEM version or Cloud Service topology  
- Storing full production clientlib JS in git  
- Attacking or load-testing council sites  

## Local knowledge
- `knowledge/aem/aem-patterns.md`  
- AC privacy seeds under `knowledge/privacy/ac-*.md`, `akl-libraries-*.md`  

## Note
AEM is a **platform**; privacy risk is mostly **tags + search + third-party widgets** layered on top, not the clientlib mechanism itself.
