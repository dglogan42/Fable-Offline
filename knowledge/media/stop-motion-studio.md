# Stop Motion Studio — offline notes (stop / motion dev kit)

**Skill:** `stop-motion-dev-kit`  
**Download (VERIFY LIVE):** [stopmotionstudio.com/download](https://www.stopmotionstudio.com/download/index.html)  
**Product:** [stopmotionstudio.com](https://www.stopmotionstudio.com/index.html)  
**Help:** [help/stopmotion/en](https://www.stopmotionstudio.com/help/stopmotion/en/)  

Vendor: **Cateater** (Stop Motion Studio). Not product endorsement. UI and store SKUs change — re-check after updates.

---

## What it is

Cross-platform **stop-motion** capture + edit app: iPhone/iPad, Mac, Android, Windows, Chromebook, Amazon Fire.  
Desktop-class frame editor, onion skin, guides, optional DSLR, green screen, audio, titles, share/export.

Vendor messaging highlights **one-time purchase / no monthly subscription** (VERIFY LIVE; free vs Pro may differ by store).  
Privacy claim on site: projects stay on device; no tracking ads (VERIFY LIVE privacy policy).

---

## Official desktop download (seed)

From download page (filenames may change):

| Build | Platform notes | Typical package |
|-------|----------------|-----------------|
| **Stop Motion Studio 2** | Windows 10 or newer | MSIX from site |
| **Stop Motion Studio 2** | macOS **13** or newer | DMG from site |
| Older **Stop Motion Studio** | Older Windows / macOS 11+ | Older Releases section |
| App Store / Microsoft Store | Alternate install path | Linked from download page |

Always prefer the **current** button on the official download page over cached URLs.

---

## FPS (official help)

[Adjust the Speed of Your Movie](https://www.stopmotionstudio.com/help/stopmotion/en/adjust-the-speed-of-your-movie.html):

- Speed = **FPS** in **Project Settings**  
- Start with **6 FPS**; if unsteady, try **12+**  
- TV-like density ≈ **25** frames per second of film (help comparison)  
- More frames/sec = smoother = more work  
- **Pause/freeze** frames for holds without extra captures  

**Frame budget:** `seconds × FPS ≈ frames` (before freezes).

---

## Feature map (product site seed)

| Area | Capabilities (marketing / help) |
|------|----------------------------------|
| Capture | Auto/manual focus, exposure, ISO, WB; 4K; RAW/ProRAW when supported |
| Guides | Grid, onion skin, aspect mask, path layer, paint marks, reference media |
| Cameras | USB cam, DSLR Live View controls, remote camera app, remote shutter |
| Edit | Frame-by-frame timeline, rearrange, copy/paste, in/out points, retime, merge frames |
| Draw | Brush layers, Apple Pencil; masking / remove objects |
| Green screen | Chroma key background replace |
| Audio | Library SFX/music, VO record, fade/effects |
| Titles | Intro/outro templates |
| Effects | FG/BG effects library; image filters (non-destructive editor) |
| Share | YouTube/Facebook/TikTok etc., GIF, sticker, flipbook, **export all images**, project transfer |
| Extra | Timelapse interval, live video mix, rotoscoping from video, keyboard shortcuts |
| Education | Classroom / MDM notes on site |

DSLR compatibility: site troubleshooting list — VERIFY LIVE.

---

## Recommended production stages

```text
Shot list → set + light + tripod → install SMS
  → project FPS/quality → capture with onion skin
  → edit holds/retimes → audio/titles
  → export master + optional image sequence
  → optional NLE/Krita → publish HITL
```

---

## Help topic index (useful deep links)

Base: `https://www.stopmotionstudio.com/help/stopmotion/en/`

| Topic | Page slug (append to base) |
|-------|----------------------------|
| First movie | `creating-your-first-movie.html` |
| Onion skin | `onion-skinning.html` |
| Guides | `animation-guides.html` |
| FPS / speed | `adjust-the-speed-of-your-movie.html` |
| Shooting on twos | `shooting-on-twos.html` |
| Freeze frame | `freeze-or-pause-a-frame.html` |
| Export format | `selecting-export-type-and-format.html` |
| Export all images | `export-all-images.html` |
| YouTube share | `share-movie-to-youtube.html` |
| Green screen | `using-the-green-screen.html` |
| DSLR | `using-a-dslr-camera.html` |
| Project transfer | `transfer-a-project-using-icloud-dropbox-or-other-services.html` |
| Rotoscoping | `rotoscoping-guide.html` |

---

## Scaffold (Fable)

```text
workspace/creative/<slug>/
  00_script/
  01_set_refs/
  02_sms_project/    # local project backups
  03_capture_raw/
  04_exports/
  05_presets/
  notes.md
```

Gitignore keeps heavy exports/masters local — see root `.gitignore`.

---

## Handoff

| Output | Next |
|--------|------|
| Master MP4/MOV | Platform HITL or `youtube-live-encoder` planning |
| Image sequence | `creative-pipeline-builds` / Resolve |
| Hybrid draw cleanup | `animation-dev-kit` (Krita) |

Never commit cloud tokens or entire project libraries.
