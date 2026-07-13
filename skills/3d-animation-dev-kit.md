# 3D animation dev kit (CG pipeline · Blender-first)

**WHEN_TO_USE:** User wants a **3D animation / VFX** production kit — pipeline stages, shot plan, Blender install, modeling→rig→anim→light→render→comp, portfolio clips, or **education pathway map** for 3D Animation & VFX programmes (e.g. Media Design School). Triggers: “3D animation”, “VFX”, “Blender”, “rig character”, “render farm”, “CG short”, “MDS animation”.

**Sources (VERIFY LIVE):**  
- Education seed (ad landing): [Media Design School — 3D Animation & VFX courses](https://www.mediadesignschool.com/courses/3d-animation-vfx-courses-degrees)  
- Production tool (FOSS default): [Download Blender](https://www.blender.org/download/) · [docs.blender.org/manual](https://docs.blender.org/manual/) · [Requirements](https://www.blender.org/download/requirements/)  
- Studio/training (optional paid ecosystem): Blender Studio, vendor docs for Maya / Houdini / C4D if user already licensed  

Companion: `animation-dev-kit` (Krita 2D), `stop-motion-dev-kit` (physical capture), `creative-pipeline-builds` (Resolve/CapCut finish), `youtube-live-encoder` (publish live).

## Stance
You coach **user-operated CG pipelines**. Default DCC for offline Fable work is **Blender** (GNU GPL, free from blender.org). Industry schools and studios also use **Maya, Houdini, Cinema 4D, Unity**, etc. — map those as **awareness / handoff**, not cracked installs.

**Not educational, careers, immigration, or financial advice.** Course lengths, rankings, fees, and “industry ready” claims on school sites must be **VERIFY LIVE**. Fable is not Media Design School, Strayer, Autodesk, SideFX, or Maxon.

“Automate” = **scaffold, checklists, render recipes, Fable workflows** — not driving Blender GUI, not render-farm bots that violate ToS, not piracy.

---

## Two tracks

| Track | Goal |
|-------|------|
| **A · Production kit** | Ship a short CG shot/clip offline with Blender |
| **B · Education map** | Compare formal 3D/VFX study options (seed: MDS page) vs self-taught portfolio |

Always ask which track if unclear. Track B never auto-enrols; user **CLICK** school sites.

---

## Kit map (production)

| Stage | Role |
|-------|------|
| **Story / board** | Script, boards, animatic (link 2D skills) |
| **Layout** | Cameras, blocking, shot lengths |
| **Model / sculpt** | Assets, topology hygiene |
| **UV / texture** | Lookdev materials |
| **Rig** | Bones, constraints, controls |
| **Animate** | Keys, curves, timing |
| **Sim** (optional) | Cloth, particles, fluids — heavy |
| **Light / shade** | Lights, world, materials |
| **Render** | Cycles / EEVEE (or engine of choice) |
| **Comp / edit** | Blender compositor or Resolve |
| **Deliver** | Master video + stills + notes |

Knowledge: `knowledge/media/3d-animation-pipeline.md`

---

## Pipeline shape (“3D build”)

```text
1. Brief: length, style, deliverable (portfolio / social / festival)
2. Install Blender from blender.org (or use licensed DCC user owns)
3. Scaffold workspace/creative/<slug>/
4. Animatic / layout (low poly, grey)
5. Hero asset model → UV → texture
6. Rig → block anim → spline → polish
7. Light → lookdev stills → full render tests
8. Comp + grade → 04_exports/
9. Portfolio cut + notes.md (tools, versions, role)
10. Publish HITL
```

A **3D animation build** = folder scaffold + FPS/res + render settings + versioned `.blend` (or DCC project) + export checklist.

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end | **cg-plan** |
| Blender install | **blender-install** |
| Project folders | **project-scaffold** |
| Shot / frame budget | **shot-budget** |
| First bouncing cube → camera | **hello-shot** |
| Character / prop pipeline | **asset-pass** |
| Rig + animate | **anim-pass** |
| Light + render | **render-pass** |
| Comp + deliver | **finish-pass** |
| Hardware / GPU notes | **machine-budget** |
| Formal study map (MDS seed) | **edu-map** |
| Portfolio shot list | **portfolio-pack** |
| Hand off 2D / stop-mo / social | **publish-handoff** |
| Short answer | **brief** |

Default: **cg-plan**. School inquiry: **edu-map**. Learning: **hello-shot**.

---

## cg-plan

**Input:** concept, seconds, style (stylized/realistic), machine class, track A/B.

**Output:**
1. **Verdict** — feasible scope for hardware/time  
2. **Track** A and/or B steps  
3. **blender-install** (or licensed DCC user names)  
4. **project-scaffold**  
5. **shot-budget** (fps × seconds = frames)  
6. Ordered passes: asset → anim → render → finish  
7. **machine-budget** warnings  
8. **publish-handoff**  
9. **OPEN** — VERIFY LIVE Blender version + school pages  

---

## blender-install

User **CLICK** only:

1. Open [blender.org/download](https://www.blender.org/download/)  
2. Pick OS build (Windows MSI/zip, macOS Apple Silicon, Linux tarball/Snap, Steam, Microsoft Store)  
3. Prefer **stable** release for production; **LTS** if long projects ([LTS page](https://www.blender.org/download/lts/))  
4. Avoid experimental daily builds for finals  
5. Check [system requirements](https://www.blender.org/download/requirements/)  
6. Optional: enable GPU compute in Preferences for Cycles  

Do **not** coach cracked Maya/Houdini/C4D. Educational licenses: user verifies eligibility with Autodesk/SideFX/Maxon directly.

---

## project-scaffold

```text
workspace/creative/<slug>/
  00_brief/           # script, refs, shot list
  01_animatic/        # boards / rough video
  02_assets/          # models, textures, libraries
  03_shots/           # per-shot .blend or DCC scenes
  04_renders/         # image sequences / previews
  05_comp/            # composites
  06_exports/         # masters for publish
  07_presets/         # render settings notes (md)
  notes.md            # fps, res, Blender version, roles
```

Version: Incremental saves (`_v01`, `_v02`); never only one copy of a hero shot.

---

## shot-budget

| Setting | Typical start |
|---------|----------------|
| FPS | **24** film / **25** PAL / **30** social — pick one |
| Resolution | 1280×720 or 1920×1080 for learning; 4K only if hardware allows |
| Frames | `seconds × FPS` (plus handles) |

Example: 5s @ 24 FPS ≈ **120 frames**. One polished 5s shot beats a messy 30s film.

---

## hello-shot

Teach pipeline on a tiny scene:

1. Default cube → keyframe location (frame 1 → 48)  
2. Camera + light  
3. EEVEE preview playblast → `04_renders/playblast/`  
4. Optional Cycles still  
5. Export short MP4 via Video Sequencer or external NLE  
6. Write `notes.md`  

---

## asset-pass

1. Blockout scale (metric units)  
2. Model with clean topology where deform needed  
3. UV unwrap; paint/bake textures  
4. Material library; name collections  
5. Export/import standards if multi-shot (linked libraries when user is ready)  

---

## anim-pass

1. Rig (armature) or use simple parented hierarchy for props  
2. Blocking poses on extremes  
3. Breakdowns → polish (Graph Editor)  
4. Playblast often; fix silhouette/timing before beauty render  

Principles: squash/stretch, arcs, easing — re-derive from refs; no fake “industry secrets.”

---

## render-pass

| Engine (Blender) | Use |
|------------------|-----|
| **EEVEE** | Fast lookdev / realtime-ish |
| **Cycles** | Path-trace quality stills/film |

Checklist: samples, denoise, color management (Filmic/AgX as available), output path as **image sequence** (safer than only video), then encode.

Heavy sims/particles: cache to disk; lower res for tests.

---

## finish-pass

1. Comp (Blender compositor or Resolve)  
2. Grade + audio (licensed music only)  
3. Masters in `06_exports/`  
4. Still frames for portfolio thumbnails  

---

## machine-budget

- GPU VRAM limits texture + render resolution  
- Prefer **proxy** / **preview** before final  
- Close browsers during long renders  
- Overnight renders: power settings; save before  

---

## edu-map (Media Design School seed)

From public MDS page (VERIFY LIVE; rankings/claims are theirs):

| Offering (seed) | Notes from page |
|-----------------|-----------------|
| **Bachelor of Art & Design – 3D Animation & VFX** | ~Three academic years |
| **Graduate Diploma of Creative Technologies – 3D Animation & VFX** | ~One academic year |
| **NZ Certificate in Arts and Design** | Foundation ~20 weeks; FT/PT |

Page themes: industry tools, portfolio, festivals, partners (**Unity**, **Houdini** certified school, VFX Guild). Alumni stories mention studios (e.g. Wētā FX) — **anecdotes**, not guarantees.

**Agent output for edu-map:**
1. Summary of offerings (from knowledge seed)  
2. What formal study adds (structure, feedback, collab films) vs self-taught Blender portfolio  
3. User **CLICK** [MDS 3D Animation & VFX](https://www.mediadesignschool.com/courses/3d-animation-vfx-courses-degrees) + specific course URLs  
4. OPEN: fees, entry, visa, dates — **not** invented  
5. Not careers advice; not an application form  

---

## portfolio-pack

Suggest 3–6 pieces max:

| Piece | Proof |
|-------|--------|
| One strong character or creature shot | Anim + light |
| One environment / layout | Modeling + mood |
| One VFX / sim or hard-surface | Tech range |
| Breakdown reel | Before/after, wire, passes |

Label **role** if team (animator vs lighter vs compositor).

---

## publish-handoff

| Next | Skill |
|------|--------|
| 2D overlays / boards | `animation-dev-kit` |
| Practical effects hybrid | `stop-motion-dev-kit` |
| Grade / deliver | `creative-pipeline-builds` |
| Social / YouTube | platform skills HITL |
| Live stream WIP | `youtube-live-encoder` |

---

## Output contract

1. **Verdict** first  
2. **Track** A/B  
3. **Install + scaffold + frame budget**  
4. **Ordered passes**  
5. **Machine / legal** risks  
6. **OPEN** with VERIFY LIVE links  
7. No job guarantees; no fake school fees  

---

## Anti-failure

- Do not recommend cracked DCC software  
- Do not invent MDS fees, rankings, or admission outcomes  
- Do not scope a feature film for a first project  
- Prefer image sequences over single fragile video export  
- Keep huge caches/renders under `workspace/creative/` (gitignored)  
- Label guesses when Blender UI differs by version (5.x evolves)  
