# CSS design-system fingerprint — TikTok product UI

**Skill:** `tiktok-analytics` · `aem-site-agent` (**fingerprint-css**) · `privacy-host-map`  
**Origin:** User-supplied **CSS-only** extract (devtools-style).  
**Likely surface:** **TikTok first-party product UI** (ads/analytics/business console family) — **not** a third-party site that merely loads `analytics.tiktok.com`.  
**Confidence:** **high** for TikTok design system; **medium** for exact product (Ads Manager / Business Center / similar) without URL.  
**Not a host map.** Pair with Network/HTML for LOAD confirmation.

---

## Verdict

This is a **first-party TikTok shell** fingerprint:

| Strong signal | Value |
|---------------|--------|
| Brand primary | `#fe2c55` (`--primary-color`) — classic TikTok pink-red |
| Fonts | **TikTok Text**, **TikTok Display** |
| Token prefix | `--ttam-*` (TikTok Ads Manager / TTAM design tokens) |
| Theme | `:root[theme-mode="dark"]` dark tokens |
| Grid | `--midas-grid-*` layout grid |
| Swiper | `--swiper-theme-color: #007aff`, navigation size 44px |

**Do not confuse** with third-party sites (e.g. VUW) that only fire TikTok Analytics beacons — those keep university CSS (e.g. Helvetica Neue grey orphan), not TikTok Text.

---

## Captured signals

### Layout / shell
| Rule | Notes |
|------|--------|
| `body` flex not required in sample | `overflow-y: auto` on body |
| `html, body { margin: 0 }` | Full-bleed app shell |
| Midas grid CSS variables | `--midas-grid-rows-height: 8px`; `--midas-grid-col-num: 40`; `--midas-grid-col-percent: 2.5%` |

### Typography
| Property | Value |
|----------|--------|
| Form controls + body stack | `TikTok Text, TikTok Display, -apple-system, BlinkMacSystemFont, Segoe UI, PingFang SC, Hiragino Sans GB, Microsoft YaHei, Helvetica Neue, sans-serif, … Emoji` |
| Default size | `14px` on `html, body` |
| Colour | `#333` |
| Smoothing | antialiased / grayscale |
| TTAM tokens | `--ttam-font-family-text`, `-display`, `-default`; weights 400 / 500 |

### Brand / theme tokens
| Token | Light/dark (from sample) |
|-------|---------------------------|
| `--primary-color` | `#fe2c55` |
| `--brand-color` | `#fff` (dark mode block) |
| `--text-color-primary` | `hsla(0,0%,100%,.9)` (dark) |
| `--scrollbar-color` | `hsla(0,0%,100%,.1)` (dark) |
| `theme-mode="dark"` | Dark theme attribute pattern |

### Component libraries (hints)
| Signal | Notes |
|--------|--------|
| Swiper CSS variables | Carousel/slider UI present in design system |
| Empty `:root { }` noise | Devtools expansion / incomplete rules — ignore for ID |

### Noise in dump
- Many empty `:root` / `element { }` blocks from inspector  
- Triple `*, ::after, ::before` border-box variants — same intent  

---

## Match checklist

| # | Signal | This sample |
|---|--------|-------------|
| 1 | Font family includes **TikTok Text** / **TikTok Display** | yes |
| 2 | `--primary-color: #fe2c55` or equivalent brand pink | yes |
| 3 | `--ttam-font-family-*` tokens | yes |
| 4 | `--midas-grid-*` | yes |
| 5 | `theme-mode="dark"` token set | yes |
| 6 | CJK fallbacks (PingFang / YaHei) in stack | yes |

**4+ yes** → TikTok product UI family (high confidence).

---

## Contrast: third-party TikTok Analytics only

| | TikTok **product UI** (this note) | **Analytics pixel** on another site |
|--|-----------------------------------|-------------------------------------|
| CSS | TikTok Text, `#fe2c55`, TTAM | Site’s own fonts (e.g. Helvetica Neue grey) |
| Network | Many first-party TikTok hosts | Often only `analytics.tiktok.com` beacon |
| Example | ads.tiktok.com / business.tiktok.com (VERIFY URL) | `www.wgtn.ac.nz` → TT analytics |
| Skill | fingerprint-css + this note | **`tiktok-analytics`** + `wgtn-ac-nz-hosts.md` |

---

## What is still missing

| Needed | Why |
|--------|-----|
| Exact URL | Bind to Ads Manager vs Creator vs other |
| Full `<head>` scripts | Confirm product bundle names |
| Network HAR | Map first-party API hosts |

---

## Attach when URL known

```markdown
## Bound product
- URL:
- Date verified:
- Confidence: high
- Notes: TTAM tokens + primary #fe2c55 + TikTok Text
```

---

## Cross-links

- Skill: `skills/tiktok-analytics.md`  
- Method: `knowledge/privacy/tiktok-analytics.md`  
- Third-party beacon example: `knowledge/privacy/wgtn-ac-nz-hosts.md`  
- Unrelated orphan (uni-like): `knowledge/web/css-design-fingerprint-helvetica-grey.md`  
