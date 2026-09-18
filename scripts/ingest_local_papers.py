#!/usr/bin/env python3
"""Ingest local Huawei Cup PDFs into the gitignored cache and manifest.

Verifies team IDs against CPMCM-Awards CSVs. First-prize rows become
full-paper-core; other awards become controls. Does not commit PDFs.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path

from _paths import RESEARCH

MANIFEST = RESEARCH / "corpus-manifest.csv"
AWARDS = RESEARCH / "cache" / "awards"
CACHE_PDF = RESEARCH / "cache" / "papers"
EXTRACT = RESEARCH / "cache" / "extracts"
FILENAME_RE = re.compile(r"^([A-F])(\d{11})\.pdf$", re.I)

FIELDNAMES = [
    "record_id",
    "year",
    "edition",
    "problem_letter",
    "team_id",
    "problem_title",
    "paper_title",
    "document_type",
    "source_url",
    "host",
    "repository",
    "commit_ref",
    "filename",
    "size_bytes",
    "blob_sha",
    "award_claim_raw",
    "award_tier_normalized",
    "verification_status",
    "verification_secondary_url",
    "match_key",
    "corpus_layer",
    "year_letter_stratum",
    "archetype_tag",
    "selection_rule",
    "deep_review",
    "license_notes",
]

TITLES_2024 = {
    "A": "风电场有功功率优化分配",
    "B": "WLAN组网中网络吞吐量建模",
    "C": "数据驱动下磁性元件的磁芯损耗建模",
    "D": "大数据驱动的地理综合问题",
    "E": "高速公路应急车道紧急启用模型",
    "F": "X射线脉冲星光子到达时间建模",
}

ARCHETYPE_2024 = {
    "A": "optimization-scheduling",
    "B": "signal-inverse",
    "C": "prediction-diagnosis",
    "D": "image-spatial",
    "E": "optimization-scheduling",
    "F": "signal-inverse",
}

EDITION = {2022: 19, 2023: 20, 2024: 21, 2025: 22}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_text(pdf_path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return ""
    reader = PdfReader(str(pdf_path))
    chunks = []
    for i, page in enumerate(reader.pages[:40], start=1):
        text = page.extract_text() or ""
        chunks.append(f"\n\n--- page {i} ---\n{text.encode('utf-8', 'replace').decode('utf-8')}")
    return "".join(chunks)


def load_awards(year: int) -> dict[str, str]:
    path = AWARDS / f"{year}.csv"
    if not path.is_file():
        return {}
    out = {}
    with path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            tid = re.sub(r"^[A-Fa-f]", "", (row.get("队号") or row.get("参赛队号") or "").strip())
            award = (row.get("所获奖项") or "").strip()
            if tid:
                out[tid] = award
    return out


def normalize_award(raw: str) -> tuple[str, str]:
    if "一等奖" in raw:
        return "first", "full-paper-core"
    if "二等奖" in raw:
        return "second", "lower-tier-control"
    if "三等奖" in raw:
        return "third", "lower-tier-control"
    if "参与" in raw or "成功参与" in raw:
        return "participation", "lower-tier-control"
    return "unknown", "unverified"


def paper_title_from_text(text: str, fallback: str) -> str:
    for line in text.splitlines():
        t = line.strip()
        if 8 <= len(t) <= 60 and "摘要" not in t and not t.startswith("!") and "页" not in t:
            if re.search(r"[\u4e00-\u9fff]", t):
                return t
    return fallback


def load_manifest() -> tuple[list[dict], set[str]]:
    if not MANIFEST.is_file():
        return [], set()
    with MANIFEST.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return rows, {r["record_id"] for r in rows}


def write_manifest(rows: list[dict]) -> None:
    with MANIFEST.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", type=Path, required=True)
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--host", default="local-baidu")
    parser.add_argument("--pilot", type=int, default=0, help="ingest only N files (0=all)")
    args = parser.parse_args()

    awards = load_awards(args.year)
    rows, seen = load_manifest()
    pdfs = sorted(p for p in args.src.rglob("*.pdf") if FILENAME_RE.match(p.name))
    if args.pilot:
        pdfs = pdfs[: args.pilot]
    EXTRACT.mkdir(parents=True, exist_ok=True)
    CACHE_PDF.mkdir(parents=True, exist_ok=True)
    index_path = EXTRACT / "index.json"
    import json

    index: list[dict] = []
    if index_path.is_file():
        raw_index = json.loads(index_path.read_text(encoding="utf-8"))
        index = raw_index if isinstance(raw_index, list) else list(raw_index.values())
    indexed_ids = {item.get("record_id") for item in index}

    added = 0
    for pdf in pdfs:
        m = FILENAME_RE.match(pdf.name)
        letter, digits = m.group(1).upper(), m.group(2)
        team = f"{letter}{digits}"
        record_id = f"{args.year}-{team}"
        if record_id in seen:
            continue
        raw_award = awards.get(digits, "")
        tier, layer = normalize_award(raw_award) if raw_award else ("unknown", "unverified")
        dest = CACHE_PDF / f"{record_id}.pdf"
        dest.write_bytes(pdf.read_bytes())
        digest = sha256_file(dest)
        text = extract_text(dest)
        garbled = (not text) or text.count("\ufffd") > 20
        extract_file = EXTRACT / f"{record_id}.txt"
        extract_file.write_text(text, encoding="utf-8")
        problem = TITLES_2024.get(letter, "") if args.year == 2024 else ""
        title = paper_title_from_text(text, problem)
        if record_id not in indexed_ids:
            index.append(
                {
                    "record_id": record_id,
                    "status": "local-ingest",
                    "sha256": digest,
                    "extract_chars": len(text),
                    "paper_title": title,
                    "source_url": str(pdf),
                    "garbled": garbled,
                }
            )
            indexed_ids.add(record_id)
        rows.append(
            {
                "record_id": record_id,
                "year": str(args.year),
                "edition": str(EDITION.get(args.year, "")),
                "problem_letter": letter,
                "team_id": team,
                "problem_title": problem,
                "paper_title": title,
                "document_type": "full-paper-pdf",
                "source_url": str(pdf),
                "host": args.host,
                "repository": "",
                "commit_ref": "",
                "filename": pdf.name,
                "size_bytes": str(pdf.stat().st_size),
                "blob_sha": digest,
                "award_claim_raw": raw_award or "unverified",
                "award_tier_normalized": tier,
                "verification_status": "team-id-matched" if raw_award else "unverified",
                "verification_secondary_url": "https://github.com/lcpmgh/CPMCM-Awards/tree/master/awardlist",
                "match_key": team,
                "corpus_layer": layer if raw_award else "unverified",
                "year_letter_stratum": f"{args.year}-{letter}",
                "archetype_tag": ARCHETYPE_2024.get(letter, "") if args.year == 2024 else "",
                "selection_rule": "local-folder-crosschecked-against-award-csv",
                "deep_review": "yes" if tier == "first" else "no",
                "license_notes": "third-party mirror; do not redistribute; local cache only",
            }
        )
        seen.add(record_id)
        added += 1
        print(f"{record_id}\t{tier}\t{raw_award or 'NO_CSV'}\tgarbled={garbled}")

    write_manifest(rows)
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"added={added} manifest={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
