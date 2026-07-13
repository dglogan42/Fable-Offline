# Privacy host map seed — Inkstone (WebNovel author platform)

**Skill:** `privacy-host-map` · `inkstone-resource-kit`  
**Apps:** [inkstone.webnovel.com](https://inkstone.webnovel.com/) · SPA CDN `www.yueimg.com/inkstone/`  
**Evidence:** HTML shell dump + public product URLs  
**Date seed:** 2026  

Not a complete privacy policy. VERIFY LIVE. Not legal advice.

---

## Host inventory

| Host | Category | Evidence | Notes |
|------|----------|----------|-------|
| `inkstone.webnovel.com` | First-party app | Product URLs | Author SPA routes: academy, novels, contests |
| `www.webnovel.com` | First-party reader / marketing | Public site | Be an Author → Inkstone |
| `wsa.webnovel.com` | Contest microsite | Public | Spirity Awards family |
| `www.yueimg.com` | CDN / static | HTML dump | `/inkstone/` assets, favicon |
| `noah2.yueimg.com` | Hybrid bridge | HTML dump | `hibridge.js` |
| `static.cloudflareinsights.com` | Analytics | HTML dump | Cloudflare beacon |
| `activity.webnovel.com` | Help / activity | Public footer seeds | Help center links may live here |

### Evidence class

| Class | Meaning |
|-------|---------|
| LOAD | Referenced in HTML or navigation |
| CONFIG | IDs/tokens in markup (strip from public notes if required) |
| CLICK | User navigation |
| BUNDLE | Hashed SPA chunks |

---

## Notes

- Academy and novel UIs are **client-rendered** — host list incomplete until Network panel after login  
- Contests add query params (`contestId`, `themeId`) — not secrets, but tie submissions to campaigns  
- Hybrid HiBridge may appear inside native WebNovel apps  

## OPEN

- Full authenticated third-party list  
- Official privacy policy pages (WebNovel privacy/cookie/terms)  
- Regional CDN variants  
