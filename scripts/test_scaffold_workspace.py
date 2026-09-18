"""Smoke test for contest workspace scaffold."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from scaffold_workspace import main  # noqa: E402


class ScaffoldTests(unittest.TestCase):
    def test_creates_tree_and_ledger(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "contest"
            self.assertEqual(main(["--dest", str(dest)]), 0)
            self.assertTrue((dest / "plans" / "STATE.md").is_file())
            self.assertTrue((dest / "plans" / "PROJECT.md").is_file())
            self.assertTrue((dest / "plans" / "experiment-matrix.md").is_file())
            self.assertTrue((dest / "results" / "result-ledger.csv").is_file())
            self.assertTrue((dest / "code" / "q1").is_dir())
            self.assertTrue((dest / "experiments" / "configs").is_dir())
            self.assertTrue((dest / "experiments" / "runs" / "README.md").is_file())
            self.assertTrue((dest / "paper" / "sections" / "abstract.md").is_file())
            self.assertFalse((dest / "compliance").exists())
            self.assertFalse((dest / "reviews").exists())
            self.assertFalse((dest / "state").exists())
            self.assertFalse((dest / "src").exists())
            text = (dest / "plans" / "STATE.md").read_text(encoding="utf-8")
            self.assertIn("current_stage: S0", text)
            self.assertNotIn("角色：M", text)


if __name__ == "__main__":
    unittest.main()
