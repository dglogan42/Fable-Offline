# CSS design-system fingerprint — Helvetica Neue / grey body (orphan)

**Skill:** `aem-site-agent` (visual/CSS fingerprint procedure) · `privacy-host-map` (when full HTML arrives)  
**Origin:** User-supplied **CSS-only** extract (no URL, no HTML head).  
**Site identity:** **UNKNOWN** — do not attribute to a named organisation until a URL or full dump is linked.  
**Not a full site map.** Not enough for privacy hosts, programmes, or content pathways.

---

## Verdict

Light **typography / base reset** fingerprint only. Useful later for “does this CSS match site X?” matching. **No scripts, no hosts, no content** in the sample.

---

## Captured signals

### Reset / box model
| Rule | Notes |
|------|--------|
| `* { margin: 0; padding: 0; }` | Global margin/padding reset |
| `*, ::after, ::before { box-sizing: border-box; }` | Universal border-box |
| `html { line-height: 1.15; -webkit-text-size-adjust: 100%; }` | Normalize-ish root |
| `html { font-size: inherit; }` | Root size inherits |

### Hidden utility
| Rule | Notes |
|------|--------|
| `element { display: none; visibility: hidden; }` | Generic hide (selector may be tool-anonymised as `element`) |
| Inline-ish zero box | `width: 0px; height: 0px` on some element |

### Body type system
| Property | Value |
|----------|--------|
| `font-family` | `"Helvetica Neue", "Segoe WP", "Nimbus Sans L", Helvetica, Arial` |
| `font-size` (default) | `1.125rem` |
| `font-size` (mid breakpoint) | `.95rem` |
| `line-height` | `1.6` |
| `color` | `#424242` (mid grey) |

### Breakpoints (from sample)
| Query | Effect |
|-------|--------|
| `max-width: 60em` and `min-width: 45em` | body → `.95rem` |
| `max-width: 60rem` and `min-width: 45rem` | same (em/rem dual media) |

**Interpretation:** tablet-ish band between ~45–60 (em/rem) slightly reduces body size; desktop base is 1.125rem (~18px if root 16px).

---

## Font stack reading

| Face | Common association |
|------|---------------------|
| Helvetica Neue | Apple / neo-grotesque default on many marketing sites |
| Segoe WP | Windows Phone / older Microsoft web stacks (uncommon on modern greenfield) |
| Nimbus Sans L | Free Helvetica-like (often Linux / open stacks) |
| Helvetica, Arial | Fallbacks |

Stack alone **does not identify** a CMS (could be custom, Drupal, WP, etc.).

---

## What is missing (need next dump)

| Needed | Why |
|--------|-----|
| URL / `<title>` | Bind fingerprint to a property |
| Full `<head>` | Scripts → privacy host map |
| Main content HTML | Knowledge pathways |
| `etc.clientlibs` / generator meta | CMS class (AEM vs other) |

---

## Match checklist (when comparing another page)

Score loosely (yes/no):

1. Same body font stack order (incl. Segoe WP + Nimbus Sans L)  
2. Body colour ≈ `#424242`  
3. Body size 1.125rem with ~.95rem mid breakpoint  
4. Breakpoints near 45 / 60 em or rem  
5. Global `*` margin/padding 0 + universal border-box  

**3+ yes** → possible same design system family; still confirm with URL.

---

## Attach later

When origin is known, add:

```markdown
## Bound site
- URL:
- Date verified:
- Confidence: low | medium | high
```

---

## Cross-links

- AEM path fingerprints: `knowledge/aem/aem-patterns.md`  
- Full host maps: `knowledge/privacy/`  
