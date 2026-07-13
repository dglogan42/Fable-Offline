# Privacy host map — Microsoft Teams free / live (seed)

**Skill:** `privacy-host-map` + `calendar-mail-meetings`  
**Scope:** Teams **free meetings** surface and related hosts, seeded from  
[https://teams.live.com/free](https://teams.live.com/free).  
**Not a penetration test. Not legal advice.** Re-verify with live Network capture.

---

## Verdict

Video meetings carry **high-sensitivity** content (voice, video, chat, shared screens, files). Prefer **user-initiated CLICK** join. Offline Fable should not embed live Teams sessions or store meeting passcodes in git.

---

## Host inventory (seed)

| Host / pattern | Tag | Notes |
|----------------|-----|--------|
| `teams.live.com` | **CLICK** / **LOAD** | Free meetings hub (`/free`), personal Teams web |
| `teams.live.com/free` | **CLICK** | Start/join free meeting landing |
| `statics.teams.cdn.live.net` | **LOAD** | Evergreen assets (images, video placeholders) on free page |
| `teams.microsoft.com` | **CLICK** | Work/school Teams web (tenant) |
| `*.teams.microsoft.com` | **CLICK** / **LOAD** | Meetup-join deep links, tenant shells |
| `login.microsoftonline.com` / Microsoft account hosts | **CLICK** / **CONFIG** | Auth (VERIFY LIVE) |
| `insider.teams.com` | **CLICK** | What’s new / product updates |
| `support.microsoft.com` | **LOAD** / **CLICK** | Official join help (e.g. join-from-calendar article) |
| `www.microsoft.com` | **CLICK** | Marketing join-by-ID (`/microsoft-teams/join-a-meeting`) |
| `privacy.microsoft.com` | **LOAD** | Privacy statement links from personal-account join notes |
| Media / SFU / TURN hosts | **LOAD** | WebRTC/media (names change; capture live) |

Exact CDN and media hostnames vary by release and region.

---

## Evidence rules

| Tag | Use |
|-----|-----|
| **CLICK** | User opens free hub, join link, or Microsoft login |
| **LOAD** | Scripts, statics, media during web session |
| **CONFIG** | Auth/config APIs after sign-in |
| Never commit | Meeting passcodes, chat exports with PII, session cookies |

---

## Related Fable maps

- Google Calendar / Meet: `knowledge/privacy/google-calendar-hosts.md`  
- Zoom: `knowledge/privacy/zoom-hosts.md`  

---

## OPEN

- Full third-party analytics on free marketing page  
- Copilot / recording data paths when paid features enabled  
- Regional compliance banners  
