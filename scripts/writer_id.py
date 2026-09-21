#!/usr/bin/env python3
"""Resolve a contest-repo writer slug from git user.name (else user.email)."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

from _paths import SKILL_ROOT

LEDGER_HEADER = (
    "run_id,question,claim,baseline,slice,metric,value,script,seed,status,paper_eligible,writer\n"
)
ACTIVITY_TEMPLATE = SKILL_ROOT / "assets" / "activity-log.md"


def slugify(raw: str) -> str:
    lowered = raw.strip().lower()
    pieces = re.findall(r"[a-z0-9]+", lowered)
    return "-".join(pieces)


def git_config(contest: Path, key: str) -> str:
    git_dir = contest / ".git"
    if not git_dir.exists():
        return ""
    proc = subprocess.run(
        ["git", "config", "--get", key],
        cwd=contest,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return ""
    return proc.stdout.strip()


def resolve_slug(name: str = "", email: str = "") -> str:
    for raw in (name, email.split("@", 1)[0] if email else ""):
        slug = slugify(raw)
        if slug:
            return slug
    return ""


def contest_slug(contest: Path) -> str:
    if not (contest / ".git").exists():
        raise SystemExit(
            f"{contest} is not a git repo. Run git init, then git config user.name."
        )
    name = git_config(contest, "user.name")
    email = git_config(contest, "user.email")
    slug = resolve_slug(name, email)
    if not slug:
        raise SystemExit(
            "Set an ASCII git user.name (or user.email) in the contest repo, "
            "e.g. git config user.name alice"
        )
    return slug


def activity_path(contest: Path, slug: str) -> Path:
    return contest / "plans" / "activity" / f"{slug}.md"


def ledger_path(contest: Path, slug: str) -> Path:
    return contest / "results" / "ledger" / f"{slug}.csv"


def init_writer_files(contest: Path, slug: str) -> tuple[Path, Path]:
    act = activity_path(contest, slug)
    led = ledger_path(contest, slug)
    act.parent.mkdir(parents=True, exist_ok=True)
    led.parent.mkdir(parents=True, exist_ok=True)
    if not act.is_file():
        if ACTIVITY_TEMPLATE.is_file():
            text = ACTIVITY_TEMPLATE.read_text(encoding="utf-8")
        else:
            text = "# Activity log\n\n"
        if not text.lstrip().startswith("writer:"):
            text = f"writer: `{slug}`\n\n" + text
        act.write_text(text, encoding="utf-8")
    if not led.is_file():
        led.write_text(LEDGER_HEADER, encoding="utf-8")
    return act, led


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contest", type=Path, required=True)
    parser.add_argument("--init", action="store_true")
    args = parser.parse_args(argv)
    contest = args.contest.resolve()
    slug = contest_slug(contest)
    if args.init:
        act, led = init_writer_files(contest, slug)
        print(slug)
        print(act)
        print(led)
        return 0
    print(slug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
