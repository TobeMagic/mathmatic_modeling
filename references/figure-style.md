# Figure and table style

Load for 作图、表、图注、配色、导出到 Word. Companion checklist: `assets/figure-checklist.md`. AI prompt skeletons: `assets/figure-ai-prompts.md`.

Figures belong in the **contest** repo `results/figures/` and `paper/`. Do not save reference-paper screenshots as our figures.

Huawei Cup has **no** official “at least 8 figures” rule. Delete a figure that has no job.

## Jobs (one per figure)

1. **Route** — whole-paper technical route
2. **Procedure** — per-question flowchart with data and solver names
3. **Comparison** — baseline vs proposed, same axes
4. **Spatial / signal** — map, radar, residual, reconstruction
5. **Sensitivity** — sweep, tornado, perturbation
6. **Diagnostic** — residual vs fitted, Q-Q, constraint slack

## Table jobs

Symbol table; solver settings; main results vs baseline; sensitivity; feasibility / error breakdown. Do not duplicate a table as a 3D bar chart.

## Production rules

- Caption states the claim, dataset, and comparator. Readable without the body.
- Axes: quantity, unit, scale. Chinese captions; `图 1` / `表 1`. Cite in text before the figure appears.
- Grayscale-safe line styles (reviewers print). Color-blind safe groups: not red/green only.
- Significant figures match measurement.
- Export **csv** from the run before polishing the figure. Caption numbers must match `result-ledger.csv`.
- Prefer vector (PDF/SVG/EMF) for line plots; PNG only for heavy rasters. Typical Word width: one-column ~7.5–8 cm, full ~14–16 cm. Body 小四; caption slightly smaller.

## Anti-patterns

Unlabeled 3D pies; notebook screenshots; logo collage; flowchart “建立模型 → 求解 → 结果”; two figures of the same bars; decorative clip-art to hit a CUMCM quota.
