# Inkstone — WebNovel author platform (offline notes)

**Skill:** `inkstone-resource-kit`  
**Product:** [inkstone.webnovel.com](https://inkstone.webnovel.com/)  
**Academy:** [academy/index](https://inkstone.webnovel.com/academy/index)  
**Example article path:** `/academy/article/{id}` e.g.  
[76088391988504901](https://inkstone.webnovel.com/academy/article/76088391988504901)  
**Reader / brand:** [webnovel.com](https://www.webnovel.com/) · Be an Author → Inkstone  
**Contests:** [wsa.webnovel.com](https://wsa.webnovel.com/) (submit via Inkstone)  

**Privacy hosts:** `knowledge/privacy/inkstone-hosts.md`  

VERIFY LIVE. SPA body text needs browser JS. Not legal/publishing advice.

---

## What it is

**Inkstone** is WebNovel’s **author writing platform** (“Become the Next Top Writer” marketing on sign-in). Authors sign in, create/manage novels, use **Writers Academy** articles, and may submit to platform contests (e.g. Spirity Awards / WSA).

Related ecosystem: Yuewen / WebNovel online literature; CDN assets often served from **yueimg.com**.

---

## Surfaces

| Surface | Purpose |
|---------|---------|
| Sign-in / dashboard | Account + novel list |
| Novel create/edit | Draft & manage stories |
| Writers Academy | Education articles for authors |
| Contests | Time-boxed submissions via Inkstone URLs |
| SPA shell | Client-rendered UI (`#root`) |

### Academy article URL shape

```text
https://inkstone.webnovel.com/academy/article/<numericId>?returnUrl=%2Facademy%2Findex
```

Article HTML shell may be empty until SPA loads — paste text for offline summary.

---

## SPA / CDN shell (forensic)

| Item | Notes |
|------|--------|
| Title | Inkstone |
| Assets | `https://www.yueimg.com/inkstone/assets/*` (index, framework, utils, antd, css) |
| Favicon | `https://www.yueimg.com/inkstone/favicon.ico` |
| Hybrid | `noah2.yueimg.com/js/common/hibridge.js` + inline HiBridge |
| Analytics | Cloudflare Insights beacon |

---

## Author workflow seed

```text
Create WebNovel/Inkstone account
  → Writers Academy (craft + platform norms)
  → Create novel / outline
  → Write & update chapters in Inkstone
  → Optional contest entry
  → Contract application (if offered) — human legal review
  → Publish path on WebNovel (platform rules)
```

---

## Academy themes (public search seeds — VERIFY LIVE)

- Novice authoring / pacing guides  
- Contract application rejected → revise language, use editing tools, read more academy  
- Using AI in writing — policy and ethics may change; re-read articles  

Do not invent article bodies for id `76088391988504901` without user paste.

---

## Contests

WebNovel annual writing contests; entries via **Inkstone** create/submit links with `contestId`. Rules and prizes on contest microsites only.

---

## Handoffs

| Goal | Skill |
|------|--------|
| Privacy host audit | `privacy-host-map` + inkstone-hosts |
| Offline outline loop | Fable `/hermes` · `/loop` |
| Specialized writing agents | `prompt-generator` |
| Classroom comics (different product) | `book-creator-comics-kit` |

---

## Privacy

- Manuscripts and account data are sensitive  
- No session cookies, HiBridge secrets, or unpublished chapters in public git  
