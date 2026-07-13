# Privacy host map — Zoom (web join seed)

**Skill:** `privacy-host-map` + `calendar-mail-meetings`  
**Scope:** Zoom **Web Client** join and related hosts, seeded from  
[https://app.zoom.us/wc/join](https://app.zoom.us/wc/join).  
**Not a penetration test. Not legal advice.** Re-verify with live Network capture.

---

## Verdict

Zoom meetings carry **high-sensitivity** content (voice, video, chat, shared screens). Prefer **user-initiated CLICK** join. Offline Fable should not embed live Zoom sessions or store passcodes in git.

---

## Host inventory (seed)

| Host / pattern | Tag | Notes |
|----------------|-----|--------|
| `app.zoom.us` | **CLICK** / **LOAD** | Web client app shell |
| `app.zoom.us/wc/join` | **CLICK** | Web join entry (Meeting ID form) |
| `app.zoom.us/wc/join/*` | **CLICK** | Web join with meeting id path |
| `*.zoom.us` | **CLICK** / **LOAD** | Regional / vanity join hosts |
| `zoom.us` / `www.zoom.us` | **CLICK** | Marketing + join redirects |
| `*.zoom.us/j/*` | **CLICK** | Classic meeting join links |
| `*.zoom.us/w/*` | **CLICK** | Web client join variants |
| Zoom CDN / media hosts | **LOAD** | WebRTC/media (confirm live; names change) |
| Analytics / marketing pixels on marketing pages | **LOAD** / **BUNDLE** | Separate from in-meeting media |

Exact WebRTC and CDN hostnames vary by region and release — capture Network tab when mapping a live session.

---

## Evidence rules

| Tag | Use |
|-----|-----|
| **CLICK** | User opens join URL or web join page |
| **LOAD** | Scripts, media, XHR during web client session |
| **CONFIG** | API endpoints, meeting config after auth |
| **BUNDLE** | Host strings only in JS until confirmed |

---

## Data classes

| Data | Sensitivity | Fable handling |
|------|-------------|----------------|
| Meeting ID | Medium–high | Local notes; minimise in git |
| Passcode / `pwd=` | Secret | `_local/` only; never commit |
| Join URL with embedded pwd | Secret | Treat as credential |
| Chat / recordings | High | Out of agent scope by default |
| Display name | Low–medium | User choice at join |

---

## Cross-links

- Join playbook: `knowledge/calendar/zoom-web-join.md`  
- Calendar stack: `knowledge/calendar/ical-and-google.md`  
- Google Meet contrast: `knowledge/privacy/google-calendar-hosts.md`  
