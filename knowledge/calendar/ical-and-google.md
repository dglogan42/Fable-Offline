# iCalendar, Google Calendar, mail & meetings

**Skill:** `calendar-mail-meetings`  
**Not legal advice.** Google and third-party marks belong to their owners.

---

## Google Calendar

| Item | Value |
|------|--------|
| Web app | [https://calendar.google.com/](https://calendar.google.com/) |
| Role | Primary interactive calendar UI (events, guests, Meet) |
| Fable scrape | **Not** for authenticated account HTML — use export / .ics / paste |
| Offline bridge | Settings → Import & export, or event → Publish event / .ics attachment from mail |

### Typical user flows (CLICK — user browser)

1. **Create meeting** — Calendar → Create → Event → Add Google Meet → Add guests → Save  
2. **Find time** — Use Google’s proposed times only as user-visible UI (agent does not call Calendar API unless separately configured)  
3. **Export** — Settings gear → Import & export → Export (zip of .ics per calendar)  
4. **Import** — Same settings → Import .ics into a calendar  
5. **Secret iCal URL** — Calendar settings → Integrate calendar → Secret address in iCal format — **credential; never commit**

### Related Google surfaces

| Host / product | Role |
|----------------|------|
| `calendar.google.com` | Calendar UI |
| `calendar.google.com/calendar/ical/...` | Private feed patterns (secret) |
| `meet.google.com` | Video meetings linked from events |
| `mail.google.com` / Gmail | Invite delivery, RSVP |
| `accounts.google.com` | Auth |
| Google Calendar API | Programmatic access (OAuth; out of default offline path) |

---

## Zoom (web client)

| Item | Value |
|------|--------|
| Web join | [https://app.zoom.us/wc/join](https://app.zoom.us/wc/join) |
| Role | Browser join (Meeting ID + passcode) without desktop app |
| In invites | Often in LOCATION / DESCRIPTION / URL of VEVENT |
| Detail | `knowledge/calendar/zoom-web-join.md` |
| Privacy | `knowledge/privacy/zoom-hosts.md` |

Tag all Zoom join URLs as **CLICK**. Mask `pwd=` in any committed notes.

---

## Microsoft Teams free (live)

| Item | Value |
|------|--------|
| Free hub | [https://teams.live.com/free](https://teams.live.com/free) |
| Role | Start free meeting or join with Meeting ID + passcode |
| In invites | Often LOCATION / DESCRIPTION; work links may use `teams.microsoft.com` |
| Detail | `knowledge/calendar/teams-live-free.md` |
| Privacy | `knowledge/privacy/teams-live-hosts.md` |
| Procedure | **join-teams** |

Tag all Teams join URLs as **CLICK**. Mask passcodes. Free duration/features VERIFY LIVE.

---

## iCalendar (.ics) essentials

RFC 5545 family. Minimal event:

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Fable Offline//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
UID:example-001@fable.local
DTSTAMP:20260712T000000Z
DTSTART:20260715T010000Z
DTEND:20260715T020000Z
SUMMARY:Example meeting
LOCATION:Meet or Zoom or Teams free link or room
DESCRIPTION:Agenda line 1\\nAgenda line 2
END:VEVENT
END:VCALENDAR
```

| Field | Meaning |
|-------|---------|
| `METHOD` | PUBLISH / REQUEST / REPLY / CANCEL (mail invites) |
| `UID` | Stable id for updates |
| `DTSTART` / `DTEND` | Instant or local+TZID |
| `RRULE` | Recurrence |
| `ORGANIZER` / `ATTENDEE` | Mail-style addresses |
| `STATUS` | CONFIRMED / TENTATIVE / CANCELLED |
| `VALARM` | Reminders |

**Parse offline:**

```bash
python scripts/ical_parse.py path/to/invite.ics
python scripts/ical_parse.py path/to/invite.ics -o workspace/ical-summary.md
```

---

## Mail integration (invites)

| Pattern | Agent action |
|---------|--------------|
| `.ics` attachment | `parse-ical` |
| Inline `BEGIN:VCALENDAR` | Paste → parse |
| RSVP buttons in Gmail | User clicks in client; agent drafts wording only |
| Thread recap | `meeting-notes` / `mail-draft` recap |

**Hygiene:** strip tracking pixels from HTML mail when pasting body text into knowledge; do not commit full mailbox exports.

---

## Meetings stack

| Stage | Procedure | Artifact |
|-------|-----------|----------|
| Before | `meeting-prep` | Agenda + GCal description paste |
| During/after | `meeting-notes` | Decisions + actions |
| Scheduling | `schedule-hygiene` / `mail-draft` | Invite or reschedule text |
| Privacy design | `map-calendar-privacy` | Host map |

See `meetings-playbook.md`.

---

## HITL gates

- Sending mail or creating remote events  
- Sharing secret calendar URLs  
- Recording meetings  
- Exporting attendee PII into shared git  

---

## Cross-links

- Privacy design → `privacy-design-planner`  
- Host evidence → `knowledge/privacy/google-calendar-hosts.md`  
- Legal retention / recording → `legal-playbook` (when counsel positions exist)
