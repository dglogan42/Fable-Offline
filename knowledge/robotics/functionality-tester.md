# Robotics functionality tester — framework

**Skill:** `robotics-functionality-tester`  
**Launch seed (2026-07-13):** [@clairemao78](https://x.com/clairemao78/status/2076780816760438784) — **Instance**: automated evals for robot policies (YC S26 / instancelabs.ai)  
**YC launch seed:** [Instance — automated evaluation for robot policies (starting with the success detector)](https://www.ycombinator.com/launches/RPi-instance-automated-evaluation-for-robot-policies-starting-with-the-success-detector)  
**Demo hardware credit seed:** Almond Robotics (Axol) — VERIFY LIVE product pages  
**Failsafe metaphor seed:** Isaac Asimov’s *Foundation* (concepts only) — dual Foundations, foresight of collapse, Terminus knowledge vault  

**Not safety certification or PE sign-off.** Physical robots can injure people and damage property — human operators own e-stop, cages, and lab rules. Fiction is not a standards body.

---

## Industry problem (why this skill exists)

Robot **policies** (learned or scripted controllers) are hard to evaluate:

| Pain | Tester response |
|------|-----------------|
| Manual review of every rollout video | Automate **success / failure** labeling where reliable |
| “It worked once” anecdotes | Fixed **task suite** + N trials + confidence |
| Sim-only metrics that don’t transfer | Declare **sim vs real** scope; never hide the gap |
| Unclear pass criteria | Write **observable success detectors** before coding |
| Unsafe eval loops | **Safety envelope** before any motor enable |
| Primary judge alone can lie or drift | **Foundation-2 failsafe** + crisis ladder |
| Cloud/tooling outage mid-eval | **Terminus vault** offline suite + local stop |

---

## Foundation-pattern failsafe (metaphor → engineering)

Asimov’s *Foundation* (high-level premise only): a long-lived “empire” is rotting while few notice; a science of foresight anticipates collapse; critical knowledge is planted at **Terminus**; dual **Foundations** and pre-named **crises** keep the plan alive when enemies and decay hit. Fable **does not** retell copyrighted plot — it maps the *structure* onto robot eval.

| Story structure | Eval / safety structure |
|-----------------|-------------------------|
| Rotten core of a thriving system | Policy demos that look good while metrics rot |
| Foresight of fall | Named **crisis ladder** before first real-robot run |
| First Foundation on Terminus | Primary **success detector** + frozen task suite |
| Second Foundation (independent) | Second judge: other sensor, geometric ground truth, or human |
| Hostile pressure after collapse starts | Wear, clutter, lighting shift, adversarial setups (L3+) |
| Encyclopedia / vault | Offline `workspace/robotics/evals/` copies of suite + detectors |
| Reduce dark ages | Catch regressions early (L4) so bad policies don’t ship |

### Dual Foundations (required pattern for ship decisions)

```text
Foundation-1 (Terminus / primary)
  → Automated success detector (vision, SaaS, hybrid…)
Foundation-2 (independent failsafe)
  → Must not share failure mode with F1 when possible
  → Geometric pose / force / separate model / human sample
Agreement policy
  → both-pass | F2 veto on F1-pass | sample K% of F1-pass
On disagreement
  → failsafe-hold · human review · no silent “majority of one”
```

**Maker ≠ grader** is the organizational form of dual Foundations: the group that trains the policy should not be the sole owner of the only judge.

### Crisis ladder (predicted, not improvised)

| Crisis id | Typical trigger | Default response |
|-----------|-----------------|------------------|
| `C-DET-FP` | Spot-check false-pass rate high | Freeze detector version; re-calibrate |
| `C-RATE-CLIFF` | Pass rate drop > δ vs suite@vN | Block deploy; review fail artifacts |
| `C-SAFE` | E-stop, force limit, intrusion | **unsafe-hold**; motors off; no auto-resume |
| `C-TOOL-DOWN` | Logger or cloud judge unavailable | Terminus vault only; stop new rollouts |
| `C-SIMREAL` | Real << sim | Scope honesty; do not ship on sim alone |
| `C-DRIFT` | Scene / object / lighting out of suite | Re-run L3; expand suite or hold |

Physical **e-stop always outranks** software Foundations.

---

## Seed product: Instance (public launch notes)

| Field | Seed (VERIFY LIVE) |
|-------|--------------------|
| Product | **Instance** — automated evaluation for robot policies |
| Entry wedge | **Success detector** — auto-judge task completion from video/rollouts |
| Longer vision | Autonomous eval rig: judge success + scene reset + next rollout (no humans in loop) |
| Team seeds | Claire Mao (@clairemao78), Lucy — MIT; YC S26 |
| Product | [instancelabs.ai](https://www.instancelabs.ai/) · demo [demo.instancelabs.ai](https://demo.instancelabs.ai) |
| Contact seed | founders@instancelabs.ai (book demo) |
| YC | [Launch writeup](https://www.ycombinator.com/launches/RPi-instance-automated-evaluation-for-robot-policies-starting-with-the-success-detector) |
| X | [Launch post](https://x.com/clairemao78/status/2076780816760438784) |
| Demo hardware credit | Almond Robotics (**Axol**) — borrowed for launch demo; VERIFY LIVE OEM pages |
| Public claim seed | Verifier benchmarked on 10k+ held-out human-labeled episodes across 7 platforms (launch copy — VERIFY LIVE) |

Fable maps **evaluation design patterns** inspired by this direction — it does not replace Instance’s product or invent API/pricing.

---

## Evaluation stack

```text
Task definition
  → Success detector (binary / multi-class / score)
  → Environment (sim | hardware-in-loop | real)
  → Policy under test
  → Rollout logger (video, proprio, events)
  → Aggregator (pass rate, latency, damage flags)
  → Report + fail artifacts
```

### Success detector (core concept)

A **success detector** is a function (or model) that maps a trajectory / final observation to **pass/fail** (or graded score) without a human watching every frame.

| Detector type | Examples | Risks |
|---------------|----------|--------|
| **Geometric** | Object in bin AABB; end-effector within ε of target | Brittle lighting / occlusion |
| **Contact / force** | Threshold force on insert | Sensor bias |
| **Vision model** | Classifier “cup upright” | Domain shift; need calibration set |
| **Hybrid** | Vision + pose + timeout | Complexity |

**Rule:** define detector **before** tuning the policy, or you overfit to the judge.

---

## Test levels (functionality tester ladder)

| Level | Name | Goal |
|-------|------|------|
| L0 | **Smoke** | Power, e-stop, joint limits, basic command echo |
| L1 | **Unit skills** | Grasp, place, open, press — single primitives |
| L2 | **Task suites** | Multi-step tasks with success detector |
| L3 | **Robustness** | Lighting, pose noise, object variants |
| L4 | **Regression** | Fixed seed suite on every policy change |
| L5 | **Field / long-horizon** | Multi-hour reliability (ops-owned) |

---

## Trial protocol template

```markdown
# Task: {name}
## Success definition (observable)
- Pass if: …
- Fail if: …
- Timeout: … s → Fail
## Setup
- Scene reset: …
- Randomization: none | bounded
## Metrics
- Pass rate over N=…
- Mean time-to-success (successes only)
- Intervention count / e-stop count
## Artifacts
- Video path / log id
- Detector confidence if any
## Safety
- Max speed / force
- Keep-out zones
- Human presence rule
```

---

## Maker ≠ grader (robotics)

| Role | Owns |
|------|------|
| **Policy author** | Controller / weights / script |
| **Eval author (Foundation-1 suite)** | Task suite + primary success detector + harness |
| **Failsafe owner (Foundation-2)** | Independent detector path / spot-check protocol |
| **Safety officer (human)** | E-stop, lab access, IRB if human subjects |

Never let the same automated loop **train and self-certify** without a frozen eval suite **and** a failsafe path.

---

## Safety envelope (minimum)

1. E-stop reachable and tested **before** policy eval  
2. Speed/force limits for eval mode  
3. No free-space motion without collision model or soft start  
4. Camera privacy if humans in frame  
5. Log who enabled motors  
6. Dual Foundations defined for any real-robot **ship** decision  

---

## Scaffold

```text
workspace/robotics/evals/
  suite.yaml          # task list + N
  detectors.md        # success definitions (F1)
  failsafe.md         # F2 + crisis ladder + vault note
  results/            # local — may be large/gitignored
  report.md
```

---

## Related Fable skills

| Skill | Overlap |
|-------|---------|
| `hermes-loop` / `loop-engineer` | Verify · state · stop for offline agent evals |
| `prompt-generator` | Multi-agent eval design swarm |
| `math-physics-agent` | Dimensional / dynamics checks (not robot control) |
| `privacy-host-map` | Vendor eval SaaS hosts when dumping sites |

---

## Literary / IP note

*Foundation* and related names are associated with Isaac Asimov’s work and rights holders. Fable uses **structural metaphor** for teaching dual failsafes. Do not paste long book text into kits; do not imply Asimov or estates endorse robotics advice.

---

## OPEN / VERIFY LIVE

- Instance API / integration docs beyond public demo  
- Pricing, SLAs, supported robots  
- Almond Robotics Axol capabilities  
- Lab-specific safety SOPs  


