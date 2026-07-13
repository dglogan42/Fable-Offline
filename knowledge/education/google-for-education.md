# Google for Education — offline hub notes

**Skill:** `google-for-education`  
**Hub:** [edu.google.com/intl/ALL_us](https://edu.google.com/intl/ALL_us/)  
**Workspace editions:** [editions/overview](https://edu.google.com/intl/ALL_us/workspace-for-education/editions/overview/)  
**Compare:** [compare-editions](https://edu.google.com/intl/ALL_us/workspace-for-education/editions/compare-editions/)  
**Classroom:** [products/classroom](https://edu.google.com/intl/ALL_us/workspace-for-education/products/classroom/) · app [classroom.google.com](https://classroom.google.com)  
**Chromebooks:** [chromebooks/overview](https://edu.google.com/intl/ALL_us/chromebooks/overview/)  
**Flex companion:** [ChromeOS Flex](https://chromeos.google/products/chromeos-flex/) · `knowledge/chromeos/chromeos-flex.md`  

Google trademarks. VERIFY LIVE. Not educational or legal advice.

---

## Hub pillars (public site)

1. **Google Workspace for Education** — collaboration suite (Gmail, Drive, Docs, Meet, Classroom, Admin, …)  
2. **Chromebooks** — managed education devices  
3. **Google Classroom** — assignments, classes, collaboration  
4. **Gemini for Education** — AI features (edition/policy dependent)  

Audience routes: K-12 · Higher Education · Education Leaders · IT Admins · Educators.

---

## Workspace editions (seed)

Public FAQ-style messaging (re-check Compare Editions):

| Tier | Marketing seed |
|------|----------------|
| **Education Fundamentals** | Foundational tools often **no cost** — Classroom, Gmail, Calendar, Meet (limits), Drive (limits), Docs/Sheets/Slides/Forms |
| **Paid editions** (Standard, Plus, Teaching & Learning add-on, etc.) | Advanced security, analytics, enhanced features |
| **Trials** | Hub has mentioned 60-day trials of paid editions — VERIFY LIVE |

Do not hardcode quotas or prices.

---

## Classroom

- Create courses, distribute classwork, streamline assignments  
- Part of Workspace for Education  
- Teacher signs in with school account  
- Optional Gemini in Classroom where enabled  

---

## Devices

| Device path | Notes |
|-------------|--------|
| Chromebooks | Education SKUs, management policies |
| ChromeOS Flex | Install on existing PC/Mac — school fleet reuse |
| Admin | Chrome management + Workspace Admin console |

---

## Privacy (seed only)

Hub FAQ: Workspace for Education Core Services and Chrome services described as FERPA compliant; schools use Access Controls and Chrome policies.  
**Schools must still follow local law, contracts, and DPAs.** Not legal advice.

---

## Fable stack handoffs

| Goal | Skill / knowledge |
|------|-------------------|
| Install Flex on lab PCs | `chromeos-flex-install-prep` |
| Stop-motion on Chromebook/Flex | `stop-motion-dev-kit` + `cloud-stop-motion.md` |
| Meeting/Calendar hygiene | `calendar-mail-meetings` |
| Credential marketing audit | `education-claim-audit` (different use case) |

---

## Scaffold (notes only)

```text
workspace/education/<school-slug>/
  notes.md          # edition, domain, device plan — no student PII
```
