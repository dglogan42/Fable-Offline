# Steam SIM games — launch notes (model perf test)

**Skill:** `steam-sim-launch`  
**Purpose:** Launch owned SIM / city-builder titles via Steam protocol to test local model performance under load.  
**Not DRM circumvention or game automation.**

---

## Protocol

```text
steam://rungameid/<APPID>
```

Windows examples:

```powershell
Start-Process "steam://rungameid/24780"
# or
& "D:\Steam\steam.exe" "steam://rungameid/24780"
```

Helper:

```bash
python scripts/steam_launch.py 24780
python scripts/steam_launch.py 24780 --steam "D:\Steam\steam.exe"
```

---

## Seed test target

| Field | Value |
|-------|--------|
| **AppID** | **24780** |
| **Name** | SimCity 4 Deluxe |
| **Protocol** | `steam://rungameid/24780` |
| **Verified (example host)** | Installed under `steamapps/common/SimCity 4 Deluxe`; process `SimCity 4.exe` |
| **Typical install size** | ~1.2 GB |

Manifest hint: `steamapps/appmanifest_24780.acf` (`name`, `installdir`, `StateFlags`).

---

## Other SIM / city-builder AppIDs (examples — verify ownership)

| AppID | Title (common) | Notes |
|-------|----------------|-------|
| 24780 | SimCity 4 Deluxe | Default Fable soak-test seed |
| 255710 | Cities: Skylines | Heavier GPU/CPU |
| 526870 | Satisfactory | Factory SIM; heavy |
| 892970 | Valheim | Survival; optional |
| 413150 | Stardew Valley | Lighter life-sim load |

Expand only with user-owned titles. Confirm AppID on Steam store URL: `store.steampowered.com/app/<APPID>/`.

---

## Perf test checklist

1. `python fable5_offline_agent.py --doctor`  
2. Optional: one short chat prompt (note lag)  
3. Launch SIM: `python scripts/steam_launch.py 24780`  
4. Confirm process running  
5. Repeat short chat / doctor notes  
6. Verdict: model OK under load / degraded / stop game for heavy agent work  

---

## Steam path discovery (Windows)

| Location | Example |
|----------|---------|
| Protocol handler | Registry `steam\shell\open\command` |
| Common | `C:\Program Files (x86)\Steam\steam.exe` |
| Custom | `D:\Steam\steam.exe` |

---

## Agent boundaries

- Launch only when user requests performance/sim test.  
- Do not scrape `steam://`.  
- Do not commit Steam credentials or large game files.  
