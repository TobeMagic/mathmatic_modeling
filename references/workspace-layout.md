# Contest workspace layout

This file is the Skill-repo spec for **a separate contest git repo**.  
The Skill lives here (`mathmatic_modeling`). Modeling, code, experiments, and **our** paper live in the contest repo created by:

```text
python scripts/scaffold_workspace.py --dest <contest-repo>
```

Do not put teammate role names on folders. Shared git folders are enough.

## Tree

```text
README.md
.gitignore
LAYOUT.md

plans/                     # Superpower-style control plane: 方案 + 实验 + 进度
  STATE.md                 # current_stage, open_gate, next action
  PROJECT.md               # year, letter, title, year-tag
  CONTEXT.md               # locked decisions (letter, baseline, write scope)
  solution.md              # 建模方案：契约、候选、淘汰
  experiment-matrix.md     # 要跑什么（计划），不是跑出的数
  execution-plan.md        # High-tier 切片
  schedule-96h.md
  claim-evidence.md        # 主张 → ledger 行 + paper_eligible（写稿侧维护）
  activity/<slug>.md       # 每人一份追加日志；S6 读全部
  run-log.md               # 可选账本快照，不要拿它代替 activity/

problem/                   # 当届题面与官方文件
  statement/
  attachments/
  official/

research/                  # 侦察与文献笔记（不是参考国一全文）
  letter-comparison-matrix.md
  literature/

modeling/                  # 假设、符号、基线说明、候选记录
  assumptions.md
  symbols.md
  baseline.md
  candidates.md

code/                      # 队友自选语言；Skill 不放语言模板
  q1/
  q2/

data/
  raw/                     # 赛题附件，默认 gitignore
  processed/

experiments/               # 配置 + 每一次运行
  configs/
  runs/
    <question>-<model>-<slug>-<yyyymmdd>-<seq>/
      config.yaml
      log.txt
      metrics.json
      hashes.txt

results/                   # 论文只引用这里的数和图
  tables/
  figures/
  exports/
  ledger/<slug>.csv        # 每人一份；不要共享 result-ledger.csv

reports/
  data-audit.md
  baseline.md
  validation.md

paper/                     # OUR draft only. Never copy ref-papers into here.
  sections/
  manuscript/
  references/
  build/                   # gitignore
  submission/
```

There is **no** `compliance/`, `reviews/`, `src/`, or top-level `state/`. Progress is `plans/STATE.md`.

## Two-repo rule

| Path | Whose paper |
|---|---|
| Skill repo `ref-papers/` | REFERENCE only. Filename starts with `{year}-{tier}-{team_id}-`. Never treat as our manuscript. |
| Contest repo `paper/` | OUR draft. Numbers only from some `results/ledger/*.csv` with `status=done` and `paper_eligible=authorized` or `in_draft`, plus a matching `run_id` in some `plans/activity/*.md`. |

Cite a reference as `[参考] 2024-first-A24102940057 p.2`. Do not write 本文 / 我们 about a file under `ref-papers/`.

## Number source of truth

`python scripts/writer_id.py --contest <contest-repo> --init` → `experiments/runs/<id>/` → **your** `results/ledger/<slug>.csv` + **append your** `plans/activity/<slug>.md` → `plans/claim-evidence.md` (`paper_eligible`, paper lane) → `paper/sections/`.

S6 reads **all** shards. A run with `metrics.json` but no `run_id` in any `plans/activity/*.md` is **not-run** for the paper lane.

`paper_eligible`: `no` | `candidate` | `authorized` | `in_draft` | `stale`. Teammates mark `candidate` on **their** ledger; G5 records `authorized` on `plans/claim-evidence.md`; S6 ingest sets `in_draft` there. Do not edit a teammate's activity or ledger file.

If code changed after a cited number, mark the ledger row `stale` on **your** shard and re-run. Append a new activity row; do not edit history.

## Git

Commit text, code, configs, **per-writer** ledgers, and small figures. Keep huge `data/raw/` local. Do not put Skill-repo reference PDFs into the contest repo. Do not commit `results/result-ledger.merged.csv`.
