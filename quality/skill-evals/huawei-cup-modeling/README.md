# Eval viewer

Open `eval-report.html` after:

```text
python quality/skill-evals/huawei-cup-modeling/run_evals.py
```

Live answers belong in `runs/<id>/{baseline,with_skill}.md`.

## What is scored

- Description trigger / exclusion phrases
- SKILL.md hard bans present
- Optional live outputs against `evals.json` regex must / must_not

Training rubric scores are **not** official jury scores. Author-written with_skill answers are dry-run evidence, not a live-LLM delta. If dry-run exceeds 30% of a claimed behavioral experiment, do not report measured effectiveness.
