# YouTube live stream with an encoder

**Skill:** `youtube-live-encoder`  
**Source:** [Create a YouTube live stream with an encoder](https://support.google.com/youtube/answer/2907883?hl=en) (YouTube Help)  
**Related:** Enable live ([answer/2474026](https://support.google.com/youtube/answer/2474026)), Verified encoders ([answer/6259859](https://support.google.com/youtube/answer/6259859)), Manage livestreams ([answer/9227510](https://support.google.com/youtube/answer/9227510))  
**Not product endorsement.** Encoder brands are third-party; evaluate yourself. **VERIFY LIVE** — UI labels change.

---

## Verdict

Official path for **encoder-based** YouTube Live: enable live → encoder → hardware → Studio stream URL/key → go live (or schedule). Encoder = software or hardware that converts A/V to a stream YouTube accepts (typically **RTMP** + stream key).

---

## Why use an encoder

Per Help, encoders let you:

- Share screen / broadcast gameplay  
- Use external audio and video hardware  
- Run advanced multi-camera / multi-mic productions  

Other YouTube live methods: **webcam**, **mobile device**.

---

## Step checklist (Help order)

### 1. Enable live streaming
- First-time enable may take **up to 24 hours**  
- After enable, stream can go live instantly  
- Follow current enable article linked from Help  

### 2. Install an encoder
- Converts video for YouTube  
- Software on PC/Mac **or** standalone hardware  
- Prefer [YouTube Live verified](https://support.google.com/youtube/answer/6259859) list as a starting shortlist — **not** made by YouTube  

### 3. Connect hardware
| Casual / gaming | Pro |
|-----------------|-----|
| Mic, webcam, headphones; optional greenscreen | Multiple mics/cameras, mixer, hardware encoder |

### 4. Connect encoder and go live
- Enter **YouTube Live server URL** + **stream key** into encoder  
- Start encoder after Studio stream exists  

---

## Studio: create stream (instant)

1. [YouTube Studio](https://studio.youtube.com)  
2. **CREATE** → **Go live** → Live Control Room  
3. **Stream** tab  
4. First stream: edit → **Create stream**  
5. Returning: previous settings (including key) may load — re-check encoder  
6. Privacy defaults (Help): ages **13–17** default **private**; **18+** default **public** — always set intentionally ([public/private/unlisted](https://support.google.com/youtube/answer/157177))  
7. YPP: monetize live if eligible  

### Connect encoder
1. Encoder “stream to YouTube” option if available  
2. Else paste **server URL** (RTMP) + **stream key**  
3. Start encoder → watch page created; notifications / subscriber feeds per YouTube  
4. End: stop encoder  

---

## Studio: schedule stream

1. Studio → CREATE → Go live  
2. **Manage** tab → **SCHEDULE STREAM**  
3. Reuse settings or create new  
4. Promote: reminders, share URL, optional [trailer](https://support.google.com/youtube/answer/9854503)  
5. At start: encoder running → wait for preview → **Go live**  
6. End: End Stream + stop encoder  

**Archive:** streams under **12 hours** auto-archived; find in Live tab / Studio dashboard.

**Live Control Panel:** pop-out dashboard (encoder/webcam) for compact views/chat revenue metrics.

---

## Encoder classes named on Help (snapshot)

### Software (examples)
OBS · Streamlabs · StreamYard · Wirecast · XSplit · PRISM Live Studio · Restream · Grabyo · AWS Elemental MediaLive · CamStreamer · Cinamaker · Elgato Game Capture · Gamecaster · Gyre · Nimbra Edge · Nimble Streamer · Stage TEN · Streamlabs Talk Studio · TITAN Live · Upstream · …

### Hardware (examples)
AJA HELO Plus · AWS Elemental Live · Blackmagic Web Presenter 4K · LiveU Solo · Teradek VidiU Go · Epiphan Pearl 2 · Osprey Talon · SlingStudio · Nimbra 400 · Appear SRT · Direkt Link · AirServer · Nvidia NVENC (GPU encode) · Elgato ecosystem · …

### Mobile (examples)
Larix Broadcaster · PRISM mobile · Streamlabs mobile · Wirecast Go · AirServer · …

**Re-verify full list** on the Help article — partners change.

---

## Secrets

| Secret | Handling |
|--------|----------|
| Stream key | Password-class; never in public git |
| Server URL | Less sensitive but keep with account security |
| Encoder cloud logins | User password manager |

---

## Policy hygiene (Fable)

- Do not coach re-uploading copyrighted live content as “24/7 live” to game watch time  
- Disclose sponsorships where required  
- Meet live eligibility and community guidelines  

---

## Cross-links

- Skill: `youtube-live-encoder`  
- Privacy of Studio pages: map with `privacy-host-map` if dumping HTML  
- RSS promote schedule: `rss-share`  
