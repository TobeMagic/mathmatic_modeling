# 论文从哪下（官方入口不可用）

`as_of`: 2026-09-01

官方研创网「优秀作品」已核验为 **宣传 PPTX**，不是论文集。不要登录去下、不要当语料。

下面是可用来找**真论文 PDF** 的第三方定位器。文件夹名叫「优秀论文」**不等于**得过奖；队号必须和 [CPMCM-Awards](https://github.com/lcpmgh/CPMCM-Awards/tree/master/awardlist) 的 `所获奖项` 对上。CSV 里的队号没有题号字母，匹配前去掉文件名开头的 `A–F`。

不要把 PDF 提交进 git。放到 `research/huawei-cup/cache/papers/`（已 gitignore）。

## 你先下这些

按优先级。链接会失效，以当时 [zhanwen/MathModel README](https://github.com/zhanwen/MathModel) 为准。

| 优先级 | 内容 | 怎么下 | 提取码 | 备注 |
|---|---|---|---|---|
| 1 | **2024 论文包**（近年缺口） | https://pan.baidu.com/s/1uxhi5n47ZsLm9fU1xqpS3g | `opr4` | zhanwen 标注「2024年优秀论文」。本仓库已本地入库 24 篇国一（24/242）。下完必须核队号。 |
| 2 | **2022–2023 全文** | GitHub 目录，不必网盘 | — | [2023](https://github.com/zhanwen/MathModel/tree/master/国赛论文/2023年优秀论文) · [2022](https://github.com/zhanwen/MathModel/tree/master/国赛论文/2022年优秀论文)。本仓库深读样本已用过。也可：`python scripts/ingest_corpus.py --per-cell 4 --download` |
| 3 | 2022 论文网盘镜像 | https://pan.baidu.com/s/1WbDSEvYerB9LqsMTcAQLNg | `i7in` | GitHub 已有同批文件时可不下。 |
| 4 | 2021 / 2020 / 2019 | https://pan.baidu.com/s/1j0rqd6tvKv4LxGRG0kUaKw · https://pan.baidu.com/s/1NK3_QXdU6gPH27_gABMUIw · https://pan.baidu.com/s/1xt8R7ad_o7zBEZGZvqA3MA | `eyzf` / `odt5` / `2uyl` | 更早届次；同样要核名单。 |
| 5 | 2024 赛题（不是论文） | https://pan.baidu.com/s/1JIH0EbDA0xFef53AIHMymA 或 GitHub `国赛试题/2024…` | `v44w` | 只作读题练习。 |

**失效，不要用：** 123 云盘 `https://www.123912.com/s/kqwxjv-aSaD3?pwd=wdXI`（2026-08-31 无效）。

2025 **没有**找到稳定的公开全文普查。目前只能下作者自存稿（见下一节），再对获奖名单。

## 作者自存（近年对照，不是官方集）

这些是单队开源，奖项以名单为准，不要凭 README 自称。

| 仓库 | 自称内容 | 用途 |
|---|---|---|
| [JunHuaBai96/Mathematical-Modeling](https://github.com/JunHuaBai96/Mathematical-Modeling) | 2024 / 2025 C 题论文+数据+代码 | 已作对照样本 |
| [LY-zhang-yi-hao/Huawei_Mathcup_OpenAccess](https://github.com/LY-zhang-yi-hao/Huawei_Mathcup_OpenAccess) | 2024 国二；另附 123 盘范文 | 对照。123 盘链接已失效，不要用。 |
| [Nanqipro/25HuaweiCup_MCM](https://github.com/Nanqipro/25HuaweiCup_MCM) | 2025 C，自称国三 | 近年对照 |
| [RessMatthew/HuaweiCup-E](https://github.com/RessMatthew/HuaweiCup-E) | 2025 E 实现 | 代码向，论文不一定全 |
| [duyu09/VibCogTriNet](https://github.com/duyu09/VibCogTriNet) | 2025 轴承/故障相关 | 代码向 |
| [Cyril-ljx/HuaweiCup_2024](https://github.com/Cyril-ljx/HuaweiCup_2024) | 2024 参赛 | 未核奖项先当未核验 |
| [ydchen0806/23yansaiE](https://github.com/ydchen0806/23yansaiE) | 2023 E，含 tex/PDF | 单题 |
| [LZH20001220/HuaweiCup2023](https://github.com/LZH20001220/HuaweiCup2023) | 2023 A 仿真代码 | 代码向 |
| [hiyouga/HuaweiCup2021-MCM-ProblemE](https://github.com/hiyouga/HuaweiCup2021-MCM-ProblemE) | 2021 E 自称国一 | 核名单后可读 |
| [qssxbhxy/2019GMCM](https://github.com/qssxbhxy/2019GMCM) | 2019 F 自称第一名+代码 | 核名单后可读 |
| [DongZhouGu/MathModel-Pretrain](https://github.com/DongZhouGu/MathModel-Pretrain) | 2021 D 自称数模之星相关 | 星级含答辩，不是纯论文名次 |
| [rnzhiw/HuaweiCupMathModel](https://github.com/rnzhiw/HuaweiCupMathModel) | 2021 D 自称国二 | 对照 |
| [Jayc-Z/2022HuaweiCup](https://github.com/Jayc-Z/2022HuaweiCup) | 2022 E 自称国三 | 弱对照 |
| [Bighhhzq/Mathematical-modeling](https://github.com/Bighhhzq/Mathematical-modeling) | 2021 D 队自存 | 对照 |
| [zhenhua-chen1/Postgraduate-Mathematical-Contest-in-Modelling](https://github.com/zhenhua-chen1/Postgraduate-Mathematical-Contest-in-Modelling) | 优化类历年代码 | 算法笔记，不是论文集 |
| [LUORANCHENG/HUAWEI_Math_Modeling_Knowledge](https://github.com/LUORANCHENG/HUAWEI_Math_Modeling_Knowledge) | 2024/2025 赛题知识点 | 选题预习，无全文 |

获奖名单（无 PDF）：[lcpmgh/CPMCM-Awards](https://github.com/lcpmgh/CPMCM-Awards) `awardlist/{year}.csv`。

## 过期大包（不必优先）

zhanwen 还挂着 2020 年左右的整库镜像，很可能**不含** 2024–2025 论文：

- 微盘 https://share.weiyun.com/Lk0sE1o4 码 `uzw9mf`
- 百度 https://pan.baidu.com/s/1dOl-MRXtkLBU2l_UWPpYdA 码 `bxdy`
- 备用 `0rm9` / `5s6y` / `29vl`（README 里的另外三条百度链）

失效就放弃，不要买 CSDN 替代。

## 不要下、不要当研赛论文

- 研创网 KDocs「优秀作品」（宣传稿）
- [cmathc 2010–2025 优秀论文网盘](https://www.cmathc.org.cn/mcm/lw/530.html)（那是**本科国赛 CUMCM**）
- CSDN / 付费「2004–2023 合集」、荔枝科研等「标准答案」
- AtomGit / GitCode 未核验「优秀论文资源库」
- 把 `personqianduixue/Math_Model` 里的**本科评阅要点**当成华为杯评分表

## 安装到本仓库之后

1. 解压 PDF 到 `research/huawei-cup/cache/papers/`，文件名尽量保留队号。
2. 在 `research/huawei-cup/cache/` 留一份清单，每行：

```text
届次  题号  队号  文件名  来源(github/baidu/123pan/author)  文档或名单上的奖项原文
```

3. 把清单发我。我可以：哈希、抽文本、对 `CPMCM-Awards`、标 `verified-first-prize` / `author-posted` / `unverified`。

没有队号的文件只当阅读材料，不进一等奖统计。
