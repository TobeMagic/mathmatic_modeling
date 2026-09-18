# Letter survey (S1)

Load this file only for all-letter reconnaissance. Do not formulate a full model. Do not pick the letter.

Evidence pointers if present: Skill-repo `ref-papers/`, `research/huawei-cup/findings.md`, `research/huawei-cup/corpus-manifest.csv`. Cite `[参考] {year}-{tier}-{team_id}-{title} p.N`. Never paste paper sentences. Never treat `ref-papers/` as contest `paper/`.

## Goal

Fill `assets/letter-comparison-matrix.md` (copy into the contest repo as `research/letter-comparison-matrix.md`) for **every** numbered contest problem (usually A–F).

Then stop with:

```text
AWAITING_HUMAN_REVIEW(problem_choice)
```

## Per-letter pass (shallow)

For each letter write:

1. **Contract sketch** — what is given, what must be computed, output form. Do not invent extra questions.
2. **Archetype** — `optimization-scheduling` | `signal-inverse` | `prediction-diagnosis` | `mechanism-simulation` | `image-spatial` | `evaluation-decision` | mix.
3. **Novelty class** — `textbook` | `prior-contest-variant` | `industry-open` | `novel-engineering` | `unknown`.
4. **Known prior** — Huawei Cup first-prize neighbours first (year-letter, team id). CUMCM/MCM analogues second, labeled `cross-contest`.
5. **Data readiness** — files present? units? size? missingness? need extra unpublished data?
6. **Baseline ≤6h?** — name one dumb method that answers Q1 (greedy, closed form, mean predictor, published formula, rule policy).
7. **Validation tractability** — is there an official metric, second attachment, hold-out, feasibility check?
8. **Difficulty 1–5** — time/risk, not prestige.
9. **Scoring tractability 1–5** — can a reviewer see a test in the abstract?
10. **Winning-paper priorities** — 2–4 discriminator bullets from findings for that archetype (tests, rejection, numbers, figure jobs). Not genre padding.
11. **Shallow directions** — 2–3 family names, no formulas, no code.
12. **Risk flags** — leakage, infeasibility, identity, missing 2026 template, data too large, defense-only star reports.

## Rules

- Survey breadth beats depth. If literature is unknown, write `unknown` and a search query; do not fake a “best practice”.
- Huawei Cup first-prize papers outrank CUMCM/MCM Outstanding papers for **what the abstract should contain**. Cross-contest papers may suggest solvers or plot types.
- Do not recommend a letter unless the user asks for a ranking **and** you still leave G1 open.
- Do not start S2 in the same turn after filling the matrix.
