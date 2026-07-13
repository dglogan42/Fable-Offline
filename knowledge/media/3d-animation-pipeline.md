# 3D animation & VFX — offline pipeline notes

**Skill:** `3d-animation-dev-kit`  
**Ad/education seed (VERIFY LIVE):** [Media Design School — 3D Animation & VFX courses](https://www.mediadesignschool.com/courses/3d-animation-vfx-courses-degrees)  
**Default DCC:** [Blender download](https://www.blender.org/download/) · [Manual](https://docs.blender.org/manual/) · [Requirements](https://www.blender.org/download/requirements/)  

Not endorsement of any school or vendor. Not careers advice.

---

## Education seed (MDS public page)

Public course hub themes (re-check live):

| Course | Duration (marketing) | Path |
|--------|----------------------|------|
| Bachelor of Art & Design – 3D Animation & VFX | Three academic years | [Bachelor page](https://www.mediadesignschool.com/courses/undergraduate-studies/bachelor-art-design-3d-animation-vfx) |
| Graduate Diploma of Creative Technologies – 3D Animation & VFX | One academic year | [GDCT page](https://www.mediadesignschool.com/courses/postgraduate-studies/graduate-diploma-creative-technologies-3d-animation-vfx) |
| NZ Certificate in Arts and Design | ~20 weeks foundation | [Certificate page](https://www.mediadesignschool.com/courses/foundation-level-courses/nz-certificate-arts-and-design) |

Page also claims (VERIFY LIVE): NZ #1 animation school (Animation Career Review), Houdini Certified school, Unity authorised training partner NZ, festival recognition for student films, long-running 3D programme.

**Fable use:** map formal study options vs self-taught production kit; never invent fees or admissions.

---

## Industry tool awareness

| Tool | Common role | License |
|------|-------------|---------|
| **Blender** | Full pipeline FOSS (model, rig, anim, render, Grease Pencil) | Free GPL — blender.org |
| **Maya** | Studio character anim / pipeline staple | Autodesk commercial / education |
| **Houdini** | Procedural VFX / sims | SideFX commercial / education |
| **Cinema 4D** | Motion graphics | Maxon commercial |
| **Unity** | Real-time / games / interactive | Unity terms |

Schools often teach multi-tool; offline Fable default remains **Blender** unless user already owns another DCC.

---

## Production stages

```text
Brief → board/animatic → layout
  → model → UV/texture → rig
  → animate → (sim) → light
  → render sequence → comp → edit/export
```

### Frame budget

`frames ≈ seconds × FPS` (+ handles).  
Learning target: **one polished 3–8s shot** before multi-shot films.

### Blender engines (seed)

| Engine | Use |
|--------|-----|
| EEVEE | Fast previews / stylized |
| Cycles | Quality path tracing |

Prefer **PNG/EXR sequences** then encode; safer recovery than only one MP4.

---

## Blender install (seed)

- Official: [blender.org/download](https://www.blender.org/download/)  
- Stable for delivery; LTS for long shows; avoid daily experimental for finals  
- Platforms: Windows, macOS (Apple Silicon), Linux, Steam, MS Store  

Versions change often — note version in `notes.md`.

---

## Scaffold

```text
workspace/creative/<slug>/
  00_brief/
  01_animatic/
  02_assets/
  03_shots/
  04_renders/
  05_comp/
  06_exports/
  07_presets/
  notes.md
```

---

## Hybrid handoff

| Need | Skill |
|------|--------|
| 2D frame animation | `animation-dev-kit` (Krita) |
| Physical stop-motion | `stop-motion-dev-kit` |
| Color / social cut | `creative-pipeline-builds` |

---

## Anti-patterns

- Feature-film scope on day one  
- Cracked Autodesk/SideFX/Maxon software  
- Committing multi-GB caches and EXR trees to git  
- Guaranteeing studio jobs from any school or tutorial path  
