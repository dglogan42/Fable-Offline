#!/usr/bin/env python3
"""
Extract text from a PDF into markdown (offline).

  python scripts/pdf_extract.py file.pdf -o workspace/extract.md
  python scripts/pdf_extract.py file.pdf --pages 1-5

Requires: pip install pypdf
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def parse_pages(spec: str | None, n_pages: int) -> range:
    if not spec:
        return range(n_pages)
    spec = spec.strip()
    if re.fullmatch(r"\d+", spec):
        i = int(spec) - 1
        if i < 0 or i >= n_pages:
            raise SystemExit(f"Page {spec} out of range 1..{n_pages}")
        return range(i, i + 1)
    m = re.fullmatch(r"(\d+)-(\d+)", spec)
    if not m:
        raise SystemExit("Use --pages N or --pages A-B (1-based)")
    a, b = int(m.group(1)), int(m.group(2))
    if a < 1 or b < a or b > n_pages:
        raise SystemExit(f"Range {spec} invalid for 1..{n_pages}")
    return range(a - 1, b)


def extract(path: Path, pages_spec: str | None) -> tuple[str, int]:
    try:
        from pypdf import PdfReader
    except ImportError as e:
        raise SystemExit(
            "Missing pypdf. Install: python -m pip install pypdf"
        ) from e

    reader = PdfReader(str(path))
    n = len(reader.pages)
    meta_lines = [
        f"# PDF extract: {path.name}",
        "",
        f"- **Source:** `{path}`",
        f"- **Pages (file):** {n}",
        f"- **Tool:** pypdf / scripts/pdf_extract.py",
        "",
    ]
    if reader.is_encrypted:
        meta_lines.append("- **Encrypted:** yes (open may fail without password)")
        meta_lines.append("")

    parts: list[str] = meta_lines
    empty = 0
    for i in parse_pages(pages_spec, n):
        text = reader.pages[i].extract_text() or ""
        text = text.strip()
        parts.append(f"## Page {i + 1}")
        parts.append("")
        if text:
            parts.append(text)
        else:
            empty += 1
            parts.append("*(no text layer — possible scan/image page; OCR needed)*")
        parts.append("")

    if empty:
        parts.append("---")
        parts.append(
            f"**Note:** {empty} page(s) had no extractable text. "
            "Use skill `pdf-render` procedure **ocr-gap**."
        )
        parts.append("")

    return "\n".join(parts), n


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Extract PDF text to markdown")
    p.add_argument("pdf", type=Path, help="Path to .pdf file")
    p.add_argument("-o", "--output", type=Path, help="Write markdown here")
    p.add_argument(
        "--pages",
        help="1-based page or range, e.g. 1 or 2-10 (default: all)",
    )
    args = p.parse_args(argv)

    pdf = args.pdf.expanduser()
    if not pdf.is_file():
        print(f"Not found: {pdf}", file=sys.stderr)
        return 1

    md, n = extract(pdf, args.pages)
    if args.output:
        out = args.output.expanduser()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md, encoding="utf-8")
        print(f"Wrote {out} ({n} pages in file)")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
