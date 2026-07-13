#!/usr/bin/env python3
"""
MBTI Personality Agent — offline switchable Myers-Briggs style lenses.

Full catalogue + Fable5 integration live in:
  mbti_types.py
  fable5_offline_agent.py  (/mbti · --mbti)
  skills/mbti-personality-customiser.md

Usage:
    python mbti_personality_agent.py
    python fable5_offline_agent.py --mbti INTJ
"""

from __future__ import annotations

import os
from datetime import datetime

from openai import OpenAI

from mbti_types import (
    MBTI_PROMPTS,
    VALID_TYPES,
    build_system_prompt,
    get_fable5_overlay,
    load_mbti_state,
    list_types_table,
    normalize_type,
    save_mbti_state,
    set_active_type,
    set_rigour,
)

# ==================== CONFIG ====================
LOCAL_LLM_BASE_URL = os.environ.get("FABLE5_BASE_URL", "http://localhost:11434/v1")
MODEL_NAME = os.environ.get("FABLE5_MODEL", os.environ.get("MBTI_MODEL", "qwen2.5:72b"))
# ===============================================


def get_client() -> OpenAI:
    return OpenAI(base_url=LOCAL_LLM_BASE_URL, api_key=os.environ.get("FABLE5_API_KEY", "ollama"))


def main() -> None:
    print("╔════════════════════════════════════════════════════════════╗")
    print("║     MBTI PERSONALITY AGENT — SWITCHABLE ARCHITECTURE       ║")
    print("║   All 16 types • Fable5 rigour optional • Fully offline    ║")
    print("║   Shared catalogue: mbti_types.py · also /mbti in Fable5   ║")
    print("╚════════════════════════════════════════════════════════════╝\n")

    client = get_client()
    state = load_mbti_state()

    # Standalone defaults to INTJ if none set (legacy behaviour)
    current_type = normalize_type(state.get("current_type")) or "INTJ"
    if state.get("current_type") is None:
        set_active_type(current_type)
        state = load_mbti_state()
    rigour_mode = bool(state.get("rigour_mode", True))

    print(f"Current personality: {current_type}")
    print(f"Rigour mode: {'ON' if rigour_mode else 'OFF'} (type 'rigour on/off' to toggle)")
    print("\nCommands: switch [TYPE], list, current, rigour on/off, quit")
    print("Tip: use `python fable5_offline_agent.py --mbti TYPE` for full Fable stack.\n")

    messages = [
        {"role": "system", "content": build_system_prompt(current_type, rigour_mode)}
    ]

    # Optional short conversation restore from state
    if state.get("conversation"):
        messages.extend(state["conversation"][-10:])
        print("(Previous conversation context loaded)\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue

            lower_input = user_input.lower()

            if lower_input in ["quit", "exit", "q"]:
                print("\nRighto, catch ya later legend.")
                state = load_mbti_state()
                state["conversation"] = [m for m in messages if m.get("role") != "system"][-20:]
                save_mbti_state(state)
                break

            if lower_input == "list":
                print("\nAvailable types:")
                print(list_types_table())
                print()
                continue

            if lower_input == "current":
                print(
                    f"\nCurrent type: {current_type} | Rigour: "
                    f"{'ON' if rigour_mode else 'OFF'}\n"
                )
                continue

            if lower_input.startswith("switch "):
                new_type = user_input.split(" ", 1)[1].upper().strip()
                if new_type in VALID_TYPES:
                    current_type = new_type
                    set_active_type(current_type, rigour=rigour_mode)
                    messages = [
                        {
                            "role": "system",
                            "content": build_system_prompt(current_type, rigour_mode),
                        }
                    ]
                    print(f"\n[Switched to {current_type} mode]")
                else:
                    print(
                        f"\nUnknown type. Available: "
                        f"{', '.join(sorted(VALID_TYPES))}"
                    )
                continue

            # Bare type code as switch (INTJ, enfp, …)
            bare = normalize_type(user_input)
            if bare and lower_input.upper() in VALID_TYPES:
                current_type = bare
                set_active_type(current_type, rigour=rigour_mode)
                messages = [
                    {
                        "role": "system",
                        "content": build_system_prompt(current_type, rigour_mode),
                    }
                ]
                print(f"\n[Switched to {current_type} mode]")
                continue

            if lower_input in ["rigour on", "rigouron"]:
                rigour_mode = True
                set_rigour(True)
                messages = [
                    {
                        "role": "system",
                        "content": build_system_prompt(current_type, rigour_mode),
                    }
                ]
                print("\n[Rigour mode ENABLED - Fable5 rules active]")
                continue

            if lower_input in ["rigour off", "rigouroff"]:
                rigour_mode = False
                set_rigour(False)
                messages = [
                    {
                        "role": "system",
                        "content": build_system_prompt(current_type, rigour_mode),
                    }
                ]
                print("\n[Rigour mode DISABLED - pure personality mode]")
                continue

            messages.append({"role": "user", "content": user_input})

            print(f"\n[{current_type}]: ", end="", flush=True)

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                temperature=0.7 if not rigour_mode else 0.4,
                max_tokens=4096,
                stream=True,
            )

            full_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    print(content, end="", flush=True)
                    full_response += content
            print("\n")

            messages.append({"role": "assistant", "content": full_response})
            state = load_mbti_state()
            state["conversation"] = [m for m in messages if m.get("role") != "system"][-20:]
            state["current_type"] = current_type
            state["rigour_mode"] = rigour_mode
            save_mbti_state(state)

        except KeyboardInterrupt:
            print("\n\nCaught ya. Saving state...")
            state = load_mbti_state()
            state["conversation"] = [m for m in messages if m.get("role") != "system"][-20:]
            save_mbti_state(state)
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Make sure Ollama is running with your model.")


if __name__ == "__main__":
    main()
