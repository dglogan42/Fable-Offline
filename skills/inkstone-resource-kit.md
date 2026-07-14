# Inkstone resource kit (WebNovel author platform)

**WHEN_TO_USE:** User works with **Inkstone** — WebNovel’s **author writing platform** — Writers Academy articles, novel dashboard, contests (WSA), contracts, or SPA/host dumps (`inkstone.webnovel.com`, `yueimg.com/inkstone`). Triggers: “Inkstone”, WebNovel author, Writers Academy, become a WebNovel writer, academy article links.

**Official entry (VERIFY LIVE):**  
| Surface | URL |
|---------|-----|
| **Inkstone home** | [inkstone.webnovel.com](https://inkstone.webnovel.com/) |
| **Writers Academy** | [inkstone.webnovel.com/academy/index](https://inkstone.webnovel.com/academy/index) |
| **Example academy article** | [article/76088391988504901](https://inkstone.webnovel.com/academy/article/76088391988504901) (content is SPA-loaded — open in browser) |
| **WebNovel reader** | [webnovel.com](https://www.webnovel.com/) |
| **Be an Author** (site footer seed) | Inkstone linked from WebNovel “Be an Author” |
| **Contests** | e.g. [WSA / Spirity Awards](https://wsa.webnovel.com/) · enter via Inkstone contest links |

**Shell / CDN evidence (prior HTML dump):** SPA assets under `https://www.yueimg.com/inkstone/` · HiBridge `noah2.yueimg.com` · Cloudflare Insights.

Companions: `manga-anime-fanfic-prompt-kit` (outline/scene prompts before draft), `privacy-host-map`, `prompt-generator` (system prompts for writing agents — optional), `book-creator-comics-kit` (different classroom tool), `rss-share` only for user-owned feeds.

## Stance
Inkstone is **WebNovel’s free author tool** for drafting, managing, and submitting online novels (platform marketing: “Become the Next Top Writer”). Fable coaches **workflow hygiene and academy reading paths** — it does **not** log into Inkstone, submit contracts, scrape chapter text, or guarantee rankings/income.

**Not legal, financial, or publishing advice.** WebNovel / Inkstone / related marks remain their owners (Yuewen ecosystem). Contract, revenue share, and contest rules **VERIFY LIVE**. Academy articles are guidance only.

**Refuse:** account theft, scraped paid chapters, AI-spam mass generation against platform rules, storing session cookies / HiBridge secrets in git.

---

## Product map

| Piece | Role |
|-------|------|
| **Inkstone SPA** | Author dashboard, novel create/edit (client-rendered) |
| **Writers Academy** | How-to articles for pacing, contracts, AI use, rejections, etc. |
| **WebNovel** | Reader marketplace + “Be an Author” entry |
| **Contests (WSA)** | Submit via Inkstone contest URLs within deadlines |
| **CDN / hybrid** | yueimg static assets; HiBridge for hybrid containers |

Knowledge: `knowledge/web/inkstone-app.md` · `knowledge/privacy/inkstone-hosts.md`

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end author kit | **ink-plan** |
| Open Inkstone / sign-in | **open-app** |
| Use Writers Academy | **academy-path** |
| Read a specific academy article | **read-article** |
| First novel / dashboard | **novel-scaffold** |
| Contests (WSA etc.) | **contest-path** |
| Contracts / rejection hygiene | **contract-hygiene** |
| Host / privacy inventory | **host-map** · **privacy-brief** |
| Hybrid bridge notes | **hibridge-notes** |
| Writing craft offline (Fable) | **craft-loop** |
| Short answer | **brief** |

Default: **ink-plan**. Academy deep-dive: **academy-path** / **read-article**.

---

## ink-plan

**Input:** goal (start writing / contest / contract issue / privacy audit), language track if known.

**Output:**
1. **Verdict** — platform identified as WebNovel Inkstone  
2. **open-app**  
3. **academy-path** or **read-article** if URL given  
4. **novel-scaffold** or **contest-path** as relevant  
5. **privacy-brief** + host notes  
6. **OPEN** — live ToS, contest deadlines, contract terms  

---

## open-app

User **CLICK** only:

1. Open [inkstone.webnovel.com](https://inkstone.webnovel.com/)  
2. **Sign in** / **Sign up** (WebNovel account family — VERIFY LIVE)  
3. Allow JS; SPA hydrates from `yueimg.com` assets (blank without JS)  
4. If shell-only CDN URL `yueimg.com/inkstone/` fails with 403, use **inkstone.webnovel.com** as primary  
5. Never paste passwords into Fable  

---

## academy-path

1. Open [Writers Academy index](https://inkstone.webnovel.com/academy/index)  
2. Browse columns/articles for novice guidance (pacing, tools, contract FAQs)  
3. Example topics seen on platform (VERIFY LIVE list):  
   - Guides for novice writers  
   - Contract application rejected / language quality  
   - Using AI in writing (platform policy may change — re-read)  
4. Use articles as **checklists**, not guarantees of contract acceptance  

---

## read-article

When user shares an academy URL (e.g.  
`https://inkstone.webnovel.com/academy/article/76088391988504901?returnUrl=%2Facademy%2Findex`):

1. Open URL in browser (content is **SPA-loaded** — static fetch often has no body text)  
2. Note **article id** from path (`76088391988504901`) and returnUrl  
3. Summarize only after user pastes text or describes content — do **not** invent article body  
4. Extract: title, takeaways, action items for the author  
5. Link related academy pieces if user provides them  

If dump is only HTML shell: report shell hosts + “body requires login/JS.”

---

## novel-scaffold

Offline planning template (author fills in Inkstone):

```markdown
# Novel project
## Working title / genre / tags
## Logline (1–2 sentences)
## Audience & length target (chapter plan)
## Update schedule
## Platform: Inkstone → WebNovel publish path (HITL)
## Academy articles read
## Contest track (if any)
## OPEN: ToS, originality, AI disclosure policy
```

In Inkstone: create novel / story entry via dashboard (UI VERIFY LIVE).

---

## contest-path

1. Open official contest hub (e.g. [wsa.webnovel.com](https://wsa.webnovel.com/))  
2. Enter via **Inkstone** contest create/submit links within the window  
3. Read eligibility, themes, language tracks, prize rules **on the contest page**  
4. Do not invent deadlines or cash prizes  
5. Keep submission confirmation offline notes without secrets  

---

## contract-hygiene

From academy themes (re-verify):

- Language quality and editing matter for applications  
- Rejection articles recommend revision + academy reading  
- Contracts are **legal instruments** — human review; Fable is not counsel  
- Never share signed contract PDFs into public git  

---

## host-map

| Host | Role | Evidence |
|------|------|----------|
| `inkstone.webnovel.com` | Author app / academy routes | Official product |
| `www.yueimg.com/inkstone/` | Static SPA assets (JS/CSS/favicon) | HTML dump |
| `noah2.yueimg.com` | HiBridge hybrid script | HTML dump |
| `static.cloudflareinsights.com` | Analytics beacon | HTML dump |
| `www.webnovel.com` | Reader / Be an Author | Public site |
| `wsa.webnovel.com` | Contest marketing | Public site |

Detail: `knowledge/privacy/inkstone-hosts.md`.

---

## hibridge-notes

- Script + inline HiBridge: hybrid web↔native routing, iframe invoker  
- Relevant if Inkstone opens inside a WebNovel app WebView  
- Do not forge bridge URLs or automate privileged native calls  

---

## privacy-brief

1. Author account + manuscript content are sensitive  
2. Analytics may load on SPA open  
3. Hybrid bridge may expose device APIs in app containers  
4. Strip CF tokens / cookies from public notes  
5. Originality and AI policies: follow WebNovel/Inkstone current rules  

---

## craft-loop

Optional offline Fable support (not a substitute for Inkstone):

1. `/loop` or `/hermes` on outline beats  
2. `prompt-generator` for specialized writing-agent prompts  
3. Maker≠checker: separate “writer” vs “editor” passes  
4. User pastes final text into Inkstone HITL  

---

## Output contract

1. **Verdict** — WebNovel author platform  
2. **Links** (Inkstone + Academy + article if given)  
3. **Next actions** (open, read, scaffold, contest)  
4. **Hosts** if audit requested  
5. **OPEN** — live ToS/contest/contract  
6. No invented article text  

---

## Anti-failure

- Do not invent academy article content from SPA shell alone  
- Do not guarantee contracts, rankings, or contest wins  
- Do not scrape chapters or mass-upload AI spam  
- Do not store `.ROBLOSECURITY`-style cookies (or WebNovel session)  
- Distinguish **Inkstone (author tool)** from Book Creator / Google Docs  
