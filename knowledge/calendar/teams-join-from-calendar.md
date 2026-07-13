# Join a Teams meeting from calendar or ID (official support)

**Skill:** `calendar-mail-meetings` (**join-teams**)  
**Official (VERIFY LIVE):**  
[Join a meeting in Microsoft Teams](https://support.microsoft.com/en-us/teams/meetings/join-a-meeting-in-microsoft-teams)  
Anchor (desktop): **Join from calendar or ID** → `#bkmk_calendar`  
Full URL seed:  
`https://support.microsoft.com/en-us/teams/meetings/join-a-meeting-in-microsoft-teams#bkmk_calendar`

Microsoft Teams / support content remain Microsoft’s. **Not legal advice.** UI labels change — re-check live help.

Related Fable notes:
- Free hub: `knowledge/calendar/teams-live-free.md` ([teams.live.com/free](https://teams.live.com/free))  
- Privacy: `knowledge/privacy/teams-live-hosts.md`  

---

## Scope

Official Microsoft Support article for **joining** Teams meetings (desktop + mobile tabs). Prefer **Teams desktop or mobile apps** for best experience (article seed). Fable only narrates **user CLICK** checklists — never auto-joins.

Troubleshooting seed: [I can't join a Teams meeting](https://support.microsoft.com/en-us/teams/meetings/i-can-t-join-a-meeting-in-microsoft-teams).

---

## Join from calendar (`#bkmk_calendar`)

### Desktop (article seed)

1. Select **Calendar** in Teams.  
2. Select a meeting.  
3. Select **Join**.  

### Mobile (article seed)

1. Tap **Calendar**.  
2. Tap the meeting you want to join.  
3. Tap **Join**.  

Same pattern for meetings organized by a **Teams personal account** user: Calendar → meeting → **Join** (no required switch between personal and work/school in article seed).

---

## Join with a meeting ID (`#bkmk_calendar` continued)

### Desktop (article seed)

1. Select **Calendar** (left side of Teams).  
2. Select dropdown next to **Meet now** → **Join with an ID**.  
3. Enter **Meeting ID** and **passcode**.  

Find ID + passcode:

| Where | Detail seed |
|-------|-------------|
| Teams calendar | Meeting → **Details** → **Show meeting info** |
| Invite email | Top of Teams meeting invite |

### Mobile (article seed)

1. Tap **Calendar**.  
2. Tap **More** → **Join with meeting ID**.  
3. Enter Meeting ID and passcode.  
4. Tap **Join meeting**.  

Find ID + passcode:

| Where | Detail seed |
|-------|-------------|
| Teams calendar | Open meeting → **Details** → **See more** |
| Invite email | Bottom of Teams meeting invite (mobile seed) |

### Join with ID without opening the app first

Article seed: [Teams marketing join page](https://www.microsoft.com/microsoft-teams/join-a-meeting)

1. Open marketing join page in browser.  
2. Enter **Meeting ID** and **Passcode**.  
3. Select **Join meeting**.  

Parallel free surface already in Fable: [teams.live.com/free](https://teams.live.com/free).

---

## Other join paths (article TOC seeds)

| Path | Summary (VERIFY LIVE) |
|------|------------------------|
| **Join by link** | Invite link → web or desktop; new invites may show full URL (after ~Jan 2026 region seeds); older “Join meeting now” still works |
| **No account** | Guest name if allowed; see [join without an account](https://support.microsoft.com/en-us/teams/meetings/join-a-meeting-without-an-account-in-microsoft-teams) |
| **Sign in** | Chat access; may enter lobby until admitted |
| **Live meeting bar** | RSVP Accept/Tentative → bar shows → **Join**; multi-meeting → **View meetings** |
| **Channel** | In-channel **Join** when meeting is in a channel |
| **Chat** | Open meeting chat → **Join** at top |
| **Phone dial-in** | Number + conference ID in invite; dial out via pre-join **Call me** |
| **Anonymous / other account** | Pre-join **Change** → pick account or **Join without signing in** + name |
| **Room audio** | Pre-join connect to nearby Teams Room (Bluetooth for detection seed) |
| **Display name** | People → edit name if organizer enabled option |
| **Avatar** | Optional avatar join (separate help article) |

---

## Invite format note (article seed)

| Era | Appearance |
|-----|------------|
| Newer (after ~20 Jan 2026; some regions from 8 Jan 2026) | Full meeting **URL** in invite |
| Older | “**Join meeting now**” style link |

Both join the same way — select the link. Meeting ID + passcode remain on invite / **Show meeting info**.

---

## Free / personal vs work-school

| Context | Notes from article family |
|---------|---------------------------|
| Work or school Teams | Calendar join + tenant policies (lobby, recording, dial-in) |
| Teams personal / free host | Join from calendar or chat link; privacy per Microsoft Privacy Statement for personal accounts |
| Feature limits | Some features unavailable for Teams Free participants — VERIFY LIVE limitations topic |

Free marketing hub remains: `teams-live-free.md`.

---

## Fable agent mapping

| User situation | Procedure / action |
|----------------|-------------------|
| Has Teams calendar event | **join-teams** → calendar steps above (HITL) |
| Has ID + passcode only | **join-teams** → Join with ID or marketing/free page |
| Has invite link | Flag as **CLICK**; prefer app if installed |
| `.ics` / mail with Teams URL | **parse-ical** → extract conference → **join-teams** |
| Prep agenda | **meeting-prep** first |

**Never:** auto-join, invent Meeting IDs, commit passcodes, or store full invite secrets in public git.

---

## Related official help (from article nav)

- [Join without a Teams account](https://support.microsoft.com/en-us/teams/meetings/join-a-meeting-without-an-account-in-microsoft-teams)  
- [Join outside your org](https://support.microsoft.com/en-us/teams/meetings/join-a-microsoft-teams-meeting-or-event-outside-your-org)  
- [Schedule a meeting](https://support.microsoft.com/en-us/teams/meetings/schedule-a-meeting-in-microsoft-teams)  
- [Schedule from Outlook](https://support.microsoft.com/en-us/teams/meetings/schedule-a-microsoft-teams-meeting-from-outlook)  
- [Schedule from Google Calendar](https://support.microsoft.com/en-us/teams/meetings/schedule-a-microsoft-teams-meeting-from-google-calendar)  
- [Manage your calendar in Teams](https://support.microsoft.com/en-us/teams/meetings/manage-your-calendar-in-microsoft-teams)  
- [Can't join](https://support.microsoft.com/en-us/teams/meetings/i-can-t-join-a-meeting-in-microsoft-teams)  

---

## HITL

- Account choice (work vs personal vs anonymous)  
- Lobby admit / org policies  
- Dial-in PIN (organizer — view-once reset seed)  
- Recording / transcript / Copilot consent  
