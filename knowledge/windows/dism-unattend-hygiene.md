# DISM / ADK / unattend — licensed image hygiene

**Skill:** `windows-install-prep`  
High-level deployment notes for admins customizing **genuine** Windows images they are licensed to use. **Not legal advice.** Not a full Microsoft Deploy Guide substitute — VERIFY LIVE on Microsoft Learn.

---

## When this applies

- Org or lab images for **owned** devices  
- Adding drivers, language packs, cumulative updates offline  
- Unattended setup answers (`unattend.xml`) without shipping secrets in git  

**Does not apply:** cracking, rebranding to fake OS names, unauthorized redistribution.

---

## Tooling map (names only)

| Tool | Role |
|------|------|
| **Windows ADK** | Assessment and Deployment Kit — imaging utilities aligned to target OS version |
| **DISM** | Service Windows images (WIM/ESD): mount, drivers, packages, features |
| **Oscdimg** / similar (ADK) | Build ISO from a **legally obtained** file set you may service |
| **Sysprep** | Generalize before capture (understand `/generalize` implications) |
| **MDT / ConfigMgr / Intune** | Org deployment stacks (choose per IT standard) |

Match ADK/DISM version guidance to the Windows build you service.

---

## DISM phase checklist (pattern)

1. **Inventory** — `Get-WimInfo` / list indexes; pick correct index (Pro vs Home, etc.).  
2. **Mount** — mount to an empty directory; watch free disk space.  
3. **Service** — add drivers, packages, enable features as policy requires.  
4. **Unmount** — commit or discard; never leave orphan mounts.  
5. **Test** — VM first, then pilot hardware, then broad deploy.  
6. **Document** — image version, packages, who approved.

Example shapes (paths are placeholders):

```text
dism /Get-WimInfo /WimFile:X:\path\install.wim
dism /Mount-Wim /WimFile:X:\path\install.wim /Index:N /MountDir:X:\mount
dism /Image:X:\mount /Add-Driver /Driver:X:\drivers /Recurse
dism /Unmount-Wim /MountDir:X:\mount /Commit
```

Run elevated; follow Microsoft docs for your build. Fable does not invent “working” generic product keys.

---

## unattend.xml hygiene

| Do | Don’t |
|----|--------|
| Use placeholders in git | Commit real `ProductKey` |
| Separate secrets (vault / deploy system) | Paste domain join passwords into knowledge/ |
| Minimize local admin password lifetime | Share one golden password in chat logs |
| Validate XML against ADK templates | Copy random internet autounattend “cracks” |

Skeleton fields admins usually decide: UI language, disk configuration, computer name pattern, domain/workgroup, OOBE privacy toggles, first logon commands **from signed org packages only**.

---

## Oscdimg / “ISO compiler” (licensed sense only)

Rebuilding an ISO after **legal** servicing of a Microsoft image you obtained officially is a normal enterprise step. Requirements:

1. Source media from Microsoft (or authorized channel).  
2. You have rights to deploy the resulting image.  
3. Branding and product name remain Microsoft’s.  
4. No bundled activators or license bypass tools.  

Fable **will not** help design an ISO toolchain whose purpose is fake “Windows 12” productization or piracy.

---

## Secrets layout (Fable repo)

| Path | Content |
|------|---------|
| `knowledge/windows/` | Curated public notes only |
| `knowledge/windows/_local/` | Org notes, key IDs **without** full keys (gitignored) |
| Password manager / escrow | Actual product keys |

---

## Cross-links

- Official media: `official-media.md`  
- Skill procedures: `windows-install-prep`  
