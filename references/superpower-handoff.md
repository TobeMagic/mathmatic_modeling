# Superpower handoff (S3)

Load after G2. Produce a plan that `aimagician-superpower` can execute as `High` work. Do not write solvers in this stage.

Copy `assets/execution-plan-slice.md` to contest `plans/execution-plan.md`. Keep progress in `plans/STATE.md` (Superpower analogue of `.planning/STATE.md`).

## Required fields

- Objective (letter, four-day paper, evidence-bound)
- Tier: `High`
- Acceptance signals (observable)
- Non-goals (no abstract until G5; no letter change without returning to S1)
- Vertical slices in order: data audit → Q1 baseline → remaining-Q baselines → optional upgrades → figures from ledger → section writes
- Requirement → evidence map (`req_id`, slice, file, check)
- Failure / recovery (baseline fail → pivot candidate; leakage → halt headlines)
- `year=` tag

## Done-when

Every numbered question has a slice that produces either a ledger `done` row or a written `failed` + pivot. `validate_submission.py` is a late slice, not a modeling slice.

Stop with:

```text
AWAITING_HUMAN_REVIEW(execution_plan)
```

After approval, later coding slices may use `aimagician-superpower`. This skill still owns G4–G7 domain gates, `not-run` discipline, and Huawei Cup rules.
