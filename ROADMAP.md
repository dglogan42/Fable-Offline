# How to Become an Agentic AI Engineer in 6 Months

**Local companion roadmap for Fable 5 Offline.**  
Order matters. Roughly one stage every two weeks. **Build real things** — do not skip to multi-agent demos.

> A regular developer writes code that does exactly what it is told.  
> An **agentic engineer** builds systems that **decide what to do**: goal → steps → tools → execute → check → adjust → loop.

Fable Offline already covers: loops, verifier ≠ maker, memory/state, skills, Hermes, build/automate, engineer mode. Use this roadmap to grow *yourself* while the agent grows *with* you.

---

## Month 1 — Foundation

### Stage 1 — Python & async (weeks 1–2)
Agents spend life **waiting** (models, APIs, tools). Blocking code crawls.

**Learn:** `asyncio`, concurrent calls, retries, FastAPI-style non-blocking handlers.  
**Build:** small server or script that fires multiple LLM calls concurrently; retry + per-tool error isolation.  
**Fable map:** shell allowlist + workflows; do not block the whole process on one failure.

### Stage 2 — LLM fundamentals for agents (weeks 3–4)
**Learn:** context limits; **model routing** (cheap vs hard tasks); token cost tracking; failure modes (hallucination, lost-in-middle, instruction drift, latency).  
**Build:** a router that sends classify/summarize to a small local model and hard reasoning to a stronger one (Ollama tags).  
**Fable map:** `FABLE5_MODEL`, effort routing in manual §9.7.

---

## Month 2 — Agent core

### Stage 3 — Tool calling & structured outputs (weeks 5–6)
Chatbots talk. Agents **use tools** and recover when tools fail.

**Learn:** tool schemas; structured JSON/Pydantic-style validation; recovery on bad tool calls.  
**Build:** agent loop that can call 2+ local tools and re-ask on invalid output.  
**Fable map:** build/automate steps, allowlisted shell, FILE scaffolds.

### Stage 4 — Memory & state (weeks 7–8)
Four memories: **short-term** (buffer), **long-term** (lessons/skills), **working** (current job), **episodic** (session/cycle logs). Compress when long.

**Fable map:** `memory/`, smart RAG, compress, `LOOP_STATE.md`, skills library.

---

## Month 3 — Building agents

### Stage 5 — Single-agent ReAct (weeks 9–10)
**Reason → Act → Observe → Decide.** Max steps. Log every step. Validate tool outputs. One solid agent > ten broken ones.

**Fable map:** `/loop`, `/hermes`, `/engineer` (PLAN→DO→VERIFY→stop).

### Stage 6 — Multi-agent orchestration (weeks 11–12)
Add agents only when one cannot do the job. **Supervisor** pattern: research → write → critic, with max revision loops and validated handoffs.

**Fable map:** `/team` or `--team` (research + writer + critic).

---

## Month 4 — Production skills

### Stage 7 — Human-in-the-loop (week 13)
Full autonomy fails expensively. **Approval gates** on high-risk actions; audit log.

**Fable map:** `/team` HITL prompts; `FABLE5_HITL=1`; automate `hitl` step.

### Stage 8 — Evals (week 14)
No eval suite → silent bugs. LLM-as-judge + fixed cases + regression.

**Fable map:** engineer criteria scores; skill `edge-vs-luck` for false “wins”; workflow evals later.

---

## Month 5 — Ship it

### Stage 9 — Observability (week 15)
Trace steps, costs, failures. Invisible prod = unfixable prod.  
**Fable map:** cycle logs, build/automate logs, LOOP_STATE.

### Stage 10 — Security & guardrails (week 16)
Prompt injection, tool blast radius, path escape, shell allowlist.  
**Fable map:** workspace sandbox, shell allowlist off by default.

---

## Month 6 — Real world

### Stage 11 — Production shape (week 17)
Async APIs, job IDs, rate limits, canary, rollback.  
**Fable map:** offline first; design skills for later FastAPI deployment.

### Stage 12 — Ship in public (week 18+)
Real GitHub agent (not a tutorial clone), architecture README, short demo, public write-up.  
**Portfolio:** Fable-Offline itself is evidence of loop + verifier + skills + offline design.

---

## The boring stages that prevent most failures
1. Blocking code under load (Stage 1)  
2. No eval suite (Stage 8)  
3. No tracing (Stage 9)  

Do them first. Do them properly.

## Progress tracking
Use `/roadmap` or open this file every two weeks. Mark stages in `memory/` lessons. Automate: `--automate agentic-checkpoint`.
