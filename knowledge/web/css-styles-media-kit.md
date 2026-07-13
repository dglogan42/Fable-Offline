# CSS styles media kit — web design rules & fingerprint catalog

**Skill:** `css-styles-media-kit`  
**Related:** `aem-site-agent` (fingerprint-css) · `privacy-host-map`  
**Fingerprints dir:** `knowledge/web/css-design-fingerprint-*.md`  

Framework for turning CSS into durable design-system notes and matching known UI families. Not a substitute for brand legal approval.

---

## Media kit template

See skill **kit-from-css** schema. Every fingerprint file should support that schema.

---

## Classification quick rules

| If you see… | Classify as… |
|-------------|---------------|
| MPL + `chrome://global/skin/media` + `.videocontrols` | **Browser chrome** (Firefox) |
| TikTok Font / `#fe2c55` / `--ttam-*` | **TikTok product UI** |
| `*-navigation` (egs, fortnite, unrealengine…) + 4.5rem + Inter | **Epic Games global nav** |
| Brutal + Titan One + MUI + `.epic-wf` | **Epic** (same family) |
| Helvetica Neue + grey `#424242` only | **Orphan** until URL |
| Ant Design chunks + empty `#root` | **SPA shell** — pair with app skill |

---

## Fingerprint catalog

| File | System | Confidence seed | Key signals |
|------|--------|-----------------|-------------|
| [css-design-fingerprint-helvetica-grey.md](css-design-fingerprint-helvetica-grey.md) | Orphan marketing/CMS | medium family / unknown site | Helvetica Neue, `#424242`, flex column body |
| [css-design-fingerprint-tiktok-ui.md](css-design-fingerprint-tiktok-ui.md) | TikTok product UI | high | TikTok Font, `#fe2c55`, `--ttam-*`, midas grid |
| [css-design-fingerprint-epic-brutal.md](css-design-fingerprint-epic-brutal.md) | Epic multi-product web | very high | `*-navigation`, 4.5rem, Inter, Brutal, Titan One, MUI, `.epic-wf` |
| [css-design-fingerprint-firefox-videocontrols.md](css-design-fingerprint-firefox-videocontrols.md) | Firefox media controls | very high | MPL, chrome://, `-moz-range-*`, `#00b6f0` progress |

Related product shell (not full fingerprint file yet): **MyFitnessPal** web — Inter + brand `#0066EE` + ~992px / 60px header (`knowledge/health/myfitnesspal.md`).

---

## Epic navigation registry (from fingerprint)

Shared: `display: flex; height: 4.5rem; font-family: Inter, sans-serif` on:

`edc-`, `egs-`, `eos-`, `epicgames-`, `fortnite-`, `rocketleague-`, `twinmotion-`, `fallguys-`, `realitycapture-`, `metahuman-`, `devportal-`, `unrealengine-`, `sac-`, `ssp-`, `kws-`, `supportkws-`, `quixel-` + `-navigation`.

---

## Firefox media control tokens (from fingerprint)

| Token role | Examples |
|------------|----------|
| Sizes | `--button-size` 30/40, `--track-size` 5/7, `--thumb-size` 13/16 |
| Focus | `--control-focus-outline: 2px solid #00ddff` |
| Progress | `#00b6f0` |
| Bar | `rgba(26, 26, 26, 0.8)` height 40px |

---

## Web design rules (agent normative)

1. Tokens before magic numbers  
2. Document font roles (display / UI / body / mono)  
3. Focus-visible for controls  
4. Touch-sized targets where `.touch` or mobile  
5. Honor contrast / reduced-motion prefs when present  
6. Separate **UA chrome** from **site CSS** in dumps  
7. Media queries catalogued, not ignored  
8. Confidence labels on attribution  
9. Escalate to HTML for hosts and CMS  
10. Write fingerprints under `knowledge/web/` with sample log  

---

## Workflow

```text
CSS paste
  → classify-css
  → kit-from-css (tables)
  → fingerprint-match / merge
  → write knowledge note
  → optional escalate-html → privacy-host-map
```

Automation: `workflows/css-styles-media-kit.json`

---

## Related app shells (not pure CSS fingerprints)

| Note | Path |
|------|------|
| Inkstone SPA | `knowledge/web/inkstone-app.md` |
| Privacy hosts (Inkstone) | `knowledge/privacy/inkstone-hosts.md` |
