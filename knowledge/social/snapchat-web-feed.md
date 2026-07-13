# Snapchat for Web — feed protocol

**Skill:** `snapchat-web-feed`  
**Entry:** [http://web.snapchat.com/](http://web.snapchat.com/) (may redirect; also [snapchat.com/web](https://www.snapchat.com/web))  
**Official help:** [Call, Snap, and Chat from Web](https://help.snapchat.com/hc/en-us/articles/7121575005332)  
**Privacy product page:** [Snapchat for Web](https://values.snap.com/privacy/privacy-by-product/snapchat-web)  
**Not legal advice.** Feature set and eligibility change — VERIFY LIVE.

---

## Verdict

Snapchat for Web is Snap’s **desktop browser client** for chat, snaps, and calls. Protocol centres on **Chat feed → conversation → action**. Not a full substitute for mobile AR; Lenses/tools are reduced on web.

---

## Access protocol

| Step | Action |
|------|--------|
| 1 | Browser: **Chrome, Microsoft Edge, or Safari** (latest) |
| 2 | Phone: latest Snapchat app, **same account** logged in |
| 3 | Open **web.snapchat.com** |
| 4 | Sign in with Snapchat credentials |
| 5 | Identity check: may **push-notify** the mobile app to confirm it’s you |
| 6 | Session rule: **one computer at a time** — new web login logs out previous computer |

---

## Chat feed protocol

| Action | How (Help) |
|--------|------------|
| Open feed | After login, use **Chat feed** (conversation list) |
| Open chat | Click a friend’s name in the Chat feed |
| Video chat | In chat → **video camera** icon |
| Audio call | In chat → **phone** icon |
| Take Snap | Click **Camera** |
| Photo Snap | Click **lens** icon |
| Video Snap | **Hold** lens icon |
| Lenses | Lens icon; **subset** of mobile Lenses on web calls |

### Presence & privacy (product notes)

| Behaviour | Detail |
|-----------|--------|
| Web presence | Bitmoji may appear with **laptop** so others know you’re on web (launch-era behaviour — VERIFY LIVE) |
| Focus privacy | Web may **hide content** when you click away (privacy screen — VERIFY LIVE) |
| Screenshots | Recipients can still screenshot or film with another device — same as app |

---

## Troubleshooting (Help)

### Can’t access Web
- Supported browser + latest version  
- Phone app latest + same account  
- Reload / try another supported browser  
- [Snapchat Support](https://help.snapchat.com/)

### Audio issues
- Mic volume; mic permission; switch mic source (arrow next to mic); disconnect headphones/BT  
- If you can’t hear: PC mute, tab mute, output source, browser sound permission  

### Video issues
- Camera permission; test camera elsewhere; switch camera source; disconnect other cameras  

### Permissions article
- Notifications / camera / mic: related Help article on changing Snapchat for Web permissions  

---

## Operator checklist (Fable protocol card)

```markdown
# Snapchat Web session — [date]
## Browser / version
## Account (username only — no password)
## 2SV / push confirm done?
## Goal (chat / call / snap)
## Feed actions taken (user)
## Issues
## Signed out on shared PC?
```

---

## What Fable must not do

- Automate login or store session cookies  
- Scrape Chat feed, friends, or snaps  
- Mass-message or spam protocols  
- Claim snaps are impossible to capture  

---

## Cross-links

- Skill: `snapchat-web-feed`  
- Privacy seed: `../privacy/snapchat-web-hosts.md`  
- Meetings contrast: Zoom web join (`calendar` knowledge)  
