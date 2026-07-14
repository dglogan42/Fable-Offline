# Integrating the communicator mode into Fable-Offline

## What's in this patch

```
fable5_communicators.py          # new, top-level, next to fable5_offline_agent.py
agents/communicators/README.md   # explains the persona set
agents/communicators/proposer.md
agents/communicators/challenger.md
agents/communicators/synthesizer.md
agents/communicators/mentor.md   # optional 4th persona, not wired in by default
tests/test_communicators.py      # stdlib unittest, no network/Ollama needed
```

## Why you're getting a patch instead of a direct edit

I built this from your cloud workspace, which currently can't reach
`github.com`'s git endpoints directly (network allowlist blocks it),
and the desktop file-bridge to your machine wasn't responding either.
So rather than guess at a `git diff` against code I couldn't fully
read, I wrote a self-contained module against a **summary** of
`fable5_offline_agent.py`'s public architecture (confirmed: the
`stream_chat()` / `make_client()` / `read_skills_bundle()` function
signatures, the `--team` supervisor pattern, and the `FABLE5_*` env
var names) and made the two integration touch points below as small
and low-risk as I could.

## Step 1 — copy files in

From this patch's root, into your repo root:

```bash
cp fable5_communicators.py /path/to/Fable-Offline/
cp -r agents/communicators /path/to/Fable-Offline/agents/
cp tests/test_communicators.py /path/to/Fable-Offline/tests/    # create tests/ if it doesn't exist
```

## Step 2 — sanity check it standalone (no changes to your main file yet)

```bash
cd /path/to/Fable-Offline
python fable5_communicators.py --commune "how should our agents log decisions"
```

This works right now even without touching `fable5_offline_agent.py`,
*if* Ollama is running locally (it lazily imports `make_client` and
`stream_chat` from your main file at call time). If you just want to
verify the logic with no LLM at all:

```bash
python tests/test_communicators.py
```

## Step 3 — wire it into the main CLI (optional, ~6 lines)

In `fable5_offline_agent.py`:

**a) argparse block** (next to the existing `--team` flag):

```python
parser.add_argument("--commune", type=str, nargs="?", const="", metavar="TOPIC",
                     help="Run a communicator session: agents propose/critique/refine/synthesize, "
                          "then write reusable lessons to skills/*.md.")
parser.add_argument("--commune-rounds", type=int, default=5, metavar="N")
parser.add_argument("--commune-agents", type=str, default="proposer,challenger,synthesizer")
```

**b) dispatch block** (wherever `args.team` currently gets handled):

```python
if args.commune:
    from fable5_communicators import run_communicator_session
    client = make_client()
    system_core = load_system_prompt(...)   # however you already build it for --team
    result = run_communicator_session(
        args.commune,
        client=client,
        rounds=args.commune_rounds,
        agent_names=[n.strip() for n in args.commune_agents.split(",") if n.strip()],
        system_core=system_core,
        self_improve=DEFAULT_SELF_IMPROVE and not args.no_self_improve,  # reuse your existing flag if present
        hitl=HITL,
    )
    print(result.transcript_markdown())
    if result.skill_path:
        print(f"\nNew skill written: {result.skill_path}")
```

Adjust the two lines that reference `load_system_prompt(...)` and
`make_client()` to match whatever your actual call sites look like —
I know their signatures conceptually but not the exact parameter
names, since I was working from a summary rather than the literal
file.

## Config knobs (all optional, same `FABLE5_*` convention)

| var | default | meaning |
|---|---|---|
| `FABLE5_COMM_ROUNDS` | `5` | critique/refinement rounds after the opening proposal |
| `FABLE5_COMM_AGENTS` | `proposer,challenger,synthesizer` | roster, comma-separated |

`FABLE5_HITL` and `FABLE5_SELF_IMPROVE` (already in your repo) gate
whether a new `skills/commune-*.md` file gets written and whether you're
asked to confirm first — same behavior as the rest of the self-improve
flow.

## How agents actually "learn from each other" here

This is the part worth double-checking matches what you had in mind:
within a session, agents literally read each other's prior messages
(each turn's prompt includes the full transcript so far). *Across*
sessions, the synthesizer's `LESSONS` get written to a new
`skills/commune-*.md` file, and because every mode in the harness
already loads `skills/*.md` into its system prompt via
`read_skills_bundle()`, a lesson one communicator session produced
shows up automatically in the next `--loop`, `--hermes`, `--team`, or
`--commune` run — that's the persistent "learning" layer, not just an
in-session chat log. If you had something more elaborate in mind
(e.g. agents adjusting numeric weights, a shared vector memory, actual
model fine-tuning), that's a different and much bigger build — tell me
and I'll scope that separately.
