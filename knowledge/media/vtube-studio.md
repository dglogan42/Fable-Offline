# VTube Studio — official site notes

**Skill:** `vtube-studio-resource-kit`  
**Site:** [https://denchisoft.com/](https://denchisoft.com/) (VTube Studio official website)  
**Privacy:** `knowledge/privacy/vtube-studio-hosts.md`  
**Logo seed:** three-cat crest (site branding / attachment)

**Not legal or financial advice.** VTube Studio marks and software remain DenchiSoft / related rightsholders. Buy/install HITL. No cracks.

---

## Product summary (homepage seed)

| Field | Value |
|-------|--------|
| Product | **VTube Studio** |
| Tagline | App for **Virtual YouTubers** that makes it easy and fun to bring **Live2D** models to life |
| Payment model seed | Active development; many features for a **non-recurring one-time payment** |
| Localization | **15+ languages** (community localization) |
| Publisher surface | DenchiSoft · [denchisoft.com](https://denchisoft.com/) |

---

## Platforms & download (VERIFY LIVE)

| Platform | Seed |
|----------|------|
| **Steam (PC/Mac)** | [store.steampowered.com/app/1325860/VTube_Studio](https://store.steampowered.com/app/1325860/VTube_Studio/) |
| **Android** | Google Play `com.denchi.vtubestudio` |
| **iOS (iPhone/iPad)** | App Store (VERIFY LIVE listing) |

### Tracking requirements (site seed)

| Method | Requirement seed |
|--------|------------------|
| Webcam face tracking | OpenSeeFace (PC seed) |
| Phone as tracker | Connected **iPhone/Android** as face tracker |
| iOS device | **Face ID** or Apple **A12+** chip |
| Android | Phone supporting **Google ARCore** |
| Hand tracking | Webcam-based hand tracking (newer feature seed) |

---

## Feature map (marketing seeds)

| Area | Capabilities |
|------|----------------|
| **Tracking** | Webcam / iPhone face tracking; eye-tracking; winking; **hand tracking** |
| **Performance** | Hotkeys for scene control; mic **lipsync**; animated **PNG props** tracking the model; post-processing **VFX** |
| **Item system** | Attach props (images, animations, customizable **Live2D props** with own tracking/hotkeys) |
| **Collab** | Online multiplayer — invite **Steam friends**; models/items on each other’s screens (low-latency claim) |
| **Twitch** | Integration: emotes thrown at model; hotkeys via redeems, subs, chat commands |
| **Plugins** | **VTube Studio API** — third-party plugins (donations, game controllers, etc.) |
| **VFX** | Built-in post-processing visual effects |
| **Docs wiki** | GitHub wiki: Item System, Live2D Items, Hand Tracking, Visual Effects, Plugins |

Wiki seeds:
- https://github.com/DenchiSoft/VTubeStudio/wiki/Item-System  
- https://github.com/DenchiSoft/VTubeStudio/wiki/Live2D-Items  
- https://github.com/DenchiSoft/VTubeStudio/wiki/Hand-Tracking  
- https://github.com/DenchiSoft/VTubeStudio/wiki/Visual-Effects  
- https://github.com/DenchiSoft/VTubeStudio/wiki/Plugins  

Related Steam app seed (collab/hand-related listing seen in dump): app **2384550** — VERIFY LIVE purpose.

---

## Support & community

| Channel | Seed |
|---------|------|
| Documentation | [denchisoft.com/documentation](https://denchisoft.com/documentation) |
| Discord | discord.gg/VTubeStudio · invite seed `discord.com/invite/j6JUarA` |
| Twitter/X | [twitter.com/VTubeStudio](https://twitter.com/VTubeStudio) |
| YouTube | youtube.com/denchisoft |
| Mail | support contact on site (VERIFY LIVE address) |
| FAQ | Discord FAQ first (site guidance) |
| Changelog | Linked from site (VERIFY LIVE path) |
| Team | denchisoft.com/team |
| License | denchisoft.com/license |
| Branding | denchisoft.com/branding |
| Impressum / Privacy | denchisoft.com/impressum |

---

## Site tech seeds

| Item | Seed |
|------|------|
| CMS | WordPress + Elementor (primaapp theme) |
| Fonts | Poppins · Roboto (Google Fonts) |
| RSS | denchisoft.com/feed/ |
| Cloudflare Insights | beacon present |
| Logo | Multi-cat faces crest (branding) |

---

## Streamer workflow seed (non-clinical)

```text
Acquire VTS (Steam/mobile) HITL
  → Live2D model (licensed / self-made)
  → Tracking: webcam or phone tracker
  → Hotkeys / items / lipsync
  → Optional: Twitch integration, plugins, collab
  → Output to OBS / encoder → stream (youtube-live-encoder etc.)
```

---

## Scaffold

```text
workspace/media/vtube-studio/
  setup-notes.md      # OS, tracker type — no licenses keys
  hotkey-map.md
  plugin-list.md
```

Do not commit paid model files, API tokens, or stream keys.

---

## Related Fable skills

| Skill | Overlap |
|-------|---------|
| `youtube-live-encoder` | Stream output |
| `steam-sim-launch` | Steam app ownership hygiene |
| `3d-animation-dev-kit` | General CG (Live2D is 2.5D) |
| `animation-dev-kit` | 2D art pipeline for assets |
| `privacy-host-map` | Host classification |
