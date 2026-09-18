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
  claim-evidence.md        # 主张 → ledger 行
  run-log.md               # 可选账本备份

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
    <run_id>/
      config.yaml
      log.txt
      metrics.json
      hashes.txt

results/                   # 论文只引用这里的数和图
  tables/
  figures/
  exports/
  result-ledger.csv

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
| Contest repo `paper/` | OUR draft. Numbers only from `results/result-ledger.csv` with `status=done`. |

Cite a reference as `[参考] 2024-first-A24102940057 p.2`. Do not write 本文 / 我们 about a file under `ref-papers/`.

## Number source of truth

`experiments/runs/<id>/` → `results/result-ledger.csv` → `plans/claim-evidence.md` → `paper/sections/`.

If code changed after a cited number, mark the ledger row `stale` and re-run.

## Git

Commit text, code, configs, ledgers, and small figures. Keep huge `data/raw/` local. Do not put Skill-repo reference PDFs into the contest repo.
