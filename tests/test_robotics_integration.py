#!/usr/bin/env python3
"""Tests for robotics integration in the offline agent."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fable5_offline_agent import build_robotics_context  # noqa: E402


class TestRoboticsIntegration(unittest.TestCase):
    def test_robotics_context_includes_cross_domain_guidance(self):
        context = build_robotics_context(
            "Design a rehab robot arm",
            include_engineer=True,
            include_education=True,
            include_health=True,
            include_physics=True,
            include_data=True,
            include_reasoning=True,
        )
        self.assertIn("robotics", context.lower())
        self.assertIn("engineer", context.lower())
        self.assertIn("education", context.lower())
        self.assertIn("health", context.lower())
        self.assertIn("physics", context.lower())
        self.assertIn("data", context.lower())
        self.assertIn("reason", context.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
