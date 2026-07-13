# Zoom web client join

**Skill:** `calendar-mail-meetings`  
**Primary CLICK:** [https://app.zoom.us/wc/join](https://app.zoom.us/wc/join)  
Zoom and related marks belong to Zoom Video Communications, Inc. **Not legal advice.**

---

## What this URL is

| Item | Value |
|------|--------|
| URL | `https://app.zoom.us/wc/join` |
| Product | **Zoom Web Client** — join a meeting in the browser (no desktop app required) |
| User action | Enter **Meeting ID** + optional **passcode** / name; or land via a full join link |
| Fable role | Document, parse join links from invites/.ics, prep agenda — **never auto-join** |

Full invite links usually look like:

| Pattern | Notes |
|---------|--------|
| `https://app.zoom.us/wc/join/{meetingId}` | Web client deep link |
| `https://*.zoom.us/j/{meetingId}` | Classic join (may offer app or browser) |
| `https://*.zoom.us/w/{meetingId}` | Web client style paths (variant) |
| `https://zoom.us/j/{meetingId}?pwd=…` | Passcode often in `pwd` query — **treat as secret** |

Do **not** commit meeting IDs + passcodes to public git. Prefer `knowledge/calendar/_local/`.

---

## Offline agent flows

1. **From calendar / mail** — extract Zoom URL from DESCRIPTION / LOCATION / URL in `.ics` (`parse-ical` / `scripts/ical_parse.py`).  
2. **Tag as CLICK** — user opens the link (or web join page) in their browser.  
3. **meeting-prep** — agenda + pre-reads; put join link only in user-held notes.  
4. **join-zoom** procedure — checklist before user joins (mic/camera, recording consent, name display).  

Fable **must not**:

- Launch Zoom or inject meeting credentials without explicit user action  
- Record or capture the call  
- Store passcodes in skills or committed knowledge  

---

## User checklist (join-zoom)

Before **CLICK** → [app.zoom.us/wc/join](https://app.zoom.us/wc/join) or invite link:

| Step | Check |
|------|--------|
| 1 | Correct Meeting ID (from invite, not chat folklore) |
| 2 | Passcode ready (password manager / invite — not spoken in open channel if sensitive) |
| 3 | Display name appropriate for audience |
| 4 | Mic/camera off until needed (default safe) |
| 5 | Recording: if host records, note retention policy; decline if required by playbook |
| 6 | Screen share: no secrets (tokens, PII, other meeting IDs) on screen |
| 7 | Waiting room / host admit — wait; don’t spam rejoin |

---

## With Google Calendar

- Add Zoom via Zoom’s calendar add-on **or** paste join URL into event location/description (user UI).  
- Export `.ics` → offline parse → flag `zoom.us` / `app.zoom.us` as conference **CLICK**.  
- Parallel: Google Meet uses `meet.google.com` — same hygiene, different host map.

---

## Privacy

See `knowledge/privacy/zoom-hosts.md`.

---

## HITL

- Joining meetings as the org’s account  
- Sharing passcodes broadly  
- Enabling cloud recording / AI companion features (vendor terms + data residency)  
