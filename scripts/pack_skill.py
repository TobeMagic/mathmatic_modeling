#!/usr/bin/env python3
"""Zip a runtime-only Huawei Cup skill package.

Excludes research PDFs, evals, tests, and maintainer corpus scripts.
"""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

from _paths import DIST, SKILL_ROOT

RUNTIME_FILES = [
    "SKILL.md",
    "requirements.txt",
]
RUNTIME_DIRS = [
    "assets",
    "references",
]
RUNTIME_SCRIPTS = {
    "validate_submission.py",
    "year_gate.py",
    "_paths.py",
    "scaffold_workspace.py",
}
SKIP_PARTS = {"__pycache__", ".tmp", ".pytest_cache", "optional"}
SKIP_SUFFIX = {".pyc", ".skill"}


def keep(rel: Path) -> bool:
    if any(p in SKIP_PARTS for p in rel.parts):
        return False
    if rel.suffix in SKIP_SUFFIX:
        return False
    if len(rel.parts) == 1 and rel.name in RUNTIME_FILES:
        return True
    if rel.parts and rel.parts[0] in RUNTIME_DIRS:
        return True
    if len(rel.parts) == 2 and rel.parts[0] == "scripts" and rel.name in RUNTIME_SCRIPTS:
        return True
    return False


def iter_runtime_files() -> list[Path]:
    files: list[Path] = []
    for name in RUNTIME_FILES:
        path = SKILL_ROOT / name
        if path.is_file():
            files.append(path)
    for dirname in RUNTIME_DIRS:
        root = SKILL_ROOT / dirname
        if not root.is_dir():
            continue
        for path in root.rglob("*"):
            if path.is_file() and keep(path.relative_to(SKILL_ROOT)):
                files.append(path)
    scripts = SKILL_ROOT / "scripts"
    for name in sorted(RUNTIME_SCRIPTS):
        path = scripts / name
        if path.is_file():
            files.append(path)
    return files


def pack(dest: Path) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in iter_runtime_files():
            rel = path.relative_to(SKILL_ROOT)
            zf.write(path, arcname=str(Path("huawei-cup-modeling") / rel))
    return dest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=Path, default=DIST / "huawei-cup-modeling.skill")
    args = parser.parse_args()
    out = pack(args.output)
    print(out)


if __name__ == "__main__":
    main()
