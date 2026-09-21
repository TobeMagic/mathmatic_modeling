# 无 activity shard 则论文侧当没跑过

`experiments/runs/q1-greedy-01/metrics.json` 和某份 ledger `done` 不够。没有任何 `plans/activity/*.md` 对应行，论文车道视为 **not-run**。

不能把 RMSE 写进摘要。先 `python scripts/writer_id.py --contest . --init`，追加**自己的** activity 文件，G5 在 `plans/claim-evidence.md` 把 `paper_eligible` 改成 `authorized` 后再 ingest。

```text
AWAITING_HUMAN_REVIEW(write_scope)
```
