# Scoring rubric (training only)

Load this file for 评阅, 打分, 模拟评审, 数模之星筛选, or “会不会得一等奖”.

## Isolation statement

There is **no** public, official, universal percentage sheet for Huawei Cup papers.

This file is a **training rubric** calibrated on verified first-prize vs weaker papers (`findings.md`, `coding-sheet.csv`). It is not a jury document. It does not predict a prize. Any blog table that says “建模 30 分 / 创新 20 分” is `unverified` unless the current official notice prints those weights. Other GitHub skills’ “国一 ≥ 85 / Outstanding ≥ 85” gates are **not** Huawei Cup rules.

Always say this out loud when scoring.

## Stage 0 — veto (binary)

If any veto fires, stop. Do not average it away.

| ID | Veto | Typical evidence |
|---|---|---|
| V1 | Identity after cover | 学校 / 队员姓名 / 参赛队号 / 学号 on page 2+ |
| V2 | Abstract missing, English-only, or clearly > 2 pages | page map |
| V3 | Not the official template / missing required cover logos for that year | visual check against current 标准文档 |
| V4 | Filename / compressed PDF / MD5 mismatch vs that year’s notice | `validate_submission.py` |
| V5 | Fabricated numbers, missing experiment claimed as done, or uncited large reuse | claim–evidence holes |
| V6 | Problem restatement invents extra questions or drops a numbered question | problem map vs paper |

Vetoed papers can still receive **diagnostic comments**. They do not receive a training total that looks like a jury score.

## Stage 1 — generic quality (100, training)

Score only with a pointer: page, formula, figure, or `missing`. Every cell needs: score, evidence, deduction, confidence (`high`/`medium`/`low`), fix priority (`P0`/`P1`/`P2`).

| ID | Dimension | Max | 3 (full) looks like | 0 looks like |
|---|---|---|---|---|
| D1 | Contracts / restatement | 12 | Each Q has input–output | Paraphrase only |
| D2 | Assumptions & symbols | 8 | Numbered, some local, units | “data authentic” |
| D3 | Method rationale | 12 | 2–3 families, one killed | Toolbox dump |
| D4 | Formulation / correctness | 14 | Model matches the ask; constraints closed | Wrong objective, silent infeasibility |
| D5 | Experiments & validation | 16 | Baseline + metric + falsifier | Method name, no test |
| D6 | Sensitivity / robustness / uncertainty | 10 | Sweep or perturbation with a table | None |
| D7 | Interpretation | 10 | Number back to the engineering ask | Orphan digits |
| D8 | Abstract & narrative | 8 | Per-Q story with numbers | Background essay |
| D9 | Figures / tables | 6 | Each figure has a job | Decorative flowcharts |
| D10 | Reproducibility, cites, AI log | 4 | Seed, source, disclosure if used | Magic code |

Band (training language only):

- 85–100: first-prize **texture** in this sample, not a prize forecast
- 70–84: complete contest paper with thin tests
- 55–69: genre-compliant, weak discrimination
- <55 or any veto: not a training pass

## Stage 2 — archetype overlay (adjust, do not hide Stage 1)

Add at most +6 / −12 from overlays. Write the overlay lines on the scorecard.

| Archetype | Extra full marks | Extra zeros |
|---|---|---|
| optimization-scheduling | Second instance, greedy baseline, feasibility | Objective only, no residual |
| signal-inverse | Classical estimator + SNR/topology sweep | “neural net beats MUSIC” with one plot |
| prediction-diagnosis | Time-aware split, leakage check, residual | Random split of a series |
| mechanism-simulation | Special-case recovery + perturbation | Unchecked DE |
| image-spatial | Pixel **and** geometry metric, failure crop | Only pretty reconstructions |
| evaluation-decision | External consensus / overlap, not self-ranking | AHP soup with no rank check |

## Scorecard output

Use headings:

1. Isolation statement
2. Veto table (pass/fail + page)
3. Stage 1 table with evidence
4. Overlay
5. Training total as `training_score=.. / 100 (not official)`
6. Top 5 fixes, P0 first
7. What was **not** scored (code not run, data not seen)

Refuse if the user asks you to “按官方百分制” with invented weights. Offer this rubric labeled as training, or wait for an official sheet.

## Route back (S7)

| Finding | Return to |
|---|---|
| Baseline missing or packaged as the main model | S4 |
| Leakage / no falsifier / empty ledger | S5 |
| Abstract cites `not-run` as a number; figure has no job | S6 |
| Identity / filename / template | S8 checklist, not a modeling rewrite |

Stop with:

```text
AWAITING_HUMAN_REVIEW(submit_ready)
```

`training_score` is never a prize forecast.
