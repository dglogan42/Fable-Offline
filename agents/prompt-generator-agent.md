# Prompt generator agent — loop brief

Use when generating or wiring **system prompts** for swarms offline.

## Mission
Produce specialized agent prompts with clean handoffs; then load them into Hermes/Fable/offline_goal_loop.

## Cycle (generate)

1. **Choose mode** — quant | custom swarm | single  
2. **Run generator** — `auto_prompt_generator` / `--prompt-gen` / `/prompt-gen`  
3. **Verify files** — `.md` present; overview + optional `swarm_config.json`  
4. **Human skim** — tighten role boundaries; enforce maker≠checker  
5. **Handoff** — next runner uses agent 01, then 02… with LOOP_STATE or sequential goals  

## Cycle (consume)

1. Load `0k_*.md` as system (or skill body)  
2. Pass previous agent's Output Contract as user message  
3. Fresh verifier / separate model for Validator-type roles  
4. Stop when swarm overview success condition met  

## Stop
- Files written and paths reported, **or**  
- Architect plan delivered with exact CLI for the human  

## Never
- Treat generated quant signals as live trading advice  
- Commit secrets into `generated_prompts/`  
- Let Idea Generator grade its own tickets as final  

## Paths
- Out: `generated_prompts/` (`FABLE5_PROMPT_GEN_DIR`)  
- Skill: `skills/prompt-generator.md`  
- Knowledge: `knowledge/swarm/prompt-generator.md`  
