# PDF.js and offline PDF render / extract

**Compiled:** 2026-07-12  
**Skill:** `pdf-render`  
**Purpose:** Identify Mozilla PDF.js dumps; run offline extract via Fable; keep binaries out of git.  

---

## PDF.js (browser renderer)

| Field | Typical value |
|-------|----------------|
| Project | Mozilla PDF.js — https://github.com/mozilla/pdf.js |
| License | Apache License 2.0 |
| Example version seen | **6.0.109** (`pdfjsBuild` `d27b9ab5f`) |
| Global API | `globalThis.pdfjsLib` — `getDocument`, `PDFWorker`, layers, editors |

**Role on public websites:** In-browser PDF viewing (plans, prospectuses, reports). Classify as **functional viewer JS**, not marketing tags — still map parent-page GTM/Eloqua separately (`privacy-host-map`).

**Do not** store full webpack bundles of PDF.js in this repo; pin `pdfjs-dist` in app projects if you build a viewer.

### Security (short)
- Parser surface → keep versions current  
- Host controls PDF URL / bytes  
- URL helper allowlists common schemes  
- Workers + `postMessage` expected for parse off main thread  

---

## Offline Fable path (no browser)

```bash
python -m pip install pypdf
python fable5_offline_agent.py --pdf path/to/file.pdf
python scripts/pdf_extract.py path/to/file.pdf -o workspace/extract.md
```

| Step | Tool |
|------|------|
| Text layer extract | `pypdf` via `--pdf` or `scripts/pdf_extract.py` |
| Structure / summarise | skill `pdf-render` procedure **structure-doc** |
| Domain review | legal / education / urban skills |
| Image-only PDF | **ocr-gap** — need external OCR or paste |

---

## Git hygiene

Ignored (see root `.gitignore`):
- `*.pdf`
- Large `pdf*.mjs` / dumped viewer bundles when patterned  
- `workspace/*` extracts  

Commit only curated markdown notes under `knowledge/pdf/` or domain folders.

---

## Related Fable skills
- `pdf-render` — procedures  
- `privacy-host-map` — viewer on a website  
- `legal-playbook` — contract PDFs  
- `urban-planner-competencies` — planning document literacy  
