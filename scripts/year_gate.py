#!/usr/bin/env python3
"""Fetch the official contest notice list and report whether 2026 ops files exist."""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
from datetime import date
from pathlib import Path

PORTAL = "https://cpipc.acge.org.cn/cw/hp/4"
NEWS = "https://cpipc.acge.org.cn/cw/contestNews/list/4/1"
UA = "huawei-cup-modeling-skill/0.1 (year-gate)"


def decode_body(data: bytes) -> str:
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", "replace")


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return decode_body(resp.read())


def notice_hits(html: str) -> list[str]:
    hits = []
    for pat, label in (
        (r"第二十三届[^<>\n]{0,12}参赛邀请函", "2026-invitation"),
        (r"第二十三届[^<>\n]{0,12}开赛公告", "2026-opening"),
        (r"2026年[^<>\n]{0,12}开赛公告", "2026-opening"),
        (r"第二十三届[^<>\n]{0,20}论文标准文档", "2026-template"),
        (r"第二十三届[^<>\n]{0,20}人工智能工具", "2026-ai"),
    ):
        if re.search(pat, html) and label not in hits:
            hits.append(label)
    return hits


def classify_html(html: str) -> dict:
    hits = notice_hits(html)
    opening = "2026-opening" in hits
    return {
        "as_of": date.today().isoformat(),
        "portal": PORTAL,
        "has_2026_invitation": "2026-invitation" in hits,
        "has_2026_opening_notice": opening,
        "has_2026_template_notice": "2026-template" in hits,
        "has_2026_ai_annex": "2026-ai" in hits,
        "notice_hits": hits,
        "operational_tag": "year=2026" if opening else "year=2025-provisional",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    report = classify_html(fetch(NEWS))
    text = json.dumps(report, ensure_ascii=False, indent=2)
    print(text)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
