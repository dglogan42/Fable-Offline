# Privacy host map seed — OpenStreetMap Wiki (Contribute map data)

**Skill:** `privacy-host-map` · `openstreetmap-contribute-kit`  
**URL:** https://wiki.openstreetmap.org/wiki/Contribute_map_data  
**Evidence:** MediaWiki HTML dump (Vector legacy, ResourceLoader, Wikimedia Commons images)  

Not legal advice. VERIFY LIVE. OSMF: [Privacy Policy](https://www.osmfoundation.org/wiki/Privacy_Policy).

---

## Host inventory

| Host | Class | Notes |
|------|-------|--------|
| `wiki.openstreetmap.org` | LOAD | Wiki HTML, `/w/load.php` ResourceLoader, images under `/w/images/` |
| `www.openstreetmap.org` | CLICK | The map, edit (iD), account, GPS traces, copyright page |
| `wiki.osmfoundation.org` | LOAD | Contributor Terms |
| `www.osmfoundation.org` | LOAD | Privacy policy link from footer |
| `upload.wikimedia.org` | LOAD | Some section icons (Commons thumbnails in dump) |
| `www.mediawiki.org` | LOAD | “Powered by MediaWiki” footer asset path family |

### First-party path families (wiki)

- `/wiki/*` — articles  
- `/w/load.php` — styles/scripts (MediaWiki RL)  
- `/w/api.php` — API / RSD  
- `/w/rest.php/v1/search` — OpenSearch  
- `/w/index.php` — actions, history, mobile toggle  
- Atom: `/w/index.php?title=Special:RecentChanges&feed=atom`  

### Map / contribute CLICK surfaces

- Edit with iD, save changeset  
- Upload GPS traces  
- Notes  
- Login / Create account (OAuth/session — never store cookies in git)  

---

## Notes

- Dump shows anonymous view (`wgUserName`: null); edit tokens are session-bound  
- Client prefs cookie pattern: `wikimwclientpreferences`  
- Gadgets seed: taginfo, dataitemlinks, maps  
- Mobile view toggle present  

## OPEN

- Full third-party analytics on www.openstreetmap.org edit session (map separate from wiki)  
- Mobile app telemetry (per-app privacy policies)  
- Imagery provider ToS when enabling backgrounds in editors  
