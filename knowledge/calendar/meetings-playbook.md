# Meetings playbook (offline)

**Skill:** `calendar-mail-meetings`  
Companion to Google Calendar / Zoom / **Microsoft Teams** / iCal / mail flows.

---

## Before (prep)

```markdown
# Prep — [title] — [local datetime + tz]
## Objective (1 sentence)
## Success looks like
## Agenda (time-boxed)
- 0–5m: context
- …: decisions
- last 5m: actions + owners
## Pre-reads
## Decisions needed
## Non-goals
## Links (Meet / Zoom / Teams / docs) — user-supplied only
- Google Meet: `meet.google.com/…`
- Zoom web join: [app.zoom.us/wc/join](https://app.zoom.us/wc/join) or full `zoom.us/j/…` invite
- Teams free: [teams.live.com/free](https://teams.live.com/free) (Meeting ID + passcode) or work `teams.microsoft.com` invite
- See `zoom-web-join.md` · `teams-live-free.md` for join checklists
```

Paste objective + agenda into Google Calendar **description** so guests see it without a separate doc if possible.

---

## During / after (notes)

```markdown
# Notes — [title] — [date]
## Attendees (present / absent)
## Decisions
## Actions | Owner | Due | Status
## Risks / blockers
## Parking lot
## Next meeting (if any)
```

---

## Mail templates (draft only)

### Invite sketch
- **Subject:** `[Meeting] {topic} — {date} {time} {tz}`
- **Body:** purpose, agenda bullets, join link placeholder, prep ask, decline path

### Decline
- Thanks + conflict + optional alternative windows (user’s real availability only)

### Recap
- Decisions, actions table, links to notes; no confidential paste into wide CC

---

## Conflict rules of thumb

1. Protect deep-work blocks on calendar (show busy)  
2. Default 25/50 minute meetings to create buffer  
3. Recurring series: kill or shrink if no decisions for two cycles  
4. Shared calendars: avoid sensitive titles (“HR: PIP — Name”)  

---

## Local storage

| Path | Content |
|------|---------|
| `knowledge/calendar/_local/` | Private agendas, secret feed notes (gitignored) |
| `workspace/` | Temporary ical parse markdown |
| `memory/lessons/` | Durable process lessons only (no PII dumps) |
