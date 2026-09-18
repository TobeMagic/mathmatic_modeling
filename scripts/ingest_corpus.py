#!/usr/bin/env python3
"""Download selected PDFs into the gitignored cache and extract text.

Default: one first-prize paper per year-letter cell from the deep sample,
plus verified non-first controls. Original PDFs are not committed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from _paths import RESEARCH, REPO_ROOT as ROOT
CACHE_PDF = RESEARCH / "cache" / "papers"
EXTRACT = RESEARCH / "cache" / "extracts"
MANIFEST = RESEARCH / "corpus-manifest.csv"
UA = "huawei-cup-modeling-skill/0.1 (research)"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def github_raw(row: dict) -> str | None:
    url = row.get("source_url") or ""
    if "github.com" not in url or "/blob/" not in url:
        return None
    return url.replace("https://github.com/", "https://raw.githubusercontent.com/").replace("/blob/", "/")


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


def load_rows() -> list[dict]:
    with MANIFEST.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def select_ingest(rows: list[dict], per_cell: int, controls: bool) -> list[dict]:
    buckets: dict[str, list[dict]] = defaultdict(list)
    chosen = []
    for row in rows:
        if row.get("document_type") != "full-paper-pdf":
            continue
        if row.get("deep_review") == "yes" and row.get("award_tier_normalized") == "first":
            buckets[row["year_letter_stratum"]].append(row)
        elif controls and row.get("award_tier_normalized") in {"second", "third", "participation"}:
            chosen.append(row)
    for _, items in sorted(buckets.items()):
        chosen.extend(items[:per_cell])
    seen = set()
    out = []
    for row in chosen:
        if row["record_id"] in seen:
            continue
        seen.add(row["record_id"])
        out.append(row)
    return out


def download_one(row: dict) -> dict:
    dest = CACHE_PDF / f"{row['record_id']}.pdf"
    raw = github_raw(row)
    status = "skip"
    digest = ""
    if dest.exists():
        digest = sha256_bytes(dest.read_bytes())
        status = "cached"
    elif raw:
        req = urllib.request.Request(raw, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = resp.read()
            dest.write_bytes(data)
            digest = sha256_bytes(data)
            status = "downloaded"
        except Exception as exc:  # noqa: BLE001
            status = f"error:{exc}"
    extract_path = EXTRACT / f"{row['record_id']}.txt"
    nchars = 0
    paper_title = ""
    if dest.exists() and dest.stat().st_size > 1000:
        text = extract_text(dest)
        extract_path.write_text(text, encoding="utf-8", errors="replace")
        nchars = len(text)
        paper_title = guess_title(text)
    return {
        "record_id": row["record_id"],
        "status": status,
        "sha256": digest,
        "extract_chars": nchars,
        "paper_title": paper_title,
        "source_url": row.get("source_url"),
    }


def guess_title(text: str) -> str:
    import re

    for pat in (
        r"题\s*目[：:\s]+([^\n]{6,80})",
        r"题目[：:\s]+([^\n]{6,80})",
    ):
        m = re.search(pat, text)
        if m:
            return re.sub(r"\s+", " ", m.group(1)).strip()[:80]
    return ""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--per-cell", type=int, default=1)
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--no-controls", action="store_true")
    args = parser.parse_args()
    CACHE_PDF.mkdir(parents=True, exist_ok=True)
    EXTRACT.mkdir(parents=True, exist_ok=True)
    rows = select_ingest(load_rows(), args.per_cell, controls=not args.no_controls)
    if not args.download:
        for row in rows:
            dest = CACHE_PDF / f"{row['record_id']}.pdf"
            print(json.dumps({"record_id": row["record_id"], "cached": dest.exists()}, ensure_ascii=False))
        return
    index = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futs = [pool.submit(download_one, row) for row in rows]
        for fut in as_completed(futs):
            item = fut.result()
            index.append(item)
            print(json.dumps(item, ensure_ascii=False), flush=True)
    index.sort(key=lambda r: r["record_id"])
    (EXTRACT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
