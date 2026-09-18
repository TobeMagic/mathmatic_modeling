"""Unit tests for year-gate classification (no network)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from year_gate import classify_html  # noqa: E402


class YearGateTests(unittest.TestCase):
    def test_invitation_without_opening_stays_provisional(self):
        html = "“华为杯”第二十三届中国研究生数学建模竞赛参赛邀请函 2026年4月30日"
        r = classify_html(html)
        self.assertTrue(r["has_2026_invitation"])
        self.assertFalse(r["has_2026_opening_notice"])
        self.assertEqual(r["operational_tag"], "year=2025-provisional")

    def test_old_opening_notice_does_not_count(self):
        html = "华为杯第十八届中国研究生数学建模竞赛开赛公告"
        r = classify_html(html)
        self.assertFalse(r["has_2026_opening_notice"])

    def test_2026_opening_flips_tag(self):
        html = "第二十三届中国研究生数学建模竞赛开赛公告"
        r = classify_html(html)
        self.assertTrue(r["has_2026_opening_notice"])
        self.assertEqual(r["operational_tag"], "year=2026")


if __name__ == "__main__":
    unittest.main()
