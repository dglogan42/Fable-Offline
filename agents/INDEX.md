# Agent surfaces — briefing pack

Every multi-step or multi-agent surface in this repo, and **how each one
actually gets its instructions loaded**. That loading mechanism differs by
surface — conflating them is the easiest way to edit the wrong file and see
no effect. Three mechanisms exist:

1. **Generic pack** — `read_agents_brief()` in `fable5_offline_agent.py`
   loads a fixed allowlist of files from this directory into every chat /
   loop / hermes / engineer system prompt.
2. **On-demand brief** — a specific `--flag` handler reads one named file
   from this directory directly, only when that flag fires. Not part of the
   generic pack above.
3. **Mode-owned roster** — a mode loads its own files from a subdirectory by
   role name (not a fixed allowlist), independent of `read_agents_brief()`.

## 1. Generic pack (`read_agents_brief`)

Always includes the first three; adds one more depending on mode.

| File | Loaded when | Role |
|------|-------------|------|
| `offline-loop-protocol.md` | Always (chat, loop, hermes, engineer) | Verifier · state · stop; five beats |
| `goal-quality.md` | Always | How to write goals that loops can finish |
| `shared-state.md` | Always | File-based state map + cross-agent communication channels |
| `hermes-agent.md` | `/hermes` · `--hermes` | Soul + RAG + repair + self-stop |
| `fable-loop-agent.md` | `/loop` · `/engineer` · `--loop` · `--engineer` | Executor/maker + engineer rules |

Truncated to `limit_chars` (default 4500) if the bundle runs long.

## 2. On-demand briefs (loaded directly by their flag handler)

Not part of the pack above — these load only when their specific mode runs,
so editing them has no effect on chat/loop/hermes unless that flag fires.

| File | Loaded by | Role |
|------|-----------|------|
| `math-physics-agent.md` | `--deep-explain` / `--theorem` / `--physics-solve` (and skill `math-physics-agent`) | deep-explain / theorem / physics-solve procedure detail |
| `prompt-generator-agent.md` | `--prompt-gen` / `/prompt-gen` | Swarm prompt gen cycle + handoff rules |

## 3. Mode-owned rosters (subdirectories, loaded by role name)

| Directory | Loaded by | Roster |
|-----------|-----------|--------|
| `communicators/` | `fable5_communicators.py` (`--commune`) | `proposer`, `challenger`, `synthesizer`, and optional `mentor` (not in the default roster — pass `--commune-agents proposer,challenger,synthesizer,mentor` to include it) |

`CommunicatorAgent.load(name)` reads `communicators/{name}.md` by the
roster name in `--commune-agents` (default
`proposer,challenger,synthesizer`), not a fixed list — add a new file and
name it in the roster to add a persona.

## Multi-agent surfaces with no `agents/*.md` file at all

These are genuinely multi-agent (separate roles, separate turns) but their
role instructions live inline in code or in a catalogue module, not here —
don't look for a briefing file that doesn't exist.

| Surface | Roles | Where the role prompts live |
|---------|-------|------------------------------|
| `--team` | research → write → critic (supervisor) | Inline in `run_team()`, `fable5_offline_agent.py` (maker ≠ grader: critic is a separate call) |
| `--mbti-feedback` | N MBTI-typed lenses, critique/refine in rounds | `mbti_types.py` (`MBTI_PROMPTS`, `build_feedback_loop_prompt`); state persisted in `mbti_state.json` |
| `--mbti TYPE` / `/mbti` | Single active MBTI lens overlay | `mbti_types.py` + `skills/mbti-personality-customiser.md` |
| Robotics functionality tester | Single coaching persona (not multi-turn agents) | `skills/robotics-functionality-tester.md`, loaded via the skills bundle (below), not `agents/` |

## Skills bundle (separate from all of the above)

`read_skills_bundle()` loads the 12 most-recently-modified files from
`skills/*.md` into every mode's system prompt (`list_skill_paths()` sorts by
mtime, not topic relevance) — this is the layer that lets one `--commune`
session's freshly-written lesson show up in the next `--loop`/`--hermes`/
`--team` run: it's the newest file, so it sorts into the top 12 automatically
(see `shared-state.md` for the write side).

## Load order (harness)

1. Operating Manual (core)
2. `SOUL.md`
3. Agent pack (mechanism 1 above: protocol + mode-specific brief)
4. Skills bundle (12 most-recently-modified `skills/*.md`)
5. Domain knowledge (mode flags)
6. Retrieved memory / LOOP_STATE (per cycle)

On-demand briefs (mechanism 2) and mode-owned rosters (mechanism 3) are
**not** part of this sequence — they're pulled in later, only inside their
own flag's handler.

## Env

| Variable | Default | Meaning |
|----------|---------|---------|
| `FABLE5_AGENTS` | `agents` | Directory of agent briefing files (root for all three mechanisms above) |
| `FABLE5_COMM_ROUNDS` | `5` | `--commune` critique/refinement rounds |
| `FABLE5_COMM_AGENTS` | `proposer,challenger,synthesizer` | `--commune` roster |
| `FABLE5_AUTO_MBTI_FEEDBACK` | `1` (on) | Auto-inject an MBTI multi-lens critique prompt into `--loop`/`--hermes`/`--engineer` cycles — see `shared-state.md` |

## Edit policy

- Keep briefs **short** (harness truncates).
- Prefer checklists over essays.
- Do not put secrets or live API keys here.
- Adding a new persona to `communicators/`? Also add its name to
  `FABLE5_COMM_AGENTS` / `--commune-agents`, or it never loads.
- Adding a new file here that should always be in context? It needs a line
  in `read_agents_brief()`'s `names` list (mechanism 1) — dropping a file
  into `agents/` alone does not make it load anywhere.
