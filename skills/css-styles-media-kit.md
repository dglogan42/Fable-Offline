# CSS styles media kit (web design rules · fingerprints)

**WHEN_TO_USE:** User pastes **CSS dumps**, design-system tokens, component rules, media-query stacks, or asks for **web design rules**, **style guides from CSS**, or **fingerprinting** which product/site a stylesheet belongs to. Triggers: “CSS fingerprint”, “design system”, “style kit”, “media kit for styles”, orphan CSS, `@media`, custom properties, MUI/Epic/TikTok/Firefox control CSS.

**Companion skills:**  
- `aem-site-agent` **fingerprint-css** — AEM + CSS-only path  
- `privacy-host-map` — when HTML/Network available  
- `tiktok-analytics` / `tiktok-ads-create` — TikTok UI fingerprints  
- `creative-pipeline-builds` — export design tokens into creative notes  
- Domain kits only after URL bind  

Knowledge index: `knowledge/web/css-styles-media-kit.md`  
Fingerprints: `knowledge/web/css-design-fingerprint-*.md`

## Stance
You turn CSS into a **structured media kit**: tokens, type, colour, layout, components, motion, media queries, a11y, and **attribution confidence**. CSS-only dumps are **orphan-OK** — never invent organisation, CMS, or hosts without URL/HTML.

**Not legal advice.** Do not copy proprietary brand assets into production without license. Fingerprints identify *systems*, not permission to rebrand.

**Refuse:** laundering stolen design systems as “original”; claiming browser chrome is a site’s brand.

---

## Media kit schema (always output)

When producing a kit from CSS (or merging fingerprints), use this structure:

```markdown
# CSS styles media kit — <name or orphan-id>
## Verdict / attribution
## Confidence (very high | high | medium | low)
## Token sheet (custom properties)
## Typography
## Colour
## Layout / shell / navigation
## Components
## Media queries / responsive
## Motion / interaction (if any)
## Accessibility
## Browser chrome vs first-party site
## Match checklist
## Fingerprint catalog links
## OPEN / next evidence needed
```

Write durable notes under `knowledge/web/` as:
- `css-design-fingerprint-<slug>.md` — single system  
- `css-styles-media-kit.md` — this rulebook + catalog  

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| Full media kit from CSS dump | **kit-from-css** |
| Classify dump (site / design system / browser chrome) | **classify-css** |
| Extract design tokens only | **token-sheet** |
| Typography + type scale | **type-system** |
| Colour palette + roles | **colour-system** |
| Layout / nav / grid | **layout-shell** |
| Components inventory | **component-map** |
| `@media` / breakpoints / prefers-* | **media-rules** |
| a11y (focus, contrast, reduced motion) | **a11y-rules** |
| Match against known fingerprints | **fingerprint-match** |
| Merge new dump into existing fingerprint | **fingerprint-merge** |
| Compare two CSS systems | **diff-systems** |
| Scaffold knowledge file | **write-fingerprint** |
| Escalate to hosts/HTML | **escalate-html** |
| Short answer | **brief** |

Default: **classify-css** → **kit-from-css** → **fingerprint-match**.

---

## classify-css

| Class | Signals | Action |
|-------|---------|--------|
| **Browser chrome** | MPL, `chrome://`, `-moz-`/`-webkit-` UA skins, `.videocontrols` | Fingerprint as browser; **not** site brand |
| **First-party product UI** | Brand fonts/tokens (TikTok Text, `--ttam-*`, Brutal+`.epic-wf`) | Product-family fingerprint |
| **Multi-brand shared nav** | Parallel `*-navigation` (egs, fortnite, unrealengine…) | Portfolio design system |
| **Marketing / CMS page** | Generic stacks (Helvetica Neue, system fonts), resets | Orphan until URL |
| **Component library only** | Pure MUI/Bootstrap without brand tokens | Library + unknown skin |
| **Noise** | Empty `element{}`, empty `:root{}` | Ignore |

Output class + one-line rationale.

---

## kit-from-css

1. **classify-css**  
2. Pull **token-sheet** (`--*` and JS-read vars)  
3. **type-system**, **colour-system**, **layout-shell**, **component-map**  
4. **media-rules**, **a11y-rules**  
5. **fingerprint-match** against catalog  
6. Emit full media kit schema  
7. Suggest `write-fingerprint` path  

---

## token-sheet

Capture:

| Kind | Examples |
|------|----------|
| Layout | `--eg-global-nav-height`, grid columns |
| Control sizes | `--button-size`, `--track-size` (players) |
| Brand | `--primary-color`, `--ttam-*` |
| Focus | `--control-focus-outline` |
| JS contract | Vars commented “used by JS” (Firefox videocontrols) |

Table: name · value · role (layout/type/colour/control) · source selector.

---

## type-system

| Capture | Notes |
|---------|--------|
| Font stacks | Brand vs system fallbacks |
| Roles | Display (Titan One), UI (Inter), CTA (Brutal), body |
| Sizes | rem/px/em; root html size |
| Weight / transform | 400–700; uppercase CTAs |
| Tracking / leading | letter-spacing, line-height |
| Platform forks | e.g. macOS Helvetica Neue in Firefox timer |

---

## colour-system

Roles: text primary/secondary, surface, bar/chrome, brand primary, hover/active, progress, disabled, high-contrast overrides.

Prefer exact CSS values (`#00b6f0`, `rgba(26,26,26,0.8)`, `hsl(...)`).

---

## layout-shell

| Pattern | Clues |
|---------|--------|
| App shell | `min-height: 100%`, flex column body |
| Global nav | fixed height (`4.5rem`), `display: flex`, `*-navigation` |
| Full-bleed controls | `width/height: 100%` overlays |
| Stack/absolute | `.stackItem`, bottom control bars |

---

## component-map

Inventory by selector family:

- Buttons / links  
- Forms / ranges / progress  
- Navigation  
- Overlays / modals / status  
- Media players  
- Typography utilities  

Note library: MUI, Swiper, Ant Design, UA chrome, custom BEM/hashes.

---

## media-rules

Catalog every `@media`:

| Query type | Examples |
|------------|----------|
| Width | `max-width: 60em` |
| Interaction | `.touch` class (not always media query) |
| Preference | `prefers-contrast`, `prefers-reduced-motion` (if present) |
| Platform | `-moz-platform: macos` / `windows` |

---

## a11y-rules

| Check | Look for |
|-------|----------|
| Focus | `:focus-visible`, outline tokens |
| Contrast | `prefers-contrast` borders; don’t assume WCAG pass |
| Hidden chrome | `opacity: 0` + a11y tree kept (Firefox bar) |
| Reduced motion | Only if in dump |
| Hit targets | Touch sizing (40px+ buttons) |

Label: **observed rules only** — not a full WCAG audit.

---

## fingerprint-match

Score against catalog (`knowledge/web/css-design-fingerprint-*.md`):

| ID | System |
|----|--------|
| `helvetica-grey` | Orphan Helvetica Neue / grey body |
| `tiktok-ui` | TikTok product (TikTok Font, `#fe2c55`, TTAM) |
| `epic-brutal` | Epic nav + Brutal/Titan One/Inter |
| `firefox-videocontrols` | Firefox media controls |

Rules:
- Use each file’s **match checklist**  
- Prefer **highest checklist score**  
- Multi-match rare; browser chrome can co-occur with site CSS in one paste — **split** them  

---

## fingerprint-merge

When new CSS extends a known system:

1. Open existing fingerprint file  
2. Append **Sample log** row  
3. Merge new selectors into tables (nav list, tokens)  
4. Raise confidence only with stronger signals  
5. Keep short codes (e.g. Epic `kws-`) as VERIFY LIVE  

---

## diff-systems

Two dumps → two verdicts + table of shared vs unique fonts, tokens, components. Never force-merge TikTok + Epic.

---

## write-fingerprint

Path: `knowledge/web/css-design-fingerprint-<slug>.md`  

Must include: Verdict · Confidence · Captured signals · Match checklist · Not-this table · Sample log · OPEN.

Update `knowledge/web/css-styles-media-kit.md` catalog row.

---

## escalate-html

Ask for / wait on:

1. Page URL  
2. HTML `<head>` + first-party scripts  
3. Network HAR or host list  

Then: `privacy-host-map` and/or domain skills (AEM, TikTok ads, etc.).

---

## Web design rules (normative checklist for agents)

When **authoring** CSS advice (not just fingerprinting), prefer:

1. **Tokens first** — colour/type/space as custom properties  
2. **Logical properties** where appropriate (`margin-inline`, etc.)  
3. **Focus visible** for interactive controls  
4. **Touch targets** ≥ ~40px on touch UIs  
5. **Respect** `prefers-contrast` / reduced motion when designing  
6. **Don’t fight the UA** — don’t restyle Firefox videocontrols as “brand” without reason  
7. **Name systems** — document font roles (display / UI / mono)  
8. **Responsive** — mobile-first or documented breakpoints  
9. **Cascade honesty** — note `!important` and inheritance traps  
10. **Attribution** — cite fingerprint or brand source  

These are **engineering hygiene**, not a full brand book.

---

## Output contract

1. **Class** (browser / product / orphan / library)  
2. **Verdict + confidence**  
3. **Media kit tables** (tokens, type, colour, layout, components, media, a11y)  
4. **Catalog match** or new slug proposal  
5. **OPEN** — URL/HTML needed?  
6. No invented hosts or brand names beyond evidence  

---

## Anti-failure

- Do not attribute browser chrome to the website  
- Do not invent organisation from Inter + flex alone  
- Do not skip confidence labels  
- Do not dump raw CSS back without structure  
- Empty `element{}` / `:root{}` are noise  
- Multi-product nav lists = portfolio system, not one domain  
