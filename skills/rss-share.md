# RSS share (feed build · subscribe · hygiene)

**WHEN_TO_USE:** Publishing or sharing updates as **RSS 2.0** (or validating RSS-style share links), building a local `feed.xml` from notes/items, coaching “how do I share via RSS?”, or documenting RSS discoverability on a site (`application/rss+xml` alternate links). Complements **`calendar-mail-meetings`** (iCal share) and domain skills that produce recaps worth syndicating.

## Stance
You coach **open, user-controlled** syndication. RSS is for **pull** subscription, not spam push. Prefer **local generation** via `scripts/rss_share.py` or site-native feeds. Do not scrape private feeds behind login without permission. Do not inject malware enclosures.

**Not legal advice** on copyright of third-party full-text republication — prefer summaries + link back.

---

## RSS-type share map

| Layer | Fable | User / host |
|-------|-------|-------------|
| **Compose items** | Titles, links, summaries from user notes | Source of truth |
| **Build feed** | `python scripts/rss_share.py items.json -o workspace/feed.xml` | |
| **Share** | Hand user the XML path or hosted URL | Host on HTTPS static / CMS |
| **Subscribe** | Instruct reader apps (Feedly, NetNewsWire, Thunderbird, …) | User CLICK |
| **Discover** | HTML `<link rel="alternate" type="application/rss+xml" …>` | Site template |

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| Create feed from items | **build-feed** |
| Draft channel + items JSON | **compose-items** |
| Share URL / file hygiene | **share-pack** |
| Validate structure | **validate-feed** |
| HTML discoverability snippet | **discover-link** |
| Site RSS audit (from HTML dump) | **scan-html-rss** |
| Persist channel config | **write-knowledge** |
| Short answer | **brief** |

Default: **compose-items** then **build-feed**.

---

## compose-items

**Output JSON shape** (for `rss_share.py`):

```json
{
  "title": "Channel title",
  "link": "https://example.com/",
  "description": "What this feed is",
  "language": "en",
  "items": [
    {
      "title": "Item title",
      "link": "https://example.com/posts/1",
      "description": "Summary (plain text; escaped in XML)",
      "pubDate": "2026-07-13T12:00:00Z",
      "guid": "optional-stable-id",
      "category": ["tag1"]
    }
  ]
}
```

Rules:
- Stable **guid** if link changes  
- Prefer **summary** over full copyrighted reprint  
- ISO-8601 `pubDate` OK (script converts to RFC 822)  

---

## build-feed

```bash
python scripts/rss_share.py path/to/items.json -o workspace/feed.xml
python scripts/rss_share.py --demo -o workspace/demo-feed.xml
```

Report: path, item count, channel title/link.

---

## share-pack

**Output:**
1. File path or public URL of `feed.xml`  
2. One-line: “Subscribe in any RSS reader: …”  
3. Optional HTML discover snippet (**discover-link**)  
4. MIME: `application/rss+xml` or `application/xml`  
5. Cache note: readers poll; don’t require login for public feeds  

---

## validate-feed

Checklist:
- [ ] Single `<rss version="2.0">` + `<channel>`  
- [ ] Channel `title`, `link`, `description`  
- [ ] Each item has `title` + (`link` or `guid`)  
- [ ] Well-formed XML (no bare `&`)  
- [ ] Dates parseable  

---

## discover-link

```html
<link rel="alternate" type="application/rss+xml"
      title="Channel title"
      href="https://example.com/feed.xml" />
```

Also mention DOC-style “Subscribe via RSS” **CLICK** links when auditing blogs.

---

## scan-html-rss

From HTML dump, extract:
- `link[rel=alternate][type*=rss]` / `type*=atom`  
- Visible “RSS” / “Subscribe” anchors  
- Tag: **CLICK** for user subscribe URLs; **LOAD** only if feed auto-fetched (rare in static HTML)

---

## Forbidden
- Hijacking others’ full-text feeds as your product without rights  
- Credentialed private feed URLs committed to git  
- Fake “breaking news” items as social engineering  

## Local knowledge
- `knowledge/social/rss-share.md`  

## Companion
| Skill | Use |
|-------|-----|
| `calendar-mail-meetings` | Parallel: iCal share |
| `pdf-render` | Attachments via link, not RSS body bloat |
| Domain skills | Item content from notes |
