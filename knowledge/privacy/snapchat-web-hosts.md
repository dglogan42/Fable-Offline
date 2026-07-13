# Privacy host map — Snapchat for Web (seed)

**Skill:** `privacy-host-map` · `snapchat-web-feed`  
**Property:** [web.snapchat.com](http://web.snapchat.com/) / Snapchat for Web  
**Evidence:** Official Help + Privacy by Product pages (not a full Network HAR)  
**Not legal advice.** Capture live Network on a logged-in session to complete.

---

## Verdict

**First-party Snap family** for authenticated chat/snap/call. Login and identity often involve **accounts.snapchat.com** and **mobile app push** confirmation. Expect standard web RTC media permissions (camera/mic) on the browser origin.

---

## Host inventory (seed)

| Host / pattern | Tag | Notes |
|----------------|-----|--------|
| `web.snapchat.com` | origin **LOAD** / **CLICK** | Web client |
| `www.snapchat.com` | **CLICK** / marketing | `/web` landing |
| `accounts.snapchat.com` | **LOAD** / auth | Login / signup |
| `help.snapchat.com` | **CLICK** | Support |
| `snap.com` / `values.snap.com` | **CLICK** | Privacy by Product |
| `*.snapchat.com` / Snap CDN | **LOAD** | App assets (VERIFY on Network) |
| Browser permissions | local | Camera, microphone, notifications |

### Auth / session (product behaviour)

| Signal | Notes |
|--------|--------|
| Credentials login | Username/email/phone + password (user-held) |
| Push to mobile app | “Make sure it’s really you” |
| Single desktop session | Concurrent web login kicks previous PC |

---

## Data classes

| Data | Sensitivity | Fable handling |
|------|-------------|----------------|
| Chat content | High | Never store in git |
| Snap media | High | Local only if user exports |
| Session cookies | Secret | Not committed |
| Friend graph | High | Not scraped |

---

## Cross-links

- Protocol: `knowledge/social/snapchat-web-feed.md`  
- Skill: `snapchat-web-feed`  
