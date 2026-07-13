# Fitness companion framework

**Skill:** `fitness-companion-agent`  
**Built from:** MyFitnessPal product dump, PhysiotherapyExercises.com homepage dump, Health NZ Find a service, NZ emergency routing.  
**Not medical, physiotherapy, or nutrition advice.**

---

## Purpose

Offline Fable mode that **companions** everyday fitness **process** (habits, logging literacy, safety routing) and **maps third-party tools** — without becoming a coach of record or a clinician.

---

## Tool map (from curated data)

### Consumer tracking — MyFitnessPal

| Field | Seed |
|-------|------|
| Site | [myfitnesspal.com](https://www.myfitnesspal.com/) |
| Role | Calorie / macro / food / exercise logging; BMR calculator marketing |
| Stack seed | Next.js, Inter, brand `#0066EE`, release v21.9.1 homepage |
| Premium seeds | Ad-free, custom macros, barcode, meal scan, voice log, fasting, multi-day, insights |
| Integrations | 40+ apps/devices (marketing); Trainerize / GymEngine widget origins |
| Privacy | Heavy third-party: GTM, CMP (TrustArc/Sourcepoint), Amplitude, ads, Datadog, Stripe pk |
| Skill | `myfitnesspal-resource-kit` |
| Notes | `knowledge/health/myfitnesspal.md` · hosts `knowledge/privacy/myfitnesspal-hosts.md` |

### Clinician booklets — PhysiotherapyExercises.com

| Field | Seed |
|-------|------|
| Site | [physiotherapyexercises.com](https://www.physiotherapyexercises.com/) |
| Role | Search exercise DB → select → **professional patient booklets** |
| Marketing | 1500+ exercises; 5000+ drawings/photos; injuries & disabilities |
| Locale dump | `data-country=NZ`, `data-defaultculture=en-AU` |
| Feeds | `/exercise/rss`, `/exercise/atom` |
| Stack | SPA `ptx-main`, JS data packs, `/ExerciseImages/` |
| Privacy | First-party + GA `UA-20604563-1` + Cloudflare Insights |
| Skill | `physiotherapy-exercises-resource-kit` |
| Notes | `knowledge/health/physiotherapy-exercises.md` · hosts `knowledge/privacy/physiotherapyexercises-hosts.md` |

### Health navigation — Health NZ (Aotearoa)

| Field | Seed |
|-------|------|
| Page | Find a service (hospitals, GP, pharmacy, etc.) |
| Emergency | **111** · Healthline for non-emergency advice |
| Skill | `emergency-services-agent` |
| Notes | `knowledge/health/healthnz-find-a-service.md` |

---

## Decision tree (companion)

```text
User asks for fitness help
  ├─ Life-threatening symptoms? → 111 / emergency-services-agent
  ├─ Pain, injury, post-op, disability rehab?
  │     ├─ User is clinician → physio booklet workflow (HITL on site)
  │     └─ User is patient → stop DIY exercise Rx → clinician + Health NZ map
  ├─ Food / calorie / macro logging?
  │     └─ MFP process map + goals hygiene (user owns numbers)
  └─ General habit / movement?
        └─ companion-loop (user-defined goals, one habit, review cadence)
```

---

## Contrast table

| Dimension | MyFitnessPal | PhysiotherapyExercises.com |
|-----------|--------------|----------------------------|
| Primary user | Consumer | Clinician (for patient handouts) |
| Core job | Log food/exercise, goals | Search/select exercises → booklet |
| Fable role | Process + privacy map | Booklet workflow map + patient hygiene |
| Risk if misused | Extreme deficits, ED triggers | DIY rehab from clinical library |
| Data in git | Never full diaries | Never patient booklets / bulk media |

---

## Companion loop template

```text
1. Intent (user words)
2. Injury screen (yes → injury-route)
3. One habit this week
4. Log surface (app HITL)
5. Review date
6. Stop rules (pain / red flags)
```

Scaffold:

```text
workspace/health/fitness-companion/
  notes.md
  tools.md
```

Sensitive material → `knowledge/health/_local/` (gitignored patterns apply).

---

## Privacy classes (summary)

| Class | Examples |
|-------|----------|
| LOAD | App CDNs, GA/GTM, Cloudflare beacon |
| CONFIG | CMP, public API hosts, og:url alternate hosts |
| CLICK | User login, goal set, booklet export, device link |
| Never commit | Session cookies, food diaries, patient IDs, clinical PDFs |

---

## OPEN / VERIFY LIVE

- App feature lists and Premium offers change  
- Physio multi-language and export formats  
- UA → GA4 migration on physio site  
- Local emergency numbers outside NZ  
