# Screenplay dev kit — structure and formatting seed

**Skill:** `screenplay-dev-kit`
**Related:** `highschool-play-scripter` (stage) · `book-creator-comics-kit` (panels) · `manga-anime-fanfic-prompt-kit` (manga script) · `broadcast-musical-mashup-kit` (trope-map)
**Not legal advice.** Named works used for tone/genre reference only; rights remain with their owners.

---

## Origin

Generalized from a single found-footage (Blair Witch–style) screenplay build: an original
investigation-horror piece using recovered-footage framing, a three-person crew, and
escalating disappearances. That build is the reference implementation for
**foundfootage-structure**; the other structures (**feature-structure**,
**multicam-structure**) generalize the same "seed" method to other screenplay modes.

---

## IP-hygiene pattern (why this exists)

A premise that names, or closely tracks, an existing copyrighted novel/film/game's plot and
characters cannot be dramatized scene-by-scene — that's a derivative work, not inspiration.
The fix used in the reference build: keep the *shape* of the idea (investigator uncovers a
toxic-fandom/leaked-files mystery) and invent a new title, cast, and plot specifics from
scratch. Always run this check before structure work, the same way
`broadcast-musical-mashup-kit` runs **ip-hygiene-check** before lyric-draft.

---

## Found-footage structure (Blair Witch model)

```text
1. Disclaimer / framing card — footage is recovered/found/leaked, by whom
2. Cold open — short unsettling teaser (often chronologically last), then title card
3. Act 1 — normalcy + setup: investigator(s), stakes, missing/wronged party;
   evidence via interviews + SCREEN INSERT (chat logs, code, documents, calls)
4. Act 2 — descent: travel to the site; local witness confirms real history;
   escalate (motif recurrence, tech mirroring fiction, misplaced evidence);
   end by separating the group
5. Act 3 — crisis: chaotic handheld footage, characters vanish one at a time,
   no clean explanation
6. Epilogue — plain factual-sounding text cards, ambiguity preserved
```

### Formatting conventions

| Convention | Example |
|---|---|
| Slugline | `INT./EXT. LOCATION - TIME` |
| Capture-medium tag | `(HANDHELD, CASS'S CAMERA)`, `(SCREEN RECORDING / WEBCAM)` |
| On-screen digital content | `SCREEN INSERT:` labeled block, not prose description |
| Heard not seen | `(O.S.)` |
| Narration/recording over footage | `(V.O.)` |
| Title/text card | Own line, caps, no scene heading |

### Escalation toolkit

- Repeating motif (sound/symbol/phrase) appears in fiction/evidence first, recurs for real on location
- Technology mirrors the story being investigated
- Physical evidence in a place it shouldn't be
- Never explain the horror cleanly — ambiguity is the payoff

### Cast pattern

2–4 person crew, each a distinct function: host/investigator, skeptic/technical expert,
someone with personal stake. One outside local/witness confirms the buried history is real.
A cursed/toxic media object (game, broadcast, book, series) drives Act 1 research scenes
via screen inserts instead of dialogue dumps.

---

## Feature structure (three-act)

| Act | Runtime | Job |
|---|---|---|
| I — Setup | ~25% | Ordinary world, inciting incident, want, lock-in |
| II — Confrontation | ~50% | Complications, midpoint reversal, low point |
| III — Resolution | ~25% | Climax, falling action, final image mirrors/contrasts opening |

## Multi-cam structure (sitcom)

Cold open → Act 1 (A-plot + B-plot launch) → Act 2 (collision) → Tag (button, under credits).

---

## Delivery pattern

Write the full script to a file (`.txt`/`.fountain`) under `workspace/creative/<slug>/`, not
just chat output. Offer an Artifact render for readability (see `artifact-design`). Offer
targeted follow-ups (extend an act, strict Fountain/PDF formatting, more inserts) rather than
treating a first draft as final.

## Expansion notes

Add sections here as new screenplay modes get built: stage-to-screen conversion specifics,
anthology/episodic formats, non-horror found-footage (mockumentary comedy), or additional
genre presets (slasher, sci-fi first-contact). Keep the IP-hygiene section genre-agnostic.
