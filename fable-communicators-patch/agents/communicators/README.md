# Communicator agents — offline loop briefs

This folder holds the persona briefs for `--commune` (see
`fable5_communicators.py` at the repo root). Same pattern as the
existing `agents/*.md` loop briefs (`hermes-agent.md`,
`fable-loop-agent.md`, ...): short, role-scoped markdown loaded
straight into the system prompt for that turn.

| file | role | one-line |
|---|---|---|
| `proposer.md` | opens the discussion | states one concrete approach |
| `challenger.md` | critiques a peer | names the single sharpest flaw |
| `synthesizer.md` | closes the session | final approach + reusable lessons |
| `mentor.md` | optional fresh-context reviewer | resolved / unresolved verdict |

Add your own by dropping `agents/communicators/<name>.md` and passing
`--agents proposer,<name>,synthesizer` (or setting
`FABLE5_COMM_AGENTS`). Any name without a matching file falls back to
a generic built-in brief defined in `fable5_communicators.py`, so a
missing file never crashes a session — it just runs with a weaker
persona until you write one.

## Why this is "learn from each other" and not just a chat

The synthesizer's `LESSONS` section gets written to a new
`skills/commune-*.md` file (gated by `FABLE5_HITL` / `--no-self-improve`,
same as the rest of Fable 5's self-improvement flow). Every future run
of *any* mode — `--loop`, `--hermes`, `--team`, another `--commune` —
loads `skills/*.md` into its system prompt via `read_skills_bundle()`.
So what one communicator session learns about (say) how to structure a
proposal or what critique pattern actually holds up becomes available
to every agent on every later run, not just within that one
conversation.
