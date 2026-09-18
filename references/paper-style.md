# Paper style (Huawei Cup)

Load for 摘要、正文、创新点、章节职责. Official length: unified Chinese abstract ≤ 2 pages (`year=2025-provisional` until 2026 attachments exist). See `official-rules.md`.

This file is about **our** contest `paper/`. Files under Skill-repo `ref-papers/` are other teams’ papers. Cite them as `[参考] {filename} p.N`. Never paste their sentences.

## Write from evidence

A number may appear only if `results/result-ledger.csv` has it with `status=done` and a run id. Otherwise leave the cell blank and write `not-run`.

Copy `assets/abstract-skeleton.md` into the contest repo `paper/sections/abstract.md`.
Copy `assets/claim-evidence-matrix.md` into `plans/claim-evidence.md`.

Write only questions authorized at G5. Later `done` rows patch that section; do not regenerate the whole manuscript.

## Abstract (first-prize texture)

One short scene paragraph, then **针对问题一/二/…**, each block:

1. What was asked
2. Family used, and what was rejected if space
3. Headline number **with comparator**
4. What it means for the engineering question

创新点 as **types**: modeling / algorithm / feature / validation / application.  
「本文方法新颖、结果合理」 is not an innovation.

Keywords: 5–8 method terms. Example texture (do not copy): 2023-A `[参考] 2023-first-A23100070049` uses WLAN；马尔科夫链模型；RTS/CTS.

## Body

1. 问题重述 — contracts, not a paraphrase contest
2. 假设与符号 — numbered; local assumptions stay local
3. 针对问题 N — model, algorithm, experiment, result, check
4. 敏感性 / 鲁棒性 / 局限
5. 参考文献 — first-appearance order

Inside 针对问题 N: claim → setup → evidence → interpretation.

## Voice

- 本文 is fine. Do not write as an AI.
- Numbers with units and comparators: `RMSE 221.61 vs Woodward 513.75`, not `误差较小`.
- Training data only? Say so.

## Identity

Upload PDF: no 学校 / 队员姓名 / 参赛队号 / 学号 after the cover.

## Banned

首次提出 (unless true), 完美拟合, 官方规定建模占 30 分, invented RMSE, copying `ref-papers/` sentences.

Stop with `AWAITING_HUMAN_REVIEW(draft)` after S6.
