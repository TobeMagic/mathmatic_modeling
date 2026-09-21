# Activity log（每人一份，只追加）

竞赛仓执行记录。身份由 `python scripts/writer_id.py --contest <contest-repo>` 从该仓 `git user.name`（否则 `user.email` 本地部分）生成 slug。

每人只写自己的 `plans/activity/<slug>.md`。禁止改别人的文件。S6 读 `plans/activity/*.md` 全部碎片。

每次真实跑完、失败、或把自己的 run ingest 进 `paper/sections/` 都**新起一行**。禁止改旧行；更正另起一行，并把旧 ledger 标 `stale`。

`paper_eligible`: `no` | `candidate` | `authorized` | `in_draft` | `stale`

- 建模/代码默认 `candidate` 或 `no`
- G5 把可写进正文的行记到 `plans/claim-evidence.md`（写稿侧维护），不要去改队友的 activity 文件
- 自己的 ingest 回执只追加**自己的** activity 文件

无任何 `plans/activity/*.md` 对应 `run_id` 的 metrics.json，论文侧视为**没跑过**。

| time | writer | question | run_id | claim | status | paper_eligible | note |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
