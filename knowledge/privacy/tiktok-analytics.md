# TikTok Analytics — method & HTML/Network signals

**Skill:** `tiktok-analytics`  
**Worked example:** [VUW / wgtn.ac.nz](wgtn-ac-nz-hosts.md) (Network 2026-07-13)  
**Not legal advice.** Hostnames and pixel bootstrap APIs change — VERIFY LIVE.

---

## What “TikTok Analytics” means here

Marketing / ads **measurement** tags that send browser events to TikTok (often for campaign attribution), distinct from:

| Surface | Tag |
|---------|-----|
| User visits tiktok.com | **CLICK** |
| Embedded TikTok video player | **LOAD** (player) — document separately from ads pixel |
| `analytics.tiktok.com` beacon | **LOAD** (tracker class) |

---

## HTML patterns to search

```text
analytics.tiktok.com
ttq
TiktokAnalyticsObject
ttq.load
ttq.page
ttq.track
_ttp
tiktok
```

Inline shape (illustrative — IDs fake):

```html
<script>
!function (w, d, t) {
  w.TiktokAnalyticsObject = t;
  var ttq = w[t] = w[t] || [];
  /* … loader … */
  ttq.load('PIXEL_ID_HERE');
  ttq.page();
}(window, document, 'ttq');
</script>
```

May also appear only inside **GTM** custom HTML (not in first HTML view-source).

---

## Network patterns (from real capture family)

| Signal | Example (VUW seed) |
|--------|---------------------|
| Host | `analytics.tiktok.com` |
| Cross-site | `Origin` + `Referer` = first-party site |
| Cookie | `_ttp` |
| No-cache | `max-age=0, no-cache, no-store` |
| JSON response | small body (e.g. 16 bytes) |
| Trace headers | `x-tt-logid`, `x-tt-trace-id`, `x-tt-trace-tag` |
| Edge | Akamai `TCP_MISS` / `x-akamai-request-id` |
| Browser | Firefox ETP “known tracker” |

### Redaction

| Keep in notes | Omit from public git |
|---------------|----------------------|
| Cookie **name** `_ttp` | Full cookie **value** |
| Header **names** `x-tt-*` | Full trace-host blobs if unique |
| Pixel ID if in HTML | Session tokens |

---

## Report template

```markdown
# TikTok Analytics — [hostname] — [YYYY-MM-DD]
## Verdict
LOAD confirmed | script only | BUNDLE only | not found
## First-party page
## Evidence
| Kind | Detail | Tag |
## Pixel / CONFIG
## Consent / ETP
## Policy alignment
## Gaps
```

---

## First-party TikTok UI (not the pixel alone)

If CSS shows **TikTok Text / TikTok Display**, `--primary-color: #fe2c55`, and **`--ttam-*`** tokens, the user is likely on a **TikTok product console** (ads/business), not merely a third-party site with a pixel.

See: `knowledge/web/css-design-fingerprint-tiktok-ui.md`.

| Context | CSS | Typical network |
|---------|-----|-----------------|
| TikTok product UI | TikTok fonts + brand pink | First-party TikTok app hosts |
| Third-party site with pixel | Site’s own design system | Often `analytics.tiktok.com` only |

---

## Cross-links

- Skill: `tiktok-analytics`  
- VUW seed: `wgtn-ac-nz-hosts.md`  
- UI fingerprint: `knowledge/web/css-design-fingerprint-tiktok-ui.md`  
- General hosts: `privacy-host-map`  
