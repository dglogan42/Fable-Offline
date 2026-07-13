# MBTI types — agent personality customiser catalogue

**Skill:** `mbti-personality-customiser`  
**Code:** `mbti_types.py` (source of truth for prompts)  
**State:** `mbti_state.json` (local)  
**Runtime:** Fable5 `/mbti` · `--mbti` · `mbti_personality_agent.py`  

**Not a clinical instrument.** Style lenses for offline agents only.

---

## Commands (Fable5)

| Command | Effect |
|---------|--------|
| `/mbti` | Help + current |
| `/mbti list` | All 16 |
| `/mbti switch CODE` | Activate type |
| `/mbti CODE` | Same as switch |
| `/mbti current` | Show active + rigour |
| `/mbti off` | Clear (SOUL-only voice) |
| `/mbti rigour on\|off` | Accuracy overlay |
| `/mbti multi T1 T2 …` | Multi-lens next answer framing |

CLI: `python fable5_offline_agent.py --mbti INTJ`

---

## Type index

| Code | Name | Stack | Group |
|------|------|-------|-------|
| INTJ | Architect / Strategist | Ni-Te-Fi-Se | NT |
| INTP | Logician / Thinker | Ti-Ne-Si-Fe | NT |
| ENTJ | Commander / Executive | Te-Ni-Se-Fi | NT |
| ENTP | Debater / Visionary | Ne-Ti-Fe-Si | NT |
| INFJ | Advocate / Counselor | Ni-Fe-Ti-Se | NF |
| INFP | Mediator / Idealist | Fi-Ne-Si-Te | NF |
| ENFJ | Protagonist / Teacher | Fe-Ni-Se-Ti | NF |
| ENFP | Campaigner / Inspirer | Ne-Fi-Te-Si | NF |
| ISTJ | Logistician / Inspector | Si-Te-Fi-Ne | SJ |
| ISFJ | Defender / Protector | Si-Fe-Ti-Ne | SJ |
| ESTJ | Executive / Supervisor | Te-Si-Ne-Fi | SJ |
| ESFJ | Consul / Provider | Fe-Si-Ti-Ne | SJ |
| ISTP | Virtuoso / Craftsman | Ti-Se-Ni-Fe | SP |
| ISFP | Adventurer / Artist | Fi-Se-Ni-Te | SP |
| ESTP | Entrepreneur / Dynamo | Se-Ti-Fe-Ni | SP |
| ESFP | Entertainer / Performer | Se-Fi-Te-Ni | SP |

Full prose prompts live in `mbti_types.MBTI_TYPES[*]["prompt"]` — do not drift wiki text out of sync; edit the Python catalogue.

---

## Cognitive functions (quick map)

| Letter pair | Functions |
|-------------|-----------|
| N/S | Intuition vs Sensing (patterns vs concrete) |
| T/F | Thinking vs Feeling (criteria vs values/people) |
| J/P | Judging vs Perceiving (structure vs flexibility) |
| I/E | Introversion vs Extraversion (energy orientation) |

Stacks (e.g. Ni-Te-Fi-Se) order preferred mental moves for the lens.

---

## Suggested use by task

| Task | Try |
|------|-----|
| Long strategy | INTJ, ENTJ |
| Logic critique | INTP |
| Brainstorm | ENTP, ENFP |
| People/impact | INFJ, ENFJ, ESFJ |
| Process compliance | ISTJ, ESTJ |
| Hands-on debug | ISTP, ESTP |
| Aesthetic / values | INFP, ISFP |

---

## State schema seed

```json
{
  "current_type": "INTJ",
  "rigour_mode": true,
  "updated_at": "…",
  "history": [{"type": "INTJ", "at": "…"}]
}
```

`current_type: null` = no MBTI layer.

---

## Scaffold

```text
workspace/personality/
  preferred.md
  notes.md
```
