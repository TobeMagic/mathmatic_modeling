# GitHub 数模 Skill 调研（用来改本仓库，不是用来换赛种）

`as_of`: 2026-08-31  
检索：GitHub 仓库名/描述含 mathmodel skill、华为杯、CPMCM、yansai；对照各仓库 README / `SKILL.md`。Star 数为当日 API 快照。

**结论先说：** 公开 Agent Skill 几乎全是 **CUMCM / MCM / 华数杯 / 电工杯**。没有发现第二个「只做中国研究生数学建模竞赛、且用获奖名单核验论文」的 skill。本仓库应继续做研赛特化，只吸收它们的**流程骨架**，不吸收它们的页数、图数、时长和「国一≥85」门槛。

## 1. 工作流类 Skill（可参考结构）

| 仓库 | ★ | 覆盖赛种 | 骨架 | 对本仓库 |
|---|---|---|---|---|
| [jihe520/MathModelAgent](https://github.com/jihe520/MathModelAgent) | 3971 | 自称国赛/华数杯/**华为杯**/美赛 Typst 模板 | 一键 `/1start-mathmodel` 出可提交论文 | **不采用**一键代写、不把社区 Typst 当官方模板。可承认「赛种要有独立模板」这一点。 |
| [XiaoMaColtAI/math-modeling-skill](https://github.com/XiaoMaColtAI/math-modeling-skill) | 975 | CUMCM、MCM/ICM | 建模手→编程手→论文手；固定交付物；独立质检 subagent；默认 ≥8 张正式图 | **采用**三角色、编程阶段、写长文前的证据门。**不采用** 8 图配额、15000 字/20 页。 |
| [zhnnky329/MathModeling-skills](https://github.com/zhnnky329/MathModeling-skills) | 670 | 建模竞赛通用 | 分阶段 + Python/MATLAB 分支 | 语言分支提醒有用；不强制 MATLAB。 |
| [yushui2022/MathModel-Skill](https://github.com/yushui2022/MathModel-Skill) | 327 | 偏 CUMCM；Trae/Claude/Codex | 可恢复 workflow；**证据门禁通过后才写正式论文**；反对一键生成 | **采用**证据门 + 「继续」恢复。与本仓库 `not-run` 纪律同向。 |
| [handsomeZR-netizen/mathmodel-skill](https://github.com/handsomeZR-netizen/mathmodel-skill) | 239 | CUMCM / MCM / 电工杯 | 10 阶段；`decision_log.json`；问答式；CUMCM 59 篇经验分位；**明确无华为杯** | **采用**启动字段、阶段懒加载、状态摘要。**不采用** CUMCM 分位当研赛分数。 |
| [sweetcornna/mathodology](https://github.com/sweetcornna/mathodology) | 148 | MCM、CUMCM、华数杯、M3… **无研赛** | 9 phase；盲评三席；Outstanding/国一 ≥85 | **不采用**把 85 分说成国一。可学「图 QA / PDF 匿名检查要脚本化」（本仓库已有 `validate_submission.py`）。 |
| [liuziyang337121/mathmodel-pro](https://github.com/liuziyang337121/mathmodel-pro) | ~9 | CUMCM/MCM | 审题→建模→编程→图表→论文→验收；**先打开数据**；MATLAB 核心计算 | **采用**先看数据、阶段验收标准。**不采用** MATLAB-only、国赛图表硬配额。 |

其它自动生成器（[xzwwwwww/Enhanced-mathmodel-Codex-skills](https://github.com/xzwwwwww/Enhanced-mathmodel-Codex-skills)、[N-allpass/modex-mh-agent](https://github.com/N-allpass/modex-mh-agent) 等）宣传「一夜出竞赛级论文 / 华为杯全覆盖」。**不采用。** 与本仓库「不代写、不编造数」冲突。

## 2. 资料库（不是 Skill，但常被误用）

| 仓库 | ★ | 注意 |
|---|---|---|
| [zhanwen/MathModel](https://github.com/zhanwen/MathModel) | ~10k | 研赛论文/试题/模板定位器。目录名不是奖状。 |
| [personqianduixue/Math_Model](https://github.com/personqianduixue/Math_Model) | 4995 | 本科国赛为主，夹了华为杯字样和**国赛评阅要点**。禁止把评阅要点写进研赛 rubric。 |
| [latexstudio/GMCMthesis](https://github.com/latexstudio/GMCMthesis) / [springli07/GMCM_LaTeX_overleaf](https://github.com/springli07/GMCM_LaTeX_overleaf) | — | 社区 LaTeX。官方仍是当届 Word《竞赛论文标准文档》。 |

## 3. 明确采用 / 明确拒绝

采用（已写进 skill；三角色只作能力，不写入运行协议）：

1. 建模、编程、写作是独立阶段能力，编程不是「实验设计」的附录；不在工作流里分派 M/C/W 队友。
2. 写摘要和长文之前必须过主张–证据门；缺数标 `not-run`。
3. 每阶段有 done-when 和人工 gate；用户说「继续」时先读 `state/workflow.md`。
4. 先打开附件数据再建模。
5. 只懒加载当前阶段的 reference。
6. 提交用脚本门禁，不用口头「已检查」。

拒绝：

1. 一键生成可提交论文。
2. CUMCM 的 72 小时、约 20 页、约 15000 字、至少 8 张正式图。
3. 「国一 / Outstanding ≥ 85」或任何冒充官方的百分制。
4. 强制 MATLAB。
5. 把本科评阅要点、美赛 COMAP 表、电工杯页序套到研赛。
6. 把研创网优秀作品 PPTX 或 CUMCM 网盘当研赛语料。

本仓库仍只服务华为杯 / 研赛 / CPMCM。需要本科国赛时，应另开那些 skill，不要混装规则。
