# Privacy host map — DOC Conservation blog (seed)

**Skill:** `privacy-host-map`  
**Scope:** [blog.doc.govt.nz](https://blog.doc.govt.nz/) WordPress stack (sample post: Becoming a DOC ranger, 2020).  
**Not a penetration test. Not legal advice.** Re-verify with live Network capture.

---

## Verdict

DOC’s public **Conservation blog** rides a **WordPress + Jetpack / WordPress.com** media and asset stack. Treat as standard government-blog WordPress hygiene: cookies/analytics may load from WP.com CDNs; content remains DOC-authored.

---

## Host inventory (from public HTML head / assets)

| Host / pattern | Tag | Notes |
|----------------|-----|--------|
| `blog.doc.govt.nz` | **LOAD** / origin | Blog application |
| `www.doc.govt.nz` | **CLICK** | Main DOC site (careers, nature, bookings) |
| `v0.wordpress.com` | **LOAD** / dns-prefetch | Jetpack / WP.com |
| `i0.wp.com` / `i1.wp.com` / `i2.wp.com` | **LOAD** | Photon/image CDN for post images |
| `c0.wp.com` | **LOAD** / preconnect | WP.com static/CSS/JS |
| `fonts.gstatic.com` | **LOAD** / preconnect | Web fonts |
| `s.w.org` | **LOAD** | Emoji assets (WP) |
| Google site verification meta | **CONFIG** | `google-site-verification` present in sample |

Sharing scripts (Facebook/LinkedIn share windows) appear as user **CLICK** outbound.

---

## Evidence rules

| Tag | Use |
|-----|-----|
| **CLICK** | User opens blog post, DOC careers, share buttons |
| **LOAD** | Scripts, images, fonts on page view |
| **CONFIG** | Verification / API endpoints in markup |
| **BUNDLE** | Strings only in minified JS until confirmed |

---

## Cross-links

- Content snapshot: `knowledge/conservation/doc-ranger-pathway.md`  
- Skill: `doc-ranger-pathway`  
