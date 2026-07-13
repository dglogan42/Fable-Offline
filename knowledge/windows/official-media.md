# Windows 11 — official install media (licensed)

**Skill:** `windows-install-prep`  
Microsoft product names and trademarks belong to Microsoft. **Not legal advice.**

---

## Primary CLICK

| Resource | URL |
|----------|-----|
| Windows 11 download / Media Creation Tool | [https://www.microsoft.com/software-download/windows11](https://www.microsoft.com/software-download/windows11) |

Use this page for:

1. **Installation assistant** (in-place upgrade path)  
2. **Create Windows 11 Installation Media** (Media Creation Tool → USB/ISO)  
3. **Download Windows 11 Disk Image (ISO)** when Microsoft offers direct ISO  

Always re-check the live page; options and builds (e.g. 24H2 / 25H2) change.

---

## License channels (overview)

| Channel | Typical use |
|---------|-------------|
| **Retail** | Boxed/digital key you purchased |
| **OEM** | License tied to device from manufacturer |
| **Digital license** | Entitlement bound to hardware / Microsoft account after genuine activation |
| **Volume** | Org agreements (Enterprise/Education etc.) — follow IT policy |

Fable does **not** supply keys. Store keys outside git.

---

## Consumer prep checklist

1. Confirm you are entitled to the **edition** you install (Home vs Pro, etc.).  
2. Backup files; export BitLocker recovery key if device is encrypted.  
3. Create media via **official** MCT/ISO only.  
4. Install; sign in; activate under **Settings → System → Activation**.  
5. Windows Update; restore data; reinstall apps from trusted sources.  

---

## About third-party / tokenized ISO links

Microsoft may serve ISOs from CDN hosts such as `software.download.prss.microsoft.com` with **time-limited** query signatures. Those links:

- **Expire**  
- Are **not** a permanent archive  
- Must not be re-hosted or rebranded as another product  

If a token URL fails, return to the evergreen software-download page and generate a fresh download.

---

## Product truth

| Claim | Reality for this skill |
|-------|------------------------|
| “Windows 12 Professional ISO” | **Not** a Microsoft consumer SKU in this playbook — decline rebrand |
| Windows 11 Pro/Home/Enterprise… | Real editions — use matching media + license |
| Custom image with org apps | Allowed under **your** license/tools — still Windows 11 |

---

## Cross-links

- DISM / unattend: `dism-unattend-hygiene.md`  
- Privacy of download hosts: map with `privacy-host-map` if auditing  
