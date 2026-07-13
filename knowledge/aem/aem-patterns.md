# Adobe AEM — public site patterns (Fable)

**Skill:** `aem-site-agent`  
**Primary examples:** Auckland Council / Auckland Libraries AEM properties  
**Not Adobe consulting advice.**

---

## Fingerprint cheat-sheet

| Path / signal | Notes |
|---------------|--------|
| `/etc.clientlibs/.../clientlib-*.lc-HASH-lc.min.js` | Clientlib bundle |
| Hash `d41d8cd98f00b204e9800998ecf8427e` | Empty file MD5 |
| `adobeDataLayer` / `data-cmp-data-layer` | Core Components analytics hooks |
| `experiencefragment` | Header/footer XF |
| `/.rum/@adobe/helix-rum-js@^2` | Helix RUM |
| `assets.adobedtm.com` + `_satellite.pageBottom()` | Adobe Launch |
| `content/dam/` | DAM assets |

### CSS-only design fingerprints (no CMS assumed)

When the dump is **styles only**, store under `knowledge/web/` and do **not** invent a host map.

| Fingerprint note | Signals |
|------------------|---------|
| `knowledge/web/css-design-fingerprint-helvetica-grey.md` | Helvetica Neue + Segoe WP + Nimbus Sans L; body `#424242`; 1.125rem / .95rem mid; 45–60 em/rem breakpoints; `*` reset + border-box |
| `knowledge/web/css-design-fingerprint-tiktok-ui.md` | TikTok Text/Display; `#fe2c55`; `--ttam-*`; midas grid; dark `theme-mode` — **first-party TikTok UI**, not pixel-on-publisher |

**Helvetica-grey sample origin is UNKNOWN** until a URL is bound. TikTok UI sample is high-confidence TikTok product CSS.

---

## Typical clientlib roles (AC)

| Name | Typical role |
|------|----------------|
| clientlib-dependencies | Often **empty** stub |
| clientlib-site | Site UI (menus, Shielded modal open/close) |
| clientlib-coveosearch | Coveo Atomic loader |
| clientlib-base | Shared utilities |
| granite/csrf | CSRF token helper |

---

## Companion stack (AC)

| Product | Examples in knowledge |
|---------|----------------------|
| GTM | GTM-MCLW6DXF (web), GTM-TDX29C (libraries) |
| Coveo | org `aucklandcouncilproductionv7ckem2o`; pipelines `ac-web`, `ac-lib` |
| Shielded | logo shielded.co.nz; iframe staticcdn.co.nz |
| Optional | Hotjar, Clarity, Qualtrics, YouTube on project pages |

---

## Privacy knowledge seeds

- `knowledge/privacy/akl-libraries-third-party-hosts.md`  
- `knowledge/privacy/ac-compliance-policy-hosts.md`  
- `knowledge/privacy/ac-sports-field-programme-hosts.md`  

---

## Empty clientlib audit note

Empty dependencies clientlib = **noise**, not a payload. Prefer fixing template categories over treating as an incident.

---

## Agent workflow

```text
HTML dump
  → aem-site-agent fingerprint-stack
  → map-clientlibs (+ optional live byte sizes)
  → map-aem-privacy (privacy-host-map)
  → write knowledge/privacy/*-hosts.md
  → domain skill for page content (urban-planner, etc.)
```
