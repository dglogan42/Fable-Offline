# Knit & Natter social club kit (local fibre meetups)

**WHEN_TO_USE:** User wants a **Knit & Natter** / knit-and-chat club, local **knitting groups**, Auckland Milford session details, how to **start a club** in a suburb, Meetup / guild discovery, or calendar invites for 2nd & 4th Tuesday sessions. Triggers: “knit and natter”, “stitch and bitch”, crochet meetup, yarn shop social, Handweavers Guild, Knit World groups.

**Official / discovery seeds (VERIFY LIVE):**  
- Knit & Natter 2026 (Auckland / Milford): [Wild & Woolly — Knit & Natter 2026](https://www.wildandwoollyyarns.co.nz/products/knit-natter-2026)  
- Meetup: search **Knitting groups — Auckland** (and other cities)  
- Handweavers & Spinners Guild Auckland — official guild channels (VERIFY LIVE)  
- Knit World: local knit & chat discovery ([knitworld.co.nz](https://www.knitworld.co.nz/) family)  

Companions: `calendar-mail-meetings` (recurring invites / .ics), `rss-share` (club newsletter feed optional), `privacy-host-map` (Meetup/Facebook event hosts), `arts-culture-agent` (venue/cultural hygiene, not fibre-specific).

## Stance
You help people **find, attend, or start** friendly local **knit & natter** social spaces. Fable does **not** take RSVPs, process payments, or run the club as merchant of record.

**Not medical, employment, or childcare advice.** Craft nights are social — not therapy. Accessibility and photo consent are host responsibilities.

**Refuse:** doxxing members; scraping private Meetup member lists into git; guaranteeing “$10 forever” without VERIFY LIVE.

---

## Seed club (Auckland Milford)

| Field | Seed |
|-------|------|
| **When** | 2nd & 4th **Tuesday**, **5:00–7:00 PM** |
| **Where** | Nirvana, **95 Kitchener Rd, Milford** (confirm door; yarn shop Wild & Woolly adjacency seed) |
| **Cost** | **$10** / person · **includes a drink** |
| **Series** | Knit & Natter **2026** — Auckland |
| **Source** | Wild & Woolly product/listing seed |

Knowledge: `knowledge/social/knit-natter-auckland.md`

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end club kit | **knit-plan** |
| Attend the Milford seed | **attend-milford** |
| Find more local groups | **discover-groups** |
| Start a club in a suburb | **start-club** |
| Cadence / calendar | **schedule-natter** |
| Host night runbook | **host-runbook** |
| Accessibility & vibe | **welcome-hygiene** |
| Privacy / platforms | **host-map** |
| Persist local notes | **write-knowledge** |
| Short answer | **brief** |

Default: **knit-plan**. User near Milford tonight → **attend-milford**. User wants to found a club → **start-club**.

---

## knit-plan

**Input:** city/suburb, attend vs start, craft (knit/crochet/spin), budget.

**Output:**
1. **Verdict** — social craft meetup; verify listing before travel  
2. **attend-milford** if Auckland North Shore / seed fits  
3. **discover-groups** for more options  
4. **start-club** blueprint if founding  
5. **schedule-natter** for calendar  
6. OPEN — prices/venues change  

---

## attend-milford

HITL checklist:

1. VERIFY LIVE [Knit & Natter 2026 listing](https://www.wildandwoollyyarns.co.nz/products/knit-natter-2026) (date, cost, venue).  
2. Confirm next **2nd or 4th Tuesday** 5–7pm.  
3. Navigate to **Nirvana, 95 Kitchener Rd, Milford** (map HITL).  
4. Bring project + tools; budget **$10** + drink included seed.  
5. Arrive ready to **natter** — all abilities welcome unless listing says otherwise.  
6. Optional: draft calendar event via `calendar-mail-meetings`.  

Do not invent sold-out status or host names.

---

## discover-groups

| Channel | How |
|---------|-----|
| Meetup | Search knitting / crochet / yarn + city |
| Yarn shops | Ask for weekly “knit night” (Wild & Woolly pattern) |
| Guilds | Handweavers & Spinners Guild Auckland — membership vs open events VERIFY LIVE |
| Retail blogs | Knit World “groups near you / knit & chat” style pages |
| Libraries | Free learn-to-knit sessions (council calendars) |
| Facebook Events | Shop-hosted Knit & Natter posts |

Rank by: recency of events, clear address, cost transparency, beginner-friendliness.

---

## start-club

Portable **local-area** blueprint:

```text
Name: Knit & Natter — {Suburb}
Cadence: 2nd & 4th Tuesday (or weekly)
Time: 17:00–19:00
Venue: café / hall / yarn shop / library room
Cover: $0–15 (drink/minimum common)
Host: volunteer or shop staff
Channels: Meetup + Event post + shop newsletter
Rules: all abilities · no hard sell · photo consent · accessibility note
```

### 30-day launch plan

| Week | Action |
|------|--------|
| 1 | Venue chat + test night of 1 hour |
| 2 | Publish first date (Event + Meetup) |
| 3 | Soft launch with friends + shop customers |
| 4 | Retrospect: time, noise, cover, frequency |

### Budget sketch (host)

| Item | Notes |
|------|--------|
| Venue | Free room vs per-head drink deal |
| Loaner tools | Cheap needle set |
| Promo | Free digital only first |
| Float | Cash for cover if needed |

Fable drafts posters/text; user publishes HITL.

---

## schedule-natter

Recurrence pattern seed: **RRULE** style “2nd and 4th Tuesday” — implement carefully (not every Tuesday).

User actions:
1. Create recurring calendar holds or two monthly series  
2. Time zone: Pacific/Auckland  
3. Location field: venue address  
4. Description: $10 + drink (if still true) + what to bring  

Skill: `calendar-mail-meetings` · optional Teams/Zoom only if hybrid (rare for natter).

---

## host-runbook

```text
T-7d: Confirm venue + post reminder
T-1d: Weather / illness cancel path
T-0: Arrive early · sign · welcome
During: Intro round · free craft · optional tip share
Close: Clean tables · thank venue · next date
```

---

## welcome-hygiene

| Practice | Why |
|----------|-----|
| All abilities | Low barrier social craft |
| No project shame | “Natter” > perfection |
| Quiet corners | Sensory / introvert option |
| Photo consent | Before group shots |
| Kids policy | State clearly if family-friendly |

---

## host-map

Classify Meetup / Facebook / shop checkout hosts with `privacy-host-map` when dumping HTML. Do not commit member rosters.

---

## write-knowledge

```text
workspace/social/knit-natter/
  clubs.md
  milford.md
```

---

## Output contract

1. Verdict — attend seed / discover / start  
2. Concrete time-place-cost when known  
3. VERIFY LIVE reminder  
4. Calendar or launch next step  
5. OPEN  

---

## Anti-failure

- Do not invent guild membership fees or Meetup ratings  
- Do not guarantee the $10 drink deal after 2026 without re-check  
- Do not list personal phone numbers of hosts without public source  
- Do not treat craft night as medical rehab  
