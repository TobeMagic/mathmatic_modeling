# Incremental paper (S6)

Load when G5 has authorized a write scope. Then load `paper-writing.md` and `figures-tables.md` as needed.

## Law

A sentence that contains a number is legal only if contest `results/result-ledger.csv` has that number with `status=done` and a run id. Reference papers in the Skill repo `ref-papers/` are not our draft.

## Per-question slice

For each authorized question:

1. Restate the contract in one paragraph.
2. Name the baseline and, if present, the upgraded model and what was killed.
3. Cite the ledger rows (id + metric + comparator).
4. Insert figures that have jobs. No figure-count quota unless `training_profile=full-draft` **and** the user asked for that profile.
5. Write limitations for that question, including `not-run` holes.

Stop. Do not rewrite other questions.

## Abstract

Write last. Include only questions whose headline claims are `done`. Mention remaining holes as unfinished work, never as numbers.

## After later experiments

Patch the existing section from the new ledger rows. Do not regenerate the whole manuscript unless the user asks.

Stop with:

```text
AWAITING_HUMAN_REVIEW(draft)
```
