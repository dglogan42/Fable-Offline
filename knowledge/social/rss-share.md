# RSS-type share — Fable offline

**Skill:** `rss-share`  
**Script:** `scripts/rss_share.py`  
**Format:** RSS 2.0 XML  

---

## Why RSS share

| Use | Example |
|-----|---------|
| Personal / team notes syndication | Changelog of Fable lessons |
| Public blog-style updates | Static site `feed.xml` |
| Reader apps | NetNewsWire, Feedly, Thunderbird, Miniflux |
| Contrast with social | Pull (RSS) vs algorithmic push (IG/TikTok/Snap) |

---

## Generate

```bash
# Demo
python scripts/rss_share.py --demo -o workspace/demo-feed.xml

# From JSON
python scripts/rss_share.py workspace/channel.json -o workspace/feed.xml \
  --title "My channel" --link "https://example.com/"
```

### Minimal `channel.json`

```json
{
  "title": "My share feed",
  "link": "https://example.com/",
  "description": "Updates",
  "language": "en",
  "items": [
    {
      "title": "Hello",
      "link": "https://example.com/hello",
      "description": "First item",
      "pubDate": "2026-07-13T10:00:00Z",
      "category": ["note"]
    }
  ]
}
```

---

## Share pack (user-facing)

1. Host `feed.xml` over **HTTPS** (GitHub Pages, static host, CMS).  
2. Tell subscribers the **feed URL**.  
3. Add HTML:

```html
<link rel="alternate" type="application/rss+xml"
      title="My share feed"
      href="https://example.com/feed.xml" />
```

4. Optional visible: “Subscribe via RSS” → feed URL (**CLICK**).

---

## Hygiene

| Do | Don’t |
|----|--------|
| Summaries + canonical link | Full repost of others’ paid content |
| Stable guids | Rotate IDs every build without reason |
| Public feeds only in public git | Commit private feed URLs with tokens |
| Escape descriptions | Break XML with raw `&` |

Private item drafts: `knowledge/social/_local/` or `workspace/` (gitignored patterns).

---

## Related Fable surfaces

| Surface | Share type |
|---------|------------|
| Snapchat Web | Ephemeral chat — not RSS |
| Instagram fit | Manual post — not RSS |
| DOC blog | Native RSS alternate links (pattern) |
| iCal | Calendar subscribe parallel |

---

## Cross-links

- Skill: `rss-share`  
- Script: `scripts/rss_share.py`  
