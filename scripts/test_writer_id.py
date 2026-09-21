"""writer_id slug and contest-git identity."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from writer_id import LEDGER_HEADER, main, resolve_slug, slugify  # noqa: E402


def _clean_git_env(home: Path) -> dict[str, str]:
    env = os.environ.copy()
    env["HOME"] = str(home)
    env["USERPROFILE"] = str(home)
    env["GIT_CONFIG_GLOBAL"] = str(home / "gitconfig-missing")
    env["GIT_CONFIG_SYSTEM"] = os.devnull
    return env


class SlugTests(unittest.TestCase):
    def test_ascii_name(self):
        self.assertEqual(slugify("Alice Smith"), "alice-smith")

    def test_email_fallback_when_name_non_ascii(self):
        self.assertEqual(resolve_slug("戴兆吉", "casperdai@example.com"), "casperdai")

    def test_email_only(self):
        self.assertEqual(resolve_slug("", "Bob.Lee@x.com"), "bob-lee")

    def test_empty(self):
        self.assertEqual(resolve_slug("", ""), "")


class ContestGitTests(unittest.TestCase):
    def test_missing_git_exits(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "contest"
            dest.mkdir()
            with self.assertRaises(SystemExit):
                main(["--contest", str(dest)])

    def test_missing_user_exits(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / "home"
            home.mkdir()
            dest = Path(tmp) / "contest"
            dest.mkdir()
            env = _clean_git_env(home)
            subprocess.run(
                ["git", "init"], cwd=dest, check=True, capture_output=True, env=env
            )
            with patch.dict(os.environ, env, clear=False):
                with self.assertRaises(SystemExit):
                    main(["--contest", str(dest)])

    def test_init_writes_shards(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / "home"
            home.mkdir()
            dest = Path(tmp) / "contest"
            dest.mkdir()
            env = _clean_git_env(home)
            subprocess.run(
                ["git", "init"], cwd=dest, check=True, capture_output=True, env=env
            )
            subprocess.run(
                ["git", "config", "user.name", "Alice Smith"],
                cwd=dest,
                check=True,
                capture_output=True,
                env=env,
            )
            with patch.dict(os.environ, env, clear=False):
                self.assertEqual(main(["--contest", str(dest), "--init"]), 0)
            act = dest / "plans" / "activity" / "alice-smith.md"
            led = dest / "results" / "ledger" / "alice-smith.csv"
            self.assertTrue(act.is_file())
            self.assertTrue(led.is_file())
            self.assertTrue(led.read_text(encoding="utf-8").startswith(LEDGER_HEADER))
            self.assertIn("alice-smith", act.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
