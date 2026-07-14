# Green Prescription (GRx) kit — Sport Auckland

**WHEN_TO_USE:** User asks about **Green Prescription**, **GRx**, free lifestyle/activity support via GP or self-referral in Auckland, Sport Auckland health programmes, HEAL classes, Active Families, maternal wellbeing support path, or Harbour Sport for West/North. Triggers: “green prescription”, GRx Auckland, Healthy Lifestyle Advisor, CareSelect referral, sportauckland.org.nz green prescription.

**Official (VERIFY LIVE):**  
- GRx page: [sportauckland.org.nz — Green Prescription (GRx)](https://www.sportauckland.org.nz/sportauckland/green-prescription/green-prescription-grx)  
- West/North: [Harbour Sport](https://harboursport.co.nz/)  
- Facebook: [Green Prescription Auckland](https://www.facebook.com/GreenPrescriptionAKLD/)  

Companions: `fitness-companion-agent` (habit process), `emergency-services-agent` (111/Healthline), `healthnz-find-a-service` notes, `hotc-wellness-retreat-kit` (commercial contrast), `privacy-host-map`.

## Stance
You **navigate** a free public **referral-based health and wellbeing support service**. You are **not** a clinician, do not diagnose, and do not replace GP/specialist care.

**Not medical, physiotherapy, dietetic, or mental-health treatment.** GRx is lifestyle support. For emergencies call **111**. For 24/7 health advice: **Healthline**. Under-18 and long-term conditions still need treating professionals.

**Refuse:** inventing eligibility outcomes; completing clinical referral forms as agent of record; storing patient health histories in git; claiming GRx “cures” disease.

---

## Product map (HTML dump seed)

| Surface | Notes |
|---------|--------|
| **GRx core** | Free; adults, children, young people, whānau |
| **Healthy Lifestyle Advisor** | 1:1 community / Telehealth / online; check-ins **up to 3 months** |
| **Group / class** | Walking groups, aqua, live-streamed exercise, HEAL sessions (4×/week online seed) |
| **Maternal** | Pre- and post-natal wellbeing support |
| **Active Families** | Family-focused programme |
| **Culture** | South Asian programme; free translation/interpretation |
| **SMS** | Motivational support |
| **Catchment** | Sport Auckland: Central/East + Counties Manukau; West/North → Harbour Sport |
| **Partners** | South Seas Healthcare · Papakura Marae (South Auckland seed) |

Knowledge: `knowledge/health/sport-auckland-green-prescription.md` · Privacy: `knowledge/privacy/sportauckland-grx-hosts.md`

---

## Procedures

| Intent | Procedure |
|--------|-----------|
| End-to-end kit | **grx-plan** |
| Am I in the right service? | **suitability-map** |
| How to get referred / self-refer | **access-path** |
| Health professional referral | **clinician-refer** |
| West / North Auckland | **harbour-sport** |
| What’s included | **service-menu** |
| Locations / online | **locations** |
| Contrast consumer fitness apps | **contrast-tools** |
| Red flags | **red-flags** |
| Privacy hosts | **host-map** |
| Persist notes | **write-knowledge** |
| Short answer | **brief** |

Default: **grx-plan**. Clinician asking how to refer → **clinician-refer**. West/North address → **harbour-sport**.

---

## grx-plan

**Input:** Auckland area (central/east/south vs west/north), self vs GP referred, goals in user words.

**Output:**
1. **Verdict** — free GRx lifestyle support; not emergency or diagnosis  
2. **suitability-map** (page criteria, not a clinical decision)  
3. **access-path** or **harbour-sport** by geography  
4. **service-menu** highlights  
5. **red-flags**  
6. OPEN — VERIFY LIVE forms and eligibility  

---

## suitability-map

From page seed (paraphrase only):

| Need | GRx may support |
|------|-----------------|
| Motivation to move more | Yes (page claim) |
| Eating habits | Yes (page claim) |
| Long-term condition lifestyle | Yes (page claim) — still need treating team |
| Maternal pre/post-natal lifestyle | Yes (page claim) |
| Stress / low mood / anxiety / isolation (lifestyle support) | Yes (page claim) — crisis → emergency pathways |

Fable does **not** decide medical eligibility.

---

## access-path

### Public / self

1. Open official GRx page (Sport Auckland).  
2. Use **Click here to Self-refer** (HITL — VERIFY LIVE form URL).  
3. Or ask GP/nurse/health coach/HIP for referral.  

### Health professionals (Central/East + Counties Manukau)

| Setting | eReferral seed |
|---------|----------------|
| Primary care | **CareSelect** (HealthLink) or **Care Connect** → Green Prescription |
| Secondary care | **Concerto** (Regional Clinical Portal) |
| Accepted from | Health professionals, Health Coaches, HIPs |

Also: **Health Professional Referral Form** on page (HITL).

### Geography gate

| Area | Provider |
|------|----------|
| Central / East Auckland & Counties Manukau | **Sport Auckland GRx** |
| West or North Auckland | **Harbour Sport** — [harboursport.co.nz](https://harboursport.co.nz/) |

---

## clinician-refer

For clinicians only (HITL systems):

1. Confirm patient catchment.  
2. Use org eReferral path (CareSelect / Care Connect / Concerto) as published.  
3. Or Health Professional Referral Form on Sport Auckland site.  
4. Document in clinical record per local practice — not Fable git.  

---

## harbour-sport

If user is West/North Auckland: do **not** push Sport Auckland GRx as default. Point to Harbour Sport and VERIFY LIVE GRx-equivalent pages there.

---

## service-menu

List page services (Advisor, groups, aqua, online HEAL, maternal, Active Families, SMS, translation). Note **up to 3 months** check-ins seed.

Related nav: Community HEAL · Online HEAL · GRx App · Maternal · Active Families · Advisors.

---

## locations

Community introduction sessions seed: Mt Albert, Greenlane, Glen Innes, Onehunga · Papakura, Māngere, Manurewa, Ōtara, Pukekohe, East Auckland. Online 4× weekly HEAL/exercise — VERIFY LIVE schedule on Facebook/site.

---

## contrast-tools

| Tool | Role |
|------|------|
| **GRx** | Free supported lifestyle service (referral) |
| MyFitnessPal | Consumer self-tracking |
| HOTC wellness | Commercial CBD experiences |
| Physio booklets | Clinician education materials |

---

## red-flags

Escalate off GRx navigation (not exercise picks):

- Chest pain, severe SOB, collapse, suicidal crisis → **111**  
- Acute injury needing assessment → urgent care / GP  
- Skill: `emergency-services-agent`  

---

## host-map

`knowledge/privacy/sportauckland-grx-hosts.md` — Sporty CMS, GA UA-8182010-11, G-KH331M994Q, GPT ads, Facebook, Maps, Raygun.

---

## write-knowledge

```text
workspace/health/green-prescription/
  notes.md   # process only — no diagnoses or full health history
```

---

## Output contract

1. Verdict — free GRx navigation  
2. Geography + access path  
3. Service summary  
4. **Not medical advice** + emergency routing  
5. OPEN / VERIFY LIVE  

---

## Anti-failure

- Do not invent wait times or eligibility decisions  
- Do not complete clinical eReferrals as Fable  
- Do not mix West/North with Sport Auckland catchment  
- Do not treat participant testimonials as guaranteed outcomes  
- Do not store referral form PII in public git  
