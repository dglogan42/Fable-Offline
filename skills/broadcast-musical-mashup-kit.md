# Broadcast musical mashup kit (IP-trope parody scripts)

**WHEN_TO_USE:** User wants an **IP-themed musical, parody stage show, or genre-mashup script** — e.g. "a Disney musical for SportsCenter", "a Broadway parody of [format]", recasting one franchise's storytelling *bones* onto an unrelated setting or broadcast format. Triggers: "musical for X", "[franchise]-themed [thing]", parody stage script, mashup libretto, fan-tribute number set.

Companions: `highschool-play-scripter` (school-safe stage IP hygiene, same shape), `book-creator-comics-kit` (classroom pages), `manga-anime-fanfic-prompt-kit` (scene prompts), `css-styles-media-kit` (design tokens for the artifact), `privacy-host-map`.

## Stance

You write **original scripts, lyrics, and characters** using a named franchise's **structure and tropes as inspiration only** — never its text.

**Never reproduce:** actual song lyrics (even "to the tune of X" is a trap — write a new lyric with new scansion, don't imply a specific existing melody), actual dialogue, copyrighted character names/likenesses as your cast, or real people (real anchors, athletes, hosts) — invent fictional equivalents instead. A one-line disclaimer at the end of the piece ("original parody, not affiliated with or endorsed by [franchise/network]") costs nothing and is honest.

**Refuse:** verbatim or near-verbatim reproduction of copyrighted lyrics/dialogue; using real private individuals as characters; treating a parody as if it were licensed/official; long copyrighted prose dumps even when a companion skill's metaphor invites it (see `robotics-functionality-tester`'s Foundation-pattern for the same rule applied elsewhere).

---

## Problem map

| Need | Deliverable |
|------|-------------|
| Map the source IP's *shape*, not its plot | **trope-map** |
| Invent a cast that stands on its own | **cast-invent** |
| Decide which numbers the mashup needs | **number-outline** |
| Write one song | **lyric-draft** |
| Check nothing crossed the line | **ip-hygiene-check** |
| Present it well (Playbill × subject-world aesthetic) | **program-design** |
| Add a real or fictional soundtrack link | **listen-along** |
| Persist | **write-knowledge** |
| Short answer | **brief** |

Default: **trope-map** → **cast-invent** → **number-outline** → **lyric-draft** (repeat per number) → **ip-hygiene-check** → **program-design**.

---

## trope-map

Identify the source IP's reusable *structure*, not its story. For a Disney-style fairy-tale musical this is usually:

```text
1. Opening ensemble number — establishes the world/routine
2. "I Want" song — the protagonist's solo, names the longing
3. Comic sidekick / patter number — exposition with jokes
4. Villain song — the antagonist explains their scheme, charismatically
5. Rivals-to-allies or romantic duet — tension resolves into partnership
6. Reprise/finale — full company, theme returns, resolved
```

Swap in the target format's own vocabulary (broadcast desk, courtroom, kitchen, spaceship bridge — whatever the user named) at every beat. The structure travels; the plot, characters, and lyrics do not.

---

## cast-invent

One entry per named archetype from **trope-map**, translated into the target world:

| Archetype | Target-world role | Note |
|-----------|--------------------|------|
| Wise elder / mentor | e.g. veteran anchor, head chef | Keeper of the world's ritual |
| Protagonist ("I Want") | e.g. rookie, new hire | Wants one concrete, small thing |
| Antagonist | e.g. ratings algorithm, a rival exec | Menace with a system, not a person, when possible — cheaper to make funny, harder to make mean-spirited |
| Sidekick | e.g. mascot, intern | Breaks the fourth wall, carries exposition |
| Rival-to-ally | e.g. competing team captain | Enters written as villain by the *story*, isn't one |

Never reuse the source IP's actual names. Invented names should sound native to the target world.

---

## number-outline

For each number: **scene-setting** (one sentence, where/when), **song title** (original), **performer(s)**, **function** (which trope-map beat it fills). Confirm runtime budget before drafting lyrics — 5–6 numbers is a comfortable one-sitting read; more needs act breaks.

---

## lyric-draft

Per song: 2–4 verses + a chorus that repeats with a variation on the last pass (title-drop it once, early). Keep stage directions in italics/parentheticals, spoken interjections separate from sung lines. Villain songs earn menace from **specificity of method**, not cruelty — show the mechanism (what it fabricates, how it profits), not a rant.

---

## ip-hygiene-check

Before finalizing, verify:

- [ ] No lyric can be sung to the source IP's actual melody by accident (scan against any real lines you can recall — if unsure, rewrite the meter)
- [ ] No character is a renamed version of a real copyrighted character (traits swapped 1:1) — archetypes are fine, copies aren't
- [ ] No real living person is depicted, even affectionately
- [ ] Closing disclaimer present, naming both the parodied franchise and the parodied format/network if either is real
- [ ] If linking real external media (companion podcast, real playlist) — label it as real and distinct from the fictional piece, don't blur the two (see **listen-along**)

---

## program-design

If shipping as an Artifact: treat it as an **editorial** piece (the user will want to keep/share it), not a memo. Ground the visual system in **both** worlds the mashup straddles — e.g. Playbill program conventions (marquee type, act dividers, cast list) crossed with the target format's own materials (scoreboard ticker, broadcast chyron, kitchen ticket rail). Pick a display face for the "marquee" voice and a body serif for lyric/stage-direction text; derive the palette from the actual subject (stadium lights, kitchen brass, control-room monitors), not a generic default. See the `artifact-design` skill for the full process — this skill only tells you *what* the two worlds to blend are.

---

## listen-along

If the user wants a companion soundtrack (real or fictional playlist/podcast) linked or embedded:

1. **Default to a link, not an embed.** Artifacts run under a strict CSP that blocks requests to external hosts — a Spotify/YouTube/etc. `<iframe>` will render blank there even though the HTML is valid. Ship a styled link chip (`target="_blank" rel="noopener noreferrer"`) that actually works.
2. **If the user explicitly insists on the iframe anyway**, add it — but say up front it will likely be blank in the artifact sandbox, and keep the working link chip alongside it as a fallback caption ("Player not loading? Open in Spotify instead").
3. **If they name a real show/playlist**, fetch the page first to confirm the real title before labeling it — don't invent a name for something that already has one. Label real media distinctly from the fictional in-story soundtrack (e.g. "The Real Deal" vs "Cast Recording") so the reader isn't misled into thinking a real show is part of the parody.
4. **Publish retries:** artifact publish failures with a numeric `deploy NNN` code (`slug check failed`, `perm write failed`, `version allocation unavailable`) are the publish service's own infrastructure, not your file — confirmed by retrying an unrelated trivial file and seeing a *different* infra error. Don't loop-retry; try once or twice with a short backoff, then stop and tell the user it's a platform-side outage. Your local file is unaffected and republishes for free once the service recovers.

---

## write-knowledge

```text
workspace/creative/broadcast-musical/
  trope-map.md
  cast.md
  script.md          # full numbers, in order
  hygiene-check.md
```

---

## Output contract

1. Trope-map (the structure being borrowed, named explicitly)
2. Cast (invented, mapped to archetypes)
3. Full numbers in running order
4. IP-hygiene disclaimer
5. OPEN — runtime trims, staging notes, artifact vs. plain text

---

## Anti-failure

- No lyric that's a light reskin of a real, identifiable song
- No renamed copy of a real copyrighted character
- No real person depicted, even in parody
- No claiming official/licensed status
- No live embed shipped without a working link fallback
- No hammering the publish service on repeated infra errors — back off, report, move on
