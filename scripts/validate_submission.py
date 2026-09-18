#!/usr/bin/env python3
"""Mechanical submission checks for Huawei Cup PDFs.

This is not a modeling-quality judge. Official templates and dates change
every year; default filename pattern follows the 2025 notice and must be
re-checked when 2026 attachments appear.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

FILENAME_RE = {
    2025: re.compile(r"^[A-F]\d{11}\.pdf$", re.IGNORECASE),
    2026: re.compile(r"^[A-F]\d{11}\.pdf$", re.IGNORECASE),
}

IDENTITY_PATTERNS = [
    re.compile(r"队员姓名"),
    re.compile(r"参赛队号"),
    re.compile(r"学\s*号"),
    re.compile(r"指导教师"),
    re.compile(r"学\s*校\s*[:：]"),
    re.compile(r"^学\s*校\s+\S", re.M),
]

ABSTRACT_START = re.compile(r"摘\s*要")
KEYWORDS_HEADING = re.compile(r"关\s*键\s*词\s*[:：]|^\s*关\s*键\s*词\s*$", re.M)
SECTION_PATTERNS = {
    "restatement": re.compile(r"问题重述"),
    "assumptions": re.compile(r"假设"),
    "symbols": re.compile(r"符号"),
    "references": re.compile(r"参考文献"),
}
FIGURE_REF = re.compile(r"图\s*[-–]?\s*\d+")
TABLE_REF = re.compile(r"表\s*[-–]?\s*\d+")
AI_HINT = re.compile(r"人工智能|大模型|ChatGPT|生成式|AI\s*工具|披露")


@dataclass
class Issue:
    severity: str  # error | warning
    code: str
    message: str
    page: int | None = None


def check_filename(name: str, year: int) -> list[Issue]:
    pat = FILENAME_RE.get(year, FILENAME_RE[2025])
    if pat.match(name):
        return []
    return [
        Issue(
            "error",
            "filename",
            f"{name} does not match {pat.pattern} for year={year}. "
            "Re-check the current official notice before treating this as final.",
        )
    ]


def check_magic(path: Path) -> list[Issue]:
    data = path.read_bytes()[:8]
    if data.startswith(b"PK"):
        return [Issue("error", "archive", "File is a ZIP/Office archive, not an uncompressed PDF.")]
    if not data.startswith(b"%PDF"):
        return [Issue("error", "magic", "File does not start with %PDF.")]
    return []


def extract_pages(path: Path) -> tuple[list[str], list[Issue]]:
    try:
        from pypdf import PdfReader
    except ImportError:
        return [], [Issue("error", "dep", "pypdf is required: pip install pypdf")]
    try:
        reader = PdfReader(str(path))
    except Exception as exc:  # noqa: BLE001
        return [], [Issue("error", "read", f"Cannot read PDF: {exc}")]
    if getattr(reader, "is_encrypted", False):
        return [], [Issue("error", "encrypted", "PDF is encrypted; 2025 notice asks for an uncompressed open PDF.")]
    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text.encode("utf-8", "replace").decode("utf-8"))
    if not pages:
        return [], [Issue("error", "empty", "PDF has no pages.")]
    return pages, []


def check_identity(pages: list[str]) -> list[Issue]:
    issues = []
    for idx, text in enumerate(pages[1:], start=2):
        for pat in IDENTITY_PATTERNS:
            if pat.search(text):
                issues.append(
                    Issue(
                        "error",
                        "identity",
                        f"Possible identity leak matching /{pat.pattern}/ after cover.",
                        page=idx,
                    )
                )
                break
    return issues


def _abstract_page_count(pages: list[str], start: int) -> int:
    """Pages from 摘要 through 关键词, excluding 目录/问题重述 that follow."""
    count = 0
    for idx in range(start, len(pages)):
        text = pages[idx]
        if idx > start and re.search(r"目\s*录|问题重述", text) and not ABSTRACT_START.search(text):
            break
        count += 1
        if KEYWORDS_HEADING.search(text):
            break
        if count > 8:
            break
    return max(count, 1)


def check_abstract(pages: list[str]) -> list[Issue]:
    issues = []
    start = None
    for idx, text in enumerate(pages):
        if ABSTRACT_START.search(text):
            start = idx
            break
    if start is None:
        return [Issue("error", "abstract-missing", "No 摘要 marker found.")]
    if start == 0:
        issues.append(
            Issue(
                "warning",
                "abstract-on-cover",
                "摘要 appears on page 1. 2025 notice puts the cover on page 1 and the abstract from page 2.",
                page=1,
            )
        )
    page_count = _abstract_page_count(pages, start)
    if page_count > 2:
        issues.append(
            Issue(
                "error",
                "abstract-length",
                f"Abstract appears to span {page_count} pages; 2025 cap is 2.",
                page=start + 1,
            )
        )
    window = "\n".join(pages[start : start + page_count])
    needed = ["思路", "方法", "模型"]
    missing_bits = [w for w in needed if w not in window]
    if missing_bits:
        issues.append(
            Issue(
                "warning",
                "abstract-coverage",
                f"Abstract pages may be missing official coverage words: {missing_bits}.",
                page=start + 1,
            )
        )
    return issues


def check_sections(pages: list[str]) -> list[Issue]:
    blob = "\n".join(pages)
    issues = []
    for code, pat in SECTION_PATTERNS.items():
        if not pat.search(blob):
            sev = "error" if code in {"restatement", "references"} else "warning"
            issues.append(Issue(sev, f"section-{code}", f"Missing marker for {code} ({pat.pattern})."))
    return issues


def check_floats(pages: list[str]) -> list[Issue]:
    blob = "\n".join(pages)
    issues = []
    figures = {m.group(0).replace(" ", "") for m in FIGURE_REF.finditer(blob)}
    for fig in sorted(figures):
        # normalize 图1 vs 图 1
        n = re.sub(r"\s+", "", fig)
        count = len(re.findall(r"图\s*" + re.escape(re.sub(r"^图", "", n)), blob))
        if count < 2:
            issues.append(
                Issue(
                    "warning",
                    "figure-unref",
                    f"{n} appears once; caption or in-text citation may be missing.",
                )
            )
    tables = {re.sub(r"\s+", "", m.group(0)) for m in TABLE_REF.finditer(blob)}
    for tab in sorted(tables):
        n = re.sub(r"^表", "", tab)
        count = len(re.findall(r"表\s*" + re.escape(n), blob))
        if count < 2:
            issues.append(
                Issue(
                    "warning",
                    "table-unref",
                    f"表{n} appears once; caption or in-text citation may be missing.",
                )
            )
    return issues


def check_ai(pages: list[str], year: int) -> list[Issue]:
    if year < 2025:
        return []
    blob = "\n".join(pages)
    if AI_HINT.search(blob):
        return []
    return [
        Issue(
            "warning",
            "ai-disclosure",
            f"year={year}: no AI-related disclosure keywords found. "
            "If tools were used, the current-year annex may require a log. "
            "If 2026 annex is unpublished, treat this as a team-internal reminder.",
        )
    ]


def check_pages(pages: list[str], year: int) -> list[Issue]:
    issues: list[Issue] = []
    issues.extend(check_identity(pages))
    issues.extend(check_abstract(pages))
    issues.extend(check_sections(pages))
    issues.extend(check_floats(pages))
    issues.extend(check_ai(pages, year))
    return issues


def validate_path(path: Path, year: int) -> list[Issue]:
    issues = []
    issues.extend(check_filename(path.name, year))
    issues.extend(check_magic(path))
    if any(i.code in {"magic", "archive"} and i.severity == "error" for i in issues):
        return issues
    pages, read_issues = extract_pages(path)
    issues.extend(read_issues)
    if pages:
        issues.extend(check_pages(pages, year))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Huawei Cup PDF mechanical checks")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--year", type=int, default=2025)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if not args.pdf.exists():
        print(f"missing file: {args.pdf}", file=sys.stderr)
        return 2
    issues = validate_path(args.pdf, args.year)
    if args.json:
        import json

        print(json.dumps([asdict(i) for i in issues], ensure_ascii=False, indent=2))
    else:
        if not issues:
            print("OK")
        for i in issues:
            loc = f" p.{i.page}" if i.page else ""
            print(f"{i.severity.upper():7} {i.code}{loc}: {i.message}")
    return 1 if any(i.severity == "error" for i in issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())
