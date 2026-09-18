#!/usr/bin/env python3
"""Build a traceable Huawei Cup paper corpus manifest.

Mirrors (GitHub) are used only to locate files. Award status is taken from
the independently maintained CPMCM-Awards transcription of official lists.
"""

from __future__ import annotations

import csv
import hashlib
import json
import random
import re
import urllib.request
from collections import defaultdict
from pathlib import Path

from _paths import RESEARCH, REPO_ROOT as ROOT
CACHE = RESEARCH / "cache"
MANIFEST = RESEARCH / "corpus-manifest.csv"
SAMPLE = RESEARCH / "deep-sample.json"
GITHUB_REPO = "zhanwen/MathModel"
COMMIT = "master"
UA = "huawei-cup-modeling-skill/0.1 (research; +https://github.com)"

PROBLEM_TITLES = {
    (2022, "A"): "移动场景超分辨定位问题",
    (2022, "B"): "方形件组批优化问题",
    (2022, "C"): "汽车制造涂装-总装缓存调序区调度优化问题",
    (2022, "D"): "PISA架构芯片资源排布问题",
    (2022, "E"): "草原放牧策略研究",
    (2022, "F"): "COVID-19疫情期间生活物资的科学管理问题",
    (2023, "A"): "WLAN网络信道接入机制建模",
    (2023, "B"): "DFT类矩阵的整数分解逼近",
    (2023, "C"): "大规模创新类竞赛评审方案研究",
    (2023, "D"): "区域双碳目标与路径规划研究",
    (2023, "E"): "出血性脑卒中临床智能诊疗建模",
    (2023, "F"): "强对流降水临近预报",
    (2024, "A"): "风电场有功功率优化调度",
    (2024, "B"): "WLAN组网中网络吞吐量建模",
    (2024, "C"): "数据驱动下磁性元件的磁芯损耗建模",
    (2024, "D"): "大数据驱动的地理综合问题",
    (2024, "E"): "高速公路应急车道启用建模",
    (2024, "F"): "X射线脉冲星光子到达时间建模",
    (2025, "A"): "通用神经网络处理器下的核内调度问题",
    (2025, "B"): "无线通信系统链路速率建模",
    (2025, "C"): "围岩裂隙精准识别与三维模型重构",
    (2025, "D"): "低空湍流监测及最优航路规划",
    (2025, "E"): "高速列车轴承智能故障诊断问题",
    (2025, "F"): "江南古典园林的美学特征建模",
}

ARCHETYPE = {
    (2022, "A"): "signal-inverse",
    (2022, "B"): "scheduling-allocation",
    (2022, "C"): "scheduling-allocation",
    (2022, "D"): "scheduling-allocation",
    (2022, "E"): "policy-evaluation",
    (2022, "F"): "scheduling-allocation",
    (2023, "A"): "communications-modeling",
    (2023, "B"): "numerical-approximation",
    (2023, "C"): "evaluation-decision",
    (2023, "D"): "policy-evaluation",
    (2023, "E"): "prediction-diagnosis",
    (2023, "F"): "prediction-diagnosis",
    (2024, "C"): "prediction-diagnosis",
    (2025, "C"): "spatial-reconstruction",
}

FIELDS = [
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


def get_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as resp:
        dest.write_bytes(resp.read())


def load_awards(year: int) -> dict[str, str]:
    path = CACHE / "awards" / f"{year}.csv"
    if not path.exists():
        download(
            f"https://raw.githubusercontent.com/lcpmgh/CPMCM-Awards/master/awardlist/{year}.csv",
            path,
        )
    mapping: dict[str, str] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            team = (row.get("队号") or "").strip()
            award = (row.get("所获奖项") or row.get("获奖") or "").strip()
            if team:
                mapping[team] = award
    return mapping


def normalize_award(raw: str) -> str:
    if not raw:
        return "unverified"
    if "一等" in raw:
        return "first"
    if "二等" in raw:
        return "second"
    if "三等" in raw:
        return "third"
    if "成功" in raw or "参与" in raw or "参加" in raw:
        return "participation"
    return raw


def lookup_award(awards: dict[str, str], team_id: str) -> str:
    if not team_id:
        return ""
    if team_id in awards:
        return awards[team_id]
    if team_id[0] in "ABCDEFGH" and team_id[1:].isdigit():
        return awards.get(team_id[1:], "")
    return ""


def list_github_papers(year: int) -> list[dict]:
    folder = f"{year}年优秀论文"
    papers = []
    for letter in "ABCDEF":
        encoded_folder = urllib.request.quote(f"国赛论文/{folder}/{letter}")
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{encoded_folder}?ref={COMMIT}"
        items = get_json(url)
        for item in items:
            name = item.get("name") or ""
            if not name.lower().endswith(".pdf"):
                continue
            m = re.match(r"^([A-F])(\d{11})\.pdf$", name, re.I)
            team_id = m.group(0).replace(".pdf", "").replace(".PDF", "") if m else Path(name).stem
            papers.append(
                {
                    "year": year,
                    "letter": letter,
                    "filename": name,
                    "team_id": team_id.upper(),
                    "html_url": item.get("html_url"),
                    "download_url": item.get("download_url"),
                    "size": item.get("size"),
                    "sha": item.get("sha"),
                }
            )
    return papers


def select_deep(rows: list[dict], per_cell: int = 4, seed: int = 20260829) -> set[str]:
    rng = random.Random(seed)
    buckets: dict[tuple[int, str], list[dict]] = defaultdict(list)
    for row in rows:
        if row["corpus_layer"] != "full-paper-core":
            continue
        if row["award_tier_normalized"] != "first":
            continue
        buckets[(int(row["year"]), row["problem_letter"])].append(row)
    selected: set[str] = set()
    for key, items in sorted(buckets.items()):
        items = sorted(items, key=lambda r: r["team_id"])
        rng.shuffle(items)
        for item in items[:per_cell]:
            selected.add(item["record_id"])
    return selected


def main() -> None:
    RESEARCH.mkdir(parents=True, exist_ok=True)
    rows = []
    for year, edition in ((2022, 19), (2023, 20)):
        awards = load_awards(year)
        papers = list_github_papers(year)
        for paper in papers:
            raw = lookup_award(awards, paper["team_id"])
            tier = normalize_award(raw) if raw else "unverified"
            status = "team-id-matched" if raw else "unverified"
            layer = "full-paper-core" if tier == "first" else "control-or-contaminant"
            record_id = f"{year}-{paper['team_id']}"
            rows.append(
                {
                    "record_id": record_id,
                    "year": year,
                    "edition": edition,
                    "problem_letter": paper["letter"],
                    "team_id": paper["team_id"],
                    "problem_title": PROBLEM_TITLES.get((year, paper["letter"]), ""),
                    "paper_title": "",
                    "document_type": "full-paper-pdf",
                    "source_url": paper["html_url"],
                    "host": "github.com",
                    "repository": GITHUB_REPO,
                    "commit_ref": COMMIT,
                    "filename": paper["filename"],
                    "size_bytes": paper["size"] or "",
                    "blob_sha": paper["sha"] or "",
                    "award_claim_raw": raw or "folder-label-only",
                    "award_tier_normalized": tier,
                    "verification_status": status,
                    "verification_secondary_url": "https://github.com/lcpmgh/CPMCM-Awards/tree/master/awardlist",
                    "match_key": paper["team_id"],
                    "corpus_layer": layer,
                    "year_letter_stratum": f"{year}-{paper['letter']}",
                    "archetype_tag": ARCHETYPE.get((year, paper["letter"]), ""),
                    "selection_rule": "census-of-github-folder-crosschecked-against-award-csv",
                    "deep_review": "no",
                    "license_notes": "third-party mirror; do not redistribute; local cache only",
                }
            )

    deep = select_deep(rows)
    for row in rows:
        if row["record_id"] in deep:
            row["deep_review"] = "yes"
            row["selection_rule"] = "census+stratified-4-per-year-letter-seed-20260829"

    recency = [
        {
            "record_id": "2025-star-champion-niu",
            "year": 2025,
            "edition": 22,
            "problem_letter": "C",
            "team_id": "",
            "problem_title": "围岩裂隙精准识别与三维重构",
            "paper_title": "基于Frangi滤波与蒙特卡洛模拟的钻孔裂隙识别与三维概率重构",
            "document_type": "university-report",
            "source_url": "https://cese.cumt.edu.cn/info/1003/7411.htm",
            "host": "cese.cumt.edu.cn",
            "repository": "",
            "commit_ref": "",
            "filename": "",
            "size_bytes": "",
            "blob_sha": "",
            "award_claim_raw": "数模之星冠军",
            "award_tier_normalized": "first",
            "verification_status": "university-report-plus-official-closing-news",
            "verification_secondary_url": "https://cpipc.acge.org.cn/cw/contestPrevious/detail/4/2c9080189e403095019e49ef61582f94?page=0",
            "match_key": "牛敏学/王聪/周缘",
            "corpus_layer": "recency-report",
            "year_letter_stratum": "2025-C",
            "archetype_tag": "spatial-reconstruction",
            "selection_rule": "official-finalist-report-layer",
            "deep_review": "yes",
            "license_notes": "public university news; not a full paper",
        },
        {
            "record_id": "2024-star-champion-sdu",
            "year": 2024,
            "edition": 21,
            "problem_letter": "C",
            "team_id": "",
            "problem_title": "数据驱动下磁性元件的磁芯损耗建模",
            "paper_title": "基于多因素分析与深度学习的磁芯损耗建模",
            "document_type": "university-report",
            "source_url": "https://www.ygb.sdu.edu.cn/info/1013/18618.htm",
            "host": "ygb.sdu.edu.cn",
            "repository": "",
            "commit_ref": "",
            "filename": "",
            "size_bytes": "",
            "blob_sha": "",
            "award_claim_raw": "数模之星冠军",
            "award_tier_normalized": "first",
            "verification_status": "university-report",
            "verification_secondary_url": "https://mp.weixin.qq.com/s/kbDDtxAI5DwurpDtvnYIyA",
            "match_key": "张良收/赵佳/王硕",
            "corpus_layer": "recency-report",
            "year_letter_stratum": "2024-C",
            "archetype_tag": "prediction-diagnosis",
            "selection_rule": "official-finalist-report-layer",
            "deep_review": "yes",
            "license_notes": "public university news; not a full paper",
        },
        {
            "record_id": "2024-star-runnerup-just",
            "year": 2024,
            "edition": 21,
            "problem_letter": "C",
            "team_id": "",
            "problem_title": "数据驱动下磁性元件的磁芯损耗建模",
            "paper_title": "",
            "document_type": "university-report",
            "source_url": "https://ygb.just.edu.cn/2025/0220/c8719a357928/page.htm",
            "host": "ygb.just.edu.cn",
            "repository": "",
            "commit_ref": "",
            "filename": "",
            "size_bytes": "",
            "blob_sha": "",
            "award_claim_raw": "数模之星亚军",
            "award_tier_normalized": "first",
            "verification_status": "university-report",
            "verification_secondary_url": "https://cpipc.acge.org.cn/cw/hp/4",
            "match_key": "薛任煊/孙慧/周心仪",
            "corpus_layer": "recency-report",
            "year_letter_stratum": "2024-C",
            "archetype_tag": "prediction-diagnosis",
            "selection_rule": "official-finalist-report-layer",
            "deep_review": "yes",
            "license_notes": "public university news; not a full paper",
        },
        {
            "record_id": "2024-control-C24102910010",
            "year": 2024,
            "edition": 21,
            "problem_letter": "C",
            "team_id": "C24102910010",
            "problem_title": "数据驱动下磁性元件的磁芯损耗建模",
            "paper_title": "",
            "document_type": "full-paper-pdf",
            "source_url": "https://github.com/JunHuaBai96/Mathematical-Modeling/blob/main/%E7%AC%AC%E4%BA%8C%E5%8D%81%E4%B8%80%E5%B1%8A%E4%B8%AD%E5%9B%BD%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B/C24102910010.pdf",
            "host": "github.com",
            "repository": "JunHuaBai96/Mathematical-Modeling",
            "commit_ref": "main",
            "filename": "C24102910010.pdf",
            "size_bytes": "",
            "blob_sha": "",
            "award_claim_raw": "成功参与奖",
            "award_tier_normalized": "participation",
            "verification_status": "team-id-to-be-checked-against-2024-csv",
            "verification_secondary_url": "https://github.com/lcpmgh/CPMCM-Awards/blob/master/awardlist/2024.csv",
            "match_key": "C24102910010",
            "corpus_layer": "lower-tier-control",
            "year_letter_stratum": "2024-C",
            "archetype_tag": "prediction-diagnosis",
            "selection_rule": "public-self-archive-control",
            "deep_review": "yes",
            "license_notes": "author-posted paper; local cache only",
        },
        {
            "record_id": "2025-control-C25102910007",
            "year": 2025,
            "edition": 22,
            "problem_letter": "C",
            "team_id": "C25102910007",
            "problem_title": "围岩裂隙精准识别与三维重构",
            "paper_title": "",
            "document_type": "full-paper-pdf",
            "source_url": "https://github.com/JunHuaBai96/Mathematical-Modeling/blob/main/%E2%80%9C%E5%8D%8E%E4%B8%BA%E6%9D%AF%E2%80%9D%E7%AC%AC%E4%BA%8C%E5%8D%81%E4%BA%8C%E5%B1%8A%E4%B8%AD%E5%9B%BD%E7%A0%94%E7%A9%B6%E7%94%9F%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%AB%9E%E8%B5%9B/C25102910007.pdf",
            "host": "github.com",
            "repository": "JunHuaBai96/Mathematical-Modeling",
            "commit_ref": "main",
            "filename": "C25102910007.pdf",
            "size_bytes": "",
            "blob_sha": "",
            "award_claim_raw": "二等奖",
            "award_tier_normalized": "second",
            "verification_status": "team-id-to-be-checked-against-2025-csv",
            "verification_secondary_url": "https://github.com/lcpmgh/CPMCM-Awards/blob/master/awardlist/2025.csv",
            "match_key": "C25102910007",
            "corpus_layer": "lower-tier-control",
            "year_letter_stratum": "2025-C",
            "archetype_tag": "spatial-reconstruction",
            "selection_rule": "public-self-archive-control",
            "deep_review": "yes",
            "license_notes": "author-posted paper; local cache only",
        },
    ]
    rows.extend(recency)

    # verify 2024/2025 controls if award csv exists
    for year in (2024, 2025):
        awards = load_awards(year)
        for row in rows:
            if row["year"] == year and row["team_id"]:
                raw = lookup_award(awards, row["team_id"])
                if raw:
                    row["award_claim_raw"] = raw
                    row["award_tier_normalized"] = normalize_award(raw)
                    row["verification_status"] = "team-id-matched"

    with MANIFEST.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "n_rows": len(rows),
        "n_full_paper_core": sum(1 for r in rows if r["corpus_layer"] == "full-paper-core"),
        "n_first_prize_matched": sum(1 for r in rows if r["award_tier_normalized"] == "first" and r["document_type"] == "full-paper-pdf"),
        "n_deep_review": sum(1 for r in rows if r["deep_review"] == "yes"),
        "deep_ids": sorted(deep),
        "seed": 20260829,
    }
    SAMPLE.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
