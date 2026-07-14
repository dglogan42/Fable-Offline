#!/usr/bin/env python3
"""Tests for randomized MBTI feedback-loop helpers."""

import importlib
import os
import random
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mbti_types import VALID_TYPES, build_feedback_loop_prompt, sample_mbti_types  # noqa: E402
from fable5_offline_agent import (  # noqa: E402
    AUTO_MBTI_FEEDBACK,
    maybe_append_mbti_feedback_prompt,
    resolve_mbti_feedback_enabled,
)


class TestMBTIFeedbackLoop(unittest.TestCase):
    def test_sample_mbti_types_is_repeatable_with_seed(self):
        rng = random.Random(7)
        selected = sample_mbti_types(3, rng=rng)
        self.assertEqual(len(selected), 3)
        self.assertTrue(all(code in VALID_TYPES for code in selected))
        self.assertEqual(len(set(selected)), len(selected))

    def test_feedback_prompt_includes_topic_and_agent_roles(self):
        prompt = build_feedback_loop_prompt(
            "Improve the launch plan",
            agent_types=["INTJ", "ENFP", "ISFJ"],
            rounds=2,
            randomize=True,
            seed=9,
        )
        self.assertIn("Improve the launch plan", prompt)
        self.assertIn("INTJ", prompt)
        self.assertIn("ENFP", prompt)
        self.assertIn("ISFJ", prompt)
        self.assertIn("Round 1", prompt)

    def test_loop_prompt_includes_mbti_feedback_guidance(self):
        prompt = maybe_append_mbti_feedback_prompt(
            "Existing prompt",
            topic="Improve the launch plan",
            cycle=2,
            randomize=True,
            seed=5,
        )
        self.assertIn("Existing prompt", prompt)
        self.assertIn("Improve the launch plan", prompt)
        self.assertIn("MBTI feedback loop", prompt)

    def test_auto_feedback_toggle_is_configurable(self):
        import fable5_offline_agent as offline_agent

        with mock.patch.dict(os.environ, {"FABLE5_AUTO_MBTI_FEEDBACK": "0"}, clear=False):
            reloaded = importlib.reload(offline_agent)
            self.assertFalse(reloaded.AUTO_MBTI_FEEDBACK)
            self.assertFalse(reloaded.resolve_mbti_feedback_enabled(env_enabled=reloaded.AUTO_MBTI_FEEDBACK, cli_override=None))

        with mock.patch.dict(os.environ, {"FABLE5_AUTO_MBTI_FEEDBACK": "1"}, clear=False):
            reloaded = importlib.reload(offline_agent)
            self.assertTrue(reloaded.AUTO_MBTI_FEEDBACK)
            self.assertFalse(reloaded.resolve_mbti_feedback_enabled(env_enabled=reloaded.AUTO_MBTI_FEEDBACK, cli_override=False))
            self.assertTrue(reloaded.resolve_mbti_feedback_enabled(env_enabled=reloaded.AUTO_MBTI_FEEDBACK, cli_override=True))


if __name__ == "__main__":
    unittest.main(verbosity=2)
