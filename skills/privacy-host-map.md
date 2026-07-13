# Privacy & third-party host map (agentic)

**WHEN_TO_USE:** Reviewing a website, HTML dump, app shell, or “what tracks me?” question — especially government/council pages, search UIs, tag managers, DV safety widgets (Shielded Site), analytics, or any page with many `script`/`iframe` tags. Use after pasting source HTML or when `knowledge/privacy/` has a prior map.

**Upstream planner:** For multi-step review programmes, agent architecture, or phased roadmaps, use **`privacy-design-planner`** first (or after the first host map).

## Stance
A host in a minified JS string is **not** proof of a live network call. Classify every third party by **how it appears** (LOAD / CONFIG / CLICK / BUNDLE). Treat impressive privacy policies as **claims** until the page’s actual processors match. Apply Section 4 (re-derive): do not invent cookies, retention periods, or consent behaviour without evidence.

**Not legal advice.** Not a penetration test. Not a guarantee of compliance (Privacy Act, GDPR, etc.).

---

## Procedures (map user intent)

| Intent | Procedure |
|--------|-----------|
| Full third-party map from HTML/JS | **map-hosts** |
| Focus on analytics/tags only | **map-tags** |
| Sensitive widget (e.g. Shielded / crisis) next to trackers | **map-tension** |
| Public API keys in page source | **key-hygiene** |
| Update or write a durable knowledge note | **write-knowledge** |

Default if unclear: **map-hosts**.

---

## Legend (required on every map)

| Tag | Meaning |
|-----|---------|
| **LOAD** | Browser can load resource on this page (script, iframe, img, link stylesheet) |
| **CONFIG** | Endpoint in page config / data attributes (search API, org id, access key) |
| **CLICK** | Outbound link or secondary product path (user-initiated) |
| **BUNDLE** | Host string inside minified vendor JS (docs/examples) — **not proof of a live call** |

Also mark:

| Scope | Meaning |
|-------|---------|
| **First-party** | Same registrable domain / org family / same-origin relative paths |
| **Same-site path, third-party code** | e.g. `/.rum/@adobe/...` served from first-party host but vendor software |

---

## What to extract from HTML / head / footer

1. **Document identity** — canonical URL, title, meta description, template name  
2. **Script tags** — `src`, async/defer, inline bootstraps (GTM, dataLayer, Adobe Launch)  
3. **Stylesheets & fonts** — third-party CDNs  
4. **Iframes** — `src`, sandbox attributes, dimensions  
5. **Forms / search config** — `data-config`, `action`, hidden API keys, org IDs, pipelines  
6. **Pixels / noscript** — GTM noscript iframes, LinkedIn/Meta pixels if present  
7. **Footer processors** — privacy policy links, gov logos, safety widgets  
8. **Clientlib / bundle names** — AEM `etc.clientlibs`, empty hashes (`d41d8cd9…` = MD5 empty)  
9. **postMessage / storage hints** — only if JS is available; note origin checks  

### Optional deeper pass (when JS available)
- Fetch non-empty first-party bundles; scan for hosts  
- Separate **runtime likely** vs **docs string only**  
- Note `localStorage` / `sessionStorage` / `document.cookie` usage patterns (signals, not a live cookie table)

---

## Common processor families (cheat-sheet)

| Family | Typical hosts | Role |
|--------|---------------|------|
| Google tags | `www.googletagmanager.com`, `www.google-analytics.com`, `www.google.com` | Tag manager / analytics |
| Adobe | `assets.adobedtm.com`, Experience Cloud, Helix RUM paths | Launch tags / RUM |
| Search SaaS | `*.cloud.coveo.com`, Algolia, Elasticsearch Cloud | Query + search analytics |
| Feedback | `*.qualtrics.com`, SurveyMonkey, Typeform | Surveys |
| Safety widgets | `shielded.co.nz`, `staticcdn.co.nz` | Shielded Site-style DV help |
| Library vendors | EBSCO, OCLC, III, OverDrive | Research / auth ecosystems |
| Social | Facebook, X/Twitter, LinkedIn, TikTok, YouTube | Share / embeds |
| CDN / UI | Cloudflare, jsDelivr, unpkg, cloudfront | Static assets (context-dependent) |

Do **not** list BUNDLE-only hosts as “this site shares data with X” without Network evidence.

---

## Checklist (score disclosure honesty 1–10, not “site quality”)

| Gate | Question |
|------|----------|
| First-party boundary | What is clearly same-org vs third-party? |
| Tag managers | GTM / Launch / Tealium IDs named? Fire-on-load vs consent? |
| Search / SaaS keys | Public tokens in HTML? Search-only vs over-privileged risk? |
| Iframes | Who owns the frame origin? Sandbox tight enough? |
| Sensitive surfaces | Crisis/DV/health tools co-located with parent-page trackers? |
| postMessage | Origin validated for close/control messages? |
| Privacy notice | Policy link present? Processors named match page reality? |
| Bundle noise | Docs/example hosts excluded from “confirmed trackers”? |
| Missing evidence | What requires DevTools Network / cookie banner test? |

---

## Sensitive surface tension (Shielded / crisis / health)

When a **safety or health widget** sits on a heavily tagged parent page:

1. Map **parent** processors separately from **iframe** origin.  
2. State isolation clearly: parent cannot automatically read iframe DOM if sandboxed; iframe cannot automatically read parent.  
3. Residual risk: parent analytics still see **page visit** and may log **widget-open** UI events if tags listen.  
4. Recommend (as hygiene, not legal advice): avoid analytics goals on safety-logo clicks when possible; keep iframe sandbox; origin-check `postMessage`.

---

## key-hygiene (public tokens)

When access keys / API keys appear in HTML:

1. Quote only redacted form in user-facing output if preferred (`xx691cbe06-…`).  
2. Classify: **public search token** (expected) vs **secret that should not be browser-side**.  
3. Required checks for public search keys: search-only, no admin, source restrictions, rate limits.  
4. Never invent that a key is “safe” without scope evidence — say **needs console verification**.

---

## Verdict labels (required)

- **Insufficient evidence** — cannot classify hosts or roles from material given  
- **Map only** — hosts listed; live Network not confirmed  
- **Partially verified** — some LOAD hosts confirmed (e.g. live fetch of empty vs non-empty scripts)  
- **Red flags** — secrets that look like private API keys, missing sandbox on sensitive iframes, trackers on safety flows without disclosure, inventing processor claims in privacy copy that contradict the page  

---

## Output shape (map-hosts)

1. **Verdict first**  
2. **Page identity** (URL, title, stack if known)  
3. **Legend reminder** (one line)  
4. **Table A — high privacy relevance** (LOAD / CONFIG): Host | Role | Tag | Notes  
5. **Table B — click / secondary ecosystems**  
6. **Table C — social** (if any)  
7. **Table D — bundle noise** (explicitly “not confirmed loads”)  
8. **Purpose diagram** (ASCII) parent → third parties  
9. **Sensitive tension** section if safety/health widget present  
10. **Key hygiene** if tokens in source  
11. **What to verify next** (Network tab, consent banner, privacy policy, key scopes)  
12. **One concrete risk** of trusting the privacy policy alone  
13. Point to `knowledge/privacy/*` if a prior map exists  

---

## write-knowledge

When asked to persist:

- Path: `knowledge/privacy/<site-slug>-third-party-hosts.md`  
- Include: date, URL, method, legend, tables, tension, checklist  
- Do **not** commit raw HTML/JS dumps; curated markdown only  
- Cross-link this skill  

---

## Forbidden

- Claiming GDPR/Privacy Act compliance or non-compliance as legal fact  
- Listing BUNDLE hosts as confirmed data-sharing partners  
- Inventing cookie names, retention days, or “they sell your data” without evidence  
- Full reproduction of live private keys when redaction is enough  
- Treating empty AEM clientlibs as malware or as full app logic  

---

## Local knowledge

If `knowledge/privacy/` contains notes (e.g. `akl-libraries-third-party-hosts.md`), **use them** and cite filenames. Still mark live re-verification as required when hashes/IDs may have changed.

### Worked examples (Auckland public sector / CCO family)
| Page | Snapshot | Notable tags |
|------|----------|--------------|
| Libraries catalogue | `akl-libraries-third-party-hosts.md` | GTM-TDX29C, Coveo ac-lib, Shielded |
| Compliance Policy | `ac-compliance-policy-hosts.md` | GTM-MCLW6DXF, Coveo ac-web, Shielded |
| Sports field programme | `ac-sports-field-programme-hosts.md` | GTM-MCLW6DXF **+ Clarity + Hotjar + GA4 gtag + YouTube + Qualtrics** |
| AAG Forever Tomorrow | `aag-forever-tomorrow-hosts.md` | React SPA, **GTM-KCGVLXLM**, **Meta Pixel**, Securiti, reCAPTCHA, Sentry, YouTube/Vimeo, Stackla |
| MPI Exporter Help | `mpi-exporter-help-hosts.md` | Silverstripe 5.4, Swiftype meta; dump incomplete — re-scan Network |
| Health NZ Find a service | `healthnz-find-a-service-hosts.md` | Silverstripe 6.2, **GTM-NQDRN6WT**, **Hotjar 3700571**, **Mapbox pk.**, geolocation, Reoako, WR Shield CSS |

Empty AEM stub pattern: `clientlib-dependencies…d41d8cd9…` (0 bytes).

---

## Agentic loop hints (for engineer / hermes)

**Success criteria examples:**
- Every high-impact host has a Tag (LOAD/CONFIG/CLICK/BUNDLE)  
- First-party vs third-party boundary stated  
- Bundle noise separated from confirmed loads  
- Sensitive iframe isolation + residual parent-tag risk stated when relevant  
- Next verification steps are concrete (Network, policy URL, key console)  
- No invented legal conclusions  

**Stop when:** map is complete for available material, or 3 cycles with no new hosts from the dump.

---

## Note
This skill produces **processor hygiene maps**. It does not replace a DPIA, lawyer, or security audit.
