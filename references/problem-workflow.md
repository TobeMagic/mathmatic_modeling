# Problem workflow

Load this file for **S2 lock-in** after G1. All-letter survey lives in `letter-survey.md`; do not re-survey here.

Evidence base: `research/huawei-cup/findings.md`. Genre conventions are entry tickets. Discriminators are tests, rejections, and numbers in the abstract.

Resume from contest `plans/STATE.md`.

## 0. Year gate

1. Open https://cpipc.acge.org.cn/cw/hp/4
2. Confirm the current opening notice. If 2026 attachments are still missing, tag every operational rule `year=2025-provisional` and load `official-rules.md`.
3. Do not start writing on the official template until the team has the **current-year** `竞赛论文标准文档`.

## 1. Problem map (before any model)

**Open the attachments before naming a model.** Record file, shape, units, missingness. A map built only from the problem PDF is incomplete.

For each numbered question write a contract:

| Q | Given (data/params) | Decide / compute | Output form | Hidden constraint | Naive baseline |
|---|---------------------|------------------|-------------|-------------------|----------------|

Rules:

- Do not invent a question the problem did not ask.
- If a later question depends on an earlier output, draw the dependency. That is the usual Huawei Cup chain; treat error as cumulative.
- Tag the **archetype**, not the letter A–F. Letters rotate. Use: `optimization-scheduling`, `signal-inverse`, `prediction-diagnosis`, `mechanism-simulation`, `image-spatial`, `evaluation-decision`. A paper may mix two.

## 2. Topic choice

Letter lock is **G1**, already decided. If the user wants to change letters, return to S1. Do not re-pick here.

## 3. Assumption audit

Write assumptions in three piles:

1. **Contest-given** (from the problem text).
2. **Local to one question** (2023-C style: 问题一假设 / 问题二假设).
3. **Convenience**. Mark these as the first things to relax in sensitivity.

Reject a single catch-all line “data are authentic”.

Keep a symbol table. One symbol, one meaning, SI units.

## 4. Method candidates (2–3, with a written kill)

For the hardest question, propose two or three **families**, not two or three package names.

Template:

- Candidate A (baseline / classical): why it should work; what would falsify it.
- Candidate B (main): what extra structure it uses; cost in hours.
- Candidate C (backup): if B fails to converge / overfits / violates constraints.

Keep a rejection log. First-prize 2022-A drops FBSS because it is fragile; 2022-E keeps GRU/Stacking only after a comparison. A method dump without a kill is a genre paper, not a discriminator paper.

## 5. 96-hour backbone

Copy `assets/schedule-96h-solo.md` into contest `plans/schedule-96h.md`. Write the solution into `plans/solution.md`. Do not assign M/C/W roles.

Milestones:

- After G1: letter locked by a human.
- Hour 24: every question has a baseline number **or** a written failure and a pivot.
- Hour 48: matrix rows are `done` / `failed` / `not-run`. No fake fill.
- Hour 72: authorized sections written from the ledger.
- Hour 90: `python scripts/validate_submission.py` + MD5 freeze rehearsal.
- Hour 96: upload path only. No model edits after MD5.

## 6. Default artifacts this mode must emit

1. Problem map table.
2. 2–3 candidates + rejection log.
3. Experiment matrix pointer (`assets/experiment-matrix.md`).
4. 96-hour solo board (no teammate roles).
5. Fatal risks (data missing, NP-hard without heuristic, leakage, identity leak).
6. Next three actions with hour marks.

Do not emit a finished abstract until experiments exist.

Stop with:

```text
AWAITING_HUMAN_REVIEW(solution_direction)
```

If the human changes letters, return to S1. If they approve, go to S3.
