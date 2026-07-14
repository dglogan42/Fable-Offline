#!/usr/bin/env python3
"""
Standalone test for fable5_communicators.py — stdlib unittest only.
"""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import fable5_communicators as comm  # noqa: E402


SCRIPTED_RESPONSES = [
    "Ship a single shared markdown skills file that every agent reads before responding. Assumption: agents run sequentially, not in parallel. Biggest risk: the file grows unbounded and blows the context budget.",
    "The unbounded-growth risk is real but understated: you never described a pruning or ranking step, so after a few dozen sessions the most useful lessons get buried under noise and stop being read at all.",
    "Refined: cap the bundle at N most-recent-and-highest-signal entries and drop low-value ones on write, addressing the burial risk directly.",
    "Fine as far as it goes, but 'highest-signal' is undefined — without a concrete signal it just becomes 'most recent', which is the same unbounded-growth problem wearing a cap.",
    "Refined further: track a simple usage counter per skill file and prefer high-usage + recent over recency alone when trimming.",
    (
        "FINAL APPROACH\n"
        "Write each session's takeaway to its own skill file, and when trimming the bundle prefer files with higher usage counts, breaking ties by recency, rather than pure recency.\n\n"
        "LESSONS\n"
        "- Always cap any growing shared-context bundle instead of letting it grow unbounded.\n"
        "- Prefer usage-weighted pruning over pure recency when trimming a shared knowledge store."
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
        self.agents_dir = self.tmp / "agents"

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

        self.assertEqual(len(result.transcript), 6)
        self.assertEqual(result.transcript[0].kind, "proposal")
        self.assertEqual(result.transcript[-1].kind, "synthesis")
        self.assertIsNotNone(result.memory_path)
        self.assertTrue(result.memory_path.exists())
        self.assertIsNotNone(result.skill_path)
        self.assertTrue(result.skill_path.exists())

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
