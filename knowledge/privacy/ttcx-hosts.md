# Privacy host map — TikTok Creative Exchange (TTCX) shell (seed)

**Skill:** `privacy-host-map` · `tiktok-analytics`  
**Property:** TikTok Creative Exchange web app (marketplace)  
**Evidence:** Static HTML head dump (`TikTok Creative Exchange` title + pumbaa-rule JSON)  
**Not legal advice.** Not a complete inventory. Re-verify Network tab on live session.

---

## Verdict

**First-party TikTok product surface** for creative marketplace. Dump shows heavy **client-side privacy/consent instrumentation** (`pumbaa-rule`) plus Google site verification. This is **not** the same as a university site loading a single pixel — this **is** TikTok’s own product domain family.

---

## Document identity (dump)

| Field | Value |
|-------|--------|
| Title | TikTok Creative Exchange |
| Description | Marketplace connecting advertisers with creative service providers |
| Robots | index, follow |
| Google site verification | present (meta) |

---

## Host / endpoint families (from dump rules + meta)

| Pattern | Tag | Notes |
|---------|-----|--------|
| `tiktok.com` / `tiktokv.com` | first-party family | Cookie domain scope in pumbaa blockers |
| `analytics.tiktok.com` | **LOAD**/CONFIG in rules | Pixel path referenced (`/api/v2/pixel`) in consent-error rule names |
| `www.google-analytics.com` / `analytics.google.com` / `stats.g.doubleclick.net` | **LOAD** family | GA collect patterns in network rules |
| `connect.facebook.net` / `www.facebook.com/tr` | **LOAD** family | Meta pixel patterns in consent rules |
| `px.ads.linkedin.com` | **LOAD** family | LinkedIn |
| `forms.hsforms.com` / `js.hsforms.net` | **LOAD** family | HubSpot forms on business surfaces |
| `player.vimeo.com` / `www.youtube.com` | **LOAD** embeds | Video embeds; YouTube cut-off rules exist |
| `bat.bing.com` | **LOAD** | Bing |
| Regional **MCS** list endpoints | **CONFIG**/telemetry | e.g. `mcs-sg.tiktok.com`, `mcs-va.tiktokv.com`, `mcs-ie.tiktokw.eu`, … (logging/list APIs in rawVal) |
| `mssdk-sg.tiktok.com` | special | Rule to ignore/report at 0 sample on `/web/report` |

### Cookie names called out in rules (CONFIG knowledge only)

Examples: `MONITOR_DEVICE_ID`, `MONITOR_WEB_ID`, plus opaque IDs; Facebook/GA/LinkedIn/TikTok Ads cookie context flags (`cookie_fbp`, `cookie_ga`, `cookie_ttads`, etc.). **Do not invent values.**

### Pumbaa behaviour (summary)

| Behaviour | Meaning |
|-----------|---------|
| Cookie blockers | Strip listed cookies on tiktok.com / tiktokv.com under conditions |
| Sample rates | Low % reporting on events/navigation |
| Consent error reporters | Report when tags fire without expected consent cookies (GA, FB, LinkedIn, TikTok pixel, etc.) |
| `battery_info` remove | Strip battery fields from queries/bodies on TikTok hosts |
| HTTP→HTTPS upgrade | plain_text rule |
| UA blocks | Block some legacy GA gif endpoints |

This is **platform self-instrumentation**, not advertiser landing-page hygiene.

---

## Cross-links

- Product knowledge: `knowledge/ads/tiktok-creative-exchange.md`  
- Pixel method: `tiktok-analytics.md`  
- Ads creation: `../ads/tiktok-ads-create.md`  
