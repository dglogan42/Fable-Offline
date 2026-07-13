# Privacy host map — Google Calendar / Meet / mail (seed)

**Skill:** `privacy-host-map` + `calendar-mail-meetings`  
**Scope:** Public product surfaces around [Google Calendar](https://calendar.google.com/).  
**Not a penetration test. Not legal advice.** Authenticated account traffic varies; re-verify with live Network capture on your session.

---

## Verdict

Google Calendar, Gmail, Meet, and Accounts form a **single-vendor identity + productivity cluster**. Offline Fable should treat calendar data as **high sensitivity** (who meets whom, when, where). Prefer **local .ics exports** over embedding live Google sessions in the agent.

---

## Host inventory (seed)

| Host / pattern | Tag | Notes |
|----------------|-----|--------|
| `calendar.google.com` | **CLICK** / session **LOAD** | Main Calendar UI |
| `calendar.google.com/calendar/u/` | **LOAD** | User-scoped UI paths |
| `calendar.google.com/calendar/ical/` | **CONFIG** / secret | Private iCal feed patterns — treat URL as secret |
| `www.google.com/calendar` | **CLICK** | Redirects / legacy entry |
| `meet.google.com` | **CLICK** / **LOAD** | Video meetings from events |
| `mail.google.com` | **CLICK** / **LOAD** | Invite delivery / RSVP |
| `accounts.google.com` | **LOAD** | Auth, session |
| `apis.google.com` / `www.googleapis.com` | **CONFIG** | API surfaces if apps integrate |
| `clients*.google.com` | **LOAD** / **BUNDLE** | Client asset patterns (verify live) |
| `ssl.gstatic.com` / `www.gstatic.com` | **LOAD** | Static assets |
| `ogads-pa.clients6.google.com` etc. | **BUNDLE** until confirmed | Internal RPC-style hosts often appear in bundles |

Exact third-party tags on a given page load require a fresh capture; Google properties change frequently.

---

## Evidence rules

| Tag | Use here |
|-----|----------|
| **CLICK** | User navigates to Calendar / Meet / Gmail |
| **LOAD** | Scripts, XHR, images on Google hosts during session |
| **CONFIG** | API endpoints, iCal feed URLs, OAuth token endpoints |
| **BUNDLE** | Host strings only in JS until Network confirms |

---

## Data classes

| Data | Sensitivity | Fable handling |
|------|-------------|----------------|
| Event titles / guests | High | Local only; minimise in git |
| Secret iCal URL | Secret | `knowledge/calendar/_local/` only |
| OAuth tokens | Secret | `.env` / OS store; never commit |
| Public help pages | Low | May summarise |

---

## Design notes for agents

1. Default scope: **readonly** local files  
2. No password prompts in agent UX  
3. HITL before any send/create  
4. Cross-link: `knowledge/calendar/ical-and-google.md`

---

## Non-claims

- This map is **not** a complete inventory of all Google subdomains.  
- Presence of a host in a bundle ≠ processing of calendar content by that host.  
