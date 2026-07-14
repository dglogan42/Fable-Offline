# VTube Studio resource kit

**WHEN_TO_USE:** User sets up **VTube Studio (VTS)** for Live2D VTubing — install (Steam/iOS/Android), face/hand tracking, items/props, Twitch integration, collab, plugins/API, OBS handoff, or dumps [denchisoft.com](https://denchisoft.com/). Triggers: “VTube Studio”, VTS, Live2D tracking, DenchiSoft, vtuber webcam.

**Official (VERIFY LIVE):**  
- Site: [https://denchisoft.com/](https://denchisoft.com/)  
- Steam: [app/1325860 VTube Studio](https://store.steampowered.com/app/1325860/VTube_Studio/)  
- Docs: [denchisoft.com/documentation](https://denchisoft.com/documentation)  
- Wiki: [github.com/DenchiSoft/VTubeStudio/wiki](https://github.com/DenchiSoft/VTubeStudio/wiki)  
- Discord: [discord.gg/VTubeStudio](https://discord.gg/VTubeStudio) · Twitter: [@VTubeStudio](https://twitter.com/VTubeStudio)  
- License / branding: denchisoft.com/license · /branding  

Companions: `youtube-live-encoder` (stream out), `steam-sim-launch` (owned Steam apps), `animation-dev-kit` / `3d-animation-dev-kit` (asset creation), `privacy-host-map`, `rss-share` (site feed if used).

## Stance
You coach **official VTube Studio setup and feature literacy**. Fable does **not** crack VTS, bypass Steam/App Store, or stream as the agent of record.

**Not legal or financial advice.** Live2D models have separate licenses — only use models you own or are licensed to perform. One-time payment claims **VERIFY LIVE** on Steam/store pages.

**Refuse:** pirated VTS builds; stolen model files; committing Twitch/stream keys or plugin API secrets.

---

## Product map (homepage seed)

| Surface | Notes |
|---------|--------|
| **Live2D performance** | Bring Live2D models to life for Virtual YouTubers |
| **Tracking** | Webcam (OpenSeeFace) · iPhone/Android as tracker · hand tracking · eyes/wink |
| **Scene control** | Hotkeys, mic lipsync, PNG props, VFX post |
| **Items** | Attach images/animations/Live2D props with tracking/hotkeys |
| **Collab** | Steam-friends multiplayer — models on each other’s screens |
| **Twitch** | Emotes, redeems, subs, chat → hotkeys |
| **Plugins** | VTS API for third-party tools |
| **Platforms** | Steam PC/Mac · iOS (FaceID/A12+) · Android (ARCore) |
| **Business model seed** | Non-recurring one-time payment; active development |

Knowledge: `knowledge/media/vtube-studio.md` · Privacy: `knowledge/privacy/vtube-studio-hosts.md`

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end kit | **vts-plan** |
| Hardware / OS fit | **sys-check** |
| Install / buy | **install-vts** |
| First tracking setup | **first-track** |
| Items & props | **item-system** |
| Hand / gesture tracking | **hand-track** |
| Twitch integration | **twitch-hook** |
| Collab session | **collab-setup** |
| Plugins / API | **plugin-path** |
| Stream handoff | **stream-handoff** |
| Support / Discord | **get-help** |
| Privacy hosts | **host-map** |
| Persist notes | **write-knowledge** |
| Short answer | **brief** |

Default: **vts-plan**. New user: **sys-check** → **install-vts** → **first-track** → **stream-handoff**.

---

## vts-plan

**Input:** OS (Win/Mac/mobile), webcam vs phone tracker, has Live2D model?, Twitch?, collab?

**Output:**
1. **Verdict** — platform path + tracker path  
2. **sys-check**  
3. **install-vts** with official links  
4. **first-track**  
5. Optional: items / Twitch / collab / plugins  
6. **stream-handoff**  
7. OPEN — VERIFY LIVE store requirements  

---

## sys-check

| Path | Need (site seed) |
|------|------------------|
| Steam PC/Mac | Webcam for OpenSeeFace **or** phone as tracker |
| iOS | Face ID **or** A12+ |
| Android | **ARCore**-capable device |
| Hand tracking | Webcam-based (VERIFY LIVE quality) |
| Model | Licensed Live2D runtime model (user-supplied) |

---

## install-vts

User HITL only:

1. Steam: [app 1325860](https://store.steampowered.com/app/1325860/VTube_Studio/)  
2. Or mobile stores (Play `com.denchi.vtubestudio` / iOS VERIFY LIVE)  
3. Launch VTS · grant camera/mic as needed  
4. Import Live2D model per official docs  

---

## first-track

1. Choose tracker: webcam vs iPhone/Android bridge  
2. Calibrate face · test eyes/wink · lipsync with mic  
3. Map basic hotkeys (expressions, animations)  
4. Optional: enable hand tracking  

Docs: denchisoft.com/documentation + GitHub wiki.

---

## item-system

Import/attach props to model (images, animations, Live2D items). Wiki: Item System · Live2D Items.

---

## hand-track

Webcam hand tracking → expressions/animations. Wiki: Hand-Tracking. Practice gestures.

---

## twitch-hook

Configure Twitch in VTS (HITL OAuth). Map redeems/subs/chat to hotkeys; emote throw. Never store OAuth tokens in git.

---

## collab-setup

Steam friends collab — invite session; models appear in each other’s VTS (latency claims VERIFY LIVE). Related Steam listing seed app 2384550 — confirm purpose live.

---

## plugin-path

VTS API for plugins (donations, controllers). Wiki: Plugins. Only install trusted plugins; review permissions.

---

## stream-handoff

1. VTS output / virtual cam / window capture  
2. OBS/encoder compose  
3. Skill **`youtube-live-encoder`** or other destination  
4. Stream key hygiene — never commit keys  

---

## get-help

1. Official documentation  
2. Discord FAQ then community  
3. Twitter @VTubeStudio · changelog  
4. Impressum/privacy on denchisoft.com  

---

## host-map

`knowledge/privacy/vtube-studio-hosts.md`

---

## write-knowledge

```text
workspace/media/vtube-studio/
  setup-notes.md
  hotkey-map.md
```

No model binaries or secrets.

---

## Output contract

1. Verdict — platform + tracker  
2. Install + first-track steps  
3. Optional feature path  
4. Stream handoff  
5. OPEN / VERIFY LIVE  

---

## Anti-failure

- No cracked VTS or pirated Live2D models  
- No invented Steam prices or feature dates  
- No stream keys / Twitch tokens in git  
- Separate model rights from VTS app license  
