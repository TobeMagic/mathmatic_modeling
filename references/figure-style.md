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
- Axes: quantity, unit, scale. Captions in Chinese, numbered `图 1` / `表 1`. Cite in text before the figure appears.
- **The image itself carries no metadata.** The `图 N` label, the overall figure title and any “数据来源 / run_id / 文件路径” line live in the caption and the body text, never inside the plot — `ctexart`’s `\caption` numbers figures and renumbers them when one is inserted, so a number burnt into the PNG will contradict it. What *is* figure content and stays: axis titles and units, ticks, legend, `(a)`/`(b)` panel markers, threshold lines, point annotations.
  - Enforce it, do not trust review: a plotting script must not call `fig.suptitle`, must not use `fig.text` for a source footnote, and must not pass `图 N …` to `ax.set_title`. Keep the caption strings in a table in the script and export them as pasteable LaTeX.
  - After removing footnotes, re-check annotation collisions: the footnote text used to stretch the canvas, and labels that cleared the bars before may now overlap them.
- Grayscale-safe line styles (reviewers print). Color-blind safe groups: not red/green only.
- Significant figures match measurement.
- Export **csv** from the run before polishing the figure. Caption numbers must match `result-ledger.csv`.
- Prefer vector (PDF/SVG/EMF) for line plots; PNG only for heavy rasters. Typical Word width: one-column ~7.5–8 cm, full ~14–16 cm. Body 小四; caption slightly smaller.

## Two visual registers (evidence from the reference set)

Rendered the route/flowchart pages of the first-prize PDFs. They do not use one
style; they use two, and mixing them is what makes a paper look amateur.

- **Overall technical roadmap — designed, tinted, full page.** Best in the set is
  2023 D23106350004 p.7: an outer rounded frame divided into one **swimlane per
  stage**, a right-pointing **banner** naming each lane, soft low-saturation
  fills (rose / sand / sage / slate) with a **hairline drop shadow**, **chevrons**
  instead of plain arrows, and a nested **"相关方法" side panel** listing the
  methods and solvers used in that lane. It occupies a whole page under its own
  heading. Add one more row per lane for *what the stage freezes and hands
  downstream* — that is what makes a four-problem paper legible at a glance.
- **In-chapter flowcharts — near-grayscale and plain.** 2022 D22103360092 p.11:
  rounded boxes, diamonds for decisions, thin black orthogonal arrows, light
  grey fills only. No tint, no shadow.

Implementation notes that cost a redraw each:
- Derive every lane/row `y` from the lane heights and the gap. Hand-placed
  coordinates put the methods panel on top of the last step of the chain.
- Draw the shadow as a second patch offset down-right, never a blur — a blur
  rasterises the whole vector figure.
- An em dash inside a CJK run (`运输—中继协同`) reads as the character 一 at
  figure sizes. Use `与`.
- Tables in this venue: horizontal rules only, light grey banding, no vertical
  lines.

## Rendering pitfalls that fail silently

These three cost a re-draw each and none of them raises an error.

- **Hard-coded CJK font.** `font.family = "Microsoft YaHei"` works on the box where the figures were first made and renders every Chinese label as a tofu box everywhere else; matplotlib only emits a `findfont` warning. Resolve against the installed faces with the Windows names first, so existing output is unchanged: `Microsoft YaHei → SimHei → Noto Sans CJK SC → Heiti SC → Hiragino Sans GB → Songti SC → Arial Unicode MS → DejaVu Sans`. Set `pdf.fonttype = 42` so the PDF embeds TrueType rather than Type 3.
- **Glyphs the CJK face does not have.** macOS system faces (Heiti SC, Songti SC) lack `⇒` (U+21D2) and `≻` (U+227B); matplotlib substitutes a blank box after a `UserWarning`. Use `→` (U+2192) and plain words (“依次为 …”) inside figures, and keep the fancy operators for LaTeX body text.
- **`bbox_inches="tight"` does not crop unused coordinate space.** The axes rectangle is itself an artist, so a hand-laid-out diagram that fills only the top 70% of a `0–100` coordinate box ships with a band of blank paper. Clamp `ylim` to the content extent before saving.
- Diagonal connectors drawn across a stack of boxes are unreadable. Route the link through its own vertical lane and turn at right angles; put the connector caption along the lane (rotated) rather than on top of the boxes it passes.

## Anti-patterns

Unlabeled 3D pies; notebook screenshots; logo collage; flowchart “建立模型 → 求解 → 结果”; two figures of the same bars; decorative clip-art to hit a CUMCM quota.
