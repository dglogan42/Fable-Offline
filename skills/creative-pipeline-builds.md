# Creative pipeline builds (Adobe · CapCut · DaVinci Resolve)

**WHEN_TO_USE:** Installing/managing **Adobe Creative Cloud** desktop apps ([CC desktop app](https://www.adobe.com/nz/creativecloud/desktop-app.html)), planning **repeatable “builds”** (export packages) for **Photoshop / Lightroom**, **CapCut** edits, or **DaVinci Resolve** timelines — project templates, preset stacks, batch export/render runbooks, handoff to YouTube Live / TikTok / IG. Not one-off “click randomly in the UI” without a recipe.

## Stance
You design **licensed, user-operated** creative pipelines. “Automated build” means **presets, templates, actions, export/render queues, and checklists** the user runs in official apps — not cracked installers, not license bypass, not unattended bot farms that violate ToS.

**Not legal advice.** Adobe, CapCut (ByteDance), Blackmagic Design trademarks remain theirs. User holds valid licenses/subscriptions.

Fable does **not** drive GUI automation that logs into accounts or bypasses DRM. User **HITL** for installs, exports, and publishes.

---

## App map

| Tool | Role in pipeline | Official start |
|------|------------------|----------------|
| **Creative Cloud desktop** | Install/update **Photoshop**, **Lightroom**, Premiere, etc. | [CC desktop app (NZ)](https://www.adobe.com/nz/creativecloud/desktop-app.html) · [Download CC](https://creativecloud.adobe.com/apps/download/creative-cloud) |
| **Lightroom** | Ingest, culling, develop presets, batch export |
| **Photoshop** | Pixel builds, actions/droplets, composites, stills for thumbnails |
| **CapCut** | Fast short-form cut/captions/export (mobile/desktop) |
| **DaVinci Resolve** | Long-form edit, color, Fairlight, deliver page renders |

Knowledge: `knowledge/media/creative-pipeline-builds.md`

---

## Pipeline shape (“build”)

```text
1. CC desktop → install/update licensed apps
2. Project template folder (workspace/creative/<slug>/)
3. Still path: Lightroom catalog/preset → export → optional Photoshop action
4. Motion path A: CapCut project template → export preset (9:16 / 16:9)
5. Motion path B: Resolve project template → Deliver render presets
6. Package: exports/ + notes.md + (optional) RSS item / social handoff
7. Publish: YouTube / TikTok / IG — separate skills (HITL)
```

A **build** = reproducible folder + presets + export settings + verification checklist.

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end pipeline recipe | **pipeline-plan** |
| Install/manage via CC desktop | **cc-desktop-setup** |
| Lightroom batch stills build | **lightroom-build** |
| Photoshop action/export build | **photoshop-build** |
| CapCut short-form edit build | **capcut-build** |
| DaVinci Resolve edit + deliver | **resolve-build** |
| Folder template scaffold | **project-scaffold** |
| Verify exports | **verify-package** |
| Hand off to social/live | **publish-handoff** |
| Persist recipe (no licenses) | **write-knowledge** |
| Short answer | **brief** |

Default: **pipeline-plan** if multi-app; single-app procedures if named.

---

## pipeline-plan

**Input:** deliverable type (stills, Reel/TikTok, YouTube long, multi-platform), assets on hand, apps installed.

**Output:**
1. Verdict — ready / missing license app / missing template  
2. Path choice: stills (LR/PS) vs CapCut vs Resolve (or hybrid)  
3. Scaffold path under `workspace/creative/`  
4. Ordered builds with presets to create once  
5. Export matrix (resolution, fps, codec, loudness target if known)  
6. Publish handoff skills  
7. OPEN  

---

## cc-desktop-setup

User **CLICK** only:

1. Open [Adobe CC desktop app page](https://www.adobe.com/nz/creativecloud/desktop-app.html) or [download Creative Cloud](https://creativecloud.adobe.com/apps/download/creative-cloud)  
2. Install **Creative Cloud desktop** with Adobe ID (licensed)  
3. Apps tab → Install **Photoshop**, **Lightroom** (or Lightroom Classic), others as needed  
4. Prefer auto-update for security; pin versions only if project requires  
5. Optional: install location via Preferences → Apps (Help: change install location)  

Do **not** coach GenP, firecracker, or piracy tools.

---

## project-scaffold

Suggest structure (user creates):

```text
workspace/creative/<slug>/
  00_inbox/          # camera originals
  01_selects/        # culled stills / clips
  02_edit/           # .prproj / .drp / CapCut project if stored
  03_graphics/       # PS builds, thumbnails
  04_exports/        # final packages
  05_presets/        # LR/PS/CapCut/Resolve preset notes
  notes.md           # recipe + versions
```

Relative paths only under `workspace/`.

---

## lightroom-build

**Build =** import → apply develop preset → sync → export preset.

Checklist:
1. Catalog location (local SSD preferred)  
2. Import from `00_inbox`  
3. Flag/star cull → `01_selects`  
4. Develop preset (name it; document in notes.md)  
5. Export preset: long edge, sRGB/web, quality, naming `{slug}_{####}` → `04_exports/stills/`  
6. Optional: “Edit in Photoshop” for retouch tier  

---

## photoshop-build

**Build =** action/droplet or scripted batch (user runs in PS).

Checklist:
1. Source from LR export or `01_selects`  
2. Record **Action**: resize, sharpen for web, watermark if licensed brand asset  
3. Batch / Image Processor / droplet → `04_exports/stills/`  
4. Thumbnail / YouTube end-card variants if needed  
5. Save `.psd` masters sparingly in `03_graphics/`  

Never require cracked fonts/plugins.

---

## capcut-build

**Build =** template project + export preset for short-form.

| Step | Notes |
|------|--------|
| Aspect | 9:16 default for Reels/TikTok/Shorts; 16:9 for YT landscape |
| Template | Intro, captions style, music bed (licensed), end CTA |
| Captions | Auto-caption then human fix |
| Export | Codec/resolution per platform; max length awareness |
| Storage | Export to `04_exports/short/` |

CapCut cloud/login is user HITL. No account-farm automation.

Cross: `instagram-selfie-selector`, `tiktok-ads-create` (creative only), `youtube-live-encoder` (different: live).

---

## resolve-build

**Build =** Resolve project template + Deliver presets.

| Page | Use |
|------|-----|
| Media | Ingest `00_inbox` / proxies |
| Cut/Edit | Assembly; leave room for color |
| Color | Node stack template; stills for grades |
| Fairlight | Loudness targets for platform (document target) |
| Deliver | Render queue: YouTube 1080/4K, vertical 1080×1920, ProRes master optional |

| Automation (legitimate) | Notes |
|-------------------------|--------|
| Project templates | Save blank `.drp` / template project |
| Render presets | Save Deliver presets by platform |
| Scripting / API | Advanced; only if user already uses official Blackmagic scripting — high-level only |

Do not distribute paid Resolve Studio keys.

---

## verify-package

| Check | |
|-------|--|
| Files exist in `04_exports/` | |
| Resolution/fps/duration match brief | |
| Audio not clipped; captions readable | |
| No accidental secrets in lower-thirds | |
| notes.md lists app versions + preset names | |

---

## publish-handoff

| Destination | Skill / protocol |
|-------------|------------------|
| YouTube VOD | User upload Studio |
| YouTube Live | `youtube-live-encoder` |
| TikTok organic/ads | CapCut export + `tiktok-ads-create` / organic HITL |
| Instagram | `instagram-selfie-selector` for stills/Reels packaging |
| RSS announce | `rss-share` |

---

## Forbidden
- Adobe/CapCut/Resolve cracks, keygens, patched hosts files  
- Automating mass account spam or fake engagement  
- Committing licensed stock without rights  
- Storing Adobe passwords or stream keys in repo  

## Local knowledge
- `knowledge/media/creative-pipeline-builds.md`  
- Adobe entry: `knowledge/media/adobe-cc-desktop.md`  

## Companion
| Skill | Use |
|-------|-----|
| `youtube-live-encoder` | Live path |
| `tiktok-ads-create` / TTCX | Paid creative volume |
| `rss-share` | Changelog of builds |
| `pdf-render` | Client PDF stills packages |
