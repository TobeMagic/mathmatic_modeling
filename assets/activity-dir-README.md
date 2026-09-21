# Per-writer activity logs

Do not share one `activity-log.md`. Each person writes only `plans/activity/<slug>.md`.

```text
python scripts/writer_id.py --contest . --init
```

Slug comes from this contest repo's `git user.name` (else `user.email` local part). ASCII `[a-z0-9-]` only.

S6 reads every `*.md` in this folder. Never edit a teammate's file.
