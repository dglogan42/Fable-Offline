# Privacy host map — Victoria University of Wellington (seed)

**Skill:** `privacy-host-map`  
**Property:** [www.wgtn.ac.nz](https://www.wgtn.ac.nz/) (Te Herenga Waka — Victoria University of Wellington)  
**Evidence type:** Browser Network capture (Firefox), single cross-site request  
**Captured:** 2026-07-13 ~04:18 UTC (from response `date` header)  
**Not legal advice. Not a full site inventory.** Re-verify with live Network tab + VUW privacy/cookie notices.

---

## Verdict

**Confirmed cross-site LOAD (tracker class):** page origin `https://www.wgtn.ac.nz` initiates a request to **TikTok Analytics** (`analytics.tiktok.com`). Firefox Enhanced Tracking Protection classifies the URL as a **known tracker** (would block with content blocking enabled).

This is **not** proof of every tool on wgtn.ac.nz — only this endpoint was documented in the dump.

---

## Request summary

| Field | Value |
|-------|--------|
| Host | `analytics.tiktok.com` |
| Method / status | (capture shows) **200** |
| Protocol | **HTTP/2** |
| Origin | `https://www.wgtn.ac.nz` |
| Referer | `https://www.wgtn.ac.nz/` |
| Sec-Fetch-Site | **cross-site** |
| Sec-Fetch-Mode | **no-cors** |
| Sec-Fetch-Dest | empty |
| Request Priority | Lowest (u=6) |
| Cookie | `_ttp=…` (TikTok pixel/cookie style; value redacted in public notes — treat as tracker ID) |
| Request Content-Type | `text/plain;charset=UTF-8` |
| Request Content-Length | 1606 |
| Response Content-Type | `application/json; charset=utf-8` |
| Response Content-Length | 16 |
| Cache | `max-age=0, no-cache, no-store` + `pragma: no-cache` |
| Server | **nginx** (origin-facing label) |
| CDN | **Akamai** (`x-cache` / `x-cache-remote` TCP_MISS; `x-akamai-request-id`; `server-timing` cdn-cache MISS) |

### TikTok / ByteDance-style response headers (CONFIG / evidence)

| Header | Role |
|--------|------|
| `x-tt-logid` | Trace / log id |
| `x-tt-trace-id` | Distributed trace |
| `x-tt-trace-host` | Trace host blob |
| `x-tt-trace-tag` | e.g. `cdn-cache=miss;type=dyn` |
| `access-control-expose-headers` | Exposes `x-tt-traceflag`, `x-tt-logid` |

Do **not** paste full cookie or trace-host values into public commits if they look session-unique; summarise as present.

---

## Host inventory (this capture)

| Host / pattern | Tag | Notes |
|----------------|-----|--------|
| `www.wgtn.ac.nz` | origin **LOAD** / first-party | Page that triggered the request |
| `analytics.tiktok.com` | **LOAD** (tracker) | TikTok / ads analytics endpoint; ETP “known tracker” |
| Akamai edge (`*.deploy.akamaitechnologies.com` in x-cache) | **LOAD** / CDN | Delivers TikTok analytics response path |

### Legend

| Tag | Meaning |
|-----|---------|
| **LOAD** | Network request observed |
| **CONFIG** | IDs / account keys (none fully extracted beyond cookie name `_ttp`) |
| **CLICK** | User-initiated navigation (not this beacon) |
| **BUNDLE** | String-only in JS (not this capture) |

---

## Risk / hygiene notes

1. **Marketing measurement** — TikTok analytics on a university marketing home page is typically for ads/attribution; confirm purpose in VUW cookie/privacy statements.  
2. **Cross-site cookie** — `_ttp` on `analytics.tiktok.com` is third-party tracking context.  
3. **Blocking** — users with ETP/strict tracking protection may not send this beacon (capture notes “would be blocked”).  
4. **Incomplete map** — expect also GTM, Meta, LinkedIn, etc. on many uni sites; **not seen in this dump**.  

---

## Possible link to CSS orphan fingerprint

Orphan CSS notes under `knowledge/web/css-design-fingerprint-helvetica-grey.md` are **not yet bound**.  
If the user confirms the same session was on wgtn.ac.nz **and** body styles match, bind with medium confidence — **do not auto-bind** from this tracker alone.

---

## Next capture checklist (to complete map)

- [ ] Document document URL path (home vs campaign landing)  
- [ ] TikTok pixel ID / `ttq.load` from page JS  
- [ ] Other third parties (GTM, Adobe, Hotjar, …)  
- [ ] Consent banner behaviour before/after accept  
- [ ] Link official VUW privacy / cookies page  

---

## Cross-links

- Skill: `privacy-host-map` · **`tiktok-analytics`**  
- Method: `knowledge/privacy/tiktok-analytics.md`  
- CSS orphan (unbound): `knowledge/web/css-design-fingerprint-helvetica-grey.md`  
- Compare uni stacks: `knowledge/privacy/uc-arts-pg-hosts.md`, `uoa-eloqua-pg-webinar-hosts.md`  
