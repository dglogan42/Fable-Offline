# PDF render & extract (offline)

**WHEN_TO_USE:** PDF files, in-browser PDF viewers, Mozilla **PDF.js** bundles, “render this PDF,” extract text/tables, summarise plan documents, audit PDF permissions/metadata, or design a local PDF-assisted agent step. Use with legal playbook (contracts), urban planning (district plans), education (catalogues), or privacy (document viewers on public sites).

## Stance
PDFs are **containers**, not ground truth. Rendering shows pixels/text layers; extraction can miss scanned pages (need OCR — out of scope unless user provides text). Never invent clause numbers or map labels not present in extracted text. Prefer **local** extract over uploading documents to cloud APIs.

**Not legal advice.** Binary PDFs and full PDF.js sources stay out of git; write **curated markdown extracts** under `knowledge/` or `workspace/`.

---

## Companion skills
| Skill | When |
|-------|------|
| `legal-playbook` | Contract/NDA PDFs |
| `education-claim-audit` | Prospectus / accreditation PDFs |
| `urban-planner-competencies` | Spatial plans, policy PDFs |
| `climate-modeling` | Climate plans, pathway/BAU tables |
| `privacy-host-map` | Site embeds PDF.js / viewer analytics |
| `privacy-design-planner` | Agent that handles document PII |
| `loop-engineer` | Multi-page extract → verify completeness |

---

## Identify stack (when user pastes JS/HTML)

| Signal | Meaning |
|--------|---------|
| `pdfjsVersion` / `pdfjsBuild` / `globalThis.pdfjsLib` | **Mozilla PDF.js** browser renderer |
| `getDocument`, `PDFWorker`, `TextLayer`, `AnnotationLayer` | PDF.js API surface |
| Apache-2.0 Mozilla header | Upstream open source — not site business logic |
| Empty `clientlib-*.js` next to PDF | Unrelated AEM stub |

**PDF.js role:** LOAD functional library to paint PDF in browser. Classify as **document viewer**, not ads — unless host page also fires analytics on open.

Known reference dump: PDF.js **6.0.109** build `d27b9ab5f` (Mozilla). Prefer official `pdfjs-dist` over page-saved megabyte bundles in the repo.

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| Render / open PDF for reading | **render-guide** |
| Extract text offline | **extract-text** |
| Summarise / structure content | **structure-doc** |
| Metadata & permissions | **inspect-meta** |
| Scanned / image-only PDF | **ocr-gap** |
| Site embeds viewer | **map-viewer** |
| Build agent step / scaffold | **design-pdf-agent** |
| Persist notes | **write-knowledge** |

Default: **extract-text** if a file path is given; **render-guide** if only PDF.js code is pasted; **structure-doc** if text is already pasted.

---

## render-guide

Explain how rendering works and what the operator can do **locally**:

```text
PDF bytes
  → parser (PDF.js worker | pypdf | OS viewer)
  → page tree
  → (optional) text layer + annotation layer
  → display or extract
```

**Browser (PDF.js):** host calls `pdfjsLib.getDocument({ url | data })` → worker parse → canvas render + `TextLayer`.  
**Offline Fable:** prefer CLI extract (below) or user paste; do not commit 800KB+ library dumps.

**Security notes for renderers:**
- Keep PDF.js updated (parser attack surface).  
- Host must not pass untrusted open URLs without allowlist.  
- `createValidAbsoluteUrl` in PDF.js limits link schemes (`http/https/ftp/mailto/tel`).  
- Annotations/forms stay local unless the **host app** POSTs them.

---

## extract-text

### Preferred harness (Fable)
```bash
python fable5_offline_agent.py --pdf path/to/file.pdf
python fable5_offline_agent.py --pdf path/to/file.pdf --pdf-pages 1-5
# or
python scripts/pdf_extract.py path/to/file.pdf -o workspace/pdf-extract.md
```

Requires optional dependency: `pypdf` (`pip install pypdf`).

### Manual / model path
If text is pasted or extract file exists under `workspace/`:
1. State **source** (filename, page range, extract tool).  
2. Do not claim OCR if only text layer was used.  
3. Note empty pages → likely scanned images.

### Output shape
1. **Verdict** — text layer OK / partial / image-only  
2. Page count (if known)  
3. Extract path or inline excerpt (cap long docs; prefer file)  
4. Gaps (missing pages, encoding, redaction holes)  

---

## structure-doc

Turn extract into usable structure:

1. Document type guess (report, contract, plan, slides-as-pdf) — label confidence  
2. Outline (headings / numbered sections if present)  
3. Key claims / numbers with page refs when available  
4. Tables as markdown if recoverable  
5. Action items / open questions  
6. Hand off to domain skill (legal / education / urban / privacy) when intent matches  

Use **rederive-numbers** on any quantitative claims.

---

## inspect-meta

From extract tool or user-provided properties, report if known:

| Field | Why |
|-------|-----|
| Title / Author / Creator / Producer | Provenance |
| Creation / mod dates | Freshness |
| Encrypted / password | Access constraint |
| Page count | Scope |
| Permissions (print/copy/modify) | PDF flag hygiene — not DRM law advice |

PDF.js `PermissionFlag` mirrors PDF permission bits (print, copy, modify, forms, etc.).

---

## ocr-gap

If extract is empty or garbage:
1. State **image-only / needs OCR**  
2. Options: user runs local OCR (Tesseract etc.), provides text, or provides page screenshots  
3. Do **not** invent page content  

---

## map-viewer

When HTML/JS shows an embedded viewer:
1. Identify library (PDF.js version if present)  
2. Tag **LOAD** for the library host (first-party vs CDN)  
3. Tag analytics on parent page separately (`privacy-host-map`)  
4. Note whether PDF URL is same-origin, signed, or public  

---

## design-pdf-agent

Agent that assists with PDFs:

| Component | Rule |
|-----------|------|
| Goal | Extract → structure → domain skill; HITL before external share |
| Tools | Local `pdf_extract` / read workspace extracts only |
| Forbidden | Upload user PDFs to third-party APIs without explicit consent |
| Memory | Store summaries, not full confidential PDFs, in `knowledge/` |
| Verify | Page coverage; quote checks; no invented clauses |
| Privacy | Contracts/HR/medical PDFs → minimise retention; gitignore binaries |

Fable stack:
```text
--pdf extract → structure-doc → legal-playbook | urban | education
             → engineer verify quotes
             → write knowledge/*.md (curated)
```

---

## write-knowledge

- Path: `knowledge/pdf/<slug>-notes.md` or domain folder (`legal/`, `urban-planning/`)  
- Include: source filename, page range, date, tool (`pypdf` / paste / PDF.js)  
- **Never** commit raw `.pdf` or full `pdf.mjs` bundles (see `.gitignore`)  

---

## Forbidden
- Fabricating PDF text not in extract  
- Treating PDF.js source review as a site’s business-logic audit  
- Committing multi‑MB viewer bundles or confidential PDFs  
- Claiming a scanned PDF was “fully read” without OCR/text  

---

## Local knowledge
- `knowledge/pdf/pdfjs-and-offline-render.md` — PDF.js identity + offline workflow  
- Extracts: `workspace/pdf-*/` (gitignored workspace)  

## Agentic criteria (engineer loops)
1. Source and page range stated  
2. Extract method named  
3. Empty/scan gaps explicit  
4. Quotes attributable  
5. No invented content  
6. Next domain skill named if applicable  

## Note
This skill covers **render/extract hygiene and agent workflow**. It does not replace a desktop PDF reader for visual layout QA.
