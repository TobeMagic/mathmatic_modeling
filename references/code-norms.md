# Code norms (no language templates)

Load for 编程、跑数、出图脚本、附件与论文对不上.

This Skill does **not** ship Python/MATLAB skeletons. Choose the language that matches the approved plan. Keep numbers honest.

## Before a solver

1. G3 approved `plans/execution-plan.md`. A data-open probe (shapes, units, missingness) may happen earlier; solvers may not.
2. Open attachments; write `reports/data-audit.md`.
3. Code the **baseline** that covers the numbered ask in hours. Do not present an upgraded solver as the first result.

## Loop per question

1. Implement baseline; print one number the paper could cite.
2. Optional upgrade only if the baseline is weak and a falsifier exists.
3. Back-substitute constraints (optimization) or score a held-out slice (prediction). Solver `success` is not evidence.
4. `python scripts/writer_id.py --contest <contest-repo> --init` if your shards do not exist.
5. Write `experiments/runs/<question>-<model>-<slug>-<yyyymmdd>-<seq>/` (`config`, `log`, `metrics`, `hashes`).
6. Copy the headline into **your** `results/ledger/<slug>.csv` (`status=done|failed|not-run`; `paper_eligible=candidate` if it should be writable, else `no`).
7. **Append** one row to **your** `plans/activity/<slug>.md`. Without a matching row in any activity shard, S6 treats the run as not-run.
8. Export figure csv before polishing.

Randomized methods: fix a seed, run ≥3 times, report mean ± spread.

## Ledger is the only number source

`paper/` and captions cite a number only from a `done` row that is `authorized` or `in_draft` and has an activity row in some `plans/activity/*.md`. After code changes, mark old rows `stale` on **your** shard and re-run. Never edit a teammate's `results/ledger/` or `plans/activity/` file.

Do not paste code from `ref-papers/` as this year’s solution.

## Attachment package (`year=2025-provisional`)

Same stem as the PDF; code that regenerates cited tables; environment versions; no identity in comments if the year forbids it.

Stop S4 with `AWAITING_HUMAN_REVIEW(baseline)`.
