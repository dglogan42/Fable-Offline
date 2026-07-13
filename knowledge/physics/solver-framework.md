# Physics guide & solver framework (offline)

**Skill:** `math-physics-agent` · procedure **physics-solve** / **dim-check**  
**Slash:** `/physics`  
**Purpose:** Conceptual support + derivations with a hard **dimensional analysis** gate.

---

## Solve pipeline

```text
Given / Find → diagram → dimensions gate → principles → derivation → number → limit check → answer
```

---

## Dimensional analysis gate

| Base (SI) | Symbol |
|-----------|--------|
| Mass | M |
| Length | L |
| Time | T |
| Current | I |
| Temperature | Θ |
| Amount | N |
| Luminosity | J |

Every additive term in an equation must share dimensions. If not → **FAIL** before final answer.

### Quick checks

| Quantity | Dimensions (typical) |
|----------|----------------------|
| Velocity | L T⁻¹ |
| Acceleration | L T⁻² |
| Force | M L T⁻² |
| Energy | M L² T⁻² |
| Power | M L² T⁻³ |
| Pressure | M L⁻¹ T⁻² |

---

## Principle tags (name one)

Newton II · energy conservation · momentum · angular momentum · Gauss/Ampère/Faraday · wave equation · thermo 1st law · Bernoulli (with assumptions) · …

State **which** principle justifies each major step.

---

## Answer hygiene

- SI units on final numeric answers  
- Significant figures honest to inputs  
- Vector direction if relevant  
- OPEN if data missing  

---

## Cross-links

- Math deep explain / theorem: `../math/`  
- Rederive: skill `rederive-numbers`  
