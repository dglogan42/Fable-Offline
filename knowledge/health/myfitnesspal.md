# MyFitnessPal — offline product notes

**Skill:** `myfitnesspal-resource-kit`  
**Companion agent:** `fitness-companion-agent` (habit/process over this product map)  
**Site:** [https://www.myfitnesspal.com](https://www.myfitnesspal.com/)  
**Canonical seed:** logged-out homepage (`/logged-out-homepage-v2`), release **v21.9.1**  
**Privacy hosts:** `knowledge/privacy/myfitnesspal-hosts.md`  

**Not medical advice.** Not product endorsement. VERIFY LIVE.

---

## Product summary (meta + marketing)

| Claim area | Seed from dump |
|------------|----------------|
| Positioning | Calorie tracker & BMR calculator; nutrition tracking app |
| Features | Macro/calorie calculator, food tracker, fasting app (meta description) |
| Premium seeds | Ad-free, custom macros/goals, barcode, meal scan, voice log, multi-day logging, food insights, net carbs, intermittent fasting |
| Integrations | 40+ apps/devices (marketing); Trainerize/GymEngine widget origins in `__ENV` |
| Brand colour | `#0066EE` (mask-icon / links) |
| Type | Inter + Helvetica/Arial system stack |
| Stack | Next.js, Emotion CSS-in-JS, asset prefix `web-assets.myfitnesspal.com/web-main/` |

### Locales (hrefLang seed)

`en`, `es`, `da`, `de`, `fr`, `it`, `ja`, `ko`, `nb`, `nl`, `pt`, `sv`, `pl`, `id`, `tl`, `ru`, `ms`, `tr`, `zh-CN`, `zh-TW` under myfitnesspal.com/{lang}.

### Related first-party hosts

| Host | Role |
|------|------|
| `www.myfitnesspal.com` | Web app |
| `web-assets.myfitnesspal.com` | Static Next assets + scripts |
| `web-main-assets.myfitnesspal.com` | Preconnect asset host |
| `api.myfitnesspal.com` | Public API host (env) |
| `blog.myfitnesspal.com` | Blog |
| `community.myfitnesspal.com` | Community (client id in env) |

---

## Partner / Premium offer seed

i18n includes medication-maker / Lilly partnership copy (6 months Premium, eligibility, 30-day redeem window, Canada-oriented terms in strings). **VERIFY LIVE** — regional and program-specific; not a general free Premium promise.

---

## Design fingerprint seeds

| Token | Value |
|-------|--------|
| Body font | `"Inter", Helvetica, Arial, -apple-system, sans-serif` |
| Body text | `rgba(0, 0, 0, 0.87)` on `#fff` |
| Brand link | `#0066EE` |
| Header height | ~60px fixed |
| Layout max | ~992px content width |
| Breakpoints seen | 0, 576, 992 |

Optional catalog: link from `css-styles-media-kit` if a dedicated fingerprint file is added later.

---

## User workflow (non-clinical)

```text
Account (HITL)
  → Goals (user-defined)
  → Log food / exercise
  → Optional Premium features
  → Device/app integrations
  → Review trends (user interpretation)
```

Fable may help with **process** and **privacy maps**, not prescriptions.

---

## Scaffold

```text
workspace/health/myfitnesspal/
  notes.md          # goals process only — no full food logs if sensitive
```
