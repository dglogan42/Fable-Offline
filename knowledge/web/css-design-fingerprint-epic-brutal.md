# CSS design-system fingerprint — Epic global navigation (Brutal · Titan One · Inter)

**Skill:** `aem-site-agent` (**fingerprint-css**) · `privacy-host-map` (when URL/HTML arrives) · creative/UI audits  
**Origin:** User-supplied **CSS-only** extracts (devtools-style).  
**Site identity:** **Epic Games multi-brand web navigation** — confirmed by product-prefixed `-navigation` selectors.  
**Confidence:** **very high** for Epic Games design system / shared global nav; **medium** for exact page without URL.  
**Not a host map.** Pair with Network/HTML for LOAD confirmation.

---

## Verdict

Shared **Epic Games web framework** chrome used across portfolio sites:

| Strong signal | Value |
|---------------|--------|
| Global nav height | **`4.5rem`** (matches `--eg-global-nav-height` / `.epic-wf`) |
| Nav type | **`font-family: Inter, sans-serif`** · `display: flex` · `height: 4.5rem` |
| Product nav hosts | `egs-`, `fortnite-`, `unrealengine-`, `epicgames-`, … (see list) |
| Display / CTA font | **Titan One** — uppercase, white on primary buttons |
| Compact UI | **Inter** — 14px / 500 |
| Button system | **MUI** + **Brutal** (0.75rem, 700, uppercase) |
| UE web naming | `.ue-link-wrap-span`, `.ue-rich-text` |

**Reading:** One nav component stylesheet styles **many Epic product shells** via parallel custom-element/class names (`*-navigation`), not a single orphan site.

---

## Product navigation registry (sample 2)

Shared rule applied to all of the following:

```css
/* conceptual — selectors joined in dump */
*-navigation {
  display: flex;
  height: 4.5rem;
  font-family: Inter, sans-serif;
}
```

| Selector | Epic / portfolio surface (seed) |
|----------|----------------------------------|
| `edc-navigation` | Epic Developer Community (or similar Dev/Community shell) |
| `egs-navigation` | **Epic Games Store** |
| `eos-navigation` | Epic Online Services |
| `epicgames-navigation` | Epic Games corporate / umbrella site |
| `fortnite-navigation` | **Fortnite** |
| `rocketleague-navigation` | **Rocket League** |
| `twinmotion-navigation` | **Twinmotion** |
| `fallguys-navigation` | **Fall Guys** |
| `realitycapture-navigation` | **RealityCapture** |
| `metahuman-navigation` | **MetaHuman** |
| `devportal-navigation` | Epic **Dev Portal** |
| `unrealengine-navigation` | **Unreal Engine** |
| `sac-navigation` | Epic account / store account center (seed — VERIFY LIVE) |
| `ssp-navigation` | Seller / partner portal family (seed — VERIFY LIVE) |
| `kws-navigation` | Kids Web Services / age-gate family (seed — VERIFY LIVE) |
| `supportkws-navigation` | Support + KWS (seed — VERIFY LIVE) |
| `quixel-navigation` | **Quixel** (Megascans) |

Exact product marketing names for short codes (`edc`, `sac`, `ssp`, `kws`) should be **VERIFY LIVE** when HTML/URL is available; long product names above are unambiguous.

---

## Captured signals (sample 1 — buttons / type)

### Typography

| Rule / selector | Properties |
|-----------------|------------|
| `.fLWzCS … button.primary/secondary .label .ue-rich-text` | `font-family: Titan One, sans-serif`; `font-size: 1.0625rem`; `letter-spacing: 0.00025em`; `color: white`; `text-transform: uppercase`; `text-shadow: none` |
| `.fLWzCS … button .typography-rich-text` | `color: black` |
| `.fSFlL` | `font-family: Inter, arial`; `font-weight: 500`; `letter-spacing: 0.26px`; `font-size: 14px`; `line-height: 16px` |
| `.MuiButton-root` | `font-family: Brutal, sans-serif`; `font-size: 0.75rem`; `font-weight: 700`; `line-height: 1.25`; `letter-spacing: 0.04em`; `text-transform: uppercase` |
| `.MuiButton-containedPrimary` | `color: #fff` |

### Colour / text

| Selector | Colour |
|----------|--------|
| Primary CTA label | `white` |
| `.cztkbk.primary` | `rgb(40, 40, 40)` |
| `.cztkbk` | `hsl(0,0%,var(--switch))` |
| `.MuiTypography-colorTextPrimary` | `#000` |

### Layout / shell

| Rule | Notes |
|------|--------|
| `.epic-wf` | `--eg-global-nav-height: 4.5rem` |
| Multi-product `*-navigation` | `height: 4.5rem` · `display: flex` · **Inter** |
| Center utilities | `.fwkynP`, `.cZAgOZ`, `.nHRIC` → `text-align: center` |

### Component libraries

| Signal | Notes |
|--------|--------|
| **MUI** | `MuiButton-*`, `MuiTypography-*`, `MuiButtonBase-root` |
| Styled hashes | `.fLWzCS`, `.fSFlL`, `.cztkbk`, `.EOZmi`, … |
| Epic/UE | `.ue-link-wrap-span`, `.ue-rich-text`, `.epic-wf`, `--eg-*` |

---

## Match checklist

| # | Signal | Sample 1 | Sample 2 |
|---|--------|----------|----------|
| 1 | Font **Brutal** on buttons | yes | — |
| 2 | Font **Titan One** on CTAs | yes | — |
| 3 | Font **Inter** | yes | yes (nav) |
| 4 | **MuiButton-*** | yes | — |
| 5 | **`.epic-wf` / `--eg-global-nav-height: 4.5rem`** | yes | height **4.5rem** on nav |
| 6 | **Product `*-navigation`** list (egs, fortnite, unrealengine, …) | — | **yes** |
| 7 | `.ue-link-wrap-span` / `.ue-rich-text` | yes | — |

**Any of:** (4+ of 1–5,7) **or** (item 6 alone) → **Epic Games shared web nav / design system**.

---

## What this is **not**

| Fingerprint | Differentiator |
|-------------|----------------|
| TikTok product UI | TikTok Text / `#fe2c55` / `--ttam-*` |
| Helvetica Neue grey orphan | Helvetica Neue stack, `#424242` body |
| Firefox videocontrols | MPL + `chrome://global/skin/media/` + `.videocontrols` |
| Book Creator / Inkstone | Different hosts and type stacks |

---

## Noise

- Empty `element { }` / empty `:root` from inspector  
- Short codes (`edc`, `sac`, `ssp`, `kws`) need HTML/URL to name precisely  
- Full brand palette (Epic yellow/black) not fully present in these dumps  

---

## Next steps

1. URL or full HTML → bind to one product (e.g. which `*-navigation` is in DOM)  
2. Network panel → `privacy-host-map` for Epic account/CDN hosts  
3. Capture more brand colour tokens if needed  
4. Orphan OK for multi-product nav CSS without a single page URL  

---

## Sample log

| # | What arrived | Delta |
|---|--------------|--------|
| 1 | Titan One + Inter + Brutal + MUI + `.epic-wf` | Baseline Epic-family type/button fingerprint |
| 2 | Multi-selector `*-navigation` flex 4.5rem Inter | **Confirms shared Epic portfolio global nav** across EGS, Fortnite, UE, Quixel, etc. |
