# ChromeOS Flex — offline notes

**Skill:** `chromeos-flex-install-prep`  
**Product:** [chromeos.google/products/chromeos-flex](https://chromeos.google/products/chromeos-flex/)  
**Install / prepare:** [support.google.com/chromeosflex/answer/11552529](https://support.google.com/chromeosflex/answer/11552529)  
**USB installer:** [answer/11541904](https://support.google.com/chromeosflex/answer/11541904)  
**Certified models:** [answer/11513094](https://support.google.com/chromeosflex/answer/11513094)  
**Flex vs ChromeOS:** [answer/11542901](https://support.google.com/chromeosflex/answer/11542901)  

Google trademarks. VERIFY LIVE after releases. Not legal advice.

---

## Purpose

Install a **ChromeOS-like**, cloud-first OS on **existing PCs and Macs** (Intel/AMD x86-64) via USB or fleet remote deploy. Free-of-charge OS install per product messaging; **management upgrades** sold separately.

Use cases in Fable stack:
- Refresh aging Windows/Mac hardware  
- Classroom cloud browsers (e.g. Cloud Stop Motion) without purchasing Chromebooks  
- Compare to full Windows reinstall (`windows-install-prep`) or macOS recovery (`macos-install-prep`)  

---

## Minimum requirements (seed)

From Google prepare docs (re-verify):

- x86-64 Intel or AMD  
- 4 GB RAM  
- 16 GB internal storage  
- USB boot + ≥ 8 GB installer stick (USB **erased**)  
- BIOS/UEFI administrator access  

Official support: **certified model list** only guaranteed.

---

## Install paths

| Path | Summary |
|------|---------|
| **USB** | Chromebook Recovery Utility → Flex image on USB → boot target → try or install |
| **Remote deploy** | Windows package + policies/Intune/SCCM etc. for fleets (admin) |
| **Image download** | Advanced `dd` from **Google** image URL only (help “Download from Google”) |

**Full install wipes internal disk.**

---

## Flex vs Chromebook

- Flex: no Chromebook-class security chip / same HW integrations  
- Managed Google Play differs  
- Enroll/manage Flex devices needs **ChromeOS Enterprise or Education Upgrade** (per product FAQs)  

---

## Post-install handoff

| App / skill | Note |
|-------------|------|
| Cloud Stop Motion | Browser app — `knowledge/media/cloud-stop-motion.md` |
| stop-motion-dev-kit | chromebook-setup / cloud-upload after Flex boots |
| Google Workspace | Cloud profiles, offline Workspace features (product marketing) |

---

## Scaffold (optional notes only)

```text
workspace/chromeos-flex/<machine-slug>/
  notes.md          # model, certified Y/N, install date, account type
  # do not store recovery images or enrollment tokens in git
```

---

## Refuse

- Random third-party Flex ISOs  
- Skipping backup  
- Guaranteeing unsupported hardware  
