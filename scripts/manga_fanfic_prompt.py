#!/usr/bin/env python3
"""
Offline manga/anime fanfiction prompt scaffolder (no LLM required).

Usage:
  python scripts/manga_fanfic_prompt.py oneshot
  python scripts/manga_fanfic_prompt.py manga --pages 8
  python scripts/manga_fanfic_prompt.py episode
  python scripts/manga_fanfic_prompt.py onset
  python scripts/manga_fanfic_prompt.py batch --n 5

Emits original scaffolds. Does not contain copyrighted novel text.
See skills/manga-anime-fanfic-prompt-kit.md
"""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COLD_OPENS = [
    "a half-eaten bento on the stairs, still warm",
    "the PA system crackles a name that never finishes",
    "shoes lined up neatly outside a classroom that is not empty",
    "a teacher’s glasses on the asphalt, one lens cracked",
    "phone screens all lighting up with the same emergency banner",
]

SETTINGS = [
    "coastal high school at morning assembly",
    "overground train stalled between stations",
    "24-hour convenience store at shift change",
    "hospital ambulance bay at dawn",
    "ferry terminal ticket hall",
]

RELATIONS = [
    "childhood friends with unfinished arguments",
    "rivals forced into the same escape route",
    "strangers who only share a class number",
    "siblings split by different exits",
]

TONES = ["desperate", "gallows humour", "gritty survival", "quiet dread", "action-thriller"]
TWISTS = [
    "the safe room was never locked from the outside",
    "the first radio report is worse than the school",
    "someone in the group is already bitten and hiding it",
    "the map leads back toward the gates",
    "help arrives — and is not help",
]


def oneshot(rng: random.Random) -> str:
    return f"""# Fanfic oneshot prompt (original scaffold)

Write a 1500–2500 word **survival / school-outbreak** oneshot in **third-person limited**.
Setting: {rng.choice(SETTINGS)}.
Timebox: **first three hours** of the crisis.
Leads: two OCs or AU versions — relationship: {rng.choice(RELATIONS)}.
Cold open image: {rng.choice(COLD_OPENS)}.
Required beats:
1) Public failure of an authority figure
2) Small-room siege (lounge / office / store room)
3) One irreversible choice (leave someone / use noise / seal a door)
Tone: {rng.choice(TONES)}. Rating: T or M (state which).
End on: {rng.choice(TWISTS)}.
Avoid: copying any commercial novel/manga dialogue or chapter order; no sexual content involving minors.

---
Rights: original scene. “First-hours outbreak” energy is a genre pressure, not a reprint of any official light novel.
"""


def manga(pages: int, rng: random.Random) -> str:
    pages = max(4, min(pages, 24))
    lines = [
        f"# Manga panel script scaffold ({pages} pages)",
        f"TITLE: (working title)",
        f"TONE: {rng.choice(TONES)} | RATING: T/M",
        f"COLD OPEN: {rng.choice(COLD_OPENS)}",
        f"SETTING: {rng.choice(SETTINGS)}",
        f"RELATIONSHIP PRESSURE: {rng.choice(RELATIONS)}",
        "",
    ]
    for p in range(1, pages + 1):
        lines.append(f"## PAGE {p}")
        n = 4 if p < pages else 5
        for i in range(1, n + 1):
            lines.append(
                f"  Panel {i} — SHOT: | ACTION: | DIALOGUE/SFX: | NOTE:"
            )
        lines.append("")
    lines.append(f"CLIMAX BEAT (use ~page {max(2, pages - 1)}): {rng.choice(TWISTS)}")
    lines.append("ART NOTES: mood words only — do not trace official art.")
    return "\n".join(lines)


def episode(rng: random.Random) -> str:
    return f"""# Anime episode beat sheet (~22 min)

TEASER: {rng.choice(COLD_OPENS)}
EPISODE QUESTION: Who do we save when the gates fail?
A-PLOT: Escape from school interior to perimeter.
B-PLOT: {rng.choice(RELATIONS)} — one secret.
MIDPOINT: {rng.choice(TWISTS)}
CLIMAX SETPIECE: faculty lounge / stairwell / front gates (pick one; original blocking).
TAG: Wider city — radio or skyline worse than campus.
TONE: {rng.choice(TONES)}
OUTPUT: scene list with estimated minutes; no commercial script lifts.
"""


def onset(rng: random.Random) -> str:
    slots = rng.sample(
        [
            "Wrong morning detail before anyone believes",
            "Authority figure fails a public ‘human’ check",
            "Primary exit becomes kill zone",
            "Small-room siege under thin doors",
            "Childhood-friend priority vs group survival",
            "First irreversible violent choice",
            "Sound discipline — noise equals death",
            "Outside scale revealed (phone/radio/skyline)",
        ],
        k=4,
    )
    return (
        "# First-hours outbreak module (original)\n\n"
        "Use these pressure slots in any school/city survival story:\n"
        + "\n".join(f"- {s}" for s in slots)
        + f"\n\nSetting seed: {rng.choice(SETTINGS)}\n"
        "Do not reproduce Highschool of the Dead: The Last Day novel text; "
        "use public ‘first hours of pandemic / school escape’ genre pressure only.\n"
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Manga/anime fanfic prompt scaffolder")
    p.add_argument(
        "mode",
        choices=["oneshot", "manga", "episode", "onset", "batch"],
        help="Scaffold type",
    )
    p.add_argument("--pages", type=int, default=8, help="Manga pages (manga mode)")
    p.add_argument("--n", type=int, default=5, help="Batch count (batch mode)")
    p.add_argument("--seed", type=int, default=None, help="RNG seed for reproducibility")
    p.add_argument(
        "-o",
        "--out",
        type=Path,
        default=None,
        help="Write to file (else stdout)",
    )
    args = p.parse_args(argv)
    rng = random.Random(args.seed)

    if args.mode == "oneshot":
        text = oneshot(rng)
    elif args.mode == "manga":
        text = manga(args.pages, rng)
    elif args.mode == "episode":
        text = episode(rng)
    elif args.mode == "onset":
        text = onset(rng)
    else:
        parts = []
        for i in range(max(1, args.n)):
            parts.append(f"## Variant {i + 1}\n\n{oneshot(rng)}")
        text = "# Fanfic prompt batch\n\n" + "\n---\n".join(parts)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"Wrote {args.out}", file=sys.stderr)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
