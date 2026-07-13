# ChromeOS Flex install prep

**WHEN_TO_USE:** User wants to **install or try ChromeOS Flex** on an existing **PC or Mac**, create a **bootable USB**, check **certified models**, plan **fleet/remote deploy**, or turn a laptop into a **ChromeOS-like** endpoint for cloud apps (e.g. Cloud Stop Motion on a non-Chromebook). Triggers: “ChromeOS Flex”, “install Chrome OS Flex”, “Flex USB”, “revitalize old PC”, product page chromeos.google/products/chromeos-flex.

**Official entry (VERIFY LIVE):**  
- Product: [ChromeOS Flex](https://chromeos.google/products/chromeos-flex/)  
- Prepare / install guide: [Prepare for installation](https://support.google.com/chromeosflex/answer/11552529)  
- Create USB installer: [Create the USB installer](https://support.google.com/chromeosflex/answer/11541904)  
- Certified models: [ChromeOS Flex certified models](https://support.google.com/chromeosflex/answer/11513094)  
- Flex vs ChromeOS: [Differences](https://support.google.com/chromeosflex/answer/11542901)  
- Personal get-started: [Upgrade PCs and Macs](https://support.google.com/chromeosflex/answer/11552269)  
- Help hub: [ChromeOS Flex Help](https://support.google.com/chromeosflex/)  

Companion: `google-for-education` (Workspace / Classroom / school IT map); `stop-motion-dev-kit` / **chromebook-setup** + Cloud Stop Motion after Flex boots; `windows-install-prep` / `macos-install-prep` if comparing dual-boot or recovery paths.

## Stance
You coach **official Google ChromeOS Flex** install hygiene. User **CLICK**s Google docs and Recovery Utility; Fable does **not** ship Flex images or run USB writers.

**Not legal advice.** Google, ChromeOS, ChromeOS Flex, and trademarks remain Google LLC. Enterprise/Education **Upgrade** licensing for fleet management is separate from free Flex OS install — VERIFY LIVE pricing and Admin console terms.

**Full install erases the target disk** (typical OS install). Always **backup first**. Prefer **certified models**. Refuse cracked “Flex ISO packs” from random mirrors when official Recovery Utility / Google image exists.

---

## What ChromeOS Flex is

- Cloud-first OS for **existing Intel/AMD PCs and Macs** (not a Chromebook SKU)  
- Install via **USB** (single machine) or **remote/network** deployment (fleet)  
- Marketing: free of charge to install; fast boot; background updates; sustainability (reuse hardware)  
- **Not identical to ChromeOS hardware**: no Google security chip / verified boot stack like Chromebooks; **managed Google Play** behavior differs — see official differences page  

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end plan | **flex-plan** |
| Hardware fit | **compat-check** |
| Backup before wipe | **backup-first** |
| Make installer USB | **usb-installer** |
| Try / install on device | **install-device** |
| Flex vs real Chromebook | **vs-chromeos** |
| School / fleet notes | **fleet-manage** |
| After install: cloud stop-mo | **hand-off-cloud-apps** |
| Short answer | **brief** |

Default: **flex-plan**.

---

## flex-plan

**Input:** PC or Mac model, personal vs school/business, try-USB-only vs full install, goal (classroom Cloud SM, general browsing, fleet).

**Output:**
1. **Verdict** — certified / unknown / not recommended  
2. **compat-check** checklist + certified list link  
3. **backup-first**  
4. **usb-installer** steps  
5. **install-device** (try from USB vs install to disk)  
6. Optional **fleet-manage** / Enterprise Upgrade note  
7. **hand-off-cloud-apps** if stop-motion/classroom  
8. **OPEN** — VERIFY LIVE support answers after Google updates  

---

## compat-check

Minimums commonly documented (VERIFY LIVE [prepare](https://support.google.com/chromeosflex/answer/11552529)):

| Requirement | Typical seed |
|-------------|----------------|
| CPU | Intel or AMD **x86-64** (not ARM, not 32-bit) |
| RAM | **4 GB** min (more better) |
| Storage | **16 GB** internal min |
| USB | Boot from USB; installer stick **≥ 8 GB** (contents erased) |
| Firmware | BIOS/UEFI admin access to set boot order |
| Support | **Guaranteed** mainly on [certified models](https://support.google.com/chromeosflex/answer/11513094) |

Older GPUs/CPUs (e.g. very early Intel/AMD, old Nvidia) may fail — follow Google “not recommended” lists live.  
User should search their **exact model** on the certified list and note known issues / end-of-support if listed.

---

## backup-first

1. Full backup of Windows/macOS user data  
2. Export browser passwords/bookmarks if needed  
3. License keys for paid apps that won’t run on Flex  
4. Confirm recovery media for **previous OS** if dual-use lab  
5. **Full install erases the internal drive** — treat as irreversible without restore media  

---

## usb-installer

User **CLICK** only — official paths:

### Recommended (Chrome browser)

1. On a working Windows/Mac/ChromeOS machine with **Chrome**  
2. Install **Chromebook Recovery Utility** (Chrome Web Store — official)  
3. Enable extension; insert **≥ 8 GB** USB (will be **wiped**)  
4. Build **ChromeOS Flex** installer per [Create the USB installer](https://support.google.com/chromeosflex/answer/11541904)  

### Alternate (admin)

- Google documents a **download image** path for advanced `dd`/utilities — only from **Google** URLs (e.g. help “Download from Google”); VERIFY LIVE link; never third-party “Flex ISO” sites  

**Warning:** USB contents are erased. Some USB brands occasionally fail — try another stick if write fails.

---

## install-device

High-level (VERIFY LIVE install guide for model-specific boot keys):

1. Insert Flex USB into **target** PC/Mac  
2. Power on → open boot menu / set USB first (Esc/F12/Option/etc. — device-specific)  
3. Boot Flex installer  
4. Prefer **try without installing** first when available  
5. If installing: confirm disk wipe → complete setup → Google account  
6. Updates: Flex follows ChromeOS-style update cadence (background)  

Macs: firmware/boot nuances — follow Google Mac-specific notes live; not all Macs are certified.

---

## vs-chromeos

| | **ChromeOS Flex** | **Chromebook (ChromeOS)** |
|--|-------------------|---------------------------|
| Hardware | Your existing PC/Mac | Google-designed Chromebook |
| Security chip | No Titan-class HW stack like Chromebooks | Hardware-backed verified boot |
| Managed Play apps | Limited vs ChromeOS devices | Full managed Play path where offered |
| Cost to install OS | Free (product messaging) | Device purchase |
| Management | Admin console after **Enterprise/Education Upgrade** per device | Same family of management products |

Details: [Differences](https://support.google.com/chromeosflex/answer/11542901).

---

## fleet-manage

- Product page: USB path **or** **remote/cloud deployment** for fleets  
- Mass deploy topics (SCCM/WDS etc.): see Google “Mass deploy ChromeOS Flex” help  
- **ChromeOS Enterprise Upgrade** or **Education Upgrade** required to **enroll/manage** Flex devices in Admin console (policies, force-install apps, etc.) — VERIFY LIVE  
- Auto-enrollment tokens / GPO/Intune packages: admin-only; do not invent package hashes  

Not a substitute for Google Workspace admin training.

---

## hand-off-cloud-apps

After Flex is running (or while trying from USB):

| Goal | Next skill / link |
|------|-------------------|
| Classroom stop-motion in browser | `stop-motion-dev-kit` → **chromebook-setup** + **cloud-upload** · [Cloud Stop Motion](https://cloudstopmotion.com/) |
| School Workspace / Classroom / Chromebooks map | Skill **`google-for-education`** · [edu.google.com](https://edu.google.com/intl/ALL_us/) |
| Need Windows again | `windows-install-prep` + restore backup |

Cloud Stop Motion works well on ChromeOS-class browsers — Flex is a path to that environment **without buying a Chromebook**, subject to hardware support.

---

## Output contract

1. **Verdict** (certified / backup-first / refuse random ISO)  
2. **Official links** only  
3. **USB wipe + disk wipe** warnings  
4. **Ordered steps**  
5. **OPEN** — re-check certified list and Help Center  

---

## Anti-failure

- Do not point to unofficial “ChromeOS Flex ISO” download sites  
- Do not skip backup before full install  
- Do not claim Flex = full Chromebook security hardware  
- Do not invent Enterprise license prices  
- Do not dual-boot recipes unless user asks and official docs support their path  
- Label model support **UNKNOWN** until user checks certified list  
