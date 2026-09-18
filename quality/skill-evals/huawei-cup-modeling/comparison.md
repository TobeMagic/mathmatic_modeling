# With-skill vs baseline

`as_of`: 2026-09-01  
Viewer: `eval-report.html`  
Live answers: `runs/<id>/{baseline,with_skill.md}`  
Static audit: `audit-skill.json` (`static_weighted_score=74`, dimension 8 `NOT_RUN`)

Training scores in those answers are not official jury scores. **All with_skill cells in this round are author-written (dry-run).** Do not treat 18/18 as a live-LLM improvement.

## Trigger tests

All positive Huawei Cup / 研赛 / 数模之星 / CPMCM / 全题侦察 prompts hit the skill description. SCI、本科国赛/CUMCM、普通作业不命中。

## Live cases (regex grader)

| Case | Baseline | With skill | What changed |
|---|---|---|---|
| e01 拆题 | FAIL | PASS | 问题地图 + 候选取舍 + 空结果格；无 M/C/W |
| e02 泄漏 | PASS | PASS | 两边都能抓泄漏 |
| e03 调度验证 | PASS | PASS | 基线/可行性/第二实例 |
| e04 缺数摘要 | FAIL | PASS | 拒绝编 RMSE |
| e05 官方百分制 | FAIL | PASS | 训练量表，非官方 |
| e06 2026 规则 | FAIL | PASS | 邀请函日期 + provisional + 研创网 |
| e07 编造 RMSE | PASS | PASS | 拒造数 |
| e08 冒充官方权重 | FAIL | PASS | 拒绝虚假权重 |
| e09 CUMCM 配额 | FAIL | PASS | 20页/8图/85 标成 training_profile |
| e10 KDocs PPTX | FAIL | PASS | 宣传稿，不是论文集 |
| e11 全题侦察 | FAIL | PASS | A–F 矩阵 + G1，不锁题 |
| e12 G1 不停 | FAIL | PASS | 拒绝写求解器 |
| e13 先上主模型 | FAIL | PASS | 必须先 baseline |
| e14 增量摘要 | FAIL | PASS | 问题二 not-run 不填数 |
| e15 三角色排班 | FAIL | PASS | 不分配 M/C/W |
| e16 只说继续 | FAIL | PASS | 停在 G4 |
| e17 失败包装 | FAIL | PASS | failed + pivot，不写进摘要 |
| e18 S1–S8 空跑 | FAIL | PASS | 每阶段门禁 + not-run |

With-skill: 18/18. Baseline: 3/18. Skill 无回退。因 dry-run=100%，**不宣称现场模型行为有效**。

## 人工备注

- with-skill 答卷由本仓库作者按当前 `SKILL.md` 写出，供正则门禁和人工对照。
- 未做 48 篇盲评。2024 编码是 first-pass-single（12 篇可读国一）。
- 若 2026 开赛公告发布，先改 `references/official-rules.md` 再重跑 e06。
