# Deep-explain framework (offline math agent)

**Skill:** `math-physics-agent` · procedure **deep-explain**  
**Purpose:** Structured, bottom-up lessons as **durable markdown**, not ephemeral chat only.

---

## Design goals

| Goal | Practice |
|------|----------|
| Bottom-up | Prerequisites → intuition → formal → example |
| Checkable | Each step is definition, theorem application, or calculation |
| Durable | Save under `workspace/lessons/` or `memory/lessons/` |
| Agent-friendly | Slash intent `/deep-explain`; loops fill one section per cycle |

---

## Lesson skeleton

```markdown
# Deep explain — <topic>
## Learning objective
## Prerequisites
## Intuition
## Formal setup
## Development
## Worked mini-example
## Common mistakes
## Exercises
## Further reading
```

---

## Quality bar

- [ ] Symbols defined before use  
- [ ] No unexplained jumps  
- [ ] Mini-example re-computable by hand  
- [ ] Mistakes section names real failure modes  
- [ ] Artifact path suggested  

---

## Cross-links

- Theorem mode: `theorem-framework.md`  
- Physics: `../physics/solver-framework.md`  
- Numbers: skill `rederive-numbers`  
