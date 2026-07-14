# Creative-writing skills integration (cross-talk mesh)

Status: **integrated**. Wires the repo's original-writing skills into a mesh so a
premise, cast, or world seeded by one skill is portable to another, following the
handoff contract in `skills/capability-mesh.md`.

## Files

```
INTEGRATION.md                              # this file
skills/screenplay-dev-kit.md                # screenplay: found-footage / feature / multi-cam
skills/highschool-play-scripter.md          # stage plays
skills/book-creator-comics-kit.md           # classroom comics
skills/manga-anime-fanfic-prompt-kit.md     # fanfic / manga script / anime beats
skills/broadcast-musical-mashup-kit.md      # parody musicals (trope-map)
skills/creative-pipeline-builds.md          # export/render/publish pipeline
skills/prompt-generator.md                  # multi-agent draft/critique swarm
knowledge/creative/                         # shared knowledge seeds
workflows/screenplay-dev-kit.json
```

## Usage

```bash
python fable5_offline_agent.py --automate screenplay-dev-kit
```

```text
Using skill screenplay-dev-kit and skill highschool-play-scripter, adapt this
stage play's cast and premise into a found-footage shooting draft.

Using skill broadcast-musical-mashup-kit's cast-invent output, write a
screenplay-dev-kit feature-structure treatment for the same world.
```

## How it's wired

The harness auto-loads the most-recent `skills/*.md` files into every system
prompt via `read_skills_bundle()` (see `fable-communicators-patch/INTEGRATION.md`
for the same loading mechanism applied to communicator personas), so any two
creative skills present in that bundle can already "see" each other. This
integration formalizes the mesh on top of that:

1. **Full companion listing.** Every creative-writing skill's `Companions:` line
   now names every other skill in the mesh, not just its one or two closest
   neighbours — `screenplay-dev-kit`, `highschool-play-scripter`,
   `book-creator-comics-kit`, `manga-anime-fanfic-prompt-kit`, and
   `broadcast-musical-mashup-kit` all cross-reference each other. This nudges the
   agent to consider a medium-swap handoff even when the user didn't name one.

2. **Shared originality-seed contract.** Every skill in the mesh that touches an
   existing named work must: (a) run its own IP-hygiene procedure by name
   (`ip-hygiene-check` in `screenplay-dev-kit` and `broadcast-musical-mashup-kit`,
   `content-mode` + rights notes in `highschool-play-scripter`, `rights-hygiene`
   in `manga-anime-fanfic-prompt-kit`), (b) output original characters/plot only,
   (c) carry the disclaimer through to its Output contract. Because the contract
   is identical in shape across skills, a cast/premise/world cleared by one
   skill's check doesn't need to be re-argued when it moves to another.

3. **Shared handoff folder.** Every mesh skill reads/writes
   `workspace/creative/<slug>/` as its `write-knowledge` target. A cast invented
   in `broadcast-musical-mashup-kit`'s **cast-invent**, or a premise cleared in
   `highschool-play-scripter`'s **play-plan**, is readable by
   `screenplay-dev-kit`'s **medium-adapt** from that same folder — no copy-paste
   required, no re-derivation of names/relationships.

## Config / conventions

| Convention | Meaning |
|---|---|
| `workspace/creative/<slug>/` | Per-project folder any mesh skill reads/writes to hand work to a sibling skill |
| `Companions:` (full mesh) | Every creative-writing skill lists every other one, not just nearest neighbours |
| Originality-seed contract | Shared shape: named-IP hygiene check → original-only output → disclaimer in Output contract |

## How skills learn from each other

Within a single request, chain skills explicitly by naming both
("adapt the cast from `broadcast-musical-mashup-kit` into a
`screenplay-dev-kit` treatment") — the `workspace/creative/<slug>/` files are the
handoff surface. Across sessions, nothing new is required beyond the existing
self-improve flow: a generalizable lesson from any mesh skill can still be
promoted to `skills/commune-*.md` per `fable-communicators-patch/INTEGRATION.md`,
and because `read_skills_bundle()` loads skills generically, that lesson becomes
visible to every other skill in the mesh on its next run — this integration adds
consistent naming and a shared folder, not a new persistence mechanism.
