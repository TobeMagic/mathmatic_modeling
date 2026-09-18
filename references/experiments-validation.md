# Experiments and validation

Load this file for **S5** after G4: 实验设计, 验证, 消融, 灵敏度, or “how do we know the number is real”. Do not skip the baseline. When the matrix is honest, stop with `AWAITING_HUMAN_REVIEW(write_scope)`.

Training observation (`findings.md`): first-prize abstracts carry a **test**, not only a method name. Participation papers often stop at the method name.

Open the data files before filling this matrix. Guessed column meanings are not a baseline.

## Hard bans

- Do not invent RMSE, accuracy, utilization, or solver gaps.
- If a run is missing, write `status=not-run` and a plan. Leave the result cell blank.
- Do not tune on the test split and then report that split as unseen.
- Do not treat a second random seed as a scientific replicate if the split leaked.

## Universal minimum (every archetype)

Every headline number needs a row in `assets/experiment-matrix.md` with:

1. Claim
2. Baseline or null
3. Data slice (and whether it is train/test/all)
4. Metric
5. Check that could falsify the claim
6. Script path / seed (no teammate role)
7. Status: `planned` | `running` | `done` | `failed` | `not-run`

The paper may cite a number only from a `done` row. Keep the same rows in contest `results/result-ledger.csv` and `plans/experiment-matrix.md`.

Plus these checks when they apply:

- Units and missing values before modeling.
- Constraint feasibility after optimization (violation count = 0, or report the slack).
- A dumb baseline: mean predictor, greedy, all-in-one-lane, published formula, random assignment.
- A failure case: where the model is wrong, and why that does not sink the contest question.

## Archetype overlays

### optimization-scheduling

- Feasibility first, objective second.
- Report objective **and** constraint residuals.
- Keep a greedy / FIFO / “single lane” policy (2022-C all-lane-4 = 35.1 vs optimized 53.04 on attachment 2).
- If the instance is large: time cap, gap, population size, and a second instance.
- Complexity or wall-clock, even if crude (2022-B reports 0.22–23.78 s).

### signal-inverse / communications

- Compare against a named classical estimator or closed-form model (Bianchi, MUSIC, FBSS).
- Sweep SNR, geometry, or topology. State which methods break (2022-A drops FBSS).
- If you “simulate”, name the event loop. 2023-A writes a discrete-event simulator, not the sentence “we simulated”.

### prediction-diagnosis

- Time-aware split. No future features in the past.
- Report at least two of RMSE / MAE / R² / class-specific error, plus residual plots.
- Ablate features and the fancy block (LSTM vs stacking in 2022-E).
- Calibration or confusion where the output is a class.

### mechanism-simulation

- Recover a known special case (zero source, conservation, steady state).
- Fit-vs-mechanism: if you add a data-driven residual, show the mechanism-only error first (2022-E Woodward RMSE 513.75 vs improved 221.61).
- Perturb inputs ±10–20% and report loss of skill (2022-E 63.91% vs 10.37%).

### image-spatial

- Pixel metrics (mPA, Accuracy) **and** a geometric metric (RMSE of fitted sine, JRC error).
- Show a failure crop, not only the best crop.
- Uncertainty: Monte Carlo / noise injection, as in the 2025 C star-champion report layer.

### evaluation-decision

- Do not “validate” a ranking with the same scores that produced it.
- Use a later-stage consensus, overlap, inversion count (2023-C 重合度 / 乱序度).
- Stress unfair reviewers, missing reviews, and load imbalance.

## Ablation, not decoration

An ablation removes one design choice. “We also tried Adam” is not an ablation.

Order:

1. Baseline
2. + the one modeling idea that the team wants to claim
3. + extra gadgets, one at a time
4. Full model
5. Full model under perturbation

## Leakage checklist (prediction and spatial)

- Target constructed with future information
- Standardizing with the test set
- Random split of a time series
- Duplicate rows across train/test (same borehole, same day, same radar volume)
- Using the contest’s own later question as a feature for an earlier one without declaring the leak

## What to write in the paper

One paragraph per question: setup, baseline, number, falsification check, limitation. Then put the table. The figure must match the table. If they disagree, the table wins until the figure is fixed.
