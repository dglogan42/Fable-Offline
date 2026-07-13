# Krita animation — offline notes (dev kit)

**Skill:** `animation-dev-kit`  
**Primary docs (VERIFY LIVE):**  
- [Animation with Krita](https://docs.krita.org/en/user_manual/animation.html)  
- [Render Animation](https://docs.krita.org/en/reference_manual/render_animation.html)  

Seeded from Krita Manual **5.3.x** family. UI labels and FFmpeg bundling can change — re-check after upgrades.

**Not product endorsement.** FOSS animation workflow hygiene for offline agents.

---

## What Krita animation is

- **Frame-by-frame raster** animation (Kickstarter-era feature set expanded over time)  
- All frames held in **RAM** → long sequences need **planning**, **clip split**, **memory hygiene**  
- Not a full video/audio montage suite → use external NLE for animatic and final assembly  

---

## Core dockers

| Docker | Purpose |
|--------|---------|
| Animation Timeline | Frames, holds, layer visibility on timeline |
| Onion Skin | Ghost previous/next frames |
| Animation Curves | Scalar tweening / transform-mask curves |
| Storyboard | Shot planning |

**Workspace:** Window → Workspace → **Animation**.

---

## Production stages (manual)

```text
Script/outline
  → Storyboard (sparse)
  → Animatic (external editor)
  → Subdivide into short clips (≤ ~10s; beginners ~12 fps)
  → Per clip: File → Import Animation Frames
  → Rough → keys → inbetweens → clean
  → Render Animation
  → Assemble in NLE → WebM/etc. → upload (HITL)
```

Beginner fps tip from manual: start around **12 fps**.  
10s @ 12 fps ≈ **120 frames**.

Early sketch resolution tip: e.g. **~800×450**; raise resolution when line art matters.

---

## Memory reduction checklist

1. Merge layers  
2. Image → Crop Layers to Image Size  
3. Convert B/W layers to grayscale color space  
4. Lower resolution  
5. Free system RAM (browsers, streaming)  
6. Incremental Backup + external copies  

Watch status-bar memory indicator.

---

## Walk cycle lab (summary)

| Step | Action |
|------|--------|
| Doc | New file e.g. 1280×1024, 72 dpi, titled |
| BG | Canvas-color fill useful |
| Layers | `environment` + transparent `walkcycle` |
| Animate | Create **Duplicate** Frame to start animated layer |
| Onion | On; past red / future green (configurable) |
| Keys | Contact extremes; copy/paste keyframes |
| Preview | Low fps (e.g. 4) then raise |
| Holds | Insert hold frames; inbetween |
| Labels | Color-label extremes vs inbetweens |
| Hands | New layer; **pin** to timeline |
| Travel | Transform mask + scalar keys (5.0+); plant feet with guides |

**Warning:** White is opaque color — keep empty canvas transparent on anim layers.

---

## Render Animation (summary)

| Mode | Notes |
|------|--------|
| Image sequence | PNG recommended; base name + frame numbers |
| Video | Encodes via FFmpeg (bundled partial since **5.2**, or external binary) |
| Range | First/last frame from selection |
| Transparency in video | Becomes black — add opaque bottom layer |
| Android | No video render in-app |
| Windows MP4 | Prefer baseline profile for WMP-class players |

External FFmpeg examples (VERIFY LIVE):  
- Windows essentials zip from gyan.dev (**not** shared)  
- macOS evermeet.cx  
- Linux package `/usr/bin/ffmpeg`  

---

## Related dockers / topics

- Import Animation Frames  
- Audio for Animation  
- Japanese Animation Template (user manual)  
- Grids and Guides (foot-plant marks)  

---

## Scaffold under Fable workspace

```text
workspace/creative/<slug>/
  00_script/
  01_storyboard/
  02_animatic/
  03_krita/          # .kra + Incremental Backups (local; often gitignored)
  04_renders/        # sequences / previews (local)
  05_presets/
  notes.md
```

---

## Handoff

| Output | Next skill |
|--------|------------|
| PNG/WebM master | `creative-pipeline-builds` |
| Live stream stills/clips | `youtube-live-encoder` |
| Short social cut | CapCut path in creative pipeline |

Never commit stream keys or huge render folders.  
