---
name: huawei-cup-modeling
description: "Use when the user mentions 华为杯, 研赛, 中国研究生数学建模竞赛, 研究生数学建模, 数模之星, CPMCM, or a four-day modeling contest workspace. Coaches all-letter reconnaissance, baseline-first modeling and coding, paper and figure style, and submission checks. CUMCM / MCM / 美赛 / 本科国赛 / 大学生数学建模 methods are secondary only. Do not use for generic SCI papers, CUMCM undergraduate contests, or ordinary homework."
category: build
subcategory: workflow
tags:
  - huawei-cup
  - cpmcm
  - modeling
  - contest
  - paper
---

# Huawei Cup modeling

This repository is the **Skill + reference-paper library**.  
A contest run is a **separate git repo**. Initialize it with `python scripts/scaffold_workspace.py --dest <contest-repo>` and do modeling, coding, experiments, and **our** paper there.

Open this repo in Cursor (root `SKILL.md`) or copy the runtime pack. Not a prize predictor. Not a one-shot ghostwriter. One Skill for the whole team (modeling + code + paper). Do not split teammate-role entry points.

Default route: **survey all letters → human chooses → deepen and plan → baseline that covers the ask → optional upgrade → write only evidenced claims → review → submit**. Pause at every `AWAITING_HUMAN_REVIEW`. Load **one** extra reference per stage.

| Stage | Stops when |
|---|---|
| S0 启动 | contest `plans/STATE.md` exists |
| S1 全题侦察 | **G1** letter choice |
| S2 锁题深挖 | **G2** `plans/solution.md` |
| S3 计划交接 | **G3** `plans/execution-plan.md` |
| S4 Baseline | **G4** ledger row per question |
| S5 优化实验 | **G5** write-scope |
| S6 增量论文 | **G6** draft |
| S7 评审回路 | **G7** submit-ready |
| S8 提交 | freeze or blocker list |

## Two-repo boundary

| Repo | Holds | Never |
|---|---|---|
| This Skill repo | `SKILL.md`, `references/`, `assets/`, `ref-papers/` | Our manuscript |
| Contest repo | `plans/`, `code/`, `experiments/`, `results/`, `paper/` | Copies of `ref-papers/` PDFs |

`ref-papers/pdf/{year}-{tier}-{team_id}-{title}.pdf` are **other teams**. Cite `[参考] {filename} p.N`. Do not write 本文 about them. Our draft is only contest `paper/`. See `references/ref-paper-usage.md`.

## Inputs

- Official portal https://cpipc.acge.org.cn/cw/hp/4
- Contest workspace (`plans/STATE.md` first)
- Optional `training_profile` in `plans/STATE.md` (`conservative-baseline` default)

## Hard bans

- Do not fabricate experimental numbers, citations, or “official” score sheets.
- If a result was not run, write `status=not-run` and leave the number blank.
- Do not put 学校 / 队员姓名 / 参赛队号 / 学号 on page 2+.
- Do not treat GitHub folder names such as `优秀论文` as award proof.
- Do not copy sentences from `ref-papers/` into contest `paper/`.
- Do not treat the official 优秀作品 KDocs as a paper corpus (promo PPTX).
- Do not start S4 coding before G3 plan approval, except a data-open probe.
- Do not lock a contest letter for the user. G1 is a human decision.
- Do not promote CUMCM/MCM page, figure, hour, language, or score quotas as Huawei Cup rules.
- Do not ship language code templates. Choose the language after the plan.

### 0. Year gate

1. Live source: https://cpipc.acge.org.cn/cw/hp/4
2. Re-check: `python scripts/year_gate.py`
3. As of 2026-09-18: 2026 invitation, opening notice, and AI annex exist; Word-template notice does not. Tag `year=2026`. Borrow unmatched format items from 2025 and label them `year=2025`.
4. Never invent official percentage weights. Training scores live in `references/scoring-rubric.md` and must be labeled `training_score, not official`.

**CHECKPOINT:** if the opening notice is missing, keep `year=2025-provisional`. If it exists, use `year=2026` and do not invent the Word template.

## Stage router

If the user mixes tasks, sequence them. Still load one reference at a time.

### 1. S0 启动

When: new contest repo, 开始, year check.  
Load: this file; `python scripts/year_gate.py`; `python scripts/scaffold_workspace.py --dest <contest-repo>`; `references/workspace-layout.md`.  
Stop when `plans/STATE.md` exists in the contest repo.

### 2. S1 全题侦察

When: A–F not locked. Load `references/letter-survey.md`.  
Stop at **G1** `AWAITING_HUMAN_REVIEW(problem_choice)`.

### 3. S2 锁题深挖

When: letter chosen. Load `references/problem-workflow.md`. Write contest `plans/solution.md`.  
Stop at **G2** `AWAITING_HUMAN_REVIEW(solution_direction)`.

### 4. S3 计划交接

When: 方案已审. Load `references/superpower-handoff.md`. Write `plans/execution-plan.md`.  
Stop at **G3** `AWAITING_HUMAN_REVIEW(execution_plan)`.  
**CHECKPOINT:** no solver code until a human approves the plan. After approval, slices may use `aimagician-superpower`; this skill keeps Huawei Cup gates.

### 5. S4 Baseline

When: plan approved; 编程. Load `references/code-norms.md`.  
Stop at **G4** `AWAITING_HUMAN_REVIEW(baseline)`.

### 6. S5 优化实验

When: baseline done. Load `references/experiments-validation.md`.  
Stop at **G5** `AWAITING_HUMAN_REVIEW(write_scope)`.

### 7. S6 增量论文

When: authorized Qs have `done` evidence. Load `references/paper-style.md`, then `references/figure-style.md` / `assets/figure-ai-prompts.md`.  
Stop at **G6** `AWAITING_HUMAN_REVIEW(draft)`.

### 8. S7 评审回路

When: 评阅. Load `references/scoring-rubric.md`.  
Stop at **G7** `AWAITING_HUMAN_REVIEW(submit_ready)` or route back to S4/S5/S6.

### 9. S8 提交

When: 文件名 / MD5 / 匿名. Load `references/official-rules.md`; `python scripts/validate_submission.py`.  
Stop at freeze or a blocker list.

Always available: `references/ai-integrity.md`; `references/workspace-layout.md`; `references/profiles.md`; `references/ref-paper-usage.md`.

## Resume

1. In the **contest** repo, read `plans/STATE.md` (then `plans/PROJECT.md`, `plans/CONTEXT.md`).
2. Continue from `current_stage`. Do not re-ask known fields.
3. If a gate is open, restate the artifact and wait. “继续” is not a decision unless they also name it (letter, approve plan, write Q1, …).
4. Missing 2026 opening notice → keep `year=2025-provisional`. Opening present and Word-template notice still missing → `year=2026`, format items stay labeled until transcribed.

## Human gates

Emit the marker on its own line. Then stop generating the next stage’s long work.

| Gate | Agent must present | Human must say |
|---|---|---|
| G1 | letter-comparison matrix for every numbered problem | the letter, or “再调研” |
| G2 | `plans/solution.md` | approve / revise / change letter |
| G3 | `plans/execution-plan.md` | approve plan |
| G4 | baseline ledger row or written failure + pivot | continue / pivot / narrow scope |
| G5 | matrix + claim–evidence status | which questions may enter the paper |
| G6 | new or updated sections + figure jobs | revise / more experiments / accept |
| G7 | veto table + `training_score=/100 (not official)` | submit-ready or loop |

Inside a stage, execute without extra confirmation. Between stages, wait.

## Conservative default

1. Cover every numbered question with a **baseline** that can finish in hours.
2. Build a paper skeleton from baseline numbers and `not-run` holes.
3. Upgrade models only where the baseline is weak **and** a falsifiable test exists.
4. Paper text may cite a number only from contest `results/result-ledger.csv` with `status=done`.

Optional `training_profile=full-draft` is a completeness target, never an official rule. See `references/profiles.md`.

## Default output

Emit only what the **current stage** can honestly fill.

1. Stage + gate marker
2. Problem map or letter-comparison matrix
3. 2–3 model candidates with a written kill (S2+)
4. Experiment matrix / result-ledger delta
5. Claim–evidence matrix
6. Outline + figure plan (jobs, not quotas)
7. Scorecard only in S7
8. Fatal risks
9. Next human decision (one sentence)

## Failure Handling

| Trigger | First response | Fallback |
|---|---|---|
| User asks to pick A–F | Fill the comparison matrix | Stop at G1; do not lock a letter |
| User says 继续 with an open gate | Restate the waiting artifact | Stay in the same stage |
| Baseline fails | Write `failed` + pivot in the ledger | Do not package a novel solver as the baseline |
| Number missing | `status=not-run`, blank cell | Refuse a plausible RMSE |
| User asks for official 百分制 / 国一≥85 | Isolation statement | Offer `training_score, not official` |
| CUMCM 20页/8图/15000字 as Huawei law | Label `training_profile` only | Keep official 2-page abstract |
| Opening a `ref-papers/` file | Prefix `[参考] {filename}` | Never treat as contest `paper/` |
| KDocs 优秀作品 as corpus | State it is promo PPTX | Point to `research/huawei-cup/download-excellent-works.md` |
| 2026 opening notice still missing | Keep `year=2025-provisional` | Re-run `python scripts/year_gate.py` |
| Opening exists, Word template unmatched | Tag `year=2026`; keep 2025 format as labeled fallback | Do not invent a 2026 filename pattern |

## Evidence boundary

Reference PDFs: `ref-papers/pdf/{year}-{tier}-{team_id}-{problem_title}.pdf` (`REFERENCE_ONLY`; see `ref-papers/manifest.csv`).  
Derived conclusions: `research/huawei-cup/findings.md`.  
Corpus metadata: `research/huawei-cup/corpus-manifest.csv`.

Primary gold: Huawei Cup national **first prize**. Second/third/participation are controls.

## Completion Contract

A stage is done when its contest artifact exists and the matching `AWAITING_HUMAN_REVIEW(...)` line has been emitted, or S8 reports a freeze/blocker list.

## Commands

```text
python scripts/year_gate.py
python scripts/scaffold_workspace.py --dest <contest-repo>
python scripts/validate_submission.py path/to/A25000010001.pdf --year 2025
```
