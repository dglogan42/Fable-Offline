#!/usr/bin/env python3
"""
Flexible EPUB generator.

By default it builds the Red Rising Companion Guide, but it can also generate an
EPUB from one or more resource files such as .py and .epub inputs.
"""

import argparse
import ast
import html
import io
import os
import re
import tokenize
import zipfile
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Sequence

DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent / "artifacts"
DEFAULT_OUTPUT_NAME = "Red_Rising_Companion_Guide.epub"


def sanitize_filename(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._")
    return cleaned or "chapter"


def _chapter_title_from_path(path: Path) -> str:
    return path.stem.replace("-", " ").replace("_", " ").title()


def _extract_python_text(path: Path) -> str:
    source = path.read_text(encoding="utf-8")
    module = ast.parse(source)
    sections = []

    if ast.get_docstring(module):
        sections.append(ast.get_docstring(module))

    for node in module.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            docstring = ast.get_docstring(node)
            if docstring:
                sections.append(docstring)

    comments = []
    for token in tokenize.generate_tokens(io.StringIO(source).readline):
        if token.type == tokenize.COMMENT:
            text = token.string.lstrip("#").strip()
            if text:
                comments.append(text)

    if comments:
        sections.append("\n".join(comments))

    return "\n\n".join(section for section in sections if section).strip()


def _extract_epub_text(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        html_entries = [
            name for name in archive.namelist()
            if name.lower().endswith((".xhtml", ".html", ".htm"))
            and not name.startswith("META-INF/")
            and not name.startswith("mimetype")
        ]
        if not html_entries:
            raise ValueError(f"No HTML content found in EPUB: {path}")

        content = archive.read(html_entries[0]).decode("utf-8", errors="ignore")
        return _strip_html_tags(content)


def _strip_html_tags(text: str) -> str:
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<script.*?</script>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", "\n", text)
    text = html.unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _resource_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".py":
        return _extract_python_text(path)
    if suffix == ".epub":
        return _extract_epub_text(path)
    if suffix in {".md", ".txt", ".html", ".htm", ".xhtml"}:
        return path.read_text(encoding="utf-8")
    raise ValueError(f"Unsupported resource type: {path}")


def _build_resource_chapter(path: Path, index: int) -> tuple[str, str, str]:
    title = _chapter_title_from_path(path)
    body = _resource_text(path)
    chapter_html = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>{title}</title><link rel="stylesheet" href="styles.css"/></head>
<body>
<h1>{title}</h1>
<p>{body.replace(chr(10), '</p>\n<p>')}</p>
</body>
</html>"""
    filename = f"chapter_{index:02d}_{sanitize_filename(path.stem)}.xhtml"
    return filename, title, chapter_html


def create_epub(
    resource_paths: Optional[Sequence[str]] = None,
    output_path: Optional[str] = None,
    title: str = "Red Rising Companion Guide",
    creator: str = "Dazza's Offline Tools",
):
    if output_path is None:
        output_path = str(DEFAULT_OUTPUT_DIR / DEFAULT_OUTPUT_NAME)

    output_path_obj = Path(output_path)
    output_path_obj.parent.mkdir(parents=True, exist_ok=True)

    chapters = []
    if resource_paths:
        for index, resource in enumerate(resource_paths):
            path = Path(resource)
            if not path.exists():
                raise FileNotFoundError(f"Resource not found: {resource}")
            chapters.append(_build_resource_chapter(path, index))
    else:
        chapters = [
            ("chapter_00_title.xhtml", "Red Rising Companion Guide", create_title_page()),
            ("chapter_01_intro.xhtml", "Introduction to the Series", create_intro()),
            ("chapter_02_reading_order.xhtml", "Reading Order", create_reading_order()),
            ("chapter_03_colors.xhtml", "The Color Caste System", create_colors()),
            ("chapter_04_setting.xhtml", "The World of Red Rising", create_setting()),
            ("chapter_05_characters.xhtml", "Key Characters (Spoiler-Light)", create_characters()),
            ("chapter_06_themes.xhtml", "Major Themes", create_themes()),
            ("chapter_07_how_to_read.xhtml", "How to Read the Series", create_how_to_read()),
        ]

    with zipfile.ZipFile(output_path_obj, 'w', zipfile.ZIP_DEFLATED) as epub:
        epub.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        epub.writestr(
            "META-INF/container.xml",
            """<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>""",
        )

        manifest_items = []
        spine_items = []
        for index, (filename, chapter_title, content) in enumerate(chapters):
            epub.writestr(f"OEBPS/{filename}", content)
            item_id = sanitize_filename(chapter_title).lower() or f"chapter_{index}"
            manifest_items.append(
                f'    <item id="{item_id}" href="{filename}" media-type="application/xhtml+xml"/>'
            )
            spine_items.append(f'    <itemref idref="{item_id}"/>')

        opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>{title}</dc:title>
    <dc:creator>{creator}</dc:creator>
    <dc:language>en</dc:language>
    <dc:identifier id="BookId">{sanitize_filename(title).lower()}-{datetime.now().strftime('%Y%m%d')}</dc:identifier>
    <meta property="dcterms:modified">{datetime.now().isoformat()}</meta>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
{"\n".join(manifest_items)}
  </manifest>
  <spine>
{"\n".join(spine_items)}
  </spine>
</package>"""
        epub.writestr("OEBPS/content.opf", opf)

        nav = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>Navigation</title></head>
<body>
<nav epub:type="toc">
  <ol>"""
        for filename, chapter_title, _ in chapters:
            nav += f'<li><a href="{filename}">{chapter_title}</a></li>'
        nav += """  </ol>
</nav>
</body>
</html>"""
        epub.writestr("OEBPS/nav.xhtml", nav)

        css = """body { font-family: Georgia, serif; line-height: 1.6; margin: 2em; }
h1, h2 { color: #8B0000; }
.gold { color: #DAA520; font-weight: bold; }
.red { color: #B22222; }
"""
        epub.writestr("OEBPS/styles.css", css)

    print(f"✅ Created: {output_path_obj}")
    print("You can open this in any EPUB reader (Apple Books, Kindle, Calibre, etc.)")
    return str(output_path_obj)


def create_title_page():
    return """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>Red Rising Companion Guide</title><link rel="stylesheet" href="styles.css"/></head>
<body>
<h1>Red Rising Companion Guide</h1>
<p><strong>A Dystopian Martian Science Fiction &amp; Fantasy Companion</strong></p>
<p>Based on the Red Rising Saga by Pierce Brown</p>
<p>Generated for offline use • {}</p>
<p><em>"I would have lived in peace. But my enemies brought me war."</em> — Darrow of Lykos</p>
</body>
</html>""".format(datetime.now().strftime("%Y-%m-%d"))


def create_intro():
    return """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>Introduction</title><link rel="stylesheet" href="styles.css"/></head>
<body>
<h1>Introduction to Red Rising</h1>
<p>Red Rising is a bestselling dystopian science fiction series by Pierce Brown, set in a brutal, color-coded caste society on Mars and across the Solar System.</p>
<p>It blends elements of <strong>Roman history</strong>, <strong>space opera</strong>, <strong>revenge tragedy</strong>, and <strong>epic fantasy</strong> with incredibly high stakes and visceral action.</p>
<p>The story follows <strong>Darrow</strong>, a Red miner who infiltrates the ruling Gold class to bring down the Society from within.</p>
<p>The series is known for its:</p>
<ul>
<li>Breakneck pacing and brutal violence</li>
<li>Complex political intrigue</li>
<li>Deep character development across multiple books</li>
<li>Themes of rebellion, identity, friendship, and the cost of revolution</li>
</ul>
<p>This companion is designed to enhance your reading without major spoilers.</p>
</body>
</html>"""


def create_reading_order():
    return """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>Reading Order</title><link rel="stylesheet" href="styles.css"/></head>
<body>
<h1>Recommended Reading Order</h1>
<ol>
<li><strong>Red Rising</strong> (2014) — The origin story. Start here.</li>
<li><strong>Golden Son</strong> (2015) — The rise continues. One of the best sequels ever written.</li>
<li><strong>Morning Star</strong> (2016) — Epic conclusion to the first trilogy.</li>
<li><strong>Iron Gold</strong> (2018) — New POVs. Starts the second trilogy.</li>
<li><strong>Dark Age</strong> (2019) — Brutal and intense. War on multiple fronts.</li>
<li><strong>Light Bringer</strong> (2023) — Excellent payoff and character work.</li>
<li><strong>Red God</strong> (TBA) — The final book.</li>
</ol>
<p><strong>Note:</strong> The first three books form a complete arc. Books 4-6 continue the story years later with new perspectives.</p>
</body>
</html>"""


def create_colors():
    return """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>The Color System</title><link rel="stylesheet" href="styles.css"/></head>
<body>
<h1>The Color Caste System</h1>
<p>The Society is rigidly divided into 14 Colors, each with specific roles and genetic modifications.</p>

<h2 class="gold">Gold — The Rulers</h2>
<p>The ruling class. Genetically enhanced for strength, intelligence, and beauty. They control the Society through the Peerless Scarred and the Senate.</p>

<h2>Other Notable Colors</h2>
<ul>
<li><strong>Obsidian</strong> — Elite shock troops and bodyguards</li>
<li><strong>Gray</strong> — Soldiers and police</li>
<li><strong>Blue</strong> — Pilots and navigators</li>
<li><strong>Yellow</strong> — Scientists and doctors</li>
<li><strong>Green</strong> — Hackers and programmers</li>
<li><strong>Violet</strong> — Artists and entertainers</li>
<li><strong>Orange</strong> — Engineers and mechanics</li>
<li><strong>Red</strong> — Lowest class. Miners, farmers, laborers. The "helots" of the Society.</li>
</ul>
<p>The system is brutal and designed to keep the lower Colors oppressed while the Golds live in luxury.</p>
</body>
</html>"""


def create_setting():
    return """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>The World</title><link rel="stylesheet" href="styles.css"/></head>
<body>
<h1>The World of Red Rising</h1>
<p>The story primarily takes place on <strong>Mars</strong>, which has been terraformed and colonized.</p>
<p>Key locations include:</p>
<ul>
<li><strong>The Institute</strong> — Where young Golds are trained and sorted into houses (similar to a deadly Hogwarts)</li>
<li><strong>Lykos</strong> — Darrow's mining colony on Mars</li>
<li><strong>The Rim</strong> — Outer asteroid belt and moons, more independent</li>
<li><strong>Luna</strong> — The moon, political heart of the Society</li>
<li><strong>Earth</strong> — Still exists but diminished</li>
</ul>
<p>The technology includes gravBoots, razors (whip-swords), pulseArmor, and starships.</p>
</body>
</html>"""


def create_characters():
    return """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>Key Characters</title><link rel="stylesheet" href="styles.css"/></head>
<body>
<h1>Key Characters (Spoiler-Light)</h1>
<p><strong>Warning:</strong> Some character details may contain minor spoilers for early books.</p>

<h2>Main Protagonist</h2>
<p><strong>Darrow of Lykos</strong> — A Red miner who undergoes a transformation to infiltrate Gold society. The heart of the series. Driven by loss and a desire for justice.</p>

<h2>Important Allies &amp; Figures</h2>
<ul>
<li><strong>Sevro au Barca</strong> — Darrow's closest friend. Wild, loyal, and deadly. Howler leader.</li>
<li><strong>Virginia au Augustus (Mustang)</strong> — Brilliant Gold. Complex relationship with Darrow.</li>
<li><strong>Cassius au Bellona</strong> — Golden rival and friend. Complex arc across the series.</li>
<li><strong>Roque au Fabii</strong> — Poet and friend. Represents a different path.</li>
<li><strong>Tactus au Rath</strong> — Charismatic but troubled.</li>
</ul>
<p>The series has an enormous cast that grows across the books.</p>
</body>
</html>"""


def create_themes():
    return """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>Major Themes</title><link rel="stylesheet" href="styles.css"/></head>
<body>
<h1>Major Themes in Red Rising</h1>
<ul>
<li><strong>Revolution and its cost</strong> — What are you willing to sacrifice?</li>
<li><strong>Identity and transformation</strong> — Who are we when we change ourselves completely?</li>
<li><strong>Friendship and loyalty</strong> — Especially in the face of betrayal and war</li>
<li><strong>Class warfare and oppression</strong> — The brutality of caste systems</li>
<li><strong>Leadership and power</strong> — How power corrupts and how to wield it responsibly</li>
<li><strong>Love and loss</strong> — The personal price of fighting for a cause</li>
<li><strong>Hope vs. despair</strong> — Finding light in the darkest times</li>
</ul>
</body>
</html>"""


def create_how_to_read():
    return """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>How to Read</title><link rel="stylesheet" href="styles.css"/></head>
<body>
<h1>How to Read the Red Rising Series</h1>
<p><strong>Best experience tips:</strong></p>
<ol>
<li>Read the first three books back-to-back if possible. The momentum is incredible.</li>
<li>Take breaks between the original trilogy and Iron Gold if you need time to process.</li>
<li>The later books have multiple POVs — pay attention to chapter headers.</li>
<li>Don't be afraid to look up the Color system or characters if you get lost (this guide helps).</li>
<li>The series gets darker and more complex. It's worth it.</li>
</ol>
<p><em>"Break the chains."</em></p>
</body>
</html>"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create an EPUB from embedded content or resource files")
    parser.add_argument("resources", nargs="*", help="Paths to .py or .epub resources")
    parser.add_argument("--output", "-o", dest="output_path", help="Path for the resulting EPUB")
    parser.add_argument("--title", default="Red Rising Companion Guide", help="EPUB title")
    parser.add_argument("--creator", default="Dazza's Offline Tools", help="EPUB creator")
    args = parser.parse_args()

    create_epub(
        resource_paths=args.resources or None,
        output_path=args.output_path,
        title=args.title,
        creator=args.creator,
    )