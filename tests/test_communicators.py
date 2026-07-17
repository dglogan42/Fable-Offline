#!/usr/bin/env python3
"""
Standalone test for fable5_communicators.py — stdlib unittest only (the
repo's only declared deps are openai + pypdf, so this deliberately avoids
requiring pytest). Uses a scripted stub chat_fn, so it needs no network,
no Ollama, and no openai package installed.

Run directly:   python tests/test_communicators.py
Or with pytest: pytest tests/test_communicators.py   (if you have it)
"""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import fable5_communicators as comm  # noqa: E402


SCRIPTED_RESPONSES = [
    # round 1: proposer opens
    "Ship a single shared markdown skills file that every agent reads before "
    "responding. Assumption: agents run sequentially, not in parallel. "
    "Biggest risk: the file grows unbounded and blows the context budget.",
    # round 2: challenger critiques
    "The unbounded-growth risk is real but understated: you never described "
    "a pruning or ranking step, so after a few dozen sessions the most useful "
    "lessons get buried under noise and stop being read at all.",
    # round 3: proposer refines
    "Refined: cap the bundle at N most-recent-and-highest-signal entries and "
    "drop low-value ones on write, addressing the burial risk directly.",
    # round 4: challenger critiques again
    "Fine as far as it goes, but 'highest-signal' is undefined — without a "
    "concrete signal (e.g. was this lesson referenced again later) it just "
    "becomes 'most recent', which is the same unbounded-growth problem "
    "wearing a cap.",
    # round 5: proposer refines again
    "Refined further: track a simple usage counter per skill file and prefer "
    "high-usage + recent over recency alone when trimming.",
    # round 6 (synthesis): synthesizer closes
    (
        "FINAL APPROACH\n"
        "Write each session's takeaway to its own skill file, and when "
        "trimming the bundle prefer files with higher usage counts, "
        "breaking ties by recency, rather than pure recency.\n\n"
        "LESSONS\n"
        "- Always cap any growing shared-context bundle instead of letting it "
        "grow unbounded.\n"
        "- Prefer usage-weighted pruning over pure recency when trimming a "
        "shared knowledge store.\n"
    ),
]


def make_scripted_chat_fn():
    calls = {"i": 0}

    def _chat_fn(client, messages, *, temperature=0.3, prefix=""):
        i = calls["i"]
        calls["i"] += 1
        if i < len(SCRIPTED_RESPONSES):
            return SCRIPTED_RESPONSES[i]
        return "No further comment."

    return _chat_fn


class TestCommunicatorSession(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="fable5-commune-test-"))
        self.skills_dir = self.tmp / "skills"
        self.memory_dir = self.tmp / "memory"
        self.agents_dir = self.tmp / "agents"  # deliberately empty -> built-in briefs

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_full_session_writes_transcript_and_skill(self):
        result = comm.run_communicator_session(
            "how should agents share what they learn",
            chat_fn=make_scripted_chat_fn(),
            rounds=5,
            agents_dir=self.agents_dir,
            skills_dir=self.skills_dir,
            memory_dir=self.memory_dir,
            self_improve=True,
            hitl=False,
        )

        # 1 proposal + 4 critique/refine rounds + 1 synthesis = 6 messages
        self.assertEqual(len(result.transcript), 6)
        self.assertEqual(result.transcript[0].kind, "proposal")
        self.assertEqual(result.transcript[0].author, "proposer")
        self.assertEqual(result.transcript[-1].kind, "synthesis")

        # critique/refinement should alternate and stay attributed correctly
        kinds = [m.kind for m in result.transcript[1:-1]]
        self.assertEqual(kinds, ["critique", "refinement", "critique", "refinement"])
        for m in result.transcript[1:-1]:
            if m.kind == "critique":
                self.assertEqual(m.author, "challenger")
            else:
                self.assertEqual(m.author, "proposer")

        # lessons extracted from the synthesizer's structured output
        self.assertGreaterEqual(len(result.lessons), 1)
        self.assertTrue(any("cap" in l.lower() or "prun" in l.lower() for l in result.lessons))

        # transcript persisted
        self.assertIsNotNone(result.memory_path)
        self.assertTrue(result.memory_path.exists())
        saved = result.memory_path.read_text(encoding="utf-8")
        self.assertIn("Round 1", saved)
        self.assertIn("proposer", saved)

        # skill file persisted (self_improve=True, hitl=False -> auto-approved)
        self.assertIsNotNone(result.skill_path)
        self.assertTrue(result.skill_path.exists())
        skill_text = result.skill_path.read_text(encoding="utf-8")
        self.assertIn("## Lessons", skill_text)
        self.assertIn("how should agents share what they learn", skill_text)

    def test_self_improve_off_writes_no_skill_file(self):
        result = comm.run_communicator_session(
            "topic",
            chat_fn=make_scripted_chat_fn(),
            rounds=3,
            agents_dir=self.agents_dir,
            skills_dir=self.skills_dir,
            memory_dir=self.memory_dir,
            self_improve=False,
            hitl=False,
        )
        self.assertIsNone(result.skill_path)
        self.assertEqual(list(self.skills_dir.glob("*.md")), [])

    def test_hitl_rejection_blocks_skill_write(self):
        result = comm.run_communicator_session(
            "topic",
            chat_fn=make_scripted_chat_fn(),
            rounds=3,
            agents_dir=self.agents_dir,
            skills_dir=self.skills_dir,
            memory_dir=self.memory_dir,
            self_improve=True,
            hitl=True,
            approve_fn=lambda skill_text: False,
        )
        self.assertIsNone(result.skill_path)
        self.assertEqual(list(self.skills_dir.glob("*.md")), [])

    def test_missing_persona_file_falls_back_to_builtin_brief(self):
        # agents_dir has no communicators/*.md at all -> should not raise
        result = comm.run_communicator_session(
            "topic",
            chat_fn=make_scripted_chat_fn(),
            agent_names=["proposer", "challenger", "synthesizer"],
            rounds=2,
            agents_dir=self.tmp / "does-not-exist",
            skills_dir=self.skills_dir,
            memory_dir=self.memory_dir,
            self_improve=False,
        )
        self.assertGreaterEqual(len(result.transcript), 2)

    def test_slugify_used_in_filenames_is_filesystem_safe(self):
        result = comm.run_communicator_session(
            "Weird / Topic: With ??? Punctuation!!",
            chat_fn=make_scripted_chat_fn(),
            rounds=2,
            agents_dir=self.agents_dir,
            skills_dir=self.skills_dir,
            memory_dir=self.memory_dir,
            self_improve=True,
            hitl=False,
        )
        self.assertTrue(result.memory_path.exists())
        self.assertNotIn("/", result.memory_path.name.replace(str(self.memory_dir), ""))


if __name__ == "__main__":
    unittest.main(verbosity=2)
