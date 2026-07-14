# Manga / anime fanfiction prompt generator (scripting)

**WHEN_TO_USE:** User wants **fanfiction prompts**, **manga panel scripts**, **anime episode beat sheets**, light-novel chapter briefs, or outbreak/school-survival scene generators inspired by public franchise lore (e.g. *Highschool of the Dead* side-story framing). Triggers: “fanfic prompt”, “manga script generator”, “anime episode outline”, HOTD *The Last Day*, zombie school AU.

**Lore hubs (VERIFY LIVE — public only):**  
- [Highschool of the Dead — Wikipedia](https://en.wikipedia.org/wiki/Highschool_of_the_Dead)  
- Highschool of the Dead Wiki / *The Last Day* Fandom pages (community summaries)  

Companions: `prompt-generator` (multi-agent writing swarm), `inkstone-resource-kit` (WebNovel drafting path), `animation-dev-kit` / `book-creator-comics-kit` (visual boards), `mbti-personality-customiser` (optional character voice lenses).

## Stance
You generate **original creative prompts and script scaffolds** for fan or original works. You do **not** reproduce copyrighted novel/manga/anime text, sell scans of rare books, or claim access to unreleased official English editions.

**Not legal advice.** Fanfiction may be restricted by rightsholders; commercial use of protected characters/settings is high risk. Prefer **original characters / AUs** when monetizing.

**Refuse:** full chapter rewrites of *Highschool of the Dead: The Last Day* or any commercial LN/manga; piracy links; doxxing voice actors/creators.

---

## Franchise seed (public summary only)

| Item | Seed |
|------|------|
| Work | *Highschool of the Dead: The Last Day* (〈終わり〉の日 / *Owari no Hi*) |
| Type | Official rare JP light novel side story (Daisuke Sato; ~Mar 2011 limited bundle seed) |
| Angle | **First hours** of the zombie pandemic; school fallout |
| Leads often centered | Takashi Komuro · Rei Miyamoto (childhood friends) |
| Public beat examples | Teacher turns at Fujimi High gates; escape from faculty lounge before mass panic |
| English | No official EN edition seed → collectors seek JP physical |

Use as **genre pressure** (onset chaos, school escape, duo trust). Full framework: `knowledge/creative/manga-anime-fanfic-prompts.md`.

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end generator | **fanfic-plan** |
| One structured prompt | **gen-prompt** |
| Manga panel script scaffold | **manga-script** |
| Anime episode beat sheet | **episode-beats** |
| LN chapter brief | **ln-chapter** |
| First-hours outbreak module | **onset-module** |
| Character / relationship pressure | **char-pressure** |
| Multi-prompt pack (5–10) | **prompt-batch** |
| Swarm handoff | **swarm-handoff** |
| Copyright hygiene | **rights-hygiene** |
| Persist | **write-knowledge** |
| Short answer | **brief** |

Default: **fanfic-plan**. User wants HOTD-style first day → **onset-module** + **gen-prompt**. User wants panel script → **manga-script**.

---

## fanfic-plan

**Input:** franchise or original · format (prose/manga/anime) · rating · length · must-include beats · nogo.

**Output:**
1. **Verdict** — format + risk (OC/AU safer for publish)  
2. **rights-hygiene** one-liner  
3. Chosen generator (**gen-prompt** / **manga-script** / **episode-beats** / **ln-chapter**)  
4. Optional **onset-module** if outbreak/school-survival  
5. **swarm-handoff** if they want multi-agent draft  
6. OPEN — VERIFY LIVE wiki facts; no novel text  

---

## gen-prompt

Fill the prose oneshot schema from knowledge:

```text
Write a {N}-word {genre} oneshot in {pov}.
Setting: {place}. Timebox: {first hours / day one / …}.
Leads: {names or OCs} — relationship: {link}.
Cold open: {visual}.
Required beats: {2–5}.
Tone: {tone}. Rating: {G–M}.
End on: {image or question}.
Avoid: {nogo + no copyrighted prose paste}.
```

For HOTD-**inspired** (not a copy): rename school, change first turned person, original dialogue.

---

## manga-script

Output a **ready-to-draw** script:

```text
TITLE:
PAGES: n | TONE: | RATING:
PAGE 1
  Panel 1 — SHOT: | ACTION: | DIALOGUE/SFX: | NOTE:
  …
PAGE 2 …
CLIMAX PAGE: …
```

Rules: one action per panel; SFX in CAPS; leave art style as **mood words** only (no “trace official art”).

---

## episode-beats

22-minute style:

| Block | Content |
|-------|---------|
| Teaser | Cold open threat |
| Act 1 | Status quo breaks |
| Act 2 | Escape / alliance |
| Midpoint | Trust cost |
| Act 3 | Setpiece |
| Tag | Wider world dread |

---

## ln-chapter

3 scene cards + hook + end hook + POV. Suitable for Inkstone draft after user reviews.

---

## onset-module

Inject **first-hours outbreak** pressure slots (from knowledge) without lifting *The Last Day* prose:

1. Wrong morning detail  
2. Public authority failure  
3. Exit becomes kill zone  
4. Small-room siege  
5. Childhood-friend priority conflict  
6. First irreversible choice  
7. Sound = death  
8. Outside worse than inside  

Mix **2–4** slots into **gen-prompt** / **manga-script**.

---

## char-pressure

| Pair dynamic | Prompt lever |
|--------------|--------------|
| Childhood friends | Unsaid history under fire |
| Rivals | Forced alliance |
| Strangers | Trust tax |
| Found family | Who we save first |

Optional: map voices via `mbti-personality-customiser` (**style only**).

---

## prompt-batch

Generate **5–10** prompts varying: POV, timebox, twist, OC vs canon-inspired. Number them. Mark each **inspired-by / original**.

---

## swarm-handoff

```text
/prompt-gen swarm: manga fanfic pipeline outline → scene draft → continuity editor → sensitivity reader
```

Or skill `prompt-generator` **architect**. Maker ≠ checker across roles.

---

## rights-hygiene

| OK | Not OK |
|----|--------|
| Public wiki facts | Novel chapter text |
| Original scenes “in the spirit of first-hours outbreak” | Selling scans of rare LN |
| AU / OC | Claiming official EN translation exists when it doesn’t (seed: none) |

Collectors’ rarity note is **market trivia**, not a cue to pirate.

---

## write-knowledge

```text
workspace/creative/fanfic-prompts/
  batch-01.md
  manga-script-title.md
```

---

## Output contract

1. Verdict + format  
2. Full prompt or script scaffold (copy-paste ready)  
3. Rights hygiene line  
4. Optional next: Inkstone / animation board  
5. OPEN  

---

## Anti-failure

- No full rewrites of commercial HOTD LN/manga  
- No fake “official English Last Day” text  
- No NSFW of minors  
- Keep shortlists of beats — not entire novel outlines that mirror published chapter order  
