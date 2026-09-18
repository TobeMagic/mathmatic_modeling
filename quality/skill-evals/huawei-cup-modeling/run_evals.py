#!/usr/bin/env python3
"""Static + file-based evals for the Huawei Cup skill.

Live model outputs (optional) are graded from evals/runs/<case>/<condition>.md
Static checks do not need a model: description triggers and SKILL.md bans.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
from _paths import QUALITY as EVALS  # noqa: E402
from _paths import SKILL_ROOT  # noqa: E402

SKILL_MD = SKILL_ROOT / "SKILL.md"


def frontmatter_description(text: str) -> str:
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    fm = parts[1]
    folded = re.search(r"description:\s*>-?\s*\n((?:[ \t]+.+\n)+)", fm)
    if folded:
        return " ".join(line.strip() for line in folded.group(1).splitlines())
    simple = re.search(r"description:\s*(.+)", fm)
    return simple.group(1).strip() if simple else fm


def trigger_hits(description: str, prompt: str) -> bool:
    desc = description.lower()
    # Skill descriptions are the routing surface. A prompt should fire if it
    # shares a distinctive contest token with the description.
    tokens = [
        "华为杯",
        "研赛",
        "中国研究生数学建模",
        "研究生数学建模",
        "数模之星",
        "cpmcm",
        "华为杯论文",
        "研赛评阅",
    ]
    prompt_l = prompt.lower()
    return any(tok.lower() in prompt_l and tok.lower() in desc for tok in tokens)


def negative_should_not_hit(description: str, prompt: str) -> bool:
    """Negative prompts may mention 数学建模; they must not be the only cue.

    Pass if the prompt does not contain a positive token, or if the
    description explicitly excludes the undergraduate / SCI case.
    """
    if trigger_hits(description, prompt):
        return False
    desc = description
    if "SCI" in prompt or "sci" in prompt.lower():
        return "SCI" in desc or "sci" in desc.lower()
    if "大学生" in prompt or "CUMCM" in prompt.upper() or "本科" in prompt:
        return "大学生" in desc or "CUMCM" in desc or "本科" in desc
    return True


def grade_text(text: str, must: list[str], must_not: list[str]) -> dict:
    misses = [p for p in must if not re.search(p, text, re.I | re.S)]
    leaks = [p for p in must_not if re.search(p, text, re.I | re.M)]
    return {"pass": not misses and not leaks, "misses": misses, "leaks": leaks}


def skill_ban_selfcheck(skill_text: str) -> dict:
    must = [
        r"not-run|不编造|fabricate",
        r"training_score|不是官方|not official",
        r"2025-provisional|尚未|unpublish",
        r"validate_submission",
        r"数模之星",
    ]
    return grade_text(skill_text, must, [r"官方百分制为", r"保证一等奖"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=Path, default=EVALS / "runs")
    args = parser.parse_args()
    spec = json.loads((EVALS / "evals.json").read_text(encoding="utf-8"))
    skill_text = SKILL_MD.read_text(encoding="utf-8")
    description = frontmatter_description(skill_text)
    report = {"skill_bans": skill_ban_selfcheck(skill_text), "triggers": [], "cases": []}

    for prompt in spec["trigger_positive"]:
        ok = trigger_hits(description, prompt)
        report["triggers"].append({"prompt": prompt, "expect": True, "hit": ok, "pass": ok})
    for prompt in spec["trigger_negative"]:
        ok = negative_should_not_hit(description, prompt)
        hit = trigger_hits(description, prompt)
        report["triggers"].append({"prompt": prompt, "expect": False, "hit": hit, "pass": ok and not hit})

    for case in spec["cases"]:
        row = {"id": case["id"], "conditions": []}
        for cond in ("baseline", "with_skill"):
            path = args.runs / case["id"] / f"{cond}.md"
            if not path.exists():
                row["conditions"].append({"condition": cond, "present": False, "pass": None})
                continue
            text = path.read_text(encoding="utf-8")
            graded = grade_text(text, case["must"], case["must_not"])
            graded.update({"condition": cond, "present": True, "path": str(path)})
            row["conditions"].append(graded)
        report["cases"].append(row)

    out = EVALS / "eval-report.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    html = EVALS / "eval-report.html"
    html.write_text(_html(report), encoding="utf-8")
    trig_pass = all(t["pass"] for t in report["triggers"])
    bans_pass = report["skill_bans"]["pass"]
    skill_live = []
    for case in report["cases"]:
        for cond in case["conditions"]:
            if cond.get("condition") == "with_skill" and cond.get("present"):
                skill_live.append(bool(cond.get("pass")))
    live_pass = all(skill_live) if skill_live else True
    print(
        json.dumps(
            {
                "skill_bans": bans_pass,
                "triggers": trig_pass,
                "with_skill_live": live_pass,
                "report": str(out),
                "html": str(html),
            },
            ensure_ascii=False,
        )
    )
    return 0 if trig_pass and bans_pass and live_pass else 1


def _html(report: dict) -> str:
    def row_ok(flag) -> str:
        if flag is True:
            return "PASS"
        if flag is False:
            return "FAIL"
        return "N/A"

    trig_rows = "".join(
        f"<tr><td>{row_ok(t['pass'])}</td><td>{'hit' if t['hit'] else 'miss'}</td><td>{t['prompt']}</td></tr>"
        for t in report["triggers"]
    )
    case_rows = []
    for case in report["cases"]:
        for cond in case["conditions"]:
            case_rows.append(
                "<tr>"
                f"<td>{case['id']}</td><td>{cond.get('condition')}</td>"
                f"<td>{row_ok(cond.get('pass'))}</td>"
                f"<td>{cond.get('misses') or ''}</td>"
                f"<td>{cond.get('leaks') or ''}</td>"
                "</tr>"
            )
    bans = report["skill_bans"]
    return f"""<!doctype html>
<meta charset="utf-8">
<title>Huawei Cup skill evals</title>
<style>
body {{ font-family: sans-serif; margin: 24px; }}
table {{ border-collapse: collapse; width: 100%; }}
td, th {{ border: 1px solid #ccc; padding: 6px 8px; text-align: left; }}
</style>
<h1>Huawei Cup skill evals</h1>
<p>Training scores in live outputs are not official jury scores.</p>
<h2>SKILL.md bans</h2>
<pre>{json.dumps(bans, ensure_ascii=False, indent=2)}</pre>
<h2>Triggers</h2>
<table><tr><th>result</th><th>hit</th><th>prompt</th></tr>{trig_rows}</table>
<h2>Live cases</h2>
<table><tr><th>id</th><th>condition</th><th>result</th><th>misses</th><th>leaks</th></tr>{''.join(case_rows)}</table>
"""


if __name__ == "__main__":
    raise SystemExit(main())
