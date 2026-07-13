# Offline loop protocol (shared)

**Consumers:** Hermes, Fable `/loop` `/engineer`, `offline_goal_loop.py`.

A **prompt** is one instruction. A **loop** is a goal the agent keeps working until a **verifier** and **stop** say stop.

## Three make-or-break parts

| Part | Rule |
|------|------|
| **Verifier** | Separate check (fresh context when possible). Maker ≠ final grader. |
| **State** | Record tried / failed / next so tomorrow resumes. |
| **Stop** | Success gate **or** hard limit (max cycles / retry ceiling). Never infinite spend. |

## Five beats (every cycle)

1. **Find the work** — Goal + state → one next concrete unit  
2. **Do it** — Produce the artifact (one bounded change preferred)  
3. **Check** — Verifier / self-check against success criteria  
4. **Remember** — Write state + memory notes  
5. **Go again or stop** — On FAIL: repair strategy, do not repeat blindly  

## Honesty

- Do not claim FINAL without evidence  
- Do not weaken success criteria to pass the gate  
- Small samples: prefer “insufficient evidence” over fake confidence  
- Prefer checkable claims over narrative polish  

## When NOT to loop

One-shot questions, vague goals (“make life better”), pure brainstorming — use chat instead.

## Related

- `program.md` — engineer constraints  
- `SOUL.md` — identity / Hermes ethics  
- Skills: `hermes-loop`, `loop-engineer`  
