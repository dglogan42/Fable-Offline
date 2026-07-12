# program.md — Loop Engineer constraints (Karpathy-style)

A **prompt** is one instruction. A **loop** is a goal the agent keeps working toward until a **verifier** and **stop condition** say stop.

You explore under these constraints. The human writes purpose once; the loop executes.

## Objective
Improve the deliverable against SUCCESS CRITERIA. Prefer **one change per cycle**.

## The three make-or-break parts
1. **Verifier** — separate checker (fresh context). No gate = grading your own homework.
2. **State** — `memory/LOOP_STATE.md` records tried / failed / next. Tomorrow resumes.
3. **Stop** — success when every criterion ≥ min score, OR hard limit (max cycles / retry ceiling).

## Allowed to change
- The artifact under construction (workspace or stated deliverable)
- Working notes that do not weaken the gate

## Not allowed
- Weakening success criteria to make the test pass (like editing `prepare.py`)
- Claiming FINAL without verifier SUCCESS_MET
- Repeating a failed unit without a new strategy

## Explore
- Fix the **WEAKEST** criterion first each cycle
- If stuck in the same pattern twice, force a different approach (bilevel outer loop may inject this)

## Stop
- **SUCCESS:** every criterion ≥ min score and SUCCESS_MET: yes → print progress and stop
- **HARD LIMIT:** max cycles or retry ceiling → stop and report (do not run forever)

## Do you need a heavy loop?
Only if: task repeats or is multi-step high-stakes; verification is strict; token budget can absorb retries; agent has checkable artifacts. Otherwise use one good prompt or `/chat`.
