# Capability mesh (interconnected skills)

**WHEN_TO_USE:** User wants to turn a broad goal into a network of specialized skills, define how each capability hands off to the next, or design an agent stack where every skill remains independently useful and still communicates clearly with the others.

## Core idea
Treat the system as a mesh, not as one monolithic prompt. Each capability should be:
- a standalone skill with a clear trigger,
- a small contract of inputs and outputs,
- a named handoff to the next skill when needed,
- a verification gate before it claims success.

## Communication contract
Each capability should exchange a compact handoff packet:

| Field | Meaning |
|------|---------|
| `capability` | Which skill is speaking |
| `intent` | What this skill is trying to achieve |
| `input` | The evidence, artifact, or request it received |
| `output` | The artifact, plan, or answer it produced |
| `next` | The next skill that should consume the output |
| `verify` | The check that proves the output is good enough |

This keeps the system modular: one skill can be reused alone, or the same skill can be chained into a larger workflow.

## Capability layers

| Layer | Skills | Job |
|------|--------|-----|
| **Coordination** | `hermes-loop`, `loop-engineer`, `build-and-automate` | Plan, execute, verify, and compound work |
| **Quality & rigor** | `edge-vs-luck`, `rederive-numbers`, `agentic-engineer-roadmap` | Prevent false confidence and weak reasoning |
| **Core domain skills** | `privacy-design-planner`, `math-physics-agent`, `urban-planner-competencies`, `legal-playbook` | Handle domain-specific reasoning |
| **Delivery & publication** | `calendar-mail-meetings`, `rss-share`, `pdf-render`, `youtube-live-encoder` | Package outputs for real-world use |

## Procedure: design a capability mesh
1. Name the capability and give it a single trigger.
2. Define the skill contract: what input it consumes and what output it produces.
3. Choose the next skill(s) that should receive the output.
4. Add a verification gate so a claim is only accepted with evidence.
5. Keep the skill reusable on its own, even when it is also part of a larger chain.
6. Store durable artifacts and handoff notes in `knowledge/`, `memory/`, or `workflows/`.

## Example mesh
A typical chain looks like this:

```text
planner → mapper → executor → verifier → publisher
```

Example skill sequence:
- `privacy-design-planner` frames the brief
- `privacy-host-map` gathers evidence
- `loop-engineer` turns the plan into verified cycles
- `build-and-automate` turns the result into a workflow or scaffold
- `rss-share` or `calendar-mail-meetings` packages the result for human use

## Checks
- Does each skill have a clear standalone use case?
- Does the handoff include an explicit input/output packet?
- Does the chain stop when evidence is missing or weak?
- Does the system preserve individual skill autonomy instead of collapsing everything into one prompt?

## Output shape
When a user asks for a capability mesh, produce:
1. **Capability map** — the skills involved and why each exists
2. **Handoff plan** — the exact next skill for each output
3. **Verification plan** — how each step will be checked
4. **Artifact plan** — where durable notes or workflows should live
