# Loop engineer

**WHEN_TO_USE:** User wants to “loop like an engineer”, run until criteria clear, Karpathy-style experiment loop, or PLAN→DO→VERIFY without babysitting — `/engineer` or `--engineer`.

## Make-or-break
1. **Verifier** — separate fresh-context checker (never self-grade as final).
2. **State** — read/write what was tried and failed (`LOOP_STATE`).
3. **Stop** — success gate OR hard limit (N tries / max cycles).

## Protocol each cycle
1. PLAN — single next step (weakest criterion first).
2. DO — one bounded change.
3. VERIFY — external scores 1–10 per criterion.
4. DECIDE — FINAL if all ≥ min score; else ITERATING.

## Preflight (honest)
Use a heavy loop only if: repeats / high-stakes multi-step; automated or strict verification; token budget ok; real artifacts to check.

## Not this
- One-shot chat with no gate
- Infinite retry without stop
- Editing the test to pass instead of improving the work
