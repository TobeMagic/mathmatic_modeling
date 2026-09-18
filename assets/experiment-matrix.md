# 实验矩阵

赛年：____　题号：____　archetype：____

| id | question | claim | baseline / null | data slice (train/test/all) | metric | falsifier | code / seed | status | result (blank if not-run) |
|----|----------|-------|-----------------|------------------------------|--------|-----------|-------------|--------|---------------------------|
| E1 | Q1 |  |  |  |  |  |  | planned |  |
| E2 | Q1 |  |  |  |  |  |  | planned |  |
| E3 | Q2 |  |  |  |  |  |  | planned |  |
| E4 | Q2 |  |  |  |  |  |  | planned |  |
| E5 | Q3 |  |  |  |  |  |  | planned |  |
| E6 | all | sensitivity / perturbation |  |  |  |  |  | planned |  |
| E7 | all | failure case |  |  |  |  |  | planned |  |

Status vocabulary: `planned` | `running` | `done` | `failed` | `not-run`

Leakage notes (prediction / spatial):
- [ ] 时间切分而非随机切分
- [ ] 标准化未用测试集统计量
- [ ] 无未来特征进入过去
- [ ] 重复样本未跨集合
