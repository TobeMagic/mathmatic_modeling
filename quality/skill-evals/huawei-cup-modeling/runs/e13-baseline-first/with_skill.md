# S4 必须先覆盖题目的 baseline

G3 计划已批准才能写求解器。默认仍是 conservative-baseline：先做一个几小时内能出数的基线（规则策略 / FIFO / 经典公式 / 均值预测），把 `results/result-ledger.csv` 写成 `done` 或 `failed`+转向。

拒绝把 Transformer 当作第一版结果。升级模型只在基线弱且有可证伪检查时进入 S5。

数据未打开则只做 data-open probe（形状、单位、缺失），仍不写深度求解器。
