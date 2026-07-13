# Snapchat for Web — feed protocol

**WHEN_TO_USE:** Using or coaching **Snapchat for Web** at [web.snapchat.com](http://web.snapchat.com/) (often redirects to [snapchat.com/web](https://www.snapchat.com/web)), Chat feed navigation, desktop snaps/calls, multi-device session rules, privacy/screen-hide behaviour, troubleshooting browsers, or contrasting web feed vs mobile. Complements **`calendar-mail-meetings`** (calls) and **`privacy-host-map`** (trackers on snap domains).

## Stance
You coach **legitimate, authenticated** use of Snap’s **official** web client. Fable does **not** log into Snapchat, scrape friends lists, harvest snaps, automate mass messaging, or bypass age/verification. User **CLICK** + login only.

**Not legal advice.** Snap Terms and Community Guidelines apply. Ephemeral does **not** mean un-saveable by others — coach hygiene, not false security.

---

## Official entry points

| URL | Role |
|-----|------|
| [http://web.snapchat.com/](http://web.snapchat.com/) | Canonical web client entry (user may be redirected) |
| [https://www.snapchat.com/web](https://www.snapchat.com/web) | Marketing / alternate web surface |
| [accounts.snapchat.com](https://accounts.snapchat.com/v2/login) | Login |
| [help.snapchat.com](https://help.snapchat.com/) | Support |
| [Privacy by Product — Snapchat for Web](https://values.snap.com/privacy/privacy-by-product/snapchat-web) | Product privacy notes |

Knowledge: `knowledge/social/snapchat-web-feed.md` · privacy seed `knowledge/privacy/snapchat-web-hosts.md`

---

## Feed protocol (high level)

```text
1. Browser check (Chrome / Edge / Safari current)
2. Open web.snapchat.com  →  login (credentials / QR / 2SV as prompted)
3. Chat feed  →  select conversation
4. Message / Snap / Call / Lenses (subset on web)
5. Privacy screen when unfocused (web behaviour)
6. One computer session at a time (logout previous)
7. Sign out when done on shared machines
```

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| Full session checklist | **web-session-protocol** |
| Open / use Chat feed | **feed-navigate** |
| Send message or snap (user does UI) | **compose-hygiene** |
| Start audio/video call | **call-from-web** |
| Privacy / shared-device hygiene | **privacy-screen-protocol** |
| Troubleshoot access | **troubleshoot-web** |
| Map hosts from dump/Network | **map-snap-privacy** |
| Contrast web vs mobile | **web-vs-mobile** |
| Persist notes (no credentials) | **write-knowledge** |
| Short answer | **brief** |

Default: **web-session-protocol**.

---

## web-session-protocol

**Output:**
1. Verdict — ready / wrong browser / 2SV needed / eligibility UNKNOWN  
2. Steps (user performs):  
   - Use **Chrome, Edge, or Safari** (latest) per Snap Help  
   - Go to **web.snapchat.com**  
   - Sign in with Snapchat credentials  
   - Complete identity check if prompted (**push notification** to mobile Snapchat app is common)  
   - Phone app should be latest + **same account**  
   - Confirm **only one computer** web session (new login kicks previous PC)  
3. After login: Chat feed left/primary list → open thread  
4. Bitmoji may show **laptop** indicator so friends know you’re on web  
5. Sign-out checklist for shared PCs  

---

## feed-navigate

| Action | Protocol |
|--------|----------|
| Open feed | After auth, use **Chat** list / feed of conversations |
| Open chat | Click friend / group name in feed |
| Context | Continue conversations from mobile (sync expectation — VERIFY LIVE) |
| Stories / Spotlight | Feature set on web may lag mobile — mark UNKNOWN if not confirmed |

Do **not** invent UI labels that change; say “Chat feed / conversation list.”

---

## compose-hygiene

User composes in web UI. Coach only:

| Do | Don’t |
|----|--------|
| Pause before sensitive snaps on **desktop camera** | Assume snaps can’t be screenshotted |
| Check who is in the thread | Paste secrets into group chats |
| Use web for multitasking carefully (privacy screen) | Leave web logged in on public PCs |
| Respect disappearing message expectations | Scrape or archive others’ content without consent |

Fable may draft **message text** offline; user pastes/sends.

---

## call-from-web

Per Snap Help (VERIFY LIVE):

1. Open friend’s chat from **Chat feed**  
2. **Video camera** icon → video chat · **Phone** icon → audio call  
3. Lenses on web: **selected set** only (not full mobile suite)  
4. Creative tools may be incomplete vs app  

**Snap capture (Help):** Camera control → click lens icon for photo · **hold** lens icon for video.  
**Screenshot honesty:** others can still screenshot or use another device.

Privacy: [Snapchat for Web](https://values.snap.com/privacy/privacy-by-product/snapchat-web) · Help privacy link on article.

---

## privacy-screen-protocol

Known web behaviour (product privacy pages / launch notes — VERIFY LIVE):

| Behaviour | Meaning for protocol |
|-----------|----------------------|
| Privacy screen when focus leaves window | Reduces shoulder-surfing when switching apps |
| Laptop Bitmoji state | Signals web presence to chat partners |
| One desktop session | Limits concurrent web logins |

Additional hygiene:

- Prefer private browser profile for work/personal separation  
- Never store Snapchat password in Fable git  
- 2SV on account  

---

## troubleshoot-web

| Symptom | Checks (Snap Help themes) |
|---------|---------------------------|
| Can’t access | Browser = Chrome / Edge / Safari latest; reload; try another supported browser |
| Login loop | Phone 2SV; network; clear site data carefully |
| Logged out unexpectedly | Another computer logged into web |
| Missing features | Expected web ≠ full mobile; use app for full Lenses/tools |
| Error page | help.snapchat.com · Chrome often recommended |

---

## map-snap-privacy

Apply **privacy-host-map** to any HTML/Network dump of web.snapchat.com / accounts.snapchat.com. Seed: `knowledge/privacy/snapchat-web-hosts.md`.

Tags: first-party Snap domains **LOAD**; third-party analytics if present; login **CLICK** to accounts.

---

## web-vs-mobile

| | Web | Mobile app |
|--|-----|------------|
| Device | Desktop browser | Phone/tablet |
| Primary use | Chat, calls, multitasking | Full camera / AR / discovery |
| Lenses / tools | Subset on calls | Full set |
| Presence cue | Laptop Bitmoji | Normal Bitmoji |
| Session | One computer at a time | Phone sessions separate rules |

---

## Forbidden
- Account takeover, credential stuffing, or 2SV bypass  
- Scraping friends, snaps, or locations  
- Bots for spam, harassment, or mass adds  
- Deepfake non-consensual snaps  
- Storing session cookies / QR login secrets in git  

## Local knowledge
- `knowledge/social/snapchat-web-feed.md`  
- `knowledge/privacy/snapchat-web-hosts.md`  

## Companion skills
| Skill | Use |
|-------|-----|
| `privacy-host-map` | Tracker inventory |
| `calendar-mail-meetings` | Call scheduling around chats |
| `instagram-selfie-selector` | Cross-platform creative (not Snap login) |
| `tiktok-ads-create` | Unrelated paid social |
