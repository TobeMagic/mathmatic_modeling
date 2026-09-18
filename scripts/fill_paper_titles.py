#!/usr/bin/env python3
"""Copy extract paper titles into corpus-manifest.csv (in-repo metadata only)."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from _paths import RESEARCH

MANIFEST = RESEARCH / "corpus-manifest.csv"
INDEX = RESEARCH / "cache" / "extracts" / "index.json"


def clean_title(raw: str, fallback: str) -> str:
    t = (raw or "").strip()
    if not t or t.startswith("!") or "摘要" in t or "摘 要" in t or len(t) > 60:
        return fallback
    return t


def main() -> None:
    titles = {r["record_id"]: (r.get("paper_title") or "").strip() for r in json.loads(INDEX.read_text(encoding="utf-8"))}
    with MANIFEST.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys())
    n = 0
    for row in rows:
        t = clean_title(titles.get(row["record_id"], ""), row.get("problem_title") or "")
        if t and t != row.get("paper_title"):
            row["paper_title"] = t
            n += 1
    with MANIFEST.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(json.dumps({"updated_titles": n, "index": len(titles)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
