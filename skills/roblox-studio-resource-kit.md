# Roblox Studio resource kit

**WHEN_TO_USE:** User wants **Roblox Studio** setup, system requirements, install, first-project orientation, Studio UI/tools map, update/beta hygiene, or education-lab notes for creating experiences. Triggers: “Roblox Studio”, “create.roblox.com”, “install Studio”, “Roblox developer”, Luau scripting start.

**Official docs (VERIFY LIVE):**  
- [Roblox Studio setup](https://create.roblox.com/docs/studio/setup) · [markdown for agents](https://create.roblox.com/docs/en-us/studio/setup.md)  
- [Studio overview](https://create.roblox.com/docs/studio)  
- [UI overview](https://create.roblox.com/docs/studio/ui-overview)  
- [Script Editor](https://create.roblox.com/docs/studio/script-editor) · [Debugging](https://create.roblox.com/docs/studio/debugging)  
- [Testing modes](https://create.roblox.com/docs/studio/testing-modes) · [Output](https://create.roblox.com/docs/studio/output)  
- [Explorer](https://create.roblox.com/docs/studio/explorer) · [Properties](https://create.roblox.com/docs/studio/properties)  
- [Terrain Editor](https://create.roblox.com/docs/studio/terrain-editor) · [Plugins](https://create.roblox.com/docs/studio/plugins)  
- Install curriculum tutorial: [Install Studio](https://create.roblox.com/docs/tutorials/curriculums/studio/install-studio)  
- Education FAQ (Studio **not** on Chromebooks/mobile for creation): [Education FAQ](https://create.roblox.com/docs/education/resources/frequently-asked-questions-education)  
- Creator Hub: [create.roblox.com](https://create.roblox.com/) · Docs index: [llms.txt](https://create.roblox.com/docs/llms.txt)  
- Account: [roblox.com](https://www.roblox.com/) · [Terms](https://www.roblox.com/info/terms) · [Privacy](https://www.roblox.com/info/privacy)  

Companions: `3d-animation-dev-kit` (general CG concepts), `minecraft-education-resource-kit` (parallel game-based learning), `google-for-education` (assign classroom briefs), `prompt-generator` (agent system prompts for Luau workflows — optional).

## Stance
You coach **official Roblox Studio** setup and creator workflow checklists. Studio is **free** per Creator Hub (VERIFY LIVE). Fable does **not** install Studio, publish experiences, or store Roblox account cookies/passwords.

**Not legal, educational, or financial advice.** Roblox marks remain Roblox Corporation. Follow [Terms](https://www.roblox.com/info/terms), age requirements, and school policies. User **HITL** for install, sign-in, publish, and monetization.

**Refuse:** cracked Studio, account stealers, exploiting games, phishing “free Robux”, or committing API keys / `.rbxl` secrets / under-13 personal data.

---

## What Roblox Studio is

Free **Windows/Mac** app to build, script, test, and publish **3D experiences** to the Roblox platform (consoles, desktop, mobile players). Bundled with the Roblox engine that powers the player app. Every experience runs on the **latest engine** — keep Studio updated.

Knowledge: `knowledge/media/roblox-studio.md`

---

## Kit map

| Piece | Role |
|-------|------|
| **Setup doc** | Sysreqs + install steps |
| **Roblox account** | Required to sign into Studio |
| **Explorer / Properties** | Hierarchy and object settings |
| **Script Editor** | Luau scripts |
| **Testing modes** | Play solo / multiplayer-style test |
| **Terrain / materials / rigs** | Build tools family |
| **Plugins** | Extend Studio |
| **Publish** | Ship experience to Roblox (HITL) |

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end resource kit | **rs-plan** |
| Hardware fit | **sysreq-check** |
| Install Studio | **install-studio** |
| First open / sign-in | **first-launch** |
| Customize UI | **customize-studio** |
| Keep current | **update-studio** |
| Optional betas | **beta-features** |
| First place / hello world | **hello-place** |
| Tool orientation map | **studio-tools-map** |
| School / lab notes | **education-lab** |
| Hand off publish / social | **publish-handoff** |
| Short answer | **brief** |

Default: **rs-plan**. New user: **sysreq-check** → **install-studio** → **first-launch** → **hello-place**.

---

## rs-plan

**Input:** OS (Win/Mac), RAM, school vs hobby, prior 3D/scripting experience.

**Output:**
1. **Verdict** — machine OK / upgrade RAM / wrong device (Chromebook/mobile)  
2. **sysreq-check** table  
3. **install-studio** steps with official links  
4. **first-launch** + account  
5. **hello-place** or **studio-tools-map**  
6. **update-studio** / **beta-features** notes  
7. **education-lab** if classroom  
8. **OPEN** — VERIFY LIVE docs after Roblox updates  

---

## sysreq-check

From official [setup](https://create.roblox.com/docs/studio/setup#system-requirements) (VERIFY LIVE):

| Spec | Minimum | Recommended |
|------|---------|-------------|
| OS | Windows **10** · macOS **10.14** | Windows **11** · macOS **14+** |
| RAM | **3 GB** | **8 GB** |
| Resolution | — | **1600×900** or higher |

**Not supported for Studio creation (education FAQ seed):** Chromebooks, smartphones/tablets as Studio hosts — need **PC or Mac** + consistent internet (updates + cloud save to account).

Linux: player/client support differs; Studio path is Win/Mac per setup doc.

---

## install-studio

User **CLICK** only — official path:

1. Open [Roblox Studio setup](https://create.roblox.com/docs/studio/setup)  
2. Use **Download Studio** (on-page button / Creator Hub flow)  
3. In dialog, click **Download Studio** again  
4. Run installer from browser downloads:  
   - Windows: `RobloxStudio.exe`  
   - Mac: `RobloxStudio.dmg`  
5. On confirmation, **Launch Studio**  
6. Sign in with [Roblox account](https://www.roblox.com/) (create if needed)  

Refuse unofficial “Studio free download” mirrors.

---

## first-launch

1. Complete sign-in  
2. Open or create a new place/experience  
3. Locate **Explorer**, **Properties**, viewport  
4. Optional: dark/light theme via Studio Settings (**Alt+S** Win / **⌥S** Mac — search “theme”)  
5. Confirm internet for updates  

---

## customize-studio

Per setup doc:

- Toolbar: custom tabs, reorganize/hide tools — [UI overview](https://create.roblox.com/docs/studio/ui-overview#toolbar-and-mezzanine)  
- Window layout customization  
- **File → Customize Shortcuts** for keybinds  
- **Studio Settings** search for known options  

---

## update-studio

- Experiences run on **latest engine**; outdated Studio risks missing APIs  
- If **Update** appears upper-right: save/close place → update → restart  
- Prefer stable updates for class; optional betas separately  

---

## beta-features

1. **File → Beta Features**  
2. Enable desired betas → **Save** → restart Studio  
3. Do not enable experimental betas on exam/production class days without testing  

---

## hello-place

Minimal first creation:

1. New Baseplate (or template)  
2. Insert a Part; move/scale in viewport  
3. Open **Output** window; note errors  
4. Insert a **Script** under ServerScriptService; `print("Hello")` on run  
5. **Play** (testing mode) → stop  
6. Save to Roblox (account cloud) — user HITL  

---

## studio-tools-map

Point users to official docs (do not invent UI labels that may change):

| Area | Doc |
|------|-----|
| Build | Align, Pivot, Terrain, Material/Texture/Rig generators |
| Script | Script Editor, Debugging |
| Test | Testing modes, Output, Developer Console |
| Hierarchy | Explorer, Properties, Experience/Avatar settings |
| Extend | Plugins, Studio widgets |
| AI assist | [Assistant guide](https://create.roblox.com/docs/assistant/guide) (VERIFY LIVE) |
| Advanced | [MCP server](https://create.roblox.com/docs/studio/mcp) (VERIFY LIVE) |

---

## education-lab

From [Education FAQ](https://create.roblox.com/docs/education/resources/frequently-asked-questions-education) seed:

1. Creation needs **PC/Mac** (not Chromebook Studio)  
2. Internet for updates and account save  
3. Install once; auto-update model  
4. Assign class briefs via `google-for-education` if school uses Classroom  
5. Age/account rules: school policy + Roblox terms  
6. No student passwords in Fable  

---

## publish-handoff

| Step | Note |
|------|------|
| Save to Roblox | Account-bound; HITL |
| Publish experience | Follow Studio publish UI + ToS |
| Age ratings / privacy | Roblox policies VERIFY LIVE |
| Portfolio | Screenshots + place link in school Drive — not git |

---

## Output contract

1. **Verdict** first  
2. **Sysreq + OS** clarity  
3. **Official install steps** only  
4. **Next learning path** (hello-place or docs map)  
5. **OPEN** — re-check create.roblox.com after updates  
6. No Robux scams; no exploit advice  

---

## Anti-failure

- Do not recommend Studio on Chromebook for **creation** (FAQ)  
- Do not invent Luau API without pointing to current docs  
- Do not store `.ROBLOSECURITY` cookies or API keys  
- Do not commit large `.rbxl` / place files to public git without review  
- Label guesses when Studio UI renames tools  
