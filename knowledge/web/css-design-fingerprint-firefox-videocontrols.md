# CSS design-system fingerprint — Firefox HTML video controls

**Skill:** `aem-site-agent` (**fingerprint-css**) · browser chrome / media UI audits  
**Origin:** User-supplied full stylesheet extract (devtools or source tree).  
**Site identity:** **Mozilla Firefox** built-in **HTML media controls** — not a website brand.  
**Confidence:** **very high** (source license, `chrome://` URLs, `-moz-*` APIs, `videocontrols.js` contract).  
**Not a host map.** This is **browser UI chrome**, not third-party page CSS.

---

## Verdict

| Strong signal | Value |
|---------------|--------|
| License | **Mozilla Public License 2.0** header (`mozilla.org/MPL/2.0/`) |
| Namespace | `@namespace url("http://www.w3.org/1999/xhtml")` |
| Root class | `.videocontrols` |
| Asset URLs | `chrome://global/skin/media/*.svg` / `.png` |
| Engine hooks | `-moz-range-thumb`, `-moz-progress-bar`, `-moz-context-properties`, `-moz-platform` |
| JS contract | Custom properties documented as read by **`videocontrols.js`** (`--playButton-width`, etc.) |
| a11y / bugs | Inline references to Bugzilla (e.g. 1766093, 1590379, 554717, 1289412) |

**Reading:** Official Firefox **in-page video/audio control skin** (shadow-DOM controls for `<video>` / media). Seeing this CSS on a page usually means **devtools inspected the browser’s control tree**, not that the site authored Firefox chrome.

---

## Captured signals

### Shell / interaction
| Rule | Notes |
|------|--------|
| `.videocontrols` | Full-size LTR controls; `user-select: none`; reset font to `sans-serif !important` |
| `.videocontrols[flipped]` | `transform: scaleX(-1)` |
| `.controlBar[hidden]` | `display: flex; opacity: 0; pointer-events: none` — hidden visually, kept for a11y |
| `.controlsSpacer[hideCursor]` | `cursor: none` during playback chrome hide |
| `.a11y-only` | Off-screen positioning for assistive tech |

### Design tokens (`.controlsContainer`)
| Token | Default | `.touch` |
|-------|---------|----------|
| `--clickToPlay-size` | 48px | 64px |
| `--button-size` | 30px | 40px |
| `--timer-size` / long | 40px / 60px | 52px / 78px |
| `--track-size` | 5px | 7px |
| `--thumb-size` | 13px | 16px |
| `--label-font-size` | 13px | 16px |
| `--control-focus-outline` | `2px solid #00ddff` | same family |
| `--control-focus-outline-offset` | `-2px` | |

JS-facing bar widths: `--playButton-width`, `--scrubberStack-width`, `--muteButton-width`, `--volumeStack-width`, `--fullscreenButton-width`, position/duration box widths (see `.controlBar` comments).

### Colour / chrome
| Element | Value |
|---------|--------|
| Controls text | `#fff` on container |
| Control bar bg | `rgba(26, 26, 26, 0.8)` · height 40px (52px touch) |
| Status overlay | `rgb(80, 80, 80, 0.85)` |
| Progress fill | `#00b6f0` |
| Hover fill / track item | `#48a0f7` |
| Active fill | `#2d89e6` |
| Buffer track | `rgba(0,0,0,0.7)` · buffer fill `rgba(255,255,255,0.3)` |
| Duration dim | `#929292` |
| PiP overlay | `rgb(12, 12, 13)` |
| Text track list | black `opacity: 0.7` · hover `#444` · checked `#48a0f7` |

### Icons (chrome://)
Play/pause, audio/mute/no-audio, closed captions on/off, fullscreen enter/exit, throbber/stalled, error, picture-in-picture — all under `chrome://global/skin/media/`.

### Platform / media queries
| Query | Effect |
|-------|--------|
| `(prefers-contrast)` | Borders on range track/progress |
| `(-moz-platform: macos)` | Position/duration uses Helvetica Neue stack |
| `(-moz-platform: windows) and (prefers-contrast)` | Transparent spacer / clickToPlay bg |
| `:host::cue` | Cue font-size / writing-mode from CSS variables |

### Components
Click-to-play overlay · control bar · scrubber/volume ranges · buffer/progress bars · closed captions list · fullscreen · picture-in-picture toggle · status/error/PiP overlays · position/duration box.

---

## Match checklist

| # | Signal | This sample |
|---|--------|-------------|
| 1 | MPL 2.0 Mozilla header | yes |
| 2 | `.videocontrols` + `.controlBar` | yes |
| 3 | `chrome://global/skin/media/` URLs | yes |
| 4 | `-moz-range-*` / `-moz-progress-bar` | yes |
| 5 | `videocontrols.js` width variable comments | yes |
| 6 | Focus cyan `#00ddff` / progress `#00b6f0` / hover `#48a0f7` | yes |

**3+ yes** → Firefox media controls skin (**very high**).

---

## What this is **not**

| Fingerprint | Differentiator |
|-------------|----------------|
| Epic / Brutal · Titan One | Brutal/Titan One/Inter, `.epic-wf` |
| TikTok product UI | TikTok Text, `#fe2c55`, `--ttam-*` |
| Helvetica grey orphan | Body type system only, no chrome:// |
| Site-authored player (YouTube/Vimeo) | No `chrome://` or MPL videocontrols root |

---

## Forensic / agent notes

1. **Attribution:** Browser UI, not “this website uses Firefox CSS as its design system.”  
2. **Shadow DOM:** Controls often live in UA shadow tree; selection/inheritance bugs called out in comments.  
3. **Touch / mobile:** `.touch` and `.mobile` modifiers; throbber suppressed on mobile for m.youtube.com conflict (bug 1289412).  
4. **a11y:** Hidden bar stays in a11y tree; focus-visible outlines on controls and tracks.  
5. **If found in a site CSS dump:** Likely accidental copy of browser chrome or a very faithful open-source fork — still treat as **Firefox control pattern**.

---

## Sample log

| # | What arrived | Delta |
|---|--------------|--------|
| 1 | Full videocontrols stylesheet (MPL + chrome:// + tokens) | Baseline Firefox media chrome fingerprint |
