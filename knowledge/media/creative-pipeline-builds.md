# Creative pipeline builds — LR / PS / CapCut / Resolve

**Skill:** `creative-pipeline-builds`  
**Adobe entry:** [CC desktop app (NZ)](https://www.adobe.com/nz/creativecloud/desktop-app.html) · `adobe-cc-desktop.md`  
**Not product endorsement.** “Build” = reproducible export recipe, not binary compile of cracked apps.

---

## Build definition

A **creative build** is:

1. Named project folder under `workspace/creative/<slug>/`  
2. Documented presets (LR export, PS action, CapCut export, Resolve Deliver)  
3. Input → process → `04_exports/`  
4. `notes.md` with app versions + checklist  

Automation = **presets + render queues + optional official scripting**, run by the user.

---

## Still pipeline (Lightroom → Photoshop)

```text
00_inbox → LR import/cull → develop preset → export preset
         → optional PS action batch → 04_exports/stills
```

| Preset to save once | Purpose |
|---------------------|---------|
| LR Develop | Look consistency |
| LR Export web | sRGB, long edge, naming |
| PS Action | Sharpen/resize/watermark |

---

## Short-form pipeline (CapCut)

```text
01_selects clips → CapCut template project → captions → export 9:16
                 → 04_exports/short
```

| Build artifact | Notes |
|----------------|--------|
| Template draft | Brand fonts/colors (licensed) |
| Caption style | Auto then human edit |
| Export preset | Platform max quality |

Cross: Instagram / TikTok organic or ads HITL.

---

## Long-form / color pipeline (DaVinci Resolve)

```text
00_inbox → Media → Edit/Cut → Color template → Fairlight → Deliver presets
        → 04_exports/long (+ optional master)
```

| Deliver preset examples | Use |
|-------------------------|-----|
| YouTube 1080p/4K H.264/H.265 | VOD upload |
| Vertical 1080×1920 | Shorts clip from long |
| ProRes / DNx master | Archive |

Resolve Free vs Studio: feature gates — VERIFY LIVE Blackmagic docs.

---

## Hybrid example (product launch pack)

| Output | Tool |
|--------|------|
| Hero stills | LR + PS |
| 15–30s teaser | CapCut |
| 5–10 min film | Resolve |
| Live Q&A | `youtube-live-encoder` |
| Frame-by-frame 2D | `animation-dev-kit` (Krita) |
| Feed announce | `rss-share` |

---

## Folder template

```text
workspace/creative/<slug>/
  00_inbox/
  01_selects/
  02_edit/
  03_graphics/
  04_exports/
    stills/
    short/
    long/
  05_presets/
  notes.md
```

---

## notes.md recipe stub

```markdown
# Build — <slug> — <date>
## Apps + versions
- Creative Cloud desktop:
- Lightroom:
- Photoshop:
- CapCut:
- Resolve:
## Presets
- LR:
- PS action:
- CapCut export:
- Resolve Deliver:
## Commands / steps (human)
1. ...
## Verify
- [ ] exports present
- [ ] no secrets on screen
```

---

## What “automated” is not

| Not allowed | Why |
|-------------|-----|
| Cracked Adobe/CapCut/Resolve | License + malware risk |
| GUI bots logging into Adobe ID unattended without user consent | Security / ToS |
| Fake engagement farms | Policy |

---

## Cross-links

- Skill: `creative-pipeline-builds`  
- Adobe: `adobe-cc-desktop.md`  
- YouTube Live: `youtube-live-encoder.md`  
- TikTok creative volume: `../ads/tiktok-creative-exchange.md`  
