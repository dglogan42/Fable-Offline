---
name: bubble-tea-news-editor
description: Assemble a new weekly issue of Bubble Tea News — the double-sided A4 freesheet published from the sibling repo github.com/dglogan42/Claude-Skills — by selecting a rotation of personas from that repo's skills library, generating fresh content for each via their own SKILL.md, and filling the print template. Tracks issue history in a rotation log so consecutive weeks don't repeat the same lineup. Use when the user asks for "this week's issue," "the next Bubble Tea News," or to regenerate/refresh the newspaper. Canonical copy lives here in Fable-Offline; the persona roster and published output live in Claude-Skills — see Cross-repo below. This is a seed skill: sparse by design; expand the roster and rotation logic as new personas are added to the library.
user-invocable: true
---

# Bubble Tea News Editor (seed)

A working method for producing a genuinely new weekly issue of *Bubble Tea
News* — not reprinting last week's content, but actually generating fresh
material from a rotating selection of persona skills, laid into the existing
print template. Treat this as a starting checklist, not a rigid template.

## Cross-repo: this skill spans two repos

Fable-Offline is the agent-harness repo; it does not carry the 21 persona
skills this editor draws on, or the print template and rotation log they
fill. Those live in the sibling repo
**[github.com/dglogan42/Claude-Skills](https://github.com/dglogan42/Claude-Skills)**:

| What | Lives in |
|---|---|
| This editor skill (canonical copy) | `Fable-Offline/skills/bubble-tea-news-editor.md` |
| The 21 roster persona `SKILL.md` files (Step 1) | `Claude-Skills/<persona-slug>/SKILL.md` |
| Print template, rotation log, web showcase | `Claude-Skills/bubble-tea-news/` |
| Published site (GitHub Pages) | `Claude-Skills/docs/` → bubbletea.nz |

Before running an issue, make sure you can actually read those upstream
files — either because they're already present locally (this session's
`~/.claude/skills/<persona-slug>/` mirror, or a clone of `Claude-Skills` under
`workspace/bubble-tea-news/Claude-Skills/`), or by fetching them. Don't
fabricate a persona's voice from the description alone if its `SKILL.md` is
unreadable — skip it for that issue rather than guess.

Generation happens here in Fable-Offline (`workspace/bubble-tea-news/`,
Step 5). Publishing happens by opening a pull request against
`Claude-Skills` (Step 7) — Fable-Offline never hosts its own copy of the
live site, so there is exactly one published version at any time.

## Step 0 — Orient before writing anything

- The print template lives at `Claude-Skills/bubble-tea-news/print-edition.html`
  (two A4 sheets, front/back, `@page A4` print CSS). Read it before starting
  an issue — it defines the exact slot structure this skill fills.
- The rotation log lives at `Claude-Skills/bubble-tea-news/rotation-log.md`.
  Read it first to see which personas ran in the last two issues; the whole
  point of this skill is that the lineup changes week to week.
- The web showcase (`Claude-Skills/bubble-tea-news/index.html`) is a
  separate, longer-form artifact — updating it is optional per issue, not
  required.

## Step 1 — The roster

Content-eligible personas/formats, each defined by its own `SKILL.md` in
`Claude-Skills` (`screenplay-creation` and `promo-shoot-brief` aren't
newspaper content and are excluded from rotation):

| Persona / format | Source skill (in Claude-Skills) |
|---|---|
| Sebastian (faded hero, laundry) | `faded-hero-voice` |
| Luke Skywalker, kyber prospector | `canon-fanfic-vignette` (Persona 1) |
| Shaggy & Scooby, vacation log | `canon-fanfic-vignette` (Persona 2) |
| Garfield, food critic | `canon-fanfic-vignette` (Persona 3) |
| Alan Grant, zookeeper essayist | `canon-fanfic-vignette` (Persona 4) |
| Daffy Duck, book critic | `canon-fanfic-vignette` (Persona 5) |
| Wren (pursuit unit turned human-seeker) | `yearning-machine-voice` |
| Legal-affairs investigator | `code-theft-dossier` |
| Seeker-eyed personal shopper | `seekers-eye-shopper` |
| Ex-lifeguard sportswriter | `lifeguards-eye-sportswriter` |
| Sherman McCoy, financial columnist | `master-of-the-universe-columnist` |
| Baxter Kline, chaos newsman | `the-world-bulletin-anchor` |
| Lewis Hamilton, dealership ads | `grand-prix-showroom-ads` |
| Dana Foley, weather anchor | `epic-forecast-anchor` |
| Ken Endo, puzzlesmith | `ken-endo-puzzle-master` |
| Te Mana Whakaatu-style classifieds | `te-mana-whakaatu-classifieds` |
| Richard Nixon, political dispatch | `silent-majority-dispatch` |
| Robin Leach, luxury lifestyle | `champagne-wishes-dispatch` |
| Clem Whitlock, rural correspondent | `ridgeline-weekly-correspondent` |
| Rebecca Black, music review | `long-game-music-review` |
| Community-outbreak-bulletin format | `community-outbreak-bulletin` |
| Steve Jobs, reality distortion field | `reality-distortion-field-report` |
| The Stickybeak, gossip column | `tabloid-gossip-voice` |

## Step 2 — Fixed weekly anchors

Some slots aren't rotated — they're weekly fixtures because the format
itself is designed to refresh every issue:

- **Breaking banner** — always `community-outbreak-bulletin`, a new
  trivial "outbreak" each week (never repeat last issue's fad).
- **Puzzle of the Week** — always `ken-endo-puzzle-master`, a newly
  constructed puzzle each issue, hand-verified per that skill's own Step 0
  integrity rule before it's printed. Never reuse a previous week's puzzle.
- **Bubble Tea Trivia** and **Joke of the Week** — not persona-bound;
  invent fresh filler each week (a real bubble-tea-adjacent fact, a short
  pun). Don't repeat a fact or joke already used in a prior logged issue.
- **Ad box(es)** — placeholder ("Your Ad Here") unless the user has actual
  advertiser content to insert for that issue.

## Step 3 — Rotating slots

The template has roughly 8–10 non-anchor content slots across both pages.
Fill them by:

1. Reading the rotation log for the last 2 issues' lineups.
2. Excluding any persona used in either of those issues, if the remaining
   pool is large enough to fill the slots (it currently is — 22 personas
   against ~9 rotating slots comfortably clears 2 issues of exclusion).
3. Picking a tonal mix, not all-comedic or all-serious: aim for a spread
   across news/politics, business, lifestyle, food, arts, sports, and at
   least one of the fully-original (non-real-person) personas alongside
   any real-person satire pieces used that week.

## Step 4 — Generate fresh content, not reused examples

For each persona selected this week, actually produce **new** content
in that persona's voice — a new topic, a new invented subject, a new
incident — following that persona's own `SKILL.md` (voice, structural
device, and any Step 0 safety/accuracy rules it carries). Do not simply
copy an existing worked example from that skill's `examples/` folder into
the issue; those examples are references for voice, not reusable content.

## Step 5 — Assemble the issue (local, in Fable-Offline)

1. Working folder: `workspace/bubble-tea-news/issues/` (create it on first
   use). Copy `print-edition.html` from `Claude-Skills` into a new file
   there, `issue-N.html`.
2. Update the issue number, date, and the "Next week" teaser line in the
   colophon — name a few personas from the excluded pool to tease forward.
3. Swap in the week's fresh content for each slot, keeping the existing
   card/blurb structure (kicker, headline, byline, 2–3 sentence body).
4. Keep every persona's own Step 0 safety/accuracy/disclosure rules intact
   in the generated content — the print template's format doesn't override
   an individual persona's own constraints.

## Step 6 — Update the rotation log (draft locally, merges via Step 7)

Draft the new entry for `rotation-log.md` alongside the issue file in
`workspace/bubble-tea-news/`: issue number, date, and the full list of
personas used (anchors plus rotating slots) — this is what makes next
week's Step 3 exclusion actually work once it lands in `Claude-Skills`.

## Step 7 — Publish: cross-repo delivery

This skill's output isn't complete until it reaches `Claude-Skills`,
because that's the only place the site is actually served from:

1. Open a pull request against `dglogan42/Claude-Skills` adding
   `bubble-tea-news/issues/issue-N.html` and the updated
   `bubble-tea-news/rotation-log.md` (and `index.html` if refreshed —
   confirm with the user first, since it replaces the current showcase
   rather than archiving it).
2. Note in the PR description which personas ran this issue and which
   were excluded for next week's teaser, so the rotation log's intent is
   reviewable, not just its diff.
3. Offer to export a PDF the same way the Gong Cha pitch was exported
   (headless Chromium/Edge `--print-to-pdf`), if a print-ready file is
   wanted immediately — attach it to the PR or hand it back directly,
   whichever the user asked for.
4. `docs/` (the GitHub Pages mirror in `Claude-Skills`) is not
   auto-synced from `bubble-tea-news/` — flag to the user that it needs a
   separate copy-over after merge if the web showcase should go live.

## To expand this skill later

As new personas get added to the Claude-Skills library, add them to the
Step 1 roster table here too — this file and the copy in `Claude-Skills`
should be edited together so the roster never silently drifts out of sync
between the two repos. If the rotation pool ever gets small enough that
2-issue exclusion can't fill the slots, widen the log lookback or shrink
the exclusion window rather than repeating a persona back-to-back.
