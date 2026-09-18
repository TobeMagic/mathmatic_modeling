# Coding codebook

Use this file when distilling Huawei Cup papers. Code **observable paper behavior**, not inferred jury intent.

## Record

Each coded unit is one document in `corpus-manifest.csv`.

Required identifiers: `record_id`, `year`, `problem_letter`, `team_id`, `award_tier_normalized`, `verification_status`, `coder_id`.

## Dimensions

Score each dimension `0` (absent), `1` (mentioned), `2` (operational, with a procedure), `3` (operational plus a check, baseline, or limitation). Quote a short evidence fragment and a page number when the score is 2 or 3.

| Code | What to look for |
|---|---|
| `problem_decomposition` | Restates each numbered question, maps inputs/outputs, does not invent extra questions |
| `assumptions_symbols` | Numbered assumptions, symbol table, which assumptions are relaxed later |
| `method_rationale` | Why this family vs 1-2 rejected families; not a method dump |
| `data_cleaning` | Missing values, outliers, units, leakage controls |
| `baseline_or_control` | Comparison method, naive model, analytical special case, or published formula |
| `solution_trace` | Algorithm, solver, parameters, and enough detail to reproduce the main number |
| `validation_error` | Hold-out, residual, constraint check, physical bound, or cross-check |
| `sensitivity_uncertainty` | Parameter sweep, noise, perturbation, confidence, scenario stress |
| `innovation_type` | `modeling` / `algorithm` / `feature` / `validation` / `application`; reject empty 创新点 |
| `result_interpretation` | Numbers tied back to the original engineering or policy question |
| `reproducibility` | Data versions, seeds, software, attachment declared |
| `limitations` | Explicit failure mode or scope limit |
| `abstract_structure` | Approach, method, model, key results, innovation, keywords; two-page discipline |
| `figure_role` | Each main figure has a claim job: process, comparison, spatial, residual, sensitivity |
| `citation_hygiene` | Formula, code, and data sources cited; AI tools disclosed if used |

## Contrast rules

- A pattern that appears in both first-prize and lower-tier papers is a **genre convention**, not a discriminator.
- A discriminator must appear in the first-prize sample **and** be missing or weaker in at least one verified lower-tier control, or be independently corroborated by a star-finalist report.
- Star champion/runner-up/third is stored as `star_final_rank`. Do not treat it as a pure paper-quality rank.

## Confidence

`high` = quoted page; `medium` = section-level; `low` = inferred from structure only.
