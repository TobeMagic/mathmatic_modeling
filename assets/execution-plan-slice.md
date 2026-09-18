# Execution plan (S3)

## Objective

Huawei Cup letter ____ ; evidence-bound paper by contest end; `year=` ____

## Tier

High

## Acceptance

- [ ] Every numbered question has baseline `done` or written `failed` + pivot
- [ ] Abstract cites only `status=done` ledger rows
- [ ] `python scripts/validate_submission.py` exit 0 or a written blocker list

## Non-goals

- No letter lock in this file (already decided at G1)
- No abstract until G5
- No invented numbers

## Vertical slices

| Slice | Requirement | Evidence file | Check |
|---|---|---|---|
| S0 data audit | R0 | reports/data-audit.md | attachments opened |
| S4 Q1 baseline | R1 | experiments/runs/<id>/ | ledger E1 done or failed |
| S4 other-Q baselines | R2 | results/result-ledger.csv | each Q a row |
| S5 optional upgrades | R3 | experiments/runs/<id>/ | kill log + falsifier |
| S6 sections | R4 | paper/sections/ | plans/claim-evidence.md |
| S8 submit | R5 | paper/submission/ | validator |

## Failure / recovery

- Baseline fails → candidate C or narrower Q scope; return to G2 if the letter is infeasible
- Leakage → halt headline metrics
- `year=2025-provisional` at submit → human accepts the tag

## Open questions
