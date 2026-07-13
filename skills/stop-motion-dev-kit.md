# Stop / motion dev kit (Stop Motion Studio)

**WHEN_TO_USE:** User wants a **stop-motion** production kit — capture plan, onion skin, FPS, green screen, DSLR/remote camera, export video/GIF/image sequence — especially with **Stop Motion Studio** (Cateater). Triggers: “stop motion”, “stop-motion”, “claymation”, “LEGO short”, “onion skin capture”, “Stop Motion Studio”, download/install the app.

**Official entry (VERIFY LIVE):**  
- [Download Stop Motion Studio](https://www.stopmotionstudio.com/download/index.html)  
- Product: [stopmotionstudio.com](https://www.stopmotionstudio.com/index.html)  
- Help hub: [stopmotionstudio.com/help/stopmotion/en/](https://www.stopmotionstudio.com/help/stopmotion/en/) (e.g. [Adjust the speed / FPS](https://www.stopmotionstudio.com/help/stopmotion/en/adjust-the-speed-of-your-movie.html))

Companion skills: `animation-dev-kit` (Krita 2D draw-frame), `creative-pipeline-builds` (post-export grade/NLE), platform publish skills (HITL).

## Stance
You coach **user-operated stop-motion** with **licensed/purchased** Stop Motion Studio (or equivalent capture tools the user already owns). “Automate” means **checklists, folder scaffolds, FPS/export recipes, and Fable workflow recipes** — **not** driving the app UI, not cracked installers, not unattended bot farms.

**Not legal advice.** Stop Motion Studio, Cateater, LEGO®, and platform marks remain their owners. User pays for Pro/one-time purchase per vendor terms. Prefer official download / App Store / Google Play / Amazon channels.

Fable does **not** install apps or auto-upload to YouTube/TikTok. User **HITL** for capture, export, and publish.

---

## Kit map

| Piece | Role |
|-------|------|
| **Stop Motion Studio 2** | Capture + frame editor + audio/titles + share |
| **Onion skin / guides** | Smooth motion between poses |
| **Camera path** | Device cam, USB cam, **DSLR** (compat list), remote cam / remote shutter |
| **FPS / speed** | Project Settings → FPS (start ~**6**; **12+** smoother) |
| **Green screen** | Chroma key backgrounds |
| **Export** | Video (up to 4K/1080p), GIF, sticker, **export all images**, project transfer |
| **External NLE** | Optional grade/montage after image-sequence export |

Knowledge: `knowledge/media/stop-motion-studio.md`

---

## Pipeline shape (“stop-motion build”)

```text
1. Story / shot list (script notes)
2. Set + lighting + fixed camera (tripod); disable auto-exposure if possible
3. Install Stop Motion Studio from official download / store
4. New project → set FPS + aspect + quality
5. Capture frames (onion skin on; remote shutter if available)
6. Edit timeline (copy/paste, holds/freeze, in-out points, retime)
7. Audio / titles / optional green screen + effects
8. Export: master video + optional PNG/JPEG sequence
9. Package under workspace/creative/<slug>/
10. Publish HITL (YouTube / TikTok / IG / RSS skills)
```

A **stop-motion build** = scaffold folder + FPS recipe + capture checklist + export matrix + backup of project file.

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end recipe | **sm-plan** |
| Get the app (official) | **download-install** |
| Project folders | **project-scaffold** |
| Rig / lighting / tripod | **set-rig** |
| FPS and timing | **fps-recipe** |
| First short (hello world) | **capture-lab** |
| Onion skin + guides | **onion-guides** |
| Camera modes (auto/manual/DSLR/remote) | **camera-setup** |
| Green screen | **chroma-key** |
| Timeline edit (holds, retime, in-out) | **edit-timeline** |
| Audio / titles | **audio-titles** |
| Export video / GIF / all images | **export-package** |
| Transfer project mobile ↔ desktop | **project-transfer** |
| Hand off grade/social | **publish-handoff** |
| Compare to Krita draw-frame | **vs-krita** |
| Short answer | **brief** |

Default: **sm-plan**. Learning: **capture-lab**. Export only: **export-package**.

---

## sm-plan

**Input:** subject (LEGO/clay/objects), length, target platform, gear (phone / DSLR), FPS preference if any.

**Output:**
1. **Verdict** — ready / missing tripod-light / missing app  
2. **download-install** steps for user’s OS  
3. **project-scaffold** path  
4. **set-rig** checklist  
5. **fps-recipe** (seconds × FPS = frame count)  
6. Ordered capture → edit → export  
7. **export-package** matrix  
8. **publish-handoff**  
9. **OPEN** — VERIFY LIVE download + help after app updates  

---

## download-install

User **CLICK** only — official sources:

| Platform | Entry |
|----------|--------|
| **Windows / macOS desktop** | [stopmotionstudio.com/download](https://www.stopmotionstudio.com/download/index.html) |
| Stop Motion Studio **2** Windows | Win 10+ — site MSIX (VERIFY LIVE filename) |
| Stop Motion Studio **2** macOS | macOS **13+** — site DMG |
| Older OS builds | “Older Releases” section on same download page (limited support) |
| App stores | Windows / Apple App Store also linked from download page |
| Mobile | iOS/iPad, Android, Amazon Fire — store listings from [product site](https://www.stopmotionstudio.com/index.html) |

Do **not** coach sideloaded cracked APKs/MSIs. Note vendor marketing: **one-time purchase / no monthly subscription** (VERIFY LIVE pricing; free vs Pro tiers vary by store).

---

## project-scaffold

```text
workspace/creative/<slug>/
  00_script/              # shot list, dialogue
  01_set_refs/            # set photos, color charts
  02_sms_project/         # exported project backups / transfers (local)
  03_capture_raw/         # optional stills if shot outside app
  04_exports/             # master video, GIF, image sequence
  05_presets/             # fps, export notes (markdown)
  notes.md                # FPS, res, frame count, gear, app version
```

---

## set-rig

1. **Tripod** or solid mount — camera must not drift  
2. **Consistent light** — avoid auto white-balance hunting; lock WB/exposure when app allows  
3. Mark character positions (tape on set)  
4. Clear hands/strings or plan **masking** / paint-out in editor  
5. Power + storage: long shoots fill device storage fast at 4K  

---

## fps-recipe

From official help ([Adjust the Speed](https://www.stopmotionstudio.com/help/stopmotion/en/adjust-the-speed-of-your-movie.html)):

| FPS | Typical use |
|-----|-------------|
| **6** | Start here — classic stop-motion feel, fewer frames/sec |
| **12+** | Smoother; more capture work |
| ~**25** | “TV-like” density (help compares regular TV ~25 fps) |

**Math:** duration_seconds × FPS ≈ **frames needed** (before holds).  
Example: 10s @ 12 FPS ≈ **120 frames**.

**In app:** Movie editor → **Project Settings** → **FPS** slider → Done.  
Use **freeze/pause frame** for holds without re-shooting (help tip).

Also see help topics: **Shooting on Twos**, freeze/pause, retime sequence (VERIFY LIVE steps in app version).

---

## capture-lab

Minimal first film:

1. Install app → New movie  
2. Set FPS (start **6**)  
3. Enable **onion skin**  
4. Capture 12–24 frames of a simple move (object slides left)  
5. Playback; adjust onion opacity if needed  
6. Export a short HD video to `04_exports/`  
7. Write `notes.md` with FPS and frame count  

---

## onion-guides

Help topics: Onion Skinning, Animation Guides.

- Onion skin shows previous pose for spacing  
- Grids, aspect masks, path layer, paint marks for motion planning  
- Reference image/video for complex scenes  
- Keep moves small and even between frames  

---

## camera-setup

| Mode | Notes |
|------|--------|
| Device camera | Auto or full manual (focus, exposure, ISO, WB) when supported |
| USB / external | Per help “Using a USB Camera” |
| **DSLR** | Live View + shutter/ISO/aperture control — [compat list](https://www.stopmotionstudio.com/en/troubleshooting/Supported_DSLR_Cameras) VERIFY LIVE |
| Remote camera | Second device as remote cam |
| Remote shutter | Headphone volume, Apple Watch, Bluetooth shutter |
| RAW / ProRAW | When device supports — for later grade |
| Timelapse | Interval capture feature |
| Live video mix | Mixed live + stop-motion (product feature) |

---

## chroma-key

- Built-in **green screen** for live/background replace  
- Adjust color + sensitivity (help: Color and Sensitivity)  
- Even lighting on green; avoid shadows/wrinkles on screen  

---

## edit-timeline

Product + help: frame-by-frame view, zoomable timeline, cut/copy/paste between projects, in/out points for loop preview, freeze/pause, retime, merge frames for fast motion, undo/redo.

Prefer **duplicate project** before destructive mass deletes.

---

## audio-titles

- Built-in SFX/music library; record VO; fade/volume/effects  
- Opening titles + closing credits templates  
- Respect music license / school-safe libraries for publish  

---

## export-package

Share / export (product + help: Selecting Export Type and Format, Export All Images, YouTube share):

| Output | Use |
|--------|-----|
| **Video** 1080p / **4K** | Master for YouTube etc. |
| **GIF** | Web/social loops |
| iMessage sticker | Apple ecosystem |
| **Export all images** | External NLE / Resolve / Krita cleanup |
| Project file | Mobile ↔ desktop transfer (iCloud/Dropbox/Drive/AirDrop etc.) |

User saves masters under `04_exports/`. Never commit huge sequences to git.

---

## project-transfer

Help: transfer via iCloud, Dropbox, other services, AirDrop, mobile→desktop export.  
Start on phone, finish on Windows/Mac when useful.  
Backup project before OS upgrades.

---

## publish-handoff

| Next | Skill |
|------|--------|
| Color / long edit from image sequence | `creative-pipeline-builds` |
| Draw-over / 2D hybrid | `animation-dev-kit` (Krita) |
| YouTube Live | `youtube-live-encoder` (separate from export) |
| Short-form recut | CapCut path in creative-pipeline |
| Feed announce | `rss-share` |

User posts manually; no auto-share credentials in Fable.

---

## vs-krita

| | **Stop Motion Studio** | **Krita (`animation-dev-kit`)** |
|--|------------------------|----------------------------------|
| Medium | Physical objects + camera | Drawn raster frames |
| Strength | Capture, onion, green screen, share | Frame-by-frame drawing, transform masks |
| Hybrid | Export images → Krita cleanup or NLE | Export PNG → SMS or Resolve |

---

## Output contract

1. **Verdict** first  
2. **OS-specific download** link(s)  
3. **FPS + frame count** estimate  
4. **Scaffold + ordered checklist**  
5. **Export matrix**  
6. **OPEN** — re-verify download/help for user’s app version  
7. Not a substitute for set safety or school media policy  

---

## Anti-failure

- Do not recommend unofficial “free Pro” APKs/cracks  
- Do not skip tripod — hand-held drift ruins onion-skin registration  
- Do not promise 4K on all free tiers — VERIFY LIVE store capabilities  
- Do not auto-post or store social tokens  
- Label guesses when UI labels differ by platform/version  
- Heavy media stays under `workspace/creative/` (gitignored)  
