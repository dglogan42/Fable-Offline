#!/usr/bin/env python3
"""
High school literature-club play scaffolder (original scripts).

Inspired by public literature-club / school-drama tropes and DDLC Plus
marketing themes (poems, club room) — does NOT contain game dialogue.

Usage:
  python scripts/highschool_play_script.py one-act --mode G
  python scripts/highschool_play_script.py two-act --mode T
  python scripts/highschool_play_script.py scene --mode T
  python scripts/highschool_play_script.py poems
  python scripts/highschool_play_script.py cw --mode T
"""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

ARCHETYPES = [
    ("HARU", "sunny recruiter / childhood-friend energy"),
    ("REN", "spiky junior who loves cute things"),
    ("Aoi", "quiet bookworm"),
    ("Mika", "club president, always composed"),
    ("NEWKID", "new member / audience surrogate"),
]

POEMS = [
    """Title: Chalk Dust
The board remembers every name we erased.
Still, white ghosts cling under our nails.
We write again — softer this time.""",
    """Title: Lunchbox Secret
I packed an extra sweet for someone.
They never came. The sugar melted.
I ate both and called it weather.""",
    """Title: Library Lights
Between shelves the air is thicker.
I hold my breath so the story won't notice
I'm eavesdropping on its ending.""",
    """Title: Clubroom Key
We argue who locks the door.
Nobody asks who unlocked us first.
The key is warm from someone's pocket.""",
]


def one_act(mode: str, rng: random.Random) -> str:
    cast = "\n".join(f"- {n}: {d}" for n, d in ARCHETYPES)
    twist = {
        "G": "The missing poem was a prank apology — club rewrites it together.",
        "T": "Poems were rewritten overnight; the president knew and stayed silent.",
        "M": "The clubroom itself seems to edit what they write (meta dread — adult/approved only).",
    }[mode]
    return f"""# One-act literature club play (ORIGINAL)

TITLE: The Poem That Wouldn't Stay Written
RUNTIME: 30–40 minutes
MODE: {mode}  (G=school-safe · T=mild mystery · M=restricted)
IP NOTE: Original work. Not an official Doki Doki Literature Club product.
CONTENT: See content-warnings section if MODE is T or M.

## Cast (rename freely)
{cast}

## Setting
After-school literature club room; brief hallway; optional small stage for poetry night.

## Beats
1. Cold open: NEWKID reads a short poem (nervous).
2. HARU recruits; MIKA welcomes; REN and AOI spar gently over genres.
3. Club rule: write one poem by next meeting.
4. Conflict: someone's poem is altered / stolen / mocked (mode-safe).
5. Choice: expose, forgive, or rewrite together.
6. Climax: poetry-night performance (or emergency club meeting).
7. Resolution: {twist}

## Production notes
- Poems: generate with `poems` mode or student writers.
- Lights: warm clubroom → cooler hallway → warm for curtain.
- No commercial game dialogue.
"""


def two_act(mode: str, rng: random.Random) -> str:
    return f"""# Two-act literature club play (ORIGINAL)

TITLE: Minutes of the Literature Club
MODE: {mode}

## Act I — Join
Scenes: recruitment · first poems · small jealousy · missing pages discovered.
Curtain on: Who changed the notebook?

## Act II — Perform
Scenes: accusations · president's private monologue · poetry night · truth · found family or bittersweet close.
Curtain sting ({mode}): {"group bow with shared poem" if mode == "G" else "lights flicker on empty club desk" if mode == "T" else "meta address to house (approved venues only)"}

IP NOTE: Original. Not official DDLC.
"""


def scene(mode: str, rng: random.Random) -> str:
    a, b = rng.sample([x[0] for x in ARCHETYPES], 2)
    return f"""# Scene draft (ORIGINAL) — MODE {mode}

SCENE 3 — THE ALTERED PAGE
SETTING: Literature club room. Late afternoon light.
AT RISE: {a} at the desk. {b} in the doorway with a notebook.

{a}
  (without looking up)
  You left this open.

{b}
  I left it closed.

{a}
  Then someone else is writing our endings.

{b}
  (stepping in)
  Read it. Out loud. If you dare.

{a}
  (reads a line, stops)
  That's not my handwriting.
  That's not even… kind.

  (beat)

  We can erase it.
  Or we can find who thinks they own our words.

LIGHTS: warm to slightly cooler on the notebook.
SFX: distant hallway bell, one beat late.
CONTENT NOTE: verbal conflict only; no graphic content.
IP NOTE: Original dialogue.
"""


def poems() -> str:
    return "# Original poems for performance\n\n" + "\n\n---\n\n".join(POEMS)


def cw(mode: str) -> str:
    base = """# Content warnings & program note

This production is an **original** high-school play about a literature club, friendship, and creative pressure.
It is **not** an official *Doki Doki Literature Club* product.

## Warnings for this MODE
"""
    extra = {
        "G": "- Mild interpersonal conflict\n- No horror or self-harm themes",
        "T": "- Psychological unease / mystery\n- Mentions of anxiety or secrecy (non-graphic)\n- Sudden blackouts / loud SFX possible",
        "M": "- Psychological horror themes\n- Possible self-harm discussion ONLY if school policy allows — review with counsellor\n- Strong distress possible; not for young audiences",
    }[mode]
    help_line = """
## Resources (adapt to your region)
- School counsellor / pastoral care
- NZ: Healthline · emergency **111** if someone is in immediate danger

## Director checklist
- [ ] Mode approved by school
- [ ] Program CW printed
- [ ] No game script used
- [ ] Cast debrief after intense scenes
"""
    return base + extra + help_line


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="High school literature-club play scaffolder")
    p.add_argument("mode", choices=["one-act", "two-act", "scene", "poems", "cw"])
    p.add_argument(
        "--content-mode",
        choices=["G", "T", "M"],
        default="G",
        help="Content dial (default G for high school)",
    )
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("-o", "--out", type=Path, default=None)
    args = p.parse_args(argv)
    rng = random.Random(args.seed)
    cm = args.content_mode

    if args.mode == "one-act":
        text = one_act(cm, rng)
    elif args.mode == "two-act":
        text = two_act(cm, rng)
    elif args.mode == "scene":
        text = scene(cm, rng)
    elif args.mode == "poems":
        text = poems()
    else:
        text = cw(cm)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"Wrote {args.out}", file=sys.stderr)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
