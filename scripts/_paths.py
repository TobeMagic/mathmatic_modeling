"""Single source of truth for repo / skill / research paths."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT
RESEARCH = REPO_ROOT / "research" / "huawei-cup"
REF_PAPERS = REPO_ROOT / "ref-papers"
QUALITY = REPO_ROOT / "quality" / "skill-evals" / "huawei-cup-modeling"
DIST = REPO_ROOT / "dist"
