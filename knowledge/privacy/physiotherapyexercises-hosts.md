# Privacy host map seed — PhysiotherapyExercises.com

**Skill:** `privacy-host-map` · `physiotherapy-exercises-resource-kit`  
**URL:** https://www.physiotherapyexercises.com  
**Evidence:** Homepage HTML dump (GA + Cloudflare + first-party media/JS)  

Not legal advice. VERIFY LIVE.

---

## Host inventory

| Host | Class | Notes |
|------|-------|--------|
| `www.physiotherapyexercises.com` | LOAD | App, exercise images, JS data packs, sprites, fonts, CSS |
| `english.physiotherapyexercises.com` | CONFIG/CLICK | `og:url` seed |
| `www.googletagmanager.com` | LOAD | gtag.js **UA-20604563-1** (Universal Analytics id form) |
| `static.cloudflareinsights.com` | LOAD | Cloudflare Web Analytics beacon |

### First-party path families

- `/ExerciseImages/` — drawings/photos  
- `/Js/ExerciseData_*` — data packs  
- `/Sprite/` — sprite CSS  
- `/media/` — branding assets  
- `/exercise/rss`, `/exercise/atom` — feeds  

---

## Notes

- SPA requires JavaScript  
- `beforeinstallprompt` suggests PWA install path  
- Patient booklet content may be generated client-side — treat exports as clinical data  

## OPEN

- Cookie consent UX after hydrate  
- Authenticated clinician features (if any)  
- Whether UA property migrates to GA4  
