# 主张—证据矩阵

| claim_id | 正文位置 | 主张（一句话） | source_run | 证据类型（公式/表/图/实验 id） | 页码或文件 | 对照基线 | status | paper_eligible | 若未完成应写进论文的句子 |
|----------|----------|----------------|------------|----------------------------------|------------|----------|--------|----------------|--------------------------|
| C1 | 摘要-问题一 |  |  |  |  |  | not-run | no | 删除该句，不要填数 |
| C2 | 问题一 |  |  |  |  |  | not-run | no |  |
| C3 | 问题二 |  |  |  |  |  | not-run | no |  |
| C4 | 问题三 |  |  |  |  |  | not-run | no |  |
| C5 | 敏感性 |  |  |  |  |  | not-run | no |  |
| C6 | 创新点1 |  |  |  |  |  | not-run | no |  |

status: `done` | `not-run` | `contradicted`  
paper_eligible: `no` | `candidate` | `authorized` | `in_draft` | `stale`

规则：

- `not-run` 的主张不得出现在摘要里。
- `contradicted` 必须改主张或改实验，禁止删图留数。
- 正文数字只许来自 `status=done` **且** `paper_eligible=authorized` 或 `in_draft` 的行。
- `candidate` 只是队友想进论文的产出，G5 之前不得 ingest。
- `source_run` 必须能在 `experiments/runs/` 与某份 `plans/activity/*.md` 对上。
- 本表由写稿侧在 G5/S6 维护。建模的人不要改这张总表；他们只追加自己的 activity/ledger。
