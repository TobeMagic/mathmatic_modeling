"""Runtime pack contains only the whitelist."""

from __future__ import annotations

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pack_skill import pack  # noqa: E402

FORBIDDEN = (
    "research/",
    "quality/",
    "evals/",
    "cache/",
    ".pdf",
    "ingest_corpus.py",
    "ingest_local_papers.py",
    "test_validate_submission.py",
)


class PackSkillTests(unittest.TestCase):
    def test_whitelist_and_no_research(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "huawei-cup-modeling.skill"
            pack(dest)
            names = zipfile.ZipFile(dest).namelist()
        self.assertTrue(any(n.endswith("SKILL.md") for n in names))
        self.assertTrue(any("scaffold_workspace.py" in n for n in names))
        joined = "\n".join(names)
        for token in FORBIDDEN:
            self.assertNotIn(token, joined, msg=token)
        self.assertFalse(any("research/distillation" in n for n in names))


if __name__ == "__main__":
    unittest.main()
