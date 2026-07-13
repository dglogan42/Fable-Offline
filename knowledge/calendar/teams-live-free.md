# Microsoft Teams free meetings (teams.live.com)

**Skill:** `calendar-mail-meetings`  
**Primary CLICK:** [https://teams.live.com/free](https://teams.live.com/free)  
**Official join help (calendar / ID):**  
[Join a meeting in Microsoft Teams](https://support.microsoft.com/en-us/teams/meetings/join-a-meeting-in-microsoft-teams#bkmk_calendar)  
→ full notes: `knowledge/calendar/teams-join-from-calendar.md`  

Microsoft Teams and related marks belong to Microsoft. **Not legal advice.**

---

## What this URL is

| Item | Value |
|------|--------|
| URL | `https://teams.live.com/free` |
| Product seed | **Free online meetings & video calls** — Teams for personal / free tier surface |
| User actions (page seed) | **Start a meeting for free** · **Join a meeting** · join with **Meeting ID** + **passcode** |
| Marketing seeds | Share links · **60-min free meetings** · live captions (40+ languages) · screen share · files · chat themes |
| Paid feature seeds (diamond on page) | **Record** meetings/calls · **Copilot** AI (plan meetings / notes from recordings) |
| Related | Insider updates: [insider.teams.com/whats-new](https://insider.teams.com/whats-new/) |
| Fable role | Parse join links, **join-teams** checklist, meeting-prep — **never auto-join** |

### Join form seed (from free page)

- Fields: **Meeting ID** \* · **Meeting passcode** \*  
- Constraint seed: alphanumeric characters  
- Button: **Join meeting**

Treat passcodes and meeting IDs as **secrets** — do not commit to public git. Prefer `knowledge/calendar/_local/`.

---

## Link patterns (VERIFY LIVE)

| Pattern | Notes |
|---------|--------|
| `https://teams.live.com/free` | Free meetings hub / start-join marketing |
| `https://teams.live.com/…` | Live/personal Teams web surfaces |
| `https://teams.microsoft.com/…` | Work/school Teams (tenant) — different auth world |
| `https://*.teams.microsoft.com/l/meetup-join/…` | Classic tenant meeting join deep links |
| Invite text with Meeting ID + passcode | User pastes into free join form |

Do not invent Meeting IDs. Distinguish **personal free (teams.live.com)** vs **work/school (teams.microsoft.com)** when coaching.

---

## Free vs paid (page seeds — VERIFY LIVE)

| Feature (marketing) | Free page seed |
|---------------------|----------------|
| Start / join meeting | Free |
| Share meeting links | Free |
| 60-min free meetings | Free (limits may change) |
| Live captions | Free claim (40+ languages) |
| Screen share | Free claim |
| Files / collaboration tools | Free claim |
| Recording | Paid feature badge |
| Copilot AI | Paid feature badge |

Limits, account requirements, and geo offers change — always **VERIFY LIVE** on Microsoft pages.

---

## Offline agent flows

1. **From calendar / mail** — extract Teams URL or ID/passcode fields from DESCRIPTION / LOCATION / pasted invite (`parse-ical` when `.ics` contains conference URL).  
2. **Tag as CLICK** — user opens [teams.live.com/free](https://teams.live.com/free) or full join link.  
3. **meeting-prep** — agenda + timebox; note 60-min free window if relevant.  
4. **join-teams** — pre-join checklist (name, mic/camera, recording consent if host records via paid tier).  

Fable **must not**:

- Auto-start or auto-join Teams  
- Store passcodes in committed knowledge  
- Claim Copilot/recording works on free without VERIFY LIVE  

---

## User checklist (join-teams)

### A — Join from Teams calendar (work/school or personal app)

Official seed ([#bkmk_calendar](https://support.microsoft.com/en-us/teams/meetings/join-a-meeting-in-microsoft-teams#bkmk_calendar)):

1. Open **Teams** app or web (user HITL).  
2. Select **Calendar**.  
3. Select the meeting → **Join**.  
4. Pre-join: mic/camera, name, account (**Change** if wrong account).  
5. **Join** / enter lobby if required.  

### B — Join with Meeting ID

1. **Calendar** → **Meet now** dropdown → **Join with an ID** (desktop seed)  
   or mobile **More** → **Join with meeting ID**.  
2. Enter ID + passcode from invite or **Details → Show meeting info**.  
3. Or browser: [teams.live.com/free](https://teams.live.com/free) / [microsoft.com/microsoft-teams/join-a-meeting](https://www.microsoft.com/microsoft-teams/join-a-meeting).  

### C — Hygiene (all paths)

| Step | Check |
|------|--------|
| 1 | Correct Meeting ID / link (from invite, not chat folklore) |
| 2 | Passcode ready (not in public channels; mask in Fable notes) |
| 3 | Free vs work account path (live.com vs microsoft.com tenant) |
| 4 | Time budget — free meetings often capped (~60 min seed) |
| 5 | Display name appropriate |
| 6 | Mic/camera off until needed |
| 7 | Recording / lobby / org policy |
| 8 | Screen share: no secrets on screen |
| 9 | Captions optional for accessibility |

Full multi-path article map: `teams-join-from-calendar.md`.

---

## With Google Calendar / iCal

- Paste Teams join link or “Meeting ID + passcode” into event location/description (user UI).  
- Or “Add Microsoft Teams” add-ons where available (VERIFY LIVE — org policy).  
- Export `.ics` → offline parse → flag `teams.live.com` / `teams.microsoft.com` as conference **CLICK**.  
- Parallel: Meet = `meet.google.com`, Zoom = `app.zoom.us/wc/join` — same hygiene, different hosts.

---

## Contrast (meeting platforms)

| Platform | Free join entry seed | Fable procedure |
|----------|----------------------|-----------------|
| Google Meet | `meet.google.com/…` | Flag CLICK in prep |
| Zoom Web | [app.zoom.us/wc/join](https://app.zoom.us/wc/join) | **join-zoom** |
| Teams free | [teams.live.com/free](https://teams.live.com/free) | **join-teams** |
| Teams work | `teams.microsoft.com` | **join-teams** (tenant notes) |

---

## Privacy

See `knowledge/privacy/teams-live-hosts.md`.

---

## HITL

- Starting/joining as the org’s account  
- Sharing passcodes broadly  
- Enabling recording / Copilot (vendor terms + data residency)  
