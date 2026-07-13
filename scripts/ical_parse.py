#!/usr/bin/env python3
"""
Parse iCalendar (.ics) files offline into markdown (no Google API).

  python scripts/ical_parse.py invite.ics
  python scripts/ical_parse.py invite.ics -o workspace/ical-summary.md
  python scripts/ical_parse.py invite.ics --json

Stdlib only. Best-effort RFC 5545 (unfolding, VEVENT fields, basic RRULE note).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def unfold(text: str) -> str:
    # RFC 5545 line folding: CRLF + space/tab continuation
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return re.sub(r"\n[ \t]", "", text)


def unescape(val: str) -> str:
    return (
        val.replace("\\n", "\n")
        .replace("\\N", "\n")
        .replace("\\,", ",")
        .replace("\\;", ";")
        .replace("\\\\", "\\")
    )


def parse_prop(line: str) -> tuple[str, dict[str, str], str]:
    """Return name, params, value for a content line."""
    if ":" not in line:
        return line.strip().upper(), {}, ""
    left, value = line.split(":", 1)
    parts = left.split(";")
    name = parts[0].strip().upper()
    params: dict[str, str] = {}
    for p in parts[1:]:
        if "=" in p:
            k, v = p.split("=", 1)
            params[k.strip().upper()] = v.strip()
        else:
            params[p.strip().upper()] = ""
    return name, params, value.strip()


def parse_ics(text: str) -> dict:
    if text.startswith("\ufeff"):
        text = text[1:]
    text = unfold(text)
    cal: dict = {
        "prodid": None,
        "version": None,
        "method": None,
        "calscale": None,
        "events": [],
        "todos": [],
        "raw_components": 0,
    }
    stack: list[str] = []
    cur: dict | None = None
    cur_type: str | None = None

    for line in text.split("\n"):
        line = line.strip("\n")
        if not line:
            continue
        name, params, value = parse_prop(line)
        if name == "BEGIN":
            comp = value.upper()
            stack.append(comp)
            cal["raw_components"] += 1
            if comp == "VEVENT":
                cur = {
                    "uid": None,
                    "summary": None,
                    "dtstart": None,
                    "dtend": None,
                    "dtstamp": None,
                    "location": None,
                    "description": None,
                    "status": None,
                    "organizer": None,
                    "attendees": [],
                    "rrule": None,
                    "url": None,
                    "params": {},
                }
                cur_type = "VEVENT"
            elif comp == "VTODO":
                cur = {
                    "uid": None,
                    "summary": None,
                    "due": None,
                    "status": None,
                    "description": None,
                }
                cur_type = "VTODO"
            continue
        if name == "END":
            comp = value.upper()
            if stack and stack[-1] == comp:
                stack.pop()
            if comp == "VEVENT" and cur_type == "VEVENT" and cur is not None:
                cal["events"].append(cur)
                cur, cur_type = None, None
            elif comp == "VTODO" and cur_type == "VTODO" and cur is not None:
                cal["todos"].append(cur)
                cur, cur_type = None, None
            continue

        if not stack:
            continue
        top = stack[-1]
        if top == "VCALENDAR":
            if name == "PRODID":
                cal["prodid"] = unescape(value)
            elif name == "VERSION":
                cal["version"] = value
            elif name == "METHOD":
                cal["method"] = value
            elif name == "CALSCALE":
                cal["calscale"] = value
            continue

        if cur is None:
            continue

        if cur_type == "VEVENT":
            if name == "UID":
                cur["uid"] = value
            elif name == "SUMMARY":
                cur["summary"] = unescape(value)
            elif name == "DTSTART":
                tz = params.get("TZID")
                cur["dtstart"] = f"{value}" + (f" ({tz})" if tz else "")
                cur["params"]["dtstart"] = params
            elif name == "DTEND":
                tz = params.get("TZID")
                cur["dtend"] = f"{value}" + (f" ({tz})" if tz else "")
            elif name == "DTSTAMP":
                cur["dtstamp"] = value
            elif name == "LOCATION":
                cur["location"] = unescape(value)
            elif name == "DESCRIPTION":
                cur["description"] = unescape(value)
            elif name == "STATUS":
                cur["status"] = value
            elif name == "RRULE":
                cur["rrule"] = value
            elif name == "URL":
                cur["url"] = value
            elif name == "ORGANIZER":
                cn = params.get("CN", "")
                cur["organizer"] = f"{cn} <{value}>".strip() if cn else value
            elif name == "ATTENDEE":
                cn = params.get("CN", "")
                role = params.get("ROLE", "")
                part = params.get("PARTSTAT", "")
                label = f"{cn} <{value}>".strip() if cn else value
                extra = ",".join(x for x in (role, part) if x)
                cur["attendees"].append(f"{label}" + (f" ({extra})" if extra else ""))
        elif cur_type == "VTODO":
            if name == "UID":
                cur["uid"] = value
            elif name == "SUMMARY":
                cur["summary"] = unescape(value)
            elif name == "DUE":
                cur["due"] = value
            elif name == "STATUS":
                cur["status"] = value
            elif name == "DESCRIPTION":
                cur["description"] = unescape(value)

    return cal


_CONF_RE = re.compile(
    r"https?://[^\s<>\"]*(?:zoom\.us|app\.zoom\.us|meet\.google\.com)[^\s<>\"]*",
    re.I,
)


def _conference_links(*parts: str | None) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for p in parts:
        if not p:
            continue
        for m in _CONF_RE.findall(p):
            # Mask passcode query values in display
            display = re.sub(r"(pwd=)[^&\s]+", r"\1***", m, flags=re.I)
            if display not in seen:
                seen.add(display)
                found.append(display)
    return found


def to_markdown(cal: dict, source: str) -> str:
    lines = [
        f"# iCal summary: {Path(source).name}",
        "",
        f"- **Source:** `{source}`",
        f"- **VERSION:** {cal.get('version') or '—'}",
        f"- **PRODID:** {cal.get('prodid') or '—'}",
        f"- **METHOD:** {cal.get('method') or '—'}",
        f"- **Events:** {len(cal.get('events') or [])}",
        f"- **Todos:** {len(cal.get('todos') or [])}",
        "",
        "## Events",
        "",
    ]
    events = cal.get("events") or []
    if not events:
        lines.append("_No VEVENT components found._")
        lines.append("")
    for i, ev in enumerate(events, 1):
        lines.append(f"### {i}. {ev.get('summary') or '(no summary)'}")
        lines.append("")
        lines.append(f"| Field | Value |")
        lines.append(f"|-------|-------|")
        for key, label in (
            ("uid", "UID"),
            ("dtstart", "Start"),
            ("dtend", "End"),
            ("dtstamp", "Stamp"),
            ("location", "Location"),
            ("status", "Status"),
            ("organizer", "Organizer"),
            ("rrule", "RRULE"),
            ("url", "URL"),
        ):
            val = ev.get(key)
            if val:
                safe = str(val).replace("|", "\\|").replace("\n", " ")
                lines.append(f"| {label} | {safe} |")
        atts = ev.get("attendees") or []
        lines.append(f"| Attendees | {len(atts)} |")
        conf = _conference_links(
            ev.get("location"),
            ev.get("description"),
            ev.get("url"),
        )
        if conf:
            lines.append(f"| Conference (CLICK) | {len(conf)} link(s) |")
        lines.append("")
        if conf:
            lines.append("**Conference links** (user CLICK — passcodes masked)")
            for c in conf:
                kind = "Zoom" if "zoom" in c.lower() else "Google Meet" if "meet.google" in c.lower() else "Video"
                lines.append(f"- {kind}: `{c}`")
            lines.append("")
            lines.append(
                "_Zoom web join entry: https://app.zoom.us/wc/join — skill procedure **join-zoom**._"
            )
            lines.append("")
        if atts:
            lines.append("**Attendee list**")
            for a in atts:
                lines.append(f"- {a}")
            lines.append("")
        desc = ev.get("description")
        if desc:
            safe_desc = re.sub(r"(pwd=)[^&\s]+", r"\1***", desc, flags=re.I)
            lines.append("**Description**")
            lines.append("")
            lines.append("```")
            lines.append(safe_desc[:4000] + ("…" if len(safe_desc) > 4000 else ""))
            lines.append("```")
            lines.append("")

    todos = cal.get("todos") or []
    if todos:
        lines.append("## Todos")
        lines.append("")
        for i, td in enumerate(todos, 1):
            lines.append(
                f"{i}. **{td.get('summary') or '(no summary)'}** — "
                f"due {td.get('due') or '—'} — {td.get('status') or '—'}"
            )
        lines.append("")

    lines.append("---")
    lines.append("Parsed offline by `scripts/ical_parse.py`. Skill: `calendar-mail-meetings`.")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Parse .ics to markdown (offline)")
    ap.add_argument("path", type=Path, help="Path to .ics file")
    ap.add_argument("-o", "--out", type=Path, help="Write markdown here")
    ap.add_argument("--json", action="store_true", help="Print JSON instead of markdown")
    args = ap.parse_args(argv)

    path: Path = args.path
    if not path.is_file():
        print(f"Not a file: {path}", file=sys.stderr)
        return 1
    text = path.read_text(encoding="utf-8", errors="replace")
    cal = parse_ics(text)

    if args.json:
        print(json.dumps(cal, indent=2, ensure_ascii=False))
        return 0

    md = to_markdown(cal, str(path))
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(md, encoding="utf-8", newline="\n")
        print(f"Wrote {args.out}")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
