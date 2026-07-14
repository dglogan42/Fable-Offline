# Communicator mode integration

Status: **integrated**. `--commune` is wired into `fable5_offline_agent.py`
and the files below live at their target locations in the repo.

## Files

```
fable5_communicators.py          # top-level, next to fable5_offline_agent.py
agents/communicators/README.md   # explains the persona set
agents/communicators/proposer.md
agents/communicators/challenger.md
agents/communicators/synthesizer.md
agents/communicators/mentor.md   # optional 4th persona, not wired in by default
tests/test_communicators.py      # stdlib unittest, no network/Ollama needed
```

## Usage

```bash
python fable5_offline_agent.py --commune "how should our agents log decisions"
python fable5_offline_agent.py --commune --commune-rounds 3 --commune-agents proposer,challenger,synthesizer
python tests/test_communicators.py   # sanity check, no LLM required
```

## How it's wired

`fable5_offline_agent.py`:

- **argparse** (~line 4119): `--commune [TOPIC]`, `--commune-rounds`,
  `--commune-agents`.
- **dispatch** (~line 4925): reuses the already-constructed `client` and
  `system` prompt from the top of `main()` — no second `make_client()` call —
  and calls:

  ```python
  from fable5_communicators import run_communicator_session

  result = run_communicator_session(
      topic,
      client=client,
      rounds=args.commune_rounds,
      agent_names=[n.strip() for n in args.commune_agents.split(",") if n.strip()],
      system_core=system,
      self_improve=DEFAULT_SELF_IMPROVE and not args.no_self_improve,
      hitl=HITL,
  )
  print(ui("\n" + result.transcript_markdown()))
  if result.memory_path:
      print(ui(f"\nTranscript saved: {result.memory_path}"))
  if result.skill_path:
      print(ui(f"New skill written: {result.skill_path}"))
  ```

## Config knobs (`FABLE5_*` convention)

| var | default | meaning |
|---|---|---|
| `FABLE5_COMM_ROUNDS` | `5` | critique/refinement rounds after the opening proposal |
| `FABLE5_COMM_AGENTS` | `proposer,challenger,synthesizer` | roster, comma-separated |

`FABLE5_HITL` and `FABLE5_SELF_IMPROVE` (existing repo-wide flags) gate
whether a new `skills/commune-*.md` file gets written and whether you're
asked to confirm first — same behavior as the rest of the self-improve flow.

## How agents learn from each other

Within a session, agents read each other's prior messages — each turn's
prompt includes the full transcript so far. Across sessions, the
synthesizer's `LESSONS` are written to a new `skills/commune-*.md` file, and
because every mode in the harness loads `skills/*.md` into its system prompt
via `read_skills_bundle()`, a lesson one `--commune` session produces shows
up automatically in the next `--loop`, `--hermes`, `--team`, or `--commune`
run. That's the persistent "learning" layer — not just an in-session chat
log. Numeric weight adjustments, shared vector memory, or actual model
fine-tuning are out of scope for this mode.
