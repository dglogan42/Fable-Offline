# Hermes loop (offline)

**WHEN_TO_USE:** Multi-step goals that need self-stopping, selective memory, and mid-run repair — invoke with `/hermes` or `--hermes`.

## Steps
1. Load **SOUL.md** for identity and boundaries.
2. Retrieve **top-K relevant memory** only (smart RAG) — never dump the full archive.
3. Execute **one bounded unit** toward the goal.
4. **Fresh-context verifier** grades the artifact (maker ≠ grader).
5. On FAIL: run **live repair** (strategy + next unit + avoid) before retrying.
6. **Self-stop** on success, retry ceiling, or cycle budget.
7. After multi-cycle runs: **compress memory** and optionally **self-improve skills**.

## Checks
- Did we inject only retrieved chunks, not all history?
- Did we stop with evidence when done or blocked?
- Did a failed unit produce a concrete repair, not a vague apology?
