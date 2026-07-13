# Create a bootable installer for macOS (Apple 101578)

**Skill:** `macos-install-prep`  
**Source snapshot:** [Create a bootable installer for macOS](https://support.apple.com/en-nz/101578)  
**Published (page):** 24 October 2025 (VERIFY LIVE — commands and version names change)  
Apple trademarks remain Apple’s. **Not legal advice.**

---

## When you need this

You **do not** need a bootable installer only to [upgrade](https://support.apple.com/en-nz/108382) or [reinstall](https://support.apple.com/en-nz/102655) macOS. It helps when those methods fail, or when installing on **multiple Macs** without re-downloading each time.

Creating a bootable installer ≠ preparing an external disk as a general startup disk ([Apple note](https://support.apple.com/en-nz/111336)).

---

## Download the full installer

1. Get the full installer via App Store, browser, or Terminal per [How to download and install macOS](https://support.apple.com/en-nz/102662).  
2. Download only — if installer opens, **quit** it.  
3. Prefer a Mac **compatible** with the macOS version you download. Pre–High Sierra often needs an older compatible Mac to build media.  
4. **Enterprise:** download from **Apple**, not a locally hosted update server.  
5. Result should be an app: **`Install macOS <Version Name>`** (e.g. Install macOS Tahoe). If you have `.dmg` / `.pkg`, follow Apple’s download article to extract the app.  
6. Location: **`/Applications`** (Finder → Go → Applications).

---

## Prepare the USB volume

1. Connect USB (or secondary volume) **directly** to the Mac.  
2. Capacity: **32 GB** enough for any current installer per Apple; **16 GB** enough for most earlier versions. Terminal warns if short.  
3. Rename volume to **`MyVolume`** (matches sample commands).  
4. **createinstallmedia erases** the volume as **Mac OS Extended (Journaled)**.

---

## createinstallmedia commands (official patterns)

Run in **Terminal** after copying the line that matches your installer.  
Host password: admin via `sudo`. Type **`Y`** when asked to erase.

| macOS | Command pattern |
|-------|-----------------|
| **Tahoe** | `sudo /Applications/Install\ macOS\ Tahoe.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume` |
| **Sequoia** | `sudo /Applications/Install\ macOS\ Sequoia.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume` |
| **Sonoma** | `sudo /Applications/Install\ macOS\ Sonoma.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume` |
| **Ventura** | `sudo /Applications/Install\ macOS\ Ventura.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume` |
| **Monterey** | `sudo /Applications/Install\ macOS\ Monterey.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume` |
| **Big Sur** | `sudo /Applications/Install\ macOS\ Big\ Sur.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume` |
| **Catalina** | `sudo /Applications/Install\ macOS\ Catalina.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume` |
| **Mojave** | `sudo /Applications/Install\ macOS\ Mojave.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume` |
| **High Sierra** | `sudo /Applications/Install\ macOS\ High\ Sierra.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume` |
| **El Capitan** | `sudo /Applications/Install\ OS\ X\ El\ Capitan.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume --applicationpath /Applications/Install\ OS\ X\ El\ Capitan.app` |

**Notes from Apple:**

- Invalid installer → delete, repair startup disk (Disk Utility), redownload.  
- Command not found → wrong command / installer not in Applications or wrong name.  
- Creating media on **macOS Sierra 10.12.6 or earlier** host: may need `--applicationpath` like El Capitan.  
- Erase failure → Disk Utility erase as Mac OS Extended (Journaled), retry.  
- Allow Terminal access to removable volumes if macOS prompts.  
- When done, volume name often matches installer (e.g. Install macOS Tahoe). Eject; optional: delete installer from Applications to free space.

**Always re-check** [101578](https://support.apple.com/en-nz/101578) for new macOS rows after releases.

---

## Use the bootable installer

Target Mac should be **online** (firmware / model data). Wrong OS for model → incomplete install or prohibitory symbol.

### Apple silicon
1. Shut down.  
2. Connect installer USB.  
3. Press and **hold power** → startup options.  
4. Select installer → Continue → follow prompts.

### Intel / other Mac
1. Shut down.  
2. Connect installer USB.  
3. Power on, hold **Option (Alt)** → select installer.  
4. T2 security: allow external/removable boot in Startup Security Utility if blocked.  
5. Utilities → Install macOS → Continue.

---

## Hygiene for Fable / git

| Do | Don’t |
|----|--------|
| Link Apple Support | Commit full Installer apps or raw USB images |
| Document version + date verified | Treat random “macOS ISO” sites as official |
| Org notes in `knowledge/macos/_local/` | Store Apple ID passwords in repo |

---

## Cross-links

- Recovery / reinstall without USB: `reinstall-and-recovery.md`  
- Skill procedures: `macos-install-prep`  
