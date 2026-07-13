# Privacy host map seed — iNaturalist

**Skill:** `privacy-host-map` · `inaturalist-flora-fauna-kit`  
**URLs:** https://www.inaturalist.org/ · https://api.inaturalist.org/ · https://github.com/inaturalist/inaturalist  
**Evidence:** Official README/CONTRIBUTING + developers/API public pages (VERIFY LIVE for trackers).  

Not legal advice.

---

## Host inventory

| Host | Class | Notes |
|------|-------|--------|
| `www.inaturalist.org` | CLICK | Observations, projects, Network, account |
| `api.inaturalist.org` | LOAD | Public/authenticated JSON API |
| `static.inaturalist.org` | LOAD | Static assets (logos, media CDN family seed) |
| `forum.inaturalist.org` | CLICK | Bug reports, feature requests |
| `github.com` | LOAD | Source code transparency (inaturalist org) |
| `crowdin.com` | CLICK | Translation project |
| Mobile app stores | CLICK | Official app install (HITL) |

### Data classes

| Class | Care |
|-------|------|
| Observation media + coords | Personal + ecological; respect geoprivacy |
| OAuth tokens | Never commit |
| API bulk pulls | Follow recommended practices; prefer exports |
| Local Docker DB | Dev only; default compose passwords not for production |

---

## Notes

- Community guidelines apply to conduct and content  
- Security issues: help+security@inaturalist.org  
- Prefer Network membership over self-hosting a competing fork for “local flora only”  

## OPEN

- Full third-party analytics stack on production web (map with live Network tab)  
- Per-Network-site cookies and regional privacy notices  
