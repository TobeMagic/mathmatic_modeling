# AI figure prompts (skeletons)

Use only for **concept / route / procedure** drafts. Comparison, sensitivity, and diagnostic plots must be drawn from `experiments/runs/` data, not from a generative image.

If you use an image model, log it in the contest `plans/run-log.md` (tool / version / purpose). Do not list “AI 作图” as 创新点. As of 2026-09-18 the AI-annex notice exists; until it is transcribed, treat 2025 hygiene as a labeled fallback (`references/ai-integrity.md`).

Replace `{...}` placeholders. Never put school names or team ids in the prompt.

## Route (技术路线)

```text
Clean academic flowchart, left-to-right, white background, black text,
Chinese labels, no 3D, no clip-art people, no logos.
Boxes: {data} → {baseline model} → {main model} → {check: feasibility or hold-out} → {output}.
Line arrows only. Printable in grayscale. 16:9, high contrast.
Not a contest paper page; no fake RMSE numbers.
```

## Procedure (单问流程)

```text
Vertical flowchart for question {Qn} only.
Nodes name real files or methods: {attachment}, {algorithm}, {metric}.
No generic ovals “建模/求解/结果”. Flat 2D, Chinese, grayscale-safe.
```

## Comparison (must be data-drawn)

Do not generate this with an image model. Plot `{metric}` vs `{baseline}` from `results/exports/{id}.csv`. Caption: claim + slice + comparator.

## Sensitivity (must be data-drawn)

Do not generate this with an image model. Sweep `{param}` ±{pct}% from the ledger run.

## Spatial / signal (must be data-drawn)

Do not invent a heatmap. Use the array written by the run script.

## After AI draft

Redraw in matplotlib / MATLAB / Origin / TikZ from real data, or keep only the route/procedure schematic and strip any invented numbers from labels.
