# MIT License

Copyright (c) 2026 David Logan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Additional notices

These notices do **not** limit the MIT grant above.

### 1. Domain knowledge and skills

Markdown under `knowledge/` and `skills/` is provided for research, education,
and offline agent operations. It is **not professional advice**. In particular
it is not financial, investment, legal, medical, planning, customs,
biosecurity, veterinary, real-estate, or emergency-response advice, and it
does not create a professional-client relationship.

### 2. Third-party content

Snapshots that summarise public websites, policies, or PDFs (including
government and institutional materials) remain the property of their
respective rights holders. Fable Offline does not claim ownership of those
third-party works. Always re-verify against primary official sources.

### 3. Emergency and safety

In an emergency in New Zealand, call **111**. Agents must not take crime,
fire, or medical reports as the agent of record.

### 4. Steam, games, and local soak tests

Scripts such as `scripts/steam_launch.py` and `scripts/steam_sim_soak.py`,
and notes under `knowledge/steam/`, are helpers for launching games the user
**already owns and has installed**, and for measuring local model performance
under concurrent load.

They are **not** a game bot, multiplayer cheat, DRM bypass, or tool for
unauthorised access. Steam, individual games, trademarks, and related
software remain the property of Valve Corporation and the respective
publishers/developers. Launch only software you are licensed to run.

### 5. Calendar, mail, meetings, and Zoom

Notes under `knowledge/calendar/`, skill `calendar-mail-meetings`, and
`scripts/ical_parse.py` help with **local** iCalendar (`.ics`) files, meeting
prep, draft mail, and join **checklists**.

| Vendor surface | Example | Fable role |
|----------------|---------|------------|
| Google Calendar | [calendar.google.com](https://calendar.google.com/) | Prep / drafts; no authenticated scrape |
| Google Meet | `meet.google.com` | Flag as user CLICK from invites |
| Zoom Web Client | [app.zoom.us/wc/join](https://app.zoom.us/wc/join) | **join-zoom** checklist; never auto-join |

Google Calendar, Gmail, Meet, and related services remain the property of
Google LLC. Zoom Web Client and related services remain the property of Zoom
Video Communications, Inc. The Software does not grant rights to those
services and is not a substitute for their terms of service.

Do **not** commit OAuth tokens, app passwords, Zoom passcodes or `pwd=` query
values, secret iCal feed URLs, or full mailbox exports. Prefer
`knowledge/calendar/_local/` (gitignored) for private material.

### 6. Windows install media and imaging

Skill `windows-install-prep` and notes under `knowledge/windows/` support
**licensed** Windows 11 deployment hygiene (official Media Creation Tool / ISO
from Microsoft, DISM/ADK/unattend for images you are entitled to use). Windows
and related trademarks remain the property of Microsoft Corporation.

The Software does **not** authorize piracy, activation cracks, redistributing
Microsoft installation media without rights, or rebranding Windows as a fake
product (including nonexistent “Windows 12 Professional” consumer builds).
Do not commit product keys or autounattend secrets.

### 7. macOS install media

Skill `macos-install-prep` and notes under `knowledge/macos/` summarise
**Apple-published** guidance for bootable installers — notably support document
[Create a bootable installer for macOS (101578)](https://support.apple.com/en-nz/101578)
(`createinstallmedia`) — and recovery method choice on **Apple-branded Macs**.
macOS, Mac, and related trademarks remain the property of Apple Inc.

The Software does **not** authorize installing macOS on non-Apple hardware
(Hackintosh), redistributing Apple installers without rights, cracked or
torrent media, or bypassing Activation Lock / Find My without lawful ownership.
Do not commit full `Install macOS *.app` bundles, IPSW images, FileVault or
recovery keys, or Apple ID credentials. Re-verify live Apple Support after each
macOS release; command tables go stale.

### 8. Social clients, feeds, and RSS

Skills such as `snapchat-web-feed`, `rss-share`, `instagram-selfie-selector`,
and related notes under `knowledge/social/` support **legitimate** use of
third-party services and **user-generated** syndication.

Snapchat, Snap Inc., and related marks remain the property of Snap Inc.
Fable protocols for [web.snapchat.com](http://web.snapchat.com/) are operational
hygiene only. The Software does **not** authorize scraping, credential theft,
session hijacking, or automated abuse of Snapchat or other social platforms.

`scripts/rss_share.py` produces standard **RSS 2.0** XML for feeds you are
entitled to publish. Do not republish third-party full-text content without
rights, and do not commit private feed URLs that embed secrets.

### 9. Creative desktop apps and pipeline builds

Skill `creative-pipeline-builds` and notes under `knowledge/media/` describe
**licensed** workflows using Adobe Creative Cloud (including the
[Creative Cloud desktop app](https://www.adobe.com/nz/creativecloud/desktop-app.html)),
Photoshop, Lightroom, CapCut, and DaVinci Resolve: project templates, presets,
export/render queues, and checklists.

Adobe, CapCut, Blackmagic Design, and related marks remain the property of
their respective owners. The Software does **not** authorize cracked installers,
license bypass tools, keygens, or malware “activators.” Do not commit Adobe
passwords, stock assets without rights, raw camera masters, or heavy export
packages. Prefer `workspace/creative/` locally (inbox/exports gitignored).

YouTube Live encoder guidance (Help answer 2907883 family) likewise requires
valid account access; never commit stream keys.

### 10. ChromeOS Flex and Google for Education

Skill `chromeos-flex-install-prep` and notes under `knowledge/chromeos/` summarise
**official** [ChromeOS Flex](https://chromeos.google/products/chromeos-flex/) install
hygiene (USB via Chromebook Recovery Utility, certified models, fleet notes).
Skill `google-for-education` and `knowledge/education/google-for-education.md` map
the public [Google for Education](https://edu.google.com/intl/ALL_us/) hub
(Workspace for Education, Classroom, Chromebooks, Gemini for Education marketing).
Skill `minecraft-education-resource-kit` and `knowledge/education/minecraft-education.md`
map **Minecraft Education** ([education.minecraft.net](https://education.minecraft.net/en-us))
with community technical notes from [Minecraft Wiki](https://minecraft.wiki)
([Minecraft Education article](https://minecraft.wiki/w/Minecraft_Education), exclusive features,
version history). Google marks remain Google LLC; Minecraft / Minecraft Education marks remain
Microsoft / Mojang. Wiki content is third-party community documentation — re-verify licensing,
prices, country availability, and app versions on official Microsoft pages before procurement.

The Software does **not** redistribute Flex images, enrollment tokens, Admin
console credentials, cracked Minecraft Education clients, or student personal
data. Full Flex install erases the target disk — user backups are required.
Prefer certified models and official edu.google.com / education.minecraft.net /
support paths. Workspace edition pricing, Minecraft Education licensing, free vs
paid messaging, and compliance claims must be VERIFY LIVE with vendors and
institutional counsel. Not educational, careers, or legal advice. Do not commit
student rosters, gamertags, or school secrets (see `.gitignore`).

### 11. Animation toolkits (2D, stop-motion, 3D)

Skills and notes under `knowledge/media/` support **user-operated** animation
workflows. They do not ship third-party binaries and do not grant licenses to
those products.

| Skill | Primary software / source | Notes |
|-------|---------------------------|--------|
| `animation-dev-kit` | [Krita](https://krita.org/) · [Animation manual](https://docs.krita.org/en/user_manual/animation.html) | FOSS frame-by-frame; optional FFmpeg |
| `stop-motion-dev-kit` | [Stop Motion Studio](https://www.stopmotionstudio.com/download/index.html) · [Cloud Stop Motion](https://cloudstopmotion.com/) | Local Studio and/or browser Chromebook / ChromeOS Flex cloud; no cracked installs; no auto-upload by Fable |
| `3d-animation-dev-kit` | [Blender](https://www.blender.org/download/) (default) | FOSS CG pipeline; Maya/Houdini/C4D only if user already licensed |
| `roblox-studio-resource-kit` | [Roblox Studio setup](https://create.roblox.com/docs/studio/setup) | Free official Win/Mac Studio; Roblox terms apply; no cracked clients |

Public **education map** seeds (e.g. [Media Design School 3D Animation & VFX](https://www.mediadesignschool.com/courses/3d-animation-vfx-courses-degrees))
are **not** enrollment, careers, or immigration advice. Re-verify fees, entry,
and rankings live. **Cloud Stop Motion** stores projects on a third-party
cloud; school use requires following institution and child-privacy policies
(COPPA/age rules as applicable). The Software does **not** upload files for
the user, hold cloud passwords or Roblox session cookies, or authorize cracked
DCC / Studio tools. Do not commit multi-GB masters (`.kra`, SMS projects, cloud
exports, `.blend`, `.rbxl`, EXR) or student rosters — keep media under
`workspace/creative/` (gitignored).

### 12. Automatic prompt generator and swarm prompts

`auto_prompt_generator.py`, skill `prompt-generator`, notes under
`knowledge/swarm/`, Fable CLI `--prompt-gen` / `/prompt-gen`, and workflows
`prompt-gen-*` produce **local** system-prompt markdown for multi-agent
workflows (including a sample quant research swarm design). Generated files
under `generated_prompts/` (see `.gitignore`) are user-local artifacts.

This is **not investment or trading advice**. Quant-style prompts describe a
research process only; they do not execute trades or guarantee alpha. Review
generated prompts before production or safety-critical use. Do not commit
secrets, API keys, or private trading parameters into generated prompt dumps.

### 13. Contributions

By submitting contributions to this repository, you agree they are licensed
under the same MIT License terms as the Software, unless you state otherwise
in writing with the copyright holders.

---

The plain-text file [`LICENSE`](LICENSE) contains the same MIT grant and
notices for tooling that expects a non-markdown license file.
