# Animation dev kit (Krita frame-by-frame)

**WHEN_TO_USE:** User wants a **frame-by-frame animation workflow**, **walk cycle**, **storyboard → animatic → clip plan**, **onion skins**, **timeline/layer hygiene**, **transform-mask motion**, or **render export** with **Krita** (FOSS raster animation). Triggers: “animate in Krita”, “animation dev kit”, “walk cycle”, “render animation”, “onion skin”, File → Render Animation / FFmpeg.

**Source of truth (re-verify live):** [Animation with Krita](https://docs.krita.org/en/user_manual/animation.html) (User Manual). Related: [Render Animation](https://docs.krita.org/en/reference_manual/render_animation.html), Timeline / Onion Skin / Curves / Storyboard dockers, [Import Animation](https://docs.krita.org/en/reference_manual/import_animation.html), [Audio for Animation](https://docs.krita.org/en/reference_manual/audio_for_animation.html), [Japanese Animation Template](https://docs.krita.org/en/user_manual/japanese_animation_template.html).

## Stance
You coach **user-operated Krita** workflows. Krita is specialized in **frame-by-frame raster animation** and keeps frames in **RAM** — plan clip length, resolution, layers, and backups. Fable does **not** run Krita GUI automation or ship FFmpeg binaries.

**Not legal advice.** Krita is free/open-source software under its own licenses (KDE / project terms). Trademarks remain with rights holders. User installs Krita + optional FFmpeg themselves.

Hand off finished exports to `creative-pipeline-builds`, `youtube-live-encoder`, TikTok/IG skills as **HITL** publish steps — not auto-post.  
Physical object capture (camera + clay/LEGO): use **`stop-motion-dev-kit`** (Stop Motion Studio) instead of or hybrid with this skill.  
Full CG / character 3D pipeline: use **`3d-animation-dev-kit`** (Blender-first).

---

## Kit map (dockers + stages)

| Piece | Role |
|-------|------|
| **Animation workspace** | Window → Workspace → **Animation** — timeline + anim dockers |
| **Timeline docker** | Keyframes, holds, layers pinned to timeline |
| **Onion Skin docker** | Past (red) / future (green) ghost frames; opacity & count |
| **Animation Curves docker** | Scalar / minor tween curves; transform-mask motion |
| **Storyboard docker** | Shot plan (composition, movement, audio notes) |
| **Render Animation** | Frame sequence and/or video (FFmpeg path) |
| **External NLE** | Animatic montage: Kdenlive, OpenShot, Olive, etc. |

Knowledge: `knowledge/media/krita-animation.md`

---

## Pipeline shape (“animation build”)

```text
1. Script / outline (any text editor)
2. Storyboard (few frames; Storyboard docker or sparse anim frames)
3. Animatic in external video editor (subdivide into ≤10s clips @ ~12 fps to start)
4. Per clip in Krita: import storyboard frames → rough → keys → inbetweens → clean/line
5. Memory hygiene (merge layers, crop, grayscale where OK, lower res early)
6. Incremental Backup at milestones
7. File → Render Animation (PNG sequence ± video)
8. Assemble clips in NLE → WebM/MP4 → platform skills (HITL)
```

An **animation build** = named folder under `workspace/creative/<slug>/` + fps/res settings + layer rules + export checklist + backup policy.

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end kit recipe | **anim-plan** |
| Install / open Krita animation UI | **workspace-setup** |
| Project folder + document settings | **project-scaffold** |
| Storyboard → animatic clip list | **storyboard-animatic** |
| RAM / duration / resolution strategy | **memory-budget** |
| First animation (walk cycle tutorial path) | **walkcycle-lab** |
| Timeline keyframes / holds / pin layers | **timeline-hygiene** |
| Onion skin config | **onion-setup** |
| Multi-layer animation | **layer-pin** |
| Move cycle without redrawing pixels | **transform-mask-move** |
| Export sequence / video | **render-export** |
| FFmpeg path notes | **ffmpeg-link** |
| Backup / milestone | **backup-policy** |
| Hand off to edit/social/live | **publish-handoff** |
| Short answer | **brief** |

Default: **anim-plan** if multi-shot; **walkcycle-lab** if learning; **render-export** if only exporting.

---

## anim-plan

**Input:** target length, fps, resolution, style (rough/clean), machine RAM class if known, deliverable (loop, short, scene).

**Output:**
1. **Verdict** — feasible on typical RAM / must split clips / missing tools  
2. **Stages** — script → board → animatic → clip list  
3. **Per-clip budget** — prefer ≤10s; start ~**12 fps** (Krita manual guidance for beginners)  
4. **Canvas** — e.g. early rough at ~800×450; raise res for line art  
5. **Scaffold** path under `workspace/creative/`  
6. **Layer plan** — few layers; pin active anim layers  
7. **Export matrix** — PNG sequence + GIF/WebM/MP4; FFmpeg notes  
8. **Handoff** — NLE assemble + platform skills  
9. **OPEN** — VERIFY LIVE docs.krita.org after version upgrades  

---

## workspace-setup

User **CLICK** only:

1. Install Krita from [krita.org](https://krita.org/) (official builds)  
2. Open or create document  
3. **Window → Workspace → Animation**  
4. Confirm Timeline at bottom; enable Onion Skin, Curves, Storyboard dockers as needed (**Settings → Dockers**)  
5. Status bar: watch **memory** bar (click resolution label) — never let it fill solid  

---

## project-scaffold

Suggest structure (user creates):

```text
workspace/creative/<slug>/
  00_script/           # outline, dialogue notes
  01_storyboard/       # board exports / stills
  02_animatic/         # NLE project + rough timing
  03_krita/            # *.kra masters + Incremental Backups
  04_renders/          # PNG sequences / preview video
  05_presets/          # fps, onion, export notes (markdown)
  notes.md             # fps, res, clip list, FFmpeg path
```

Document settings (from walk-cycle lab, adapt as needed):
- Example canvas: **1280×1024**, **72 dpi**, title set (used as save suggestion)  
- Background: **canvas-color** fill is useful so transparent bits fill with BG  
- Animation layer must stay **semi-transparent** where empty for onion skins (white is a color, not transparency)

---

## storyboard-animatic

Per Krita manual:

1. Script or action outline first  
2. **Storyboard** — composition + movement/camera/audio notes; fewer frames than full anim  
3. Boards keep **important elements in similar screen positions** across shots (viewer eyes stay put)  
4. Export board via **Render Animation** if using anim frames  
5. **Animatic** in an **external** editor (Krita is not a full NLE)  
6. Subdivide into clips ≤ ~10s; at 12 fps, 10s ≈ **120 frames**  
7. Import frames for a clip: **File → Import Animation Frames**  

---

## memory-budget

Krita holds frames in RAM. Reduce consumption:

1. **Merge layers** — fewer layers is better  
2. **Image → Crop Layers to Image Size** — drop off-canvas pixels  
3. **Layers → Convert → Convert Layer Color Space** → grayscale for B/W line layers (~half RAM)  
4. **Work smaller** — even ~20% res cut helps a lot before line art  
5. Close RAM hogs (browsers, chat, streaming) or move them to another device  
6. Prefer short clips over one giant `.kra`  

Status bar memory bar full → slowdowns; export may fail.

---

## walkcycle-lab

Guided path from the manual (teach-by-doing):

1. New file (e.g. 1280×1024, 72 dpi, title `walk cycle`)  
2. Animation workspace  
3. Layers: bottom `environment`, top `walkcycle` (transparent)  
4. Environment: ground line (Straight Line tool)  
5. Draw head/torso on `walkcycle`  
6. Make animated layer: timeline → **Create Duplicate Frame** (not Blank, or you lose content)  
7. Onion skin on; past red / future green  
8. Extremes: legs far apart vs stride; copy keyframes; set fps low (e.g. **4**) to preview  
9. Insert **Hold frames** between keys; draw inbetweens (heel → foot → knee → leg is one workflow)  
10. Color-label keyframes (extremes / first inbetweens / lesser)  
11. Optional second layer `hands` — **pin** to timeline  
12. Optional: group + **Transform mask** + scalar keys for left-right travel; contact-foot sync with guides  
13. **File → Render Animation**  

Do **not** invent contact-timing physics as “correct” without user art direction — describe the method.

---

## timeline-hygiene

- New frames are **not** automatic until the layer is animated (first keyframe / duplicate frame)  
- **Create Blank Frame** clears content; **Create Duplicate Frame** preserves drawing  
- **Alt+drag** on a frame moves it and all after  
- Multi-select → **Hold frames → Insert Hold Frame** between keys  
- Color labels for extremes vs inbetweens  
- Pin layers you are working on (Krita **4.3+** pins new layers by default; older: pin icon)  

---

## onion-setup

- Toggle onion in timeline  
- Onion Skin docker: how many past/future frames, opacity, colors  
- Empty areas must be **true transparency**, not white paint  
- Fix mistakes with **Color to Alpha** filter; prefer prevention  

---

## layer-pin

- Timeline can hide layers not pinned — feature for busy scenes  
- Pin active anim layers via pin icon while layer selected  
- Recommend pinning every layer currently animated  

---

## transform-mask-move (Krita 5.0+)

1. Group animated layers  
2. Right-click group → **Add → Transform mask**  
3. Animation Curves docker; add **scalar** keyframes (diamond markers)  
4. Transform tool: first frame start position, last frame end; confirm with Enter  
5. Repeat walk cycle frames so travel duration matches steps  
6. For sliding feet: mark foot-plant frames with guides; adjust transform per plant so foot sticks  

Curves support ease-in/out; per-frame plant adjust is often faster for walks.

---

## render-export

**File → Render Animation** (replaces old Export Animation).

| Path | Notes |
|------|--------|
| **Image sequence** | Prefer **PNG**; base name + numbering; optional “only unique frames” |
| **Video** | Sequence then encode (or bundled FFmpeg options since 5.2); GIF / MP4 / MKV / OGG etc. |
| Range | First/Last frame from timeline selection |
| Transparent video | **Not supported** as transparent — transparent becomes black; add opaque bottom layer before render |
| Android | Video render unavailable — transfer `.kra` or sequence to desktop |
| MP4 on Windows | Prefer **baseline** profile for broader players (manual tip) |

User places sequence on disk with free space; optional delete sequence after video encode.

---

## ffmpeg-link

- Krita **5.2+** bundles limited FFmpeg (WebM/Matroska/OGG + several codecs) — enough for many users  
- Optional external FFmpeg for more codecs: point path in Render dialog  
  - Windows: [gyan.dev builds](https://www.gyan.dev/ffmpeg/builds/) — **essentials** zip, **not** `shared`  
  - macOS: [evermeet.cx/ffmpeg](https://evermeet.cx/ffmpeg/)  
  - Linux: distro package, often `/usr/bin/ffmpeg` (GIF palette needs adequate version)  
- VERIFY LIVE paths and Krita version notes  

Fable does **not** download or install FFmpeg for the user.

---

## backup-policy

At every milestone (rough done, line art, tough section):

1. **File → Incremental Backup**  
2. Copy project to external drive / user cloud of choice  
3. Take a break (manual tip — long anims need rest)  

Power loss / file corruption → last incremental still usable.

---

## publish-handoff

| Next | Skill |
|------|--------|
| Color / long edit / deliver | `creative-pipeline-builds` (Resolve path) |
| Short-form recut | CapCut build in creative-pipeline |
| YouTube Live | `youtube-live-encoder` |
| Still thumbnails | Lightroom/Photoshop builds |
| Feed announce | `rss-share` |

User owns publish; no auto-upload.

---

## Output contract

1. **Verdict** first  
2. **Recommended procedure** + ordered steps  
3. **Scaffold paths** and fps/res choices  
4. **Memory / backup** warnings when length > few seconds  
5. **Export** checklist  
6. **OPEN** — re-check docs.krita.org for user’s Krita version  
7. **Not** a substitute for art direction or client delivery sign-off  

---

## Anti-failure

- Do not treat white fill as transparent for onion skins  
- Do not plan hour-long 4K frame-by-frame in one `.kra` on low RAM  
- Do not invent FFmpeg install paths that may not exist on the user’s machine  
- Do not coach cracked software; Krita is free — use official channels  
- Do not claim Krita is a full NLE; animatic assembly is external  
- VERIFY LIVE manual after major Krita releases (5.x UI/FFmpeg notes change)  
