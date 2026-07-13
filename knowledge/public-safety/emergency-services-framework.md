# Emergency services agent — framework (NZ)

**Skill:** `emergency-services-agent`  
**Not medical, legal, or emergency-response advice.**

---

## Numbers (Aotearoa)

| Number | Use |
|--------|-----|
| **111** | Emergency — Police, Fire, or Ambulance |
| **105** | Police non-emergency (phone 24/7 + online paths) |
| **Healthline** | 24/7 health advice (use official Health NZ channels for current number/app) |

---

## Agency map

| Need | Primary channel | Knowledge seed |
|------|-----------------|----------------|
| Crime emergency | 111 Police | — |
| Crime non-emergency | 105 / police.govt.nz/use-105 | `nz-police-105.md` |
| Fire emergency | 111 Fire; get out stay out | `fenz-incident-reports.md` |
| Fire incidents / escape plan education | fireandemergency.nz | `fenz-incident-reports.md` |
| Health emergency | 111 Ambulance | — |
| Health service find | healthnz.govt.nz Find a service | `healthnz-find-a-service.md` |
| Health advice non-emergency | Healthline | Health NZ pages |

---

## Escape plan (FENZ education)

1. First escape route  
2. Second escape route  
3. Meeting place  
4. Get low · be fast · close doors · get out stay out  
5. Call 111 for FIRE when safe  

---

## Privacy seeds

- `knowledge/privacy/nz-police-105-hosts.md`  
- `knowledge/privacy/fenz-incident-reports-hosts.md`  
- `knowledge/privacy/healthnz-find-a-service-hosts.md`  

---

## Agent hard gate

```text
if immediate_danger or unclear_emergency:
    return "Call 111"
```
