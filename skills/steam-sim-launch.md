# Steam SIM launch (model performance test)

**WHEN_TO_USE:** Launching **simulation / city-builder / life-sim** games via Steam to **stress-test** a local LLM setup (RAM/VRAM contention, context lag while a heavy game runs), or documenting Steam protocol launches. Seed test: **SimCity 4 Deluxe** (`steam://rungameid/24780`).

## Stance
This skill is for **local harness ops**, not Steam cheating, multiplayer abuse, or bypassing DRM. Launch only games the user **owns and has installed**. Prefer explicit user consent before starting long-running games.

**Not a game bot.** Do not automate in-game actions or overlays for unfair advantage.

---

## Companion
| Resource | Use |
|----------|-----|
| `knowledge/steam/sim-games-launch.md` | App IDs, paths, checklist |
| `agentic-engineer-roadmap` | Eval / observability mindset |
| `--doctor` | Baseline system health before/after launch |

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| Launch a known SIM for load test | **launch-sim** |
| Pre/post model performance check | **perf-baseline** |
| Resolve steam:// or appid | **resolve-app** |
| Stop game process (user asked) | **stop-sim** |
| Short note | **brief** |

---

## launch-sim

1. Confirm **appid** and game name (table or user).  
2. Confirm Steam installed / protocol works.  
3. Prefer:  
   - Windows: `Start-Process "steam://rungameid/<APPID>"` or `"%STEAM%\steam.exe" steam://rungameid/<APPID>`  
   - Or: `python scripts/steam_launch.py <APPID>`  
4. Wait a few seconds; verify process (e.g. `SimCity 4.exe` for 24780).  
5. Log: time, appid, process name, success/fail.  

**Default test target:** `24780` — SimCity 4 Deluxe.

---

## perf-baseline

Run **before** and **after** game launch (or with game in background):

| Check | How |
|-------|-----|
| Ollama/backend | `python fable5_offline_agent.py --doctor` |
| Simple chat latency | One short prompt; note seconds to first token if possible |
| Memory pressure | User Task Manager / `Get-Process` working sets |
| Concurrent load | Optional: small `/loop` or chat while SIM runs |

**Report shape:**
1. Verdict — model usable / degraded / OOM risk  
2. Pre metrics (notes)  
3. Game launched (appid, name)  
4. Post metrics  
5. Recommendation (close game for heavy loops; use smaller model; etc.)  

---

## resolve-app

| Input | Output |
|-------|--------|
| `steam://rungameid/24780` | appid **24780**, name SimCity 4 Deluxe |
| App name | Look up in knowledge table; VERIFY on steamdb if unknown |
| Protocol only | Tag as **local CLICK**, not HTTP scrape |

Fable `--scrape` **cannot** fetch `steam://` URLs.

---

## stop-sim

Only if user asks: stop known process names for that app (e.g. `SimCity 4`). Prefer graceful exit; avoid `taskkill /F` unless stuck and user confirms.

---

## Forbidden
- Launching games not owned/installed  
- Automating gameplay for multiplayer advantage  
- Storing Steam credentials  
- Treating SteamDB/store as free redistribution of game assets  

## Local knowledge
- `knowledge/steam/sim-games-launch.md`  

## Note
SIM games are useful **background load** for offline LLM soak tests because they are long-running and GPU/CPU heavy on some systems (SC4 is mostly CPU/legacy).
