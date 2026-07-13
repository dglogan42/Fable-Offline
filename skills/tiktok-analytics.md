# TikTok Analytics / Pixel (page & Network evidence)

**WHEN_TO_USE:** HTML/JS dumps or DevTools Network captures that mention **TikTok** ads/analytics — `analytics.tiktok.com`, `ttq`, `_ttp`, `pixel`, Events API references, or “does this site use TikTok tracking?”. Use after pasting source HTML, HAR-style header dumps, or when `knowledge/privacy/*` already flags TikTok.

**Upstream:** Full multi-vendor maps → **`privacy-host-map`**. Programme design → **`privacy-design-planner`**. University seeds: **`knowledge/privacy/wgtn-ac-nz-hosts.md`**.

## Stance
You classify **evidence strength** for TikTok measurement tags. A host string in minified JS is **BUNDLE** only. A live request with `Origin`/`Referer` is **LOAD**. Pixel IDs in `ttq.load('…')` are **CONFIG**. Do not invent pixel IDs, data-sharing agreements, or “they sell your data to TikTok” legal conclusions without evidence.

**Not legal advice.** Not a penetration test. Not a how-to for ad fraud or bypassing consent. Prefer official site privacy/cookie notices for purpose statements.

---

## Evidence legend (same family as privacy-host-map)

| Tag | Meaning for TikTok |
|-----|--------------------|
| **LOAD** | Browser requested a TikTok analytics/pixel host (Network) or `<script src>` to TikTok CDN |
| **CONFIG** | Pixel ID, `ttq.load`, account keys, Events API endpoints in page config |
| **CLICK** | User opens tiktok.com / share-to-TikTok link (not the pixel) |
| **BUNDLE** | Host string only inside vendor or GTM bundle — not proof of fire |

Also note:

| Scope | Example |
|-------|---------|
| **Cross-site beacon** | `Sec-Fetch-Site: cross-site` to `analytics.tiktok.com` |
| **First-party page** | `Origin` / `Referer` = the site under review |
| **ETP / blocked** | Browser labels known tracker; request may not fire for all users |

---

## What to extract from HTML / JS

1. **Script tags** — `https://analytics.tiktok.com/…`, `https://www.tiktok.com/…`, other `*tiktok*` CDN paths  
2. **Inline bootstrap** — `ttq`, `window.TiktokAnalyticsObject`, `ttq.load('PIXEL_ID')`, `ttq.page()`, `ttq.track(`  
3. **noscript / img pixels** if present  
4. **GTM / Launch / Tealium** — TikTok tags may fire only via tag manager (look for tag names / custom HTML in export if available)  
5. **Cookie names** — especially **`_ttp`** (and related TikTok cookies when documented)  
6. **Consent** — whether tag is gated behind CMP (OneTrust, Cookiebot, custom) — only if code/banner evidence  

### What to extract from Network (preferred for LOAD)

| Field | Why |
|-------|-----|
| Host | e.g. `analytics.tiktok.com` |
| Status / protocol | 200, h2 |
| Origin / Referer | First-party page that triggered call |
| Sec-Fetch-* | cross-site / no-cors typical for beacons |
| Cookie | `_ttp` present? (redact value in knowledge notes) |
| Request body size / type | Often `text/plain` POST-like payloads |
| Response headers | `x-tt-logid`, `x-tt-trace-id`, `x-tt-trace-tag`, Akamai cache headers |
| CDN | Akamai / other in `x-cache` |

**Redact** full `_ttp` values, long `x-tt-trace-host` blobs, and session IDs in committed notes.

---

## Host & header cheat-sheet

| Pattern | Typical role |
|---------|----------------|
| `analytics.tiktok.com` | Analytics / pixel events (ads measurement) |
| `*.tiktok.com` / `*.tiktokw.us` / related CDNs | Pixel scripts, assets (VERIFY LIVE — hosts evolve) |
| Cookie `_ttp` | TikTok browser ID-style cookie on TikTok domain context |
| Headers `x-tt-*` | TikTok/ByteDance trace & logging |
| Akamai on TT analytics | Common edge for TikTok endpoints |

Do not treat every `tiktok.com` **CLICK** (embed, share, careers social link) as an analytics pixel.

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| Detect TikTok from HTML/JS only | **scan-html** |
| Confirm live fire from Network | **confirm-network** |
| Full TikTok-focused map for a page | **map-tiktok** |
| Compare policy claim vs reality | **policy-tension** |
| Write durable knowledge note | **write-knowledge** |
| Short answer | **brief** |

Default: **map-tiktok** if both HTML and Network available; else **scan-html** or **confirm-network** alone.

---

## scan-html

**Output:**
1. Verdict — TikTok **present / not found / BUNDLE-only**  
2. Table: signal · tag (LOAD script vs CONFIG vs BUNDLE) · snippet (truncated, no secrets)  
3. Pixel ID if found (CONFIG) — mark UNKNOWN if only Network without ID  
4. Tag manager dependency (GTM/Launch?) UNKNOWN if not proven  
5. Next step: Network confirm  

---

## confirm-network

**Input:** headers dump (as from Firefox/Chrome) or HAR summary.

**Output:**
1. Verdict — **LOAD confirmed** / blocked / failed  
2. Origin page vs host  
3. Cookie / cache / CDN / `x-tt-*` summary  
4. ETP or user-agent notes if present  
5. Link to property knowledge path if known (e.g. wgtn)  

**Worked seed:** VUW home → `analytics.tiktok.com` 200 — `knowledge/privacy/wgtn-ac-nz-hosts.md`.

---

## map-tiktok

Combine scan + network:

```markdown
# TikTok Analytics — [site] — [date]
## Verdict
## LOAD evidence
## CONFIG (pixel IDs)
## BUNDLE-only noise
## Cookies / storage
## Consent / blocking
## Policy notes (claims vs evidence)
## Gaps
```

---

## policy-tension

| Question | Evidence needed |
|----------|-----------------|
| Is TikTok named in cookie/privacy notice? | Policy page + date |
| Ads vs product analytics? | Purpose language |
| Runs before consent? | Banner + Network order |
| Essential? | Almost never for marketing pixels — mark marketing unless site claims otherwise with basis |

Score **disclosure honesty** 1–10 (not “is TikTok evil”).

---

## write-knowledge

Prefer: `knowledge/privacy/<site>-hosts.md` section **TikTok** or dedicated `knowledge/privacy/tiktok-*.md` for methodology.  
Never commit raw HAR with full cookies.

---

## Forbidden
- Building tools to steal pixel data or spoof conversions for fraud  
- Claiming GDPR/Privacy Act breach without legal analysis  
- Pasting full live cookie values into public git  
- Treating social **CLICK** links as equivalent to analytics **LOAD**  

## Local knowledge
- `knowledge/privacy/tiktok-analytics.md` (method)  
- `knowledge/privacy/wgtn-ac-nz-hosts.md` (worked example)  

## Companion skills
| Skill | Use |
|-------|-----|
| `privacy-host-map` | Full third-party inventory |
| `privacy-design-planner` | Reduce/replace trackers programme |
| `aem-site-agent` | If TikTok loaded via AEM/Launch |
| `instagram-selfie-selector` | Unrelated content skill — do not confuse |
