#!/usr/bin/env python3
"""Build ref-papers/ with unambiguous REFERENCE filenames.

PDFs copied into git must stay under ~200MB total. Larger files remain
in the gitignored cache; extracts are still copied.

Naming: {year}-{tier}-{team_id}-{problem_title}.pdf
"""

from __future__ import annotations

import csv
import re
import shutil
from pathlib import Path

from _paths import REF_PAPERS, RESEARCH

ILLEGAL = re.compile(r'[<>:"/\\|?*]')
TIER_MAP = {
    "first": "first",
    "second": "second",
    "third": "third",
    "participation": "participation",
}
MAX_TOTAL = 190_000_000
MAX_ONE = 8_000_000
CODED_2024 = {
    "A24102940057",
    "A24103350007",
    "B24102860287",
    "B24104760033",
    "C24103860012",
    "C24104220149",
    "D24103850092",
    "D24104250063",
    "E24101480006",
    "E24102870008",
    "F24102870082",
    "F24910020063",
}


def slug(text: str, max_len: int = 36) -> str:
    t = (text or "").strip()
    t = ILLEGAL.sub("", t)
    t = re.sub(r"\s+", "", t)
    return (t[:max_len] if t else "untitled")


def tier_of(row: dict) -> str:
    if (row.get("corpus_layer") or "") == "recency-report":
        return "report"
    return TIER_MAP.get(row.get("award_tier_normalized") or "", "unknown")


def dest_stem(row: dict) -> str | None:
    year = row.get("year") or ""
    team = row.get("team_id") or ""
    if not re.match(r"^\d{4}$", year) or not team:
        return None
    title = row.get("problem_title") or row.get("paper_title") or team
    return f"{year}-{tier_of(row)}-{team}-{slug(title)}"


def src_pdf(row: dict, cache_pdf: Path) -> Path | None:
    for cand in (
        cache_pdf / (row.get("filename") or ""),
        cache_pdf / f"{row.get('record_id')}.pdf",
    ):
        if cand.is_file():
            return cand
    return None


def eligible(row: dict, src: Path) -> bool:
    if src.stat().st_size > MAX_ONE:
        return False
    if row.get("deep_review") == "yes" and row.get("award_tier_normalized") in {
        "first",
        "participation",
    }:
        return True
    if row.get("team_id") in CODED_2024:
        return True
    return False


def main() -> int:
    dest_dir = REF_PAPERS / "pdf"
    extract_dest = REF_PAPERS / "extracts"
    dest_dir.mkdir(parents=True, exist_ok=True)
    extract_dest.mkdir(parents=True, exist_ok=True)
    for old in dest_dir.glob("*.pdf"):
        old.unlink()
    cache_pdf = RESEARCH / "cache" / "papers"
    cache_ext = RESEARCH / "cache" / "extracts"
    with (RESEARCH / "corpus-manifest.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    index_rows = []
    copied = 0
    total = 0
    candidates = []
    for row in rows:
        stem = dest_stem(row)
        if not stem:
            continue
        src = src_pdf(row, cache_pdf)
        ext_src = cache_ext / f"{row.get('record_id')}.txt"
        if ext_src.is_file():
            shutil.copy2(ext_src, extract_dest / f"{stem}.txt")
        rec = {
            "ref_filename": f"{stem}.pdf",
            "record_id": row.get("record_id"),
            "year": row.get("year"),
            "tier": tier_of(row),
            "team_id": row.get("team_id"),
            "problem_title": row.get("problem_title"),
            "in_git_pdf": "no",
            "role": "REFERENCE_ONLY",
            "blob_sha": row.get("blob_sha"),
            "verification_status": row.get("verification_status"),
        }
        if src and eligible(row, src):
            candidates.append((src.stat().st_size, src, stem, rec))
        else:
            index_rows.append(rec)

    candidates.sort(key=lambda x: x[0])
    for size, src, stem, rec in candidates:
        if total + size > MAX_TOTAL:
            index_rows.append(rec)
            continue
        shutil.copy2(src, dest_dir / f"{stem}.pdf")
        rec["in_git_pdf"] = "yes"
        index_rows.append(rec)
        copied += 1
        total += size

    fields = [
        "ref_filename",
        "record_id",
        "year",
        "tier",
        "team_id",
        "problem_title",
        "in_git_pdf",
        "role",
        "blob_sha",
        "verification_status",
    ]
    with (REF_PAPERS / "manifest.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(sorted(index_rows, key=lambda r: r["ref_filename"] or ""))
    print(f"pdf_in_git={copied} bytes={total} extracts={len(list(extract_dest.glob('*.txt')))} index={len(index_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
