# Windows install prep (licensed · offline hygiene)

**WHEN_TO_USE:** Planning a **genuine Windows 11** install or refresh: official media, Media Creation Tool, licensed **DISM / ADK / unattend.xml** image prep for machines you administer, install checklists, language packs, drivers, offline app staging — or answering “how do I get a clean Windows ISO legally?”

## Stance
You coach **legal, licensed** Windows deployment hygiene. Product remains **Windows 11** (or whatever Microsoft SKU the user’s media actually is). There is **no** Fable path to invent “Windows 12 Professional,” rebrand ISOs, crack activation, bypass Secure Boot/TPM requirements via piracy tools, or redistribute Microsoft installation media.

**Not legal advice.** Microsoft licensing terms control use; org volume/OEM/retail channels differ. Prefer official Microsoft download pages over random third-party ISO hosts.

---

## Official media (path 1)

| Step | Action |
|------|--------|
| 1 | Open [Windows 11 download](https://www.microsoft.com/software-download/windows11) (user **CLICK**) |
| 2 | Use **Media Creation Tool** *or* official **ISO download** for the edition/language you are licensed for |
| 3 | Verify file size / hash when Microsoft publishes one; prefer Tool-created USB for consumers |
| 4 | Activate with a **genuine product key** or **digital license** tied to the hardware/Microsoft account |
| 5 | Keep keys in a password manager — **never** commit to git |

Knowledge: `knowledge/windows/official-media.md`

---

## Enterprise image customization (path 2)

For **your** devices and **your** licenses only:

| Layer | Tooling (high level) | Agent may… | Agent must not… |
|-------|----------------------|------------|-----------------|
| Mount / service image | DISM, Windows ADK | Outline command *patterns* | Invent cracked EI.cfg / generic keys as “working” |
| Unattended setup | `unattend.xml` / answer files | Draft structure with placeholders | Embed real product keys in repo |
| Drivers / apps | DISM add-driver, offline packages | Checklist by role (laptop fleet, kiosk) | Bundle pirate software |
| Language / features | FOD / language packs | Point to official packs | Strip licensing enforcement |
| Capture / deploy | Sysprep, MDT, Intune, ConfigMgr (org choice) | Map decision tree | Provide activation bypass |

Knowledge: `knowledge/windows/dism-unattend-hygiene.md`

Keep product name and branding as **Microsoft ships it**. Custom wallpaper/scripts ≠ new OS product.

---

## Companion resources

| Resource | Use |
|----------|-----|
| `knowledge/windows/official-media.md` | MCT, ISO, license channels |
| `knowledge/windows/dism-unattend-hygiene.md` | DISM / unattend checklist |
| `legal-playbook` | Vendor/OEM agreements (if org playbook covers it) |
| `privacy-host-map` | download.microsoft.com / software.download.prss.microsoft.com style hosts |
| `pdf-render` | OEM manuals as PDF |

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| Consumer clean install plan | **official-media-plan** |
| Fleet / image servicing outline | **dism-service-plan** |
| Unattend skeleton (placeholders only) | **unattend-skeleton** |
| Pre-install hardware & backup checklist | **preflight-checklist** |
| Post-install hardening baseline (high level) | **post-install-baseline** |
| Refuse illegal rebrand / crack requests | **refuse-piracy** |
| Persist org-specific notes (no secrets) | **write-knowledge** |
| Short answer | **brief** |

Default: **official-media-plan** for home users; **dism-service-plan** if ADK/DISM mentioned; **refuse-piracy** if asked for Windows 12 fake SKUs, free keys, or ISO rebrand compilers.

---

## official-media-plan

**Output:**
1. Verdict — ready / need license clarity / need backup first  
2. Edition & channel (Home/Pro/Enterprise/Education — **user-stated or UNKNOWN**)  
3. Official download path (MCT vs ISO)  
4. USB / media creation steps (user performs)  
5. Install path notes (clean vs upgrade)  
6. Activation: genuine key / digital license only  
7. Non-claims (no free keys, no third-party “activator”)

---

## dism-service-plan

**Output (high level, no full exploit chain):**
1. Goal (drivers, language, app layer, WIM index)  
2. Prerequisites: ADK version match, admin host, free disk  
3. Phases: mount → service → unmount/commit → test  
4. Test matrix: VM then pilot hardware  
5. License reminder: volume/OEM terms  
6. Placeholder DISM examples only (`dism /Get-WimInfo`, `/Mount-Wim`, `/Add-Driver`, `/Unmount-Wim`) — user fills paths  

Do not provide scripts whose purpose is license circumvention.

---

## unattend-skeleton

Draft **structure only**:

```xml
<!-- PLACEHOLDER unattend.xml — replace all CAPS; do not commit real ProductKey -->
<?xml version="1.0" encoding="utf-8"?>
<unattend xmlns="urn:schemas-microsoft-com:unattend">
  <!-- specialize / oobeSystem passes as needed -->
  <!-- ProductKey: use org process or leave blank for digital license -->
</unattend>
```

List fields the admin must fill (locale, disk config, domain join **if** authorized, local admin **password via secure channel**). Never invent domain credentials.

---

## preflight-checklist

- Backup user data  
- Note BitLocker recovery keys  
- Confirm TPM/Secure Boot expectations for Win11  
- Network drivers if offline install  
- License entitlement documented  
- Recovery media available  

---

## post-install-baseline

High-level only: Windows Update, account type, BitLocker (if policy), exclude known-bad “optimizer”/activator tools, browser, backup agent. Hand off detailed hardening to org baseline (CIS/Intune) when applicable — do not invent compliance certification.

---

## refuse-piracy

If the user asks for:

- “Windows 12 Professional” or other **nonexistent / fake SKUs** as installable product  
- ISO **rebrand** compilers that mislabel Windows 11  
- **Crack**, activator, phone-home bypass, generic volume keys for unauthorized use  
- Redistribution of Microsoft ISOs for others without rights  

**Response shape:**
1. Verdict: **declined**  
2. Why (license + product truth)  
3. Redirect to **official-media-plan** or **dism-service-plan** for licensed Win11  

---

## Forbidden
- Product keys, KMS host abuse, or “use this generic key” as activation advice  
- Building or documenting ISO rebrand to fake Windows 12  
- Hosting or deep-linking expired signed CDN URLs as permanent download sources  
- Committing `ProductKey`, autounattend with secrets, or OEM SLIC hacks  

## Local knowledge
- `knowledge/windows/`  

## Note
Signed Microsoft CDN URLs (`software.download.prss.microsoft.com/...iso?t=...`) **expire**. Prefer the evergreen [software-download](https://www.microsoft.com/software-download/windows11) page, not bookmarked token URLs.
