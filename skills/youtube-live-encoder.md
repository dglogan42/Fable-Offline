# YouTube live stream with an encoder

**WHEN_TO_USE:** Setting up **YouTube Live** via **encoder** (OBS, Streamlabs, hardware RTMP, etc.), Studio Live Control Room steps, stream key hygiene, schedule vs instant go-live, VTuber capture from **VTube Studio**, or coaching first-time encoder streams. Official guide: [Create a YouTube live stream with an encoder](https://support.google.com/youtube/answer/2907883?hl=en). Companion: `vtube-studio-resource-kit` for Live2D tracking before encode.

## Stance
You coach **legitimate** YouTube Live production using official Studio + third-party encoders. YouTube does not make those encoder products — evaluate them yourself. **Never** paste or store **stream keys** in git, chat logs, or public knowledge.

**Not legal advice.** Follow [YouTube policies](https://support.google.com/youtube) (live, spam, monetization). Do not coach policy evasion, fake live 24/7 scrapes of others’ content, or key theft.

User creates streams and starts encoders **themselves** (HITL).

---

## Three ways to stream (official)

| Method | Typical use |
|--------|-------------|
| Webcam | Simple in-browser / Studio webcam path |
| Mobile device | Phone/tablet live |
| **Encoder** | Screen/game capture, external A/V, multi-cam production |

Encoder benefits (Help): share screen/gameplay · external mics/cameras · advanced multi-source production.

---

## Protocol (encoder path)

```text
1. Enable live streaming on the channel (first time may take up to 24 hours)
2. Install / set up encoder (software or hardware)
3. Connect cameras, mics, capture devices to encoder
4. YouTube Studio → CREATE → Go live → Stream tab → create/reuse stream
5. Copy Server URL (RTMP) + Stream key into encoder
6. Start encoder → go live (instant or scheduled flow)
7. End: stop encoder; optional End Stream in Studio
```

Knowledge: `knowledge/media/youtube-live-encoder.md`

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| Full first-stream plan | **live-encoder-plan** |
| Enable live + eligibility | **enable-live** |
| Pick encoder type | **choose-encoder** |
| Hardware / A/V setup | **connect-hardware** |
| Studio + RTMP connect | **connect-go-live** |
| Schedule + promote | **schedule-stream** |
| Stream key / security hygiene | **key-hygiene** |
| End stream + archive | **end-archive** |
| Persist runbook (no secrets) | **write-knowledge** |
| Short answer | **brief** |

Default: **live-encoder-plan**.

---

## live-encoder-plan

**Output:**
1. Verdict — ready / wait for enable / missing gear  
2. Steps 1–7 from protocol  
3. Encoder recommendation class (free software vs browser studio vs hardware) — not product endorsement  
4. Preflight: bitrate/resolution vs upload; audio levels; key private  
5. Links: answer/2907883, enable live, verified encoders list  
6. OPEN unknowns  

---

## enable-live

- First enable may take **up to 24 hours**; after that, stream instantly (Help).  
- Point user to official “start live streaming / enable” article ([answer/2474026](https://support.google.com/youtube/answer/2474026) family — VERIFY LIVE).  
- Channel must meet YouTube’s current live eligibility (VERIFY LIVE — requirements change).  

---

## choose-encoder

| Class | Examples named by YouTube Help (third-party) | Notes |
|-------|-----------------------------------------------|--------|
| Free / OSS software | **OBS**, Streamlabs, PRISM, XSplit (free tiers) | Popular starting point |
| Browser / cloud studio | StreamYard, Streamlabs Talk Studio, Restream, Grabyo, … | Less local install |
| Game capture | Elgato software, Gamecaster, … | Console/PC game |
| Hardware | AJA HELO, Blackmagic Web Presenter, LiveU Solo, Teradek, … | Pro / field |
| Mobile apps | Larix, PRISM mobile, Wirecast Go, Streamlabs mobile | IRL |

Full curated names: knowledge file. Re-check [YouTube Live verified encoders](https://support.google.com/youtube/answer/6259859). **None made by YouTube.**

---

## connect-hardware

Typical kits (Help framing):

| Tier | Gear |
|------|------|
| Gaming / casual | Mic, webcam, headphones; optional greenscreen |
| Pro | Multi-cam, multi-mic, mixer, hardware encoder |

Confirm devices appear in encoder; set levels before go-live.

---

## connect-go-live

**Create stream (Studio):**
1. [studio.youtube.com](https://studio.youtube.com)  
2. **CREATE** → **Go live** → Live Control Room  
3. **Stream** tab  
4. First time: edit → **Create stream**; later: previous settings/key may reload  
5. Privacy: Help notes default **private** for ages 13–17, **public** for 18+ — always confirm setting  
6. YPP monetization options if eligible ([monetize live](https://support.google.com/youtube/answer/7385599) family)

**Encoder:**
1. Prefer encoder’s built-in YouTube destination if present  
2. Else paste **Server URL** (RTMP) + **Stream key**  
3. Start encoding → watch page created; notifications/subscriber feed per YouTube  
4. End: stop encoder (and End Stream in Studio when scheduled flow requires)

**Scheduled flow:** Manage tab → SCHEDULE STREAM → at start time, encoder + **Go live** after preview appears.

---

## key-hygiene

| Rule |
|------|
| Treat stream key like a password |
| Never commit to git, paste in public tickets, or screenshot publicly |
| Rotate/reset key in Studio if leaked |
| Prefer `knowledge/media/_local/` only if must note key id — not the key itself |

---

## schedule-stream

- Promote: reminders, share URL, trailers ([trailers](https://support.google.com/youtube/answer/9854503) family)  
- Reuse settings or create new  
- At start: encoder + Studio **Go live** after preview  

---

## end-archive

- Stop encoder; End Stream in Studio if needed  
- Streams under **12 hours** auto-archived (Help)  
- Manage in Live tab / Studio dashboard  

**Live Control Panel:** pop-out dashboard during encoder/webcam streams for compact views/chat revenue.

---

## Forbidden
- Sharing or harvesting others’ stream keys  
- Coaching ToS-breaking “fake live” / recycled content abuse  
- Guaranteeing monetization or recommended eligibility  
- Storing stream keys in repo  

## Local knowledge
- `knowledge/media/youtube-live-encoder.md`  

## Companion
| Skill | Use |
|-------|-----|
| `tiktok-ads-create` | Paid social — different platform |
| `rss-share` | Promote schedule via feed (optional) |
| `privacy-host-map` | Studio/analytics hosts if dumping HTML |
