# macOS install prep (Apple-licensed · bootable installer)

**WHEN_TO_USE:** Planning a **genuine macOS** upgrade, reinstall, or **bootable installer** USB for Macs you administer; `createinstallmedia`; recovery vs full installer; multi-Mac offline install prep — or “how do I make a macOS install USB legally?”

**Primary Apple doc:** [Create a bootable installer for macOS](https://support.apple.com/en-nz/101578) (HT201372 family; region may redirect).

## Stance
You coach **Apple-supported** install hygiene on **Apple-branded Mac hardware**. Prefer official Apple Support, App Store / Apple download methods, and `createinstallmedia` as published. There is **no** Fable path to pirate macOS, redistribute Apple installers, install macOS on non-Apple PCs (Hackintosh), or ship cracked “combo” DMGs from untrusted sites.

**Not legal advice.** Apple software license terms apply. Enterprise: download from Apple, not a locally hosted update server, per Apple’s note for administrators.

---

## Path A — You may not need a bootable USB

Per Apple: a bootable installer is **optional**. Often enough:

| Goal | Prefer first |
|------|----------------|
| Upgrade in place | Software Update / App Store full installer |
| Reinstall | macOS Recovery / Internet Recovery |
| Multiple Macs / failed methods | **Bootable installer** (this skill) |

Related official topics (user **CLICK**, VERIFY LIVE):

- How to download and install macOS  
- How to reinstall macOS  
- Other macOS installation methods  
- Upgrade macOS  

Knowledge: `knowledge/macos/bootable-installer.md`, `reinstall-and-recovery.md`

---

## Path B — Bootable installer (Apple 101578)

| Step | Action |
|------|--------|
| 1 | Download **full** installer (`Install macOS <Name>.app`) — do not need to run install; quit if it auto-opens |
| 2 | Place installer in **Applications** |
| 3 | Connect USB (typically **32 GB** enough for current; 16 GB many older) — **will be erased** |
| 4 | Rename volume to **`MyVolume`** (name used in Apple’s sample commands) |
| 5 | Run matching `createinstallmedia` via **Terminal** (admin password) |
| 6 | Confirm erase (`Y`); allow Terminal removable-volume access if prompted |
| 7 | Eject; boot target Mac from installer (Apple silicon vs Intel steps differ) |
| 8 | Target Mac needs **internet** during install for firmware/model-specific data |

**Destructive:** `createinstallmedia` erases the named volume. Confirm the volume name before `sudo`.

---

## Path C — Org / fleet (licensed Macs only)

| Layer | Apple-oriented tools | Agent may… | Agent must not… |
|-------|----------------------|------------|-----------------|
| Installer | Official full installer + createinstallmedia | Checklist + command **patterns** from Apple | Host pirate mirrors |
| MDM | Apple Business/School Manager, MDM | High-level enrollment order | Bypass Activation Lock for stolen devices |
| Imaging | Modern: ADE/MDM erase-install; legacy: as org allows | Map decision tree | Provide Genned serial / boarding pass fraud |
| Config | Configuration profiles, scripts you own | Outline | Spyware / credential theft |

Still macOS as Apple ships it — no “macOS Pro cracked” rebrand.

---

## Companion resources

| Resource | Use |
|----------|-----|
| `knowledge/macos/bootable-installer.md` | createinstallmedia steps & commands |
| `knowledge/macos/reinstall-and-recovery.md` | Recovery / when USB not needed |
| `windows-install-prep` | Contrast Windows MCT path (different OS) |
| `privacy-host-map` | apps.apple.com / swcdn.apple.com style hosts if mapping |
| `legal-playbook` | Org software license notes if present |

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| Consumer / admin bootable USB plan | **bootable-installer-plan** |
| Pick recovery vs USB vs upgrade | **method-chooser** |
| Terminal createinstallmedia guidance | **createinstallmedia-guide** |
| Boot from USB (silicon vs Intel) | **boot-from-installer** |
| Preflight backup & volume check | **preflight-checklist** |
| Post-install baseline (high level) | **post-install-baseline** |
| Refuse piracy / non-Apple hardware | **refuse-piracy** |
| Persist org notes (no secrets) | **write-knowledge** |
| Short answer | **brief** |

Default: **method-chooser** if unclear; **bootable-installer-plan** if USB requested; **refuse-piracy** for Hackintosh, cracked installers, or redistributing Apple media.

---

## method-chooser

**Output:**
1. Verdict — upgrade / recovery / bootable USB / need model+version  
2. Why that method (Apple: USB not required for normal upgrade/reinstall)  
3. Next procedure  

---

## bootable-installer-plan

**Output:**
1. Verdict — ready / need compatible Mac to download / backup first  
2. Target macOS name (Tahoe, Sequoia, … — **user-stated or UNKNOWN**)  
3. Compatibility note: download from a Mac compatible with that version (Apple rule)  
4. USB size & **erase warning**  
5. Steps 1–8 from Path B  
6. Link to [support.apple.com/en-nz/101578](https://support.apple.com/en-nz/101578)  
7. Non-claims  

---

## createinstallmedia-guide

1. Confirm installer path: `/Applications/Install macOS <Name>.app`  
2. Confirm volume: `/Volumes/MyVolume` (or document rename)  
3. Paste **only** the command matching that version (from knowledge table; VERIFY LIVE on Apple Support — names change)  
4. `sudo` → admin password (no echo) → `Y` to erase  
5. Troubleshoot per Apple: invalid installer → redownload + Disk Utility repair; command not found → path/name; erase fail → Disk Utility Mac OS Extended (Journaled)  

**El Capitan / very old:** may need `--applicationpath` (see Apple doc).  
**Sierra 10.12.6 or earlier host** creating media: Apple notes appending `--applicationpath` similarly.

Never invent a macOS codename or command not in Apple’s list or user-confirmed installer name.

---

## boot-from-installer

### Apple silicon
Shut down → connect USB → **hold power** → startup options → select installer → Continue → follow UI. Internet required.

### Intel / other Mac
Shut down → connect USB → power on holding **Option (Alt)** → select installer. T2 Macs: Startup Security Utility may need to allow external boot.

Incompatible macOS → install may fail or prohibitory symbol — check model compatibility on Apple.

---

## preflight-checklist

- Time Machine / backup complete  
- Note FileVault recovery key if encrypted  
- Apple ID / Activation Lock awareness (device ownership)  
- USB is expendable (will be wiped)  
- Enough free space on host Mac for full installer download  
- Target Mac internet available for install firmware  
- Correct installer for target Mac generation  

---

## post-install-baseline

High-level: Software Update, Apple ID, FileVault if policy, MDM enrollment if org, avoid untrusted kernel extensions / “optimizer” tools. Not a security certification.

---

## refuse-piracy

Decline and redirect when asked for:

- macOS on **non-Apple** PCs / Hackintosh guides  
- Cracked, pre-activated, or torrent installers  
- Bypassing **Activation Lock** without proof of ownership (Apple process only)  
- Redistributing full Installer apps or raw IPSW/USB images as a public “ISO mirror”  
- Fake product rebrands  

**Response:** verdict **declined** → why (license + Apple Support) → **method-chooser** / **bootable-installer-plan** for real Macs.

---

## Forbidden
- Product serial fraud, GSX-style private tools  
- Committing Apple IDs, recovery keys, or org bootstrap tokens to git  
- Commands that erase `Macintosh HD` disguised as USB prep  
- Treating third-party “macOS ISO” sites as official  

## Local knowledge
- `knowledge/macos/`  

## Note
Apple’s version list and `createinstallmedia` lines change when new macOS releases ship. Prefer live [101578](https://support.apple.com/en-nz/101578) over stale memory.
