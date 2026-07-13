#!/usr/bin/env python3
"""
Launch a Steam game by AppID (for local model soak tests).

  python scripts/steam_launch.py 24780
  python scripts/steam_launch.py steam://rungameid/24780
  python scripts/steam_launch.py 24780 --steam "D:\\Steam\\steam.exe"

Does not automate gameplay. Requires Steam installed and game owned/installed.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import time
from pathlib import Path

# Common SIM seeds for Fable perf tests (name only — ownership not checked)
KNOWN = {
    "24780": "SimCity 4 Deluxe",
    "255710": "Cities: Skylines",
    "413150": "Stardew Valley",
}


def parse_appid(raw: str) -> str:
    raw = raw.strip()
    m = re.fullmatch(r"steam://rungameid/(\d+)", raw, re.I)
    if m:
        return m.group(1)
    if re.fullmatch(r"\d+", raw):
        return raw
    raise SystemExit(f"Expected AppID or steam://rungameid/APPID, got: {raw!r}")


def find_steam(explicit: str | None) -> Path | None:
    if explicit:
        p = Path(explicit).expanduser()
        return p if p.is_file() else None
    env = os.environ.get("STEAM_EXE") or os.environ.get("FABLE5_STEAM")
    if env and Path(env).is_file():
        return Path(env)
    candidates = [
        Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Steam" / "steam.exe",
        Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Steam" / "steam.exe",
        Path(r"D:\Steam\steam.exe"),
        Path.home() / ".steam" / "steam" / "steam.sh",
        Path("/usr/bin/steam"),
    ]
    for c in candidates:
        if c.is_file():
            return c
    return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Launch Steam game by AppID (SIM soak-test helper)")
    ap.add_argument("target", help="AppID or steam://rungameid/APPID")
    ap.add_argument("--steam", help="Path to steam.exe / steam binary")
    ap.add_argument("--dry-run", action="store_true", help="Print command only")
    args = ap.parse_args(argv)

    appid = parse_appid(args.target)
    name = KNOWN.get(appid, "(unknown title — check store)")
    uri = f"steam://rungameid/{appid}"
    steam = find_steam(args.steam)

    print(f"AppID:  {appid}")
    print(f"Name:   {name}")
    print(f"URI:    {uri}")
    print(f"Steam:  {steam or '(protocol handler only)'}")

    if args.dry_run:
        if steam:
            print(f"Would run: {steam} {uri}")
        else:
            print(f"Would open: {uri}")
        return 0

    try:
        if steam and sys.platform == "win32":
            subprocess.Popen([str(steam), uri], close_fds=True)
        elif steam:
            subprocess.Popen([str(steam), uri], start_new_session=True)
        elif sys.platform == "win32":
            os.startfile(uri)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.Popen(["open", uri])
        else:
            subprocess.Popen(["xdg-open", uri])
    except Exception as e:
        print(f"Launch failed: {e}", file=sys.stderr)
        return 1

    print("Launch requested. Waiting 3s…")
    time.sleep(3)
    print("Done (check Task Manager / game window).")
    print("Skill: steam-sim-launch · knowledge/steam/sim-games-launch.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
