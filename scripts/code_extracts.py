#!/usr/bin/env python3
"""Heuristic codebook scoring of cached extracts + disagreement vs human sheet."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

from _paths import RESEARCH

EXTRACT = RESEARCH / "cache" / "extracts"
MANIFEST = RESEARCH / "corpus-manifest.csv"
HUMAN = RESEARCH / "coding-sheet.csv"
OUT = RESEARCH / "coding-sheet-heuristic.csv"
ADJ = RESEARCH / "coding-adjudication.csv"

DIMS = [
    "problem_decomposition",
    "assumptions_symbols",
    "method_rationale",
    "data_cleaning",
    "baseline_or_control",
    "solution_trace",
    "validation_error",
    "sensitivity_uncertainty",
    "result_interpretation",
    "reproducibility",
    "limitations",
    "abstract_structure",
    "figure_role",
    "citation_hygiene",
]


def score(text: str) -> dict[str, int]:
    t = text
    def hit(*pats: str) -> bool:
        return any(re.search(p, t) for p in pats)

    s: dict[str, int] = {}
    s["problem_decomposition"] = 3 if hit(r"问题重述", r"针对问题") else 1 if hit(r"摘\s*要") else 0
    s["assumptions_symbols"] = 3 if hit(r"假设") and hit(r"符号") else 1 if hit(r"假设|符号") else 0
    s["method_rationale"] = (
        3 if hit(r"相比|对比") and hit(r"放弃|不采用|敏感|局限") else 2 if hit(r"相比|对比|优于") else 1 if hit(r"模型") else 0
    )
    s["data_cleaning"] = 2 if hit(r"异常值|缺失|清洗|预处理") else 1 if hit(r"数据") else 0
    s["baseline_or_control"] = (
        3 if hit(r"基线|对照|现有模型|传统") and hit(r"RMSE|MAE|CSI|利用率|重合度") else 2 if hit(r"对比|相比|优于") else 0
    )
    s["solution_trace"] = 3 if hit(r"算法|遗传|NSGA|求解") and hit(r"参数|迭代|种群") else 2 if hit(r"算法|求解") else 1
    s["validation_error"] = (
        3 if hit(r"RMSE|MAE|R2|R²|CSI|交叉验证|训练集") else 2 if hit(r"误差|精度|准确") else 0
    )
    s["sensitivity_uncertainty"] = (
        3
        if hit(r"灵敏|扰动|鲁棒|敏感性") and hit(r"%|百分|±")
        else 2
        if hit(r"灵敏|鲁棒|扰动|敏感性")
        else 0
    )
    s["result_interpretation"] = 2 if hit(r"表明|说明|因此") and hit(r"针对问题") else 1
    s["reproducibility"] = 2 if hit(r"附件|MATLAB|Python|种子|参数") else 1
    s["limitations"] = 2 if hit(r"不足|局限|缺点") else 0
    s["abstract_structure"] = (
        3
        if hit(r"摘\s*要") and hit(r"针对问题|问题一|问题\s*1") and hit(r"关键词")
        else 1
        if hit(r"摘\s*要")
        else 0
    )
    s["figure_role"] = 3 if hit(r"图\s*\d") and hit(r"对比|路线|灵敏") else 1 if hit(r"图\s*\d") else 0
    s["citation_hygiene"] = 2 if hit(r"参考文献") else 0
    if hit(r"创新"):
        inn = "algorithm" if hit(r"算法|NSGA|LSTM|遗传") else "modeling"
    else:
        inn = "unknown"
    s["innovation_type"] = inn  # type: ignore[assignment]
    return s


def garbled(text: str) -> bool:
    if len(text) < 500:
        return True
    cn = len(re.findall(r"[\u4e00-\u9fff]", text[:4000]))
    return cn < 80


def load_manifest() -> dict[str, dict]:
    with MANIFEST.open(encoding="utf-8", newline="") as f:
        return {r["record_id"]: r for r in csv.DictReader(f)}


def load_human() -> dict[str, dict]:
    if not HUMAN.exists():
        return {}
    with HUMAN.open(encoding="utf-8", newline="") as f:
        return {r["record_id"]: r for r in csv.DictReader(f)}


def main() -> None:
    man = load_manifest()
    human = load_human()
    rows = []
    for path in sorted(EXTRACT.glob("*.txt")):
        if path.name == "index.json":
            continue
        rec = path.stem
        text = path.read_text(encoding="utf-8", errors="replace")
        sc = score(text)
        m = man.get(rec, {})
        quality = "garbled-extract" if garbled(text) else "ok"
        row = {
            "record_id": rec,
            "award_tier_normalized": m.get("award_tier_normalized", ""),
            "archetype": m.get("archetype_tag", ""),
            "extract_quality": quality,
            "coder_id": "heuristic-v1",
            "extract_chars": len(text),
            **{k: sc[k] for k in DIMS if k in sc},
            "innovation_type": sc.get("innovation_type", ""),
        }
        rows.append(row)
    if rows:
        fieldnames = list(rows[0].keys())
        with OUT.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(rows)

    disagreements = []
    numeric = [d for d in DIMS if d != "innovation_type"]
    for rec, h in human.items():
        heur = next((r for r in rows if r["record_id"] == rec), None)
        if not heur:
            continue
        for dim in numeric:
            try:
                a, b = int(h[dim]), int(heur[dim])
            except (KeyError, ValueError):
                continue
            if abs(a - b) >= 2:
                disagreements.append(
                    {
                        "record_id": rec,
                        "dimension": dim,
                        "human": a,
                        "heuristic": b,
                        "delta": b - a,
                    }
                )
    if disagreements:
        with ADJ.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["record_id", "dimension", "human", "heuristic", "delta"])
            w.writeheader()
            w.writerows(disagreements)

    summary = {
        "n_extracts": len(rows),
        "n_ok": sum(1 for r in rows if r["extract_quality"] == "ok"),
        "n_garbled": sum(1 for r in rows if r["extract_quality"] != "ok"),
        "n_human": len(human),
        "n_disagreements_ge2": len(disagreements),
        "disagreement_dims": dict(Counter(d["dimension"] for d in disagreements)),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
