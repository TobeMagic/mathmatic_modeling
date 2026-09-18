# Training profiles (not official rules)

Huawei Cup official constraints stay in `official-rules.md` (anonymity, 2-page Chinese abstract, filename, MD5, template). Everything below is optional completeness.

Record the active profile in contest `plans/STATE.md` as `training_profile=`.

| Profile | Use | What it adds | What it must not do |
|---|---|---|---|
| `conservative-baseline` (default) | four-day contest | every Q has a baseline number or written failure; figures only if they have jobs | skip tests; invent RMSE |
| `full-draft` | user asked for a thick paper | aim ~20 pages, ~15000 字, ≥8 figures **with jobs** | claim these are Huawei Cup official quotas; pad clip-art |
| `matlab` | team runtime is MATLAB | core solvers in `.m`; Python only for glue | refuse Python when MATLAB is absent; hide the runtime actually used |
| `cross-contest-borrow` | CUMCM/MCM paper as method hint | cite the foreign paper as a method neighbour | copy CUMCM 评阅要点, 72h, 8-figure rules, or “国一≥85” |

`training_score` in S7 is independent of `full-draft`. A short evidenced paper can outscore a padded long one on the training rubric.

Borrowed from public contest skills (see `research/distillation/`): evidence gate before long prose, open-data-first, phase stop markers, PDF/anonymity scripts. Rejected as Huawei Cup law: one-click submittable papers, MATLAB-only, Outstanding/国一 ≥85.
