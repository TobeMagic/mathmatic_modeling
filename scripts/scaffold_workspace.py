#!/usr/bin/env python3
"""Create a contest workspace git tree (separate from this Skill repo)."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from _paths import SKILL_ROOT

DIRS = [
    "plans",
    "problem/statement",
    "problem/attachments",
    "problem/official",
    "research/literature",
    "modeling",
    "code/q1",
    "code/q2",
    "data/raw",
    "data/processed",
    "experiments/configs",
    "experiments/runs",
    "results/tables",
    "results/figures",
    "results/exports",
    "reports",
    "paper/sections",
    "paper/manuscript",
    "paper/references",
    "paper/build",
    "paper/submission",
]

COPIES = {
    "assets/plans-STATE.md": "plans/STATE.md",
    "assets/plans-PROJECT.md": "plans/PROJECT.md",
    "assets/plans-CONTEXT.md": "plans/CONTEXT.md",
    "assets/plans-solution.md": "plans/solution.md",
    "assets/execution-plan-slice.md": "plans/execution-plan.md",
    "assets/experiment-matrix.md": "plans/experiment-matrix.md",
    "assets/schedule-96h-solo.md": "plans/schedule-96h.md",
    "assets/claim-evidence-matrix.md": "plans/claim-evidence.md",
    "assets/run-log.md": "plans/run-log.md",
    "assets/letter-comparison-matrix.md": "research/letter-comparison-matrix.md",
    "assets/abstract-skeleton.md": "paper/sections/abstract.md",
    "assets/figure-checklist.md": "paper/figure-checklist.md",
    "assets/workspace-template/README.md": "LAYOUT.md",
}

LEDGER = """run_id,question,claim,baseline,slice,metric,value,script,seed,status
"""

GITIGNORE = """data/raw/
experiments/runs/*/tmp/
paper/build/
*.pdf
.DS_Store
"""

README = """# Contest workspace

Initialized from the Huawei Cup Skill repo (`scaffold_workspace.py`).

- Progress: `plans/STATE.md`
- Plan / matrix: `plans/solution.md`, `plans/experiment-matrix.md`, `plans/execution-plan.md`
- Numbers: `results/result-ledger.csv`
- Our paper: `paper/`
- Reference first-prize PDFs stay in the **Skill** repo under `ref-papers/`. Do not copy them here.
"""

RUN_README = """# One folder per run

Name: `{question}-{model}-{yyyymmdd}-{seq}` e.g. `q1-fifo-20260923-01`

Keep: `config.yaml`, `log.txt`, `metrics.json`, `hashes.txt`.
Copy headline metrics into `results/result-ledger.csv`.
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dest", type=Path, required=True)
    args = parser.parse_args(argv)
    dest = args.dest.resolve()
    dest.mkdir(parents=True, exist_ok=True)
    for rel in DIRS:
        folder = dest / rel
        folder.mkdir(parents=True, exist_ok=True)
        if not any(p.is_file() for p in folder.glob("*")):
            (folder / ".gitkeep").write_text("", encoding="utf-8")
    for src_rel, dst_rel in COPIES.items():
        src = SKILL_ROOT / src_rel
        dst = dest / dst_rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.is_file():
            shutil.copyfile(src, dst)
    (dest / "results" / "result-ledger.csv").write_text(LEDGER, encoding="utf-8")
    (dest / "experiments" / "runs" / "README.md").write_text(RUN_README, encoding="utf-8")
    (dest / "reports" / "data-audit.md").write_text("# Data audit\n\n", encoding="utf-8")
    (dest / "reports" / "baseline.md").write_text("# Baseline report\n\n", encoding="utf-8")
    (dest / "reports" / "validation.md").write_text("# Validation report\n\n", encoding="utf-8")
    (dest / "modeling" / "assumptions.md").write_text("# Assumptions\n\n", encoding="utf-8")
    (dest / "modeling" / "symbols.md").write_text("# Symbols\n\n", encoding="utf-8")
    (dest / "modeling" / "baseline.md").write_text("# Baseline notes\n\n", encoding="utf-8")
    (dest / "modeling" / "candidates.md").write_text("# Candidates\n\n", encoding="utf-8")
    (dest / ".gitignore").write_text(GITIGNORE, encoding="utf-8")
    (dest / "README.md").write_text(README, encoding="utf-8")
    print(dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
