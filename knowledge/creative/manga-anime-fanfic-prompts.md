# Manga / anime fanfiction prompt generator — framework

**Skill:** `manga-anime-fanfic-prompt-kit`  
**Handoff:** `inkstone-resource-kit` (serialize web novel), `prompt-generator` (agent swarm), `animation-dev-kit` (board/animatic)  
**Not legal advice.** Transformative fan works may still infringe rights by jurisdiction — user owns compliance. Prefer **original characters / settings** when publishing commercially.

---

## Franchise seed (public lore only): *Highschool of the Dead: The Last Day*

| Field | Public seed (VERIFY LIVE wiki) |
|-------|--------------------------------|
| JP title | 学園黙示録 HIGHSCHOOL OF THE DEAD 〈終わり〉の日 (*Owari no Hi*) |
| Form | Official **light novel** side story |
| Author | **Daisuke Sato** (series creator) |
| Pub seed | **March 2011** · limited-edition bundle · rare in print |
| English | **No official English edition** seed — collectors seek physical JP copies |
| Role | Side story of the **immediate onset** of the worldwide zombie pandemic |
| Focus | Main cast fallout; **Takashi Komuro** & childhood friend **Rei Miyamoto** |
| Iconic beats (summary only) | Teacher turns at **Fujimi High** front gates; frantic escape from faculty lounge before mass panic |
| Lore hubs | [Wikipedia — Highschool of the Dead](https://en.wikipedia.org/wiki/Highschool_of_the_Dead) · HOTD Wiki · *The Last Day* Fandom page |

**Fable rule:** Use for **tone / structure prompts** (first hours of outbreak, school escape, duo POV). Do **not** paste copyrighted novel text, scan pages, or generate a chapter-by-chapter rewrite of the commercial LN. Generate **new** scenes, OCs, AUs, or “inspired by” beats.

---

## Prompt stack (what a good fanfic prompt includes)

| Layer | Contents |
|-------|----------|
| **Format** | oneshot · multi-chapter · script (manga panel / anime episode) · light-novel prose |
| **POV** | 1st · 3rd limited · multi-POV · dual (e.g. two leads) |
| **Genre tags** | zombie · school · survival · romance · horror · action · found family · dark comedy |
| **Tone** | desperate · gallows humour · gritty · soft recovery · YA thriller |
| **Time box** | first hour · first day · three-day siege · timeskip AU |
| **Constraint** | word count · page count · rating (G–M) · no-go list |
| **Conflict** | external threat · moral choice · interpersonal trust · scarce resources |
| **Twist seed** | optional single twist — not a full spoiler dump |
| **Output contract** | outline · scene · full script · panel descriptions |

---

## Manga / anime script schemas

### A — Prose oneshot prompt
```text
Write a {word_count}-word {genre} oneshot in {pov}.
Setting: {setting}. Time: {timebox}.
Protagonists: {chars} (relationship: {relation}).
Opening image: {cold_open}.
Must include: {beats}.
Tone: {tone}. Rating: {rating}.
End on: {ending_type}.
Avoid: {nogo}.
```

### B — Manga panel script
```text
Format: manga script, {pages} pages, {panels_per_page} panels avg.
Page 1 cold open → …
Each panel: SHOT | ACTION | DIALOGUE/SFX | NOTES
Style refs: {art_mood} (original art notes only — no tracing).
Climax page: {climax}.
```

### C — Anime episode beat sheet
```text
Runtime target: {minutes} (e.g. 22).
Teaser | A-plot | B-plot | Midpoint | Climax | Tag.
Cold open visual: {image}.
Episode question: {question}.
Act-out cliff: {cliff}.
```

### D — Light-novel chapter brief
```text
Chapter goal: {goal}.
POV character: {char}.
Hook sentence idea: {hook}.
3 scene cards: (1) (2) (3).
End hook: {end_hook}.
```

---

## Outbreak / “first hours” module (HOTD-adjacent, original-safe)

Use when user wants **chaotic onset** energy without copying *The Last Day* prose:

| Beat slot | Prompt pressure |
|-----------|-----------------|
| Normal morning | Routine at school/work — one wrong detail |
| First wrong body | Authority figure fails public “human” check |
| Gate / exit blocked | Escape route becomes kill zone |
| Small room siege | Faculty lounge / classroom / store room |
| Trust fracture | Childhood friend vs stranger priority |
| First kill decision | Moral cost before skills exist |
| Noise = death | Sound design in prose/panels |
| Outside wider than school | Radio/phone → city-scale dread |

**OC / AU variants:** different school · rural station · ferry · mall · hospital shift change.

---

## Trope dials (safe generators)

| Dial | Low | High |
|------|-----|------|
| Romance | Glances | Confession under fire |
| Gore | Off-panel | Explicit (rating gate) |
| Tactics | Pure panic | Early military competence (justify) |
| Hope | Bleak | Found-family spark |
| Comedy | None | Dark one-liners |

---

## Anti-copy checklist

| Do | Don’t |
|----|--------|
| Original dialogue & scene order | Reproduce LN chapter text |
| AU / OC / “inspired by first-hours outbreak” | Claim official unpublished English text |
| Cite wiki for **public** facts | Scrape paid raws / pirated PDFs |
| User HITL for publish platform ToS | Mass-spam low-quality chapters to Inkstone |

---

## Scaffold

```text
workspace/creative/fanfic-prompts/
  hotd-style-first-hours.md
  manga-script-01.md
  episode-beats-01.md
generated_prompts/fanfic/   # optional bulk (gitignored pattern may apply)
```

---

## Related hubs

- Franchise lore: Wikipedia + fandom wikis (VERIFY LIVE)  
- Serialization: `inkstone-resource-kit`  
- Agent swarms for outline→draft→editor: `prompt-generator`  
