# README cover direction record

## Product brief

- **Name:** Huawei Cup modeling Skill (`huawei-cup-modeling`)
- **Category:** Cursor Agent Skill + first-prize reference library for 中国研究生数学建模竞赛
- **Audience:** Contest teams using Cursor; one Skill for modeling, code, and paper
- **Decision:** Understand two-repo split, run scaffold, trust S0–S8 / G1–G7
- **Hero proof:** `assets/plans-STATE.md` as copied into contest `plans/STATE.md`
- **Shipped commands:** `python scripts/scaffold_workspace.py --dest <contest-repo>`, `python scripts/year_gate.py`
- **Operational tag:** `year=2026` (`research/huawei-cup/year-gate.json`, as_of 2026-09-18; Word template notice still unmatched)
- **Forbidden claims:** live-LLM 18/18, official scores, invented RMSE, “AI 一键写论文”

## Exemption

User asked for README polish and PDF commit in one pass. Three real 1600×900 sources exist. Selected **A (contest STATE board)** because the distinctive product is the Superpower-style control plane, not a CLI skin or a paper catalog.

## Directions

| Id | Idea | First signal | Proof | Type / color | Risk |
|---|---|---|---|---|---|
| A selected | Contest STATE board | `S0` + two-repo | Real `plans/STATE.md` YAML | Serif wordmark + mono ledger; ink / paper / vermillion gate | Looks like a filled contest if fields are invented — keep scaffold blanks |
| B | Year-gate terminal | `python scripts/year_gate.py` | Keys from `year-gate.json` | Mono on near-black; gold tag | Generic terminal chrome |
| C | Filename grammar | `{year}-{tier}-{team_id}-{title}` | Real 2024 first-prize stem | Oversized type + red stamp | Reads as if we authored those papers |

## Geometry

README hero: 1600×900 PNG, source `readme-hero.html`, output `../readme-hero.png`.
