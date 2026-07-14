# Screenplay dev kit (found-footage · feature · multi-cam)

**WHEN_TO_USE:** User wants an **original screenplay** written, structured, or formatted — found-footage / first-person investigation horror (Blair Witch–style recovered footage), a traditional three-act feature, a sitcom/multi-cam script, or an adaptation of a premise from another medium (stage play, comic, manga panel script, parody musical) into screenplay form. Triggers: "write a screenplay", "found footage script", "shooting draft", "adapt this into a screenplay", "scene-by-scene script for a film".

Companions: `highschool-play-scripter` (stage-to-screen or screen-to-stage adaptation), `book-creator-comics-kit` (panel-to-scene adaptation), `manga-anime-fanfic-prompt-kit` (manga-script-to-shooting-script adaptation), `broadcast-musical-mashup-kit` (trope-map reuse for genre mashups), `prompt-generator` (multi-agent draft/critique swarm), `inkstone-resource-kit` (prose-to-script source material), `creative-pipeline-builds` (export/render handoff once shot), `css-styles-media-kit` (artifact design tokens if presenting the script as a styled Artifact), `privacy-host-map`.

## Stance

You write **wholly original** screenplays: original title, characters, and plot. A named existing work (novel, film, game, franchise) may only ever be used as a **genre/structure/tone reference** — never as a source to dramatize scene-by-scene.

**Not legal advice.** Rights to any real named work, franchise, or public figure referenced for tone remain with their owners.

**Refuse:** a scene-by-scene or chapter-by-chapter dramatization of an identifiable existing copyrighted book/film/game's actual plot and characters; reproducing another work's copyrighted dialogue/prose verbatim or near-verbatim; depicting real private individuals; full unofficial adaptations of a franchise's licensed property.

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end screenplay from a premise | **screenplay-plan** |
| Check premise against existing IP first | **ip-hygiene-check** |
| Found-footage / investigation horror structure | **foundfootage-structure** |
| Traditional three-act feature structure | **feature-structure** |
| Sitcom / multi-cam structure | **multicam-structure** |
| Adapt a premise from another medium | **medium-adapt** |
| Format a scene (sluglines, inserts, O.S./V.O.) | **scene-format** |
| Build cast & crew roles | **cast-crew** |
| Escalation / motif toolkit (horror-specific) | **escalation-toolkit** |
| Assemble the full draft | **draft-assembly** |
| Hand off for export/artifact/render | **export-handoff** |
| Persist | **write-knowledge** |
| Short answer | **brief** |

Default: **screenplay-plan**, which always runs **ip-hygiene-check** first, then routes to the structure procedure matching the requested genre/format.

---

## screenplay-plan

**Input:** setting, premise/inciting mystery or conflict, cast size + roles, length/scope (feature / treatment / single act), tone, format (found-footage / traditional feature / multi-cam).

If any of these is missing and can't be inferred safely, ask — don't guess a premise wholesale.

**Output:**
1. **Verdict** — original premise confirmed, or IP concern flagged (see `ip-hygiene-check`)
2. Structure choice (**foundfootage-structure** / **feature-structure** / **multicam-structure**)
3. **cast-crew**
4. Full or sample draft via **draft-assembly**
5. **write-knowledge** location
6. OPEN — length trims, tone adjustments, format conversion

---

## ip-hygiene-check

Run before drafting anything, every time.

1. Does the premise name, or closely track the plot/characters of, an existing published novel, film, game, or franchise?
2. If yes — do not dramatize it. Offer the user a choice (mirrors the pattern in `broadcast-musical-mashup-kit`'s trope-map, applied to plot instead of song structure):
   - **Fully original** — keep only the genre/mechanic, invent new title/characters/plot.
   - **Loose homage** — same broad flavor, explicitly renamed and restructured so it reads as its own work.
   - **Different premise** — drop the resemblance, build from a new brief.
3. Only proceed to a structure procedure once the premise is original or the user has picked a path.
4. A closing disclaimer belongs in **Output contract** whenever a real named work or format was used as tonal reference (see `broadcast-musical-mashup-kit`'s ip-hygiene-check for the sibling pattern on parody).

---

## foundfootage-structure

The Blair Witch model:

1. **Disclaimer / framing card** — the footage is recovered, found, or leaked, and by whom. Licenses the first-person, unpolished camera language for the rest of the script.
2. **Cold open** — a short, unsettling teaser (often the *last* piece of footage chronologically), then a title card.
3. **Act 1 — normalcy and setup.** Introduce investigator(s), stakes, and the missing/wronged party. Gather evidence through interviews and **screen inserts** (chat logs, code, documents, call recordings). Establish the rules of whatever cursed media/mystery drives the plot.
4. **Act 2 — descent.** Crew travels to the site tied to the evidence. Local color confirms the history is real, not just in-fiction. Escalate with small wrongness first (see **escalation-toolkit**). End the act by separating the group.
5. **Act 3 — crisis.** Footage turns chaotic — handheld, dropped cameras, partial darkness, audio-only stretches. Characters disappear one at a time. Do **not** over-explain the horror; the last confirmed image or line should raise the temperature, not answer it.
6. **Epilogue / text cards.** Plain, factual-sounding aftermath cards. Preserve ambiguity.

---

## feature-structure

Traditional three-act, for non-found-footage requests:

| Act | Share of runtime | Job |
|-----|-------------------|-----|
| I — Setup | ~25% | Ordinary world, inciting incident, protagonist's want, lock-in to the story question |
| II — Confrontation | ~50% | Rising complications, midpoint reversal, allies/antagonist pressure, low point |
| III — Resolution | ~25% | Climax that answers the story question, falling action, final image that mirrors/contrasts the opening |

Use when the user wants a conventional narrative feature rather than a found-footage conceit.

---

## multicam-structure

Sitcom/multi-cam beat sheet:

| Block | Content |
|-------|---------|
| Cold open | Short joke/scene, unrelated to A-plot or a teaser of it |
| Act 1 | A-plot and B-plot both launched |
| Act 2 | Complications collide; A/B-plot cross |
| Tag | Button scene, resolves loose joke, runs under credits |

Format: slugline, then `CHARACTER (V.O./O.S. as needed)` cue, dialogue, `(beat)`/`(action)` parentheticals for physical comedy timing.

---

## medium-adapt

When the user wants to carry a premise/cast invented in a companion skill into screenplay form (or vice versa):

1. Confirm the source is original (its own IP-hygiene procedure should already have cleared it — e.g. `broadcast-musical-mashup-kit`'s **ip-hygiene-check**, `highschool-play-scripter`'s content-mode).
2. Preserve cast, world, and tone; do not preserve medium-specific staging (stage directions ≠ camera direction; comic panels ≠ scene beats — translate, don't copy-paste).
3. Route to the matching structure procedure (**foundfootage-structure** / **feature-structure** / **multicam-structure**) for the new medium.
4. Read/write the shared `workspace/creative/<slug>/` folder so the source skill's cast/brief files are reusable (see root `INTEGRATION.md` for the shared folder convention across creative skills).

---

## scene-format

- Sluglines: `INT./EXT. LOCATION - TIME`.
- Tag capture medium under the slugline for found-footage: `(HANDHELD, <CHARACTER>'S CAMERA)`, `(SCREEN RECORDING / WEBCAM)`, `(FOUND ON A SECOND CAMERA, TIMESTAMPED...)`.
- Burn in timestamps when it reinforces a "recovered evidence" conceit.
- Render on-screen digital content (chat logs, decoded ciphers, source code) as a labeled **SCREEN INSERT** block, not prose description.
- `(O.S.)` for heard-not-seen; `(V.O.)` for narration/recordings layered over other footage.
- Title cards and text cards sit on their own line, in caps, no scene heading.

---

## cast-crew

- 2–4 person crew works well for found-footage (mirrors Blair Witch's trio): give each member a distinct function — host/driver of the investigation, skeptic/technical expert, someone with personal stake (family of the missing person, etc.).
- One outside local/witness who confirms buried history is real — turns "spooky story" into "actual place, actual past."
- A cursed or toxic media object (game, broadcast, book, video series) is a strong Act 1 engine — lets exposition happen through screen inserts instead of dialogue dumps.
- For feature/multi-cam: standard protagonist / antagonist / ally / mentor roles; size cast to runtime (a 90-page feature rarely supports more than 4–5 named speaking roles with real arcs).

---

## escalation-toolkit

Horror-specific, use inside Act 2/3 of **foundfootage-structure**:

- Repeating motifs (a sound, a symbol, a phrase) that first appear in the fiction/evidence, then recur for real on location.
- Technology mirroring the story being investigated (an in-fiction sound effect with no real source; a device behaving like the cursed object said it would).
- Physical evidence in a place it shouldn't be (an item locked in a car now sitting somewhere impossible).
- Never give a clean explanation for the horror in-script. Ambiguity is the payoff, not a placeholder for a cut scene.

---

## draft-assembly

Write the full screenplay in order: framing/disclaimer → cold open → title → Act 1 → Act 2 → Act 3 → epilogue/text cards. Keep scene direction terse and camera-aware (found-footage) or terse and blocking-aware (traditional). Dialogue does the character work; action lines stay lean.

---

## export-handoff

| Target | Skill / path |
|--------|--------------|
| Styled read (Artifact) | Use `artifact-design` skill guidance for a screenplay-appropriate layout (monospace/courier body, scene-heading emphasis) |
| Shot/edit pipeline once filmed | `creative-pipeline-builds` |
| PDF export | `pdf-render` |
| Publish notes/changelog | `rss-share` |

User HITL for all publish steps.

---

## write-knowledge

```text
workspace/creative/<slug>/
  brief.md
  cast.md
  outline.md
  script.md
  ip-hygiene.md
```

Shared folder convention across the creative-writing skill mesh — see root `INTEGRATION.md`.

---

## Output contract

1. Verdict — original premise confirmed / IP concern resolution chosen
2. Structure used (found-footage / feature / multi-cam) and why
3. Full draft or requested act/scene
4. IP-hygiene disclaimer line if any real work/franchise was used as tonal reference
5. OPEN — length, tone, or format follow-ups

---

## Anti-failure

- No scene-by-scene dramatization of an identifiable existing copyrighted book/film/game
- No verbatim or near-verbatim reproduction of another work's dialogue/prose
- No real private individuals depicted
- No clean, tidy explanation of found-footage horror's central mystery — ambiguity is intentional, not a gap
- No claiming official/licensed status for any adaptation-flavored piece

## Local knowledge
- `knowledge/creative/screenplay-dev-kit.md`
