# CSS design-system fingerprint — Helvetica Neue / grey body (orphan)

**Skill:** `aem-site-agent` (**fingerprint-css**) · `privacy-host-map` (when full HTML arrives)  
**Origin:** User-supplied **CSS-only** extracts (no URL, no HTML head).  
**Site identity:** **UNKNOWN** — do not attribute to a named organisation until a URL or full dump is linked.  
**Samples:** 2 CSS dumps (same family; second adds layout/smoothing).  
**Not a full site map.** Not enough for privacy hosts, programmes, or content pathways.

---

## Verdict

**Same design-system family** as the first orphan sample (match checklist **5/5** on shared rules). Second dump **enriches** body layout: full-height **column flex** shell + font smoothing. Still **CSS-only** — CMS and organisation remain **UNKNOWN**.

---

## Sample log

| # | What arrived | Delta |
|---|--------------|--------|
| 1 | Reset + type + breakpoints + hide utility | Baseline |
| 2 | Same type/breakpoints/reset + **body flex column** + **min-height 100%** + **font-smoothing** | Confirms sticky full-page column layout pattern |

---

## Captured signals (merged)

### Reset / box model
| Rule | Notes |
|------|--------|
| `* { margin: 0; padding: 0; }` | Global margin/padding reset |
| `*, ::after, ::before { box-sizing: border-box; }` | Universal border-box |
| `html { line-height: 1.15; -webkit-text-size-adjust: 100%; }` | Normalize-ish root |
| `html { font-size: inherit; }` | Root size inherits |

### Body layout shell (sample 2)
| Property | Value |
|----------|--------|
| `margin` | `0` (also on body) |
| `display` | `flex` (+ webkit/ms prefixes) |
| `flex-direction` | `column` |
| `min-height` | `100%` |

**Reading:** App-shell style page: column flex from top to bottom, at least full viewport height (often pairs with sticky footer patterns — footer not in dump).

### Body type system
| Property | Value |
|----------|--------|
| `font-family` | `"Helvetica Neue", "Segoe WP", "Nimbus Sans L", Helvetica, Arial` |
| `font-size` (default) | `1.125rem` |
| `font-size` (mid breakpoint) | `.95rem` |
| `line-height` | `1.6` |
| `color` | `#424242` (mid grey) |
| `-webkit-font-smoothing` | `antialiased` (sample 2) |
| `-moz-osx-font-smoothing` | `grayscale` (sample 2) |

### Breakpoints
| Query | Effect |
|-------|--------|
| `max-width: 60em` and `min-width: 45em` | body → `.95rem` |
| `max-width: 60rem` and `min-width: 45rem` | same (em/rem dual media) |

**Interpretation:** tablet-ish band ~45–60 (em/rem) slightly reduces body size; desktop base 1.125rem (~18px if root 16px).

### Other
| Rule | Notes |
|------|--------|
| `element { }` | Empty rule in sample 2 (devtools anonymised selector) |
| Sample 1 hide utility | `display: none; visibility: hidden` + 0×0 box — not repeated in sample 2 |

---

## Font stack reading

| Face | Common association |
|------|---------------------|
| Helvetica Neue | Neo-grotesque / marketing defaults |
| Segoe WP | Older Microsoft / WP web stacks |
| Nimbus Sans L | Free Helvetica-like (often open/Linux stacks) |
| Helvetica, Arial | Fallbacks |

Stack + flex shell **still do not identify** a CMS.

---

## Match checklist (this family)

| # | Signal | Sample 1 | Sample 2 |
|---|--------|----------|----------|
| 1 | Font stack order incl. Segoe WP + Nimbus Sans L | yes | yes |
| 2 | Body colour `#424242` | yes | yes |
| 3 | 1.125rem / .95rem mid | yes | yes |
| 4 | Breakpoints ~45–60 em **and** rem | yes | yes |
| 5 | `*` reset + universal border-box | yes | yes |
| 6 | Body flex column + min-height 100% | — | yes |
| 7 | Font smoothing antialiased/grayscale | — | yes |

**3+ of 1–5** → possible same family; **5/5 + 6–7** → strong same-family confidence without a URL.

---

## What is still missing

| Needed | Why |
|--------|-----|
| URL / `<title>` | Bind fingerprint to a property |
| Full `<head>` | Scripts → privacy host map |
| Main content HTML | Knowledge pathways |
| CMS paths / meta | AEM vs WP vs custom |

---

## Attach later

```markdown
## Bound site
- URL:
- Date verified:
- Confidence: low | medium | high
- Notes: matches samples 1–2 flex+Helvetica grey shell
```

---

## Cross-links

- AEM path fingerprints: `knowledge/aem/aem-patterns.md`  
- Procedure: `aem-site-agent` → **fingerprint-css**  
- Full host maps: `knowledge/privacy/`  
