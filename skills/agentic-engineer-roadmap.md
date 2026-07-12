# Agentic engineer roadmap (6 months)

**WHEN_TO_USE:** Career path, learning plan, “how do I become an agentic AI engineer,” portfolio advice, or sequencing what to build next with Fable Offline.

## Core shift
- **Developer:** code that does exactly what it is told  
- **Agentic engineer:** systems that **decide** — goal → steps → tools → execute → check → adjust → loop  
You design **reasoning systems**, not only step lists.

## Order (do not skip ahead)
| Stage | Focus | Build |
|-------|--------|--------|
| 1 | Python async, retries, non-blocking I/O | Concurrent LLM calls + resilient errors |
| 2 | Context limits, routing, tokens, model failure modes | Cheap/hard task router |
| 3 | Tool calling + structured outputs | Agent + tools + schema validation |
| 4 | Short/long/working/episodic memory + compress | Memory that survives sessions |
| 5 | Single ReAct agent, max steps, logs | One end-to-end working agent |
| 6 | Multi-agent only if needed; supervisor + handoffs | Research → write → critic |
| 7 | Human-in-the-loop on high risk | Approval gates + audit log |
| 8 | Evals, LLM-as-judge, regression | Test suite that catches silent fails |
| 9 | Tracing, cost, observability | Every step visible |
| 10 | Security, injection, guardrails | Least privilege tools |
| 11 | Deploy shape: async jobs, rate limits | API/job pattern design |
| 12 | Ship in public | Real repo + demo + write-up |

## Fable Offline mapping
- Stages 4–5 → `/loop`, `/hermes`, `/engineer`, memory, skills  
- Stage 6 → `/team` multi-agent  
- Stage 7 → HITL approvals  
- Stage 3/10 → workspace sandbox, shell allowlist  
- Stage 12 → this repo as portfolio proof  

## Coaching rules
1. Prefer **one real artifact** over another video.  
2. If they want multi-agent first, redirect to Stages 1 + 5.  
3. Production failures cluster on: blocking I/O, no evals, no traces.  
4. End every coaching reply with **this week’s concrete build task**.
