# macOS reinstall & recovery (when USB is optional)

**Skill:** `macos-install-prep`  
Companion to [bootable installer (101578)](https://support.apple.com/en-nz/101578).  
**VERIFY LIVE** on Apple Support — recovery key chords and internet requirements vary by chip.

---

## Method chooser (summary)

| Situation | First try (official) |
|-----------|----------------------|
| Upgrade only | Software Update / [upgrade macOS](https://support.apple.com/en-nz/108382) |
| Reinstall same/compatible OS | [macOS Recovery](https://support.apple.com/en-nz/102655) / Internet Recovery |
| Multiple machines / recovery failed | [Bootable installer](https://support.apple.com/en-nz/101578) |
| Download options overview | [How to download and install macOS](https://support.apple.com/en-nz/102662) |
| Other methods | [macOS installation methods](https://support.apple.com/en-nz/102662) (and related) |

Apple states you **do not need** a bootable installer solely to upgrade or reinstall.

---

## Recovery hygiene (high level)

1. **Backup first** (Time Machine or clone).  
2. Know **FileVault** recovery key if disk is encrypted.  
3. Confirm **device ownership** (Activation Lock / Find My).  
4. Prefer wired power; stable network for Internet Recovery.  
5. Erase only after backup and ownership confirmed.  
6. After install: Software Update, restore data, MDM if org-owned.

Exact key combinations (Command-R, Option-Command-R, power-button hold on silicon, etc.) — **follow live Apple articles for your Mac model**; do not invent chords.

---

## Compatibility

- Installer must support the **target Mac model**.  
- Prohibitory symbol / failed install often means incompatible OS ([Apple](https://support.apple.com/en-nz/101666)).  
- Download full installer from a Mac compatible with that macOS version when Apple requires it.

---

## Enterprise note

Administrators: obtain installers from **Apple**, not only an internal caching server, when creating bootable media (per 101578).

---

## Cross-links

- USB steps & commands: `bootable-installer.md`  
- Windows contrast: `knowledge/windows/official-media.md`  
