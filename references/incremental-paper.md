# Incremental paper (S6 ingest)

Load when the user asks 写论文 / 补摘要 / 改问题N, or after G5 has authorized a write scope. Then load `paper-style.md` and `figures-tables.md` as needed.

This is the contest analog of wiki Ingest: compile **already recorded** teammate outputs into `paper/sections/`. Do not invent a manuscript from chat. Do not assign 论文手 / 建模手 / 编程手.

Each teammate writes only `plans/activity/<slug>.md` and `results/ledger/<slug>.csv` (`python scripts/writer_id.py --contest <contest-repo> --init`). S6 **reads all shards**. Ingest receipts go only in **your** activity file. Do not edit a teammate's files. Do not maintain `plans/activity-log.md`.

## Law

A sentence that contains a number is legal only if **all** of these hold:

1. Some `results/ledger/*.csv` has that number with `status=done` and a `run_id`.
2. The same `run_id` has an **append-only** row in some `plans/activity/*.md`.
3. `paper_eligible` is `authorized` or `in_draft` in `plans/claim-evidence.md` (paper lane).

`candidate` = teammate wants it in the paper; not yet ingestable.  
`no` = diagnostic / probe.  
Missing activity row in **every** `plans/activity/*.md` = **not-run** for the paper lane, even if `metrics.json` exists.  
Reference papers in the Skill repo `ref-papers/` are not our draft.

## Orient (every S6 turn)

1. Read contest `plans/STATE.md`.
2. Read **every** `plans/activity/*.md` (latest rows; do not rewrite old rows or other people's files).
3. Read `plans/claim-evidence.md` and **every** `results/ledger/*.csv`.
4. List source files you will open (`experiments/runs/<id>/`, figures). Search existing `paper/sections/` before creating a new section.

## Ingest

For each `authorized` question with `status=done`:

1. Restate the contract in one paragraph.
2. Name the baseline and, if present, the upgraded model and what was killed.
3. Cite the ledger rows (id + metric + comparator + writer slug).
4. Insert figures that have jobs. No figure-count quota unless `training_profile=full-draft` **and** the user asked for that profile.
5. Write limitations for that question, including `not-run` holes.
6. Patch the existing section. Do not regenerate the whole manuscript unless the user asks.
7. Set those claim rows to `paper_eligible=in_draft` in `plans/claim-evidence.md` only.
8. **Append** a row to **your** `plans/activity/<slug>.md`: `ingested {run_id} → paper/sections/...`.

Stop. Do not rewrite unauthorized questions. Do not fill `candidate` numbers.

## Parallel with S4/S5

Modeling/code may keep appending **their own** shards while S6 ingests already-`authorized` questions. New runs stay `candidate` until a human re-opens G5 (or names the row `authorized` in claim-evidence).

If the user mixes “继续跑实验” and “写论文”, sequence them: record the run first, then ingest only what is already authorized.

## Abstract

Write last. Include only questions whose headline claims are `done` and `authorized`/`in_draft`. Mention remaining holes as unfinished work, never as numbers.

## After later experiments

Patch the existing section from the new **authorized** ledger rows. Mark superseded cited numbers `stale`.

Stop with:

```text
AWAITING_HUMAN_REVIEW(draft)
```
