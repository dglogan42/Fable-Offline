# Build and automate (offline)

**WHEN_TO_USE:** User wants to scaffold a project, chain multi-step work, or run a reusable workflow recipe — `/build`, `--build`, `/automate`, `--automate`.

## Build
1. Clarify deliverable + how they will run it.
2. Emit PLAN with goals and run steps (Win/macOS/Linux when useful).
3. Emit FILE blocks with relative paths only.
4. Keep scaffolds small, complete, and runnable offline.
5. End with DONE summary.

## Automate
1. Prefer an existing `workflows/*.json` recipe.
2. Step types: build, hermes, loop, improve, compress, llm, shell, note.
3. Shell only when explicitly enabled and allowlisted.
4. Stop on first hard error unless the recipe says otherwise.
5. Log outcomes to memory for later self-improve.

## Checks
- No absolute paths or `..` in build files
- No invented secrets
- Automation leaves a clear trail in memory logs
