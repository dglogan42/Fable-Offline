# Cloud Stop Motion — offline notes (Chromebook · browser · cloud)

**Skill:** `stop-motion-dev-kit` (cloud / Chromebook procedures)  
**Product (VERIFY LIVE):** [cloudstopmotion.com](https://cloudstopmotion.com/)  
**App entry:** [app.cloudstopmotion.com](https://app.cloudstopmotion.com)  
**Why cloud:** [Why the cloud](https://cloudstopmotion.com/pages/why-the-cloud)  
**Schools:** [Education](https://cloudstopmotion.com/pages/cloud-stop-motion-in-education) · [Org console](https://cloudstopmotion.com/pages/org-console) · [Pricing](https://cloudstopmotion.com/pages/pricing) · [COPPA / safety](https://cloudstopmotion.com/pages/coppa-compliance)  

Not product endorsement. Plans, free tiers, and UI labels change — re-check live.

---

## What it is

**Cloud Stop Motion** is a **browser-based** stop-motion tool aimed at **school and home** use:

- Runs on **Chromebook**, tablet, laptop, desktop — **nothing to install** (also installable as app on some devices)  
- **Projects stay in the vendor cloud** (frames, edits, audio per marketing)  
- Start on one device, continue on another after sign-in  
- Schools: users/groups, review projects, **export finished work**, org admin  

Companion **desktop/mobile** product family: Stop Motion Studio (Cateater) — `stop-motion-studio.md` — often **on-device** projects with optional file transfer.

---

## Chromebook / ChromeOS Flex path (seed)

**Hardware options:** real Chromebook **or** PC/Mac with **ChromeOS Flex**  
([chromeos.google/products/chromeos-flex](https://chromeos.google/products/chromeos-flex/) · skill `chromeos-flex-install-prep`).

```text
1. Device online + camera permission in browser
2. User CLICK https://app.cloudstopmotion.com (or Start Free from site)
3. Sign in / school account (per plan)
4. New project → capture frames (webcam / allowed camera)
5. Auto cloud save (vendor cloud — not Fable)
6. Edit, sound, optional green screen (blog tutorials)
7. Export finished movie + optional download masters to Files app
8. Optional: school admin reviews/exports via org console
9. Local handoff: copy export to workspace/creative/<slug>/04_exports/ if using Fable PC
```

**“Upload to cloud”** in this kit means: **use Cloud Stop Motion so project data is stored by the service**, and/or **export finished work** that teachers/admins can pull from the **organization console**. It does **not** mean Fable uploads files for the user.

---

## Cloud vs local (comparison seed)

| | **Cloud Stop Motion** | **Stop Motion Studio** |
|--|----------------------|-------------------------|
| Install | Browser / PWA-style; no classic desktop install | Native apps (Win/Mac/mobile stores) |
| Project storage | Vendor **cloud** (sign-in) | Typically **on device** + optional transfer |
| Chromebook | Primary classroom fit | Android/Chrome OS availability varies — VERIFY LIVE |
| School admin | Users, groups, review, export | Classroom notes exist; different product |
| Offline capture | Needs connectivity model of product — VERIFY LIVE | Strong offline once installed |

---

## Blog / tutorial seeds

Base hub: [cloud-stop-motion-hub](https://cloudstopmotion.com/blogs/cloud-stop-motion-hub)

| Topic | Notes |
|-------|--------|
| Org console (schools) | 10-step admin guide for users/roles/projects/storage |
| Green screen / chroma | Cloud Stop Motion chroma key tutorial |
| Recording sound | VO/SFX steps; export when done |
| Gallery | [stopmotiongallery.com](https://stopmotiongallery.com/) moderated examples |

---

## Privacy & school policy

- Student work in a **third-party cloud** — follow school/parent consent, COPPA/age rules, and district policies  
- Site pages claim safety/compliance tooling — **VERIFY LIVE**  
- Do **not** put school admin passwords or student PII into Fable memory/git  
- Prefer school-managed accounts over personal accounts for class work  

---

## Hardware

Optional shop items (e.g. HD Animation Webcam) — VERIFY LIVE product page pricing.  
Chromebook built-in cam is enough for many class shorts; tripod still recommended for registration.

---

## Fable scaffold add-ons

```text
workspace/creative/<slug>/
  02_cloud_exports/   # movies downloaded from Cloud SM / teacher export
  05_presets/
    cloud-notes.md    # account type, school org?, FPS, export formats used
  notes.md
```

Never commit cloud session cookies, org API keys, or full student rosters.
