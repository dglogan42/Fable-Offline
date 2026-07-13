# Third-party source mirrors (local only)

Fable ships **curated skills/knowledge**, not full upstream application trees.

## iNaturalist

| Item | Value |
|------|--------|
| Upstream | https://github.com/inaturalist/inaturalist |
| Licence | MIT |
| Role | Rails app behind [inaturalist.org](https://www.inaturalist.org/) |
| Fable skill | `inaturalist-flora-fauna-kit` |
| Knowledge | `knowledge/geo/inaturalist-flora-fauna.md` |

### Optional local sparse clone

Full clones on **Windows** may fail on long fixture filenames under `spec/fixtures/`. Prefer sparse checkout:

```powershell
git clone --filter=blob:none --sparse --depth 1 https://github.com/inaturalist/inaturalist.git third_party/inaturalist
cd third_party/inaturalist
git sparse-checkout set --skip-checks README.md CONTRIBUTING.md MIT-LICENSE Makefile Dockerfile docker-compose.yml docker-compose.override.yml.example .ruby-version Gemfile package.json
```

Or enable Windows long paths and clone normally if you need the full tree for Docker dev (`make services`, etc.).

**Do not commit** `third_party/inaturalist/` — it is gitignored. Re-clone after fresh checkout.

### Product vs code

- **Observe flora/fauna:** use iNaturalist.org / official apps (HITL).  
- **Change the platform:** Forum first; see upstream `CONTRIBUTING.md`. Prefer [iNaturalist Network](https://www.inaturalist.org/sites/network) over forking the community.  
