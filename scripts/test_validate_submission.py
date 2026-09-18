"""Tests for mechanical Huawei Cup PDF checks."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import REPO_ROOT as ROOT  # noqa: E402

from validate_submission import (  # noqa: E402
    check_filename,
    check_magic,
    check_pages,
    main,
)


def ok_pages() -> list[str]:
    return [
        "封面 中国研究生数学建模竞赛",
        "题目 测试\n摘要：建模思路、主要方法、模型与结果。创新点是对照实验。\n关键词：调度；基线\n",
        "一、问题重述\n二、模型假设\n三、符号说明\n见图 1。\n图 1 技术路线\n见表 1。\n表 1 结果\n参考文献\n[1] 例\n人工智能工具未作为核心方法，仅用于语法检查。\n",
    ]


class FilenameTests(unittest.TestCase):
    def test_accepts_2025_pattern(self):
        self.assertEqual(check_filename("A25000010001.pdf", 2025), [])

    def test_rejects_wrong_stem(self):
        issues = check_filename("paper.pdf", 2025)
        self.assertEqual(issues[0].code, "filename")


class PageTests(unittest.TestCase):
    def test_clean_draft_has_no_errors(self):
        errors = [i for i in check_pages(ok_pages(), 2025) if i.severity == "error"]
        self.assertEqual(errors, [])

    def test_identity_after_cover(self):
        pages = ok_pages()
        pages[1] += "\n队员姓名 张三\n"
        codes = [i.code for i in check_pages(pages, 2025)]
        self.assertIn("identity", codes)

    def test_missing_abstract(self):
        pages = ["封面", "正文 问题重述 假设 符号 参考文献"]
        codes = [i.code for i in check_pages(pages, 2025)]
        self.assertIn("abstract-missing", codes)

    def test_abstract_longer_than_two_pages(self):
        pages = [
            "封面",
            "摘要：建模思路 方法 模型 第一页",
            "摘要续页，尚未结束",
            "摘要仍在第三页",
            "关键词：调度\n问题重述 假设 符号 参考文献",
        ]
        codes = [i.code for i in check_pages(pages, 2025)]
        self.assertIn("abstract-length", codes)

    def test_missing_references_is_error(self):
        pages = [
            "封面",
            "摘要：思路 方法 模型\n关键词：a",
            "问题重述 假设 符号 图 1 见图 1",
        ]
        codes = [i.code for i in check_pages(pages, 2025)]
        self.assertIn("section-references", codes)

    def test_unrefed_figure_is_warning(self):
        pages = ok_pages()
        pages[2] += "\n图 9 装饰\n"
        warnings = [i.code for i in check_pages(pages, 2025) if i.severity == "warning"]
        self.assertIn("figure-unref", warnings)

    def test_ai_warning_when_silent_in_2025(self):
        pages = [
            "封面",
            "摘要：建模思路、主要方法、模型。\n关键词：a",
            "问题重述 假设 符号 见图 1。图 1 x 参考文献 [1]",
        ]
        codes = [i.code for i in check_pages(pages, 2025)]
        self.assertIn("ai-disclosure", codes)

    def test_ai_not_required_before_2025(self):
        pages = [
            "封面",
            "摘要：建模思路、主要方法、模型。\n关键词：a",
            "问题重述 假设 符号 见图 1。图 1 x 参考文献 [1]",
        ]
        codes = [i.code for i in check_pages(pages, 2024)]
        self.assertNotIn("ai-disclosure", codes)


class PdfSmokeTests(unittest.TestCase):
    def test_zip_is_rejected(self, tmp_path: Path | None = None):
        folder = Path(__file__).parent / "fixtures"
        folder.mkdir(exist_ok=True)
        zip_path = folder / "A25000010001.pdf"
        zip_path.write_bytes(b"PK\x03\x04fake")
        issues = check_magic(zip_path)
        self.assertEqual(issues[0].code, "archive")
        zip_path.unlink()

    def test_cli_missing_file(self):
        self.assertEqual(main(["no-such.pdf"]), 2)


if __name__ == "__main__":
    unittest.main()
