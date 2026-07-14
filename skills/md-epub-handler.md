# Markdown → EPUB handler (offline)

**WHEN_TO_USE:** A Markdown file or folder of notes needs to become a portable EPUB for offline reading, e-reading, or handoff to a reader app. Use this when the user wants to turn a book outline, knowledge notes, lesson pack, or article collection into a single EPUB artifact without cloud tooling.

## Stance
Markdown is the source of truth. EPUB is the delivery format. Keep content curated, structured, and readable in both plain text and in an e-reader. Prefer clear headings, short paragraphs, lists, and quoted material over dense formatting. Preserve the original meaning rather than trying to force every Markdown feature into a reader-specific layout.

**Not legal advice.** Respect copyright and redistribution constraints; prefer summaries, excerpts, or user-owned content. Do not silently publish third-party full-text works unless the user has permission or the content is clearly allowed.

---

## Companion skills
| Skill | When |
|-------|------|
| `pdf-render` | If the source begins as a PDF and needs to be restructured first |
| `prompt-generator` | When the EPUB content is part of a prompt-pack or instructional artifact |
| `loop-engineer` | When the source needs multi-step validation before packaging |
| `capability-mesh` | When the content should be split across multiple specialist chapters |

---

## Input forms
- A single `.md` file
- A folder of related Markdown notes
- One or more Markdown files plus existing EPUB resources to merge into a richer book

## Preferred workflow
1. **Normalize the source**
   - Save as UTF-8 Markdown
   - Use a clear title and H1/H2 hierarchy
   - Keep paragraphs short and chunked for readability
   - Convert long documents into multiple files if the result becomes unwieldy

2. **Choose a packaging target**
   - Single-file EPUB for a compact guide or booklet
   - Multi-file EPUB for a longer document or a chaptered knowledge pack

3. **Package offline**
   - Use the repository EPUB builder: `python red_rising_companion_guide.py ...`
   - Pass each Markdown resource as an input path
   - Set `--output` to a destination under `artifacts/` or `workspace/`

4. **Verify the artifact**
   - Open the generated EPUB in an e-reader or calibre
   - Check that chapter order, titles, and content are intact
   - If the content is long, split it into additional Markdown resources and re-run

---

## Example commands
```bash
python red_rising_companion_guide.py --output artifacts/my-notes.epub notes.md
python red_rising_companion_guide.py --output artifacts/guide.epub chapter1.md chapter2.md chapter3.md
```

If the source is already in a different format such as Python or an existing EPUB, the same pipeline can be used as a mixed-source package.

---

## Content rules
- Use a clear title as the first H1 heading
- Put one core topic per chapter or file
- Keep lists and tables readable in both Markdown and EPUB
- Prefer plain text and simple formatting over complex HTML tricks
- Do not fabricate content or invent missing sections

## Output shape
For each packaged source, the EPUB should include:
1. A title page or readable opening chapter
2. Chapter titles derived from the source files
3. The content body as readable XHTML
4. A navigation structure that can be opened in standard EPUB readers

## Local knowledge
- `red_rising_companion_guide.py` — offline EPUB builder used by this skill
- `artifacts/` — generated EPUB output folder
- `workspace/` — temporary packaging outputs if needed

## Agentic criteria
1. Source files are named and ordered clearly
2. The output path is explicit
3. The EPUB is opened or inspected after creation
4. Long or disorganized content is split into multiple chapters
5. The generated artifact is treated as derived output, not the only source of truth
