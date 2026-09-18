# Distilled findings

`as_of`: 2026-09-01  
`coder_id`: first-pass-single  
`sample`: 12 verified 2022–2023 first-prize PDFs (seed `20260829`) plus 12 readable 2024 first-prize local ingest papers (2 per A–F, excluding garbled extracts), 1 verified 2022 participation control, 2 author-posted 2024/2025 papers, 3 university star-finalist reports.  
`coding_sheet`: `research/huawei-cup/coding-sheet.csv`  
`not_claimed`: a 48-paper full coding; official jury weights; “this pattern guarantees first prize”.

Short quotes below are for analysis. Do not copy them into a contest paper.

## 1. Genre conventions (high frequency, weak discriminator)

These appear in both first-prize papers and lower-tier / participation papers:

- Cover + unified abstract + 问题重述 + 假设 + 符号 + 逐问建模.
- “针对问题一/二/…” as the abstract backbone.
- A keyword line after the abstract.
- A closing 创新点 list.

Evidence:

- First prize 2023-C `C23102980125` abstract is organized as 针对问题一/二… and ends with 关键词 (extract pp. 2–3).
- Participation 2022-E `E22100160013` also uses 摘要 + 关键词: 微分方程；LSTM；ARIMA (extract p. 2).
- 2024 participation `C24102910010` uses the same 针对问题一…四 skeleton (extract p. 2).

Treat these as **entry tickets**, not ranking features.

## 2. Discriminators (stronger in the first-prize / star layer)

### 2.1 Abstract carries numbers, baselines, and a check

First-prize abstracts do not stop at method names. They report a headline number and what it was compared with.

- 2023-C `C23102980125` p. 2: optimal assignment 120 papers/expert, crossover 1.92; later 重合度 / 乱序度 14 and 83 with a 55.56% improvement claim.
- 2022-C `C22103190082` p. 2: PBS scores 26.91 then 53.04 on a second attachment; a trivial “all lane 4” policy scores 35.1.
- 2023-A `A23100070049` p. 2: names Bianchi as the starting model, states the extra effects (hidden/exposed terminals, natural loss), and promises a discrete-event simulator rather than a verbal “we simulated”.

The 2024 participation control `C24102910010` p. 2 names MSE/R² but does not say how the test split, baseline family, or second dataset was constructed. The 2024 star-champion report (SDU) states LSTM/BiLSTM plus an ideal-point NSGA, i.e. a named baseline family plus an optimization close.

### 2.2 Every claim has a visible test

Recurring test types by archetype:

| Archetype | Test that showed up | Example |
|---|---|---|
| Scheduling | Second instance / greedy baseline / constraint score | 2022-C attachment 2 vs “全走 4 车道” |
| Communications / signal | Simulator or SNR sweep vs classical estimators | 2023-A MATLAB DES; 2022-A DOA methods vs FBSS |
| Mechanism + data | RMSE/MAE/R² vs literature model, then perturbation | 2022-E first-prize: Woodward model RMSE 513.75 vs 221.61; perturbation loss 63.91% vs 10.37% (extract p. 4) |
| Evaluation / scoring | Rank overlap vs a later-stage consensus | 2023-C 重合度/乱序度 against stage-2 一等奖排序 |
| Spatial reconstruction | Pixel metrics + RMSE of geometric fit + uncertainty map | 2025 C champion report (Frangi/Otsu, DBSCAN, JRC, Monte Carlo); 2025 second-prize self-archive also reports mPA/Accuracy/RMSE |

### 2.3 Method choice is a rejection, not a catalogue

First-prize papers name what was tried and dropped.

- 2022-A extract: FBSS dropped because it is sensitive to reflection coefficients.
- 2022-E first-prize: LSTM-FC vs Stacking; GA-MPSO vs the unimproved PSO.
- 2023-A: RTS/CTS on vs off across asymmetric topologies.

### 2.4 Figures have jobs

Observed figure jobs, not decorations:

1. Full-paper technical route (2022-E first-prize 图 1).
2. Per-question flowchart (图 3, 图 8 in the same paper).
3. Prediction vs baseline overlay (图 4–6).
4. Sensitivity / perturbation (图 7, ±20% step 5%).
5. Spatial / radar / residual plots in reconstruction and ML papers.

If a figure cannot be given one of those jobs, first-prize papers usually do not keep it.

### 2.5 Assumptions are local to a question

2023-C splits 全局假设 / 问题一假设 / 问题二假设. 2023-D writes numbered scenario assumptions (GDP doubling, carbon sink 10%, energy mix). This is more useful to a reviewer than a single vague “data are authentic” line.

## 3. Contrast notes (limited, so labelled)

`E22100160013` is a **successful-participation** paper in the same 2022-E cell as first-prize `E22103350038`.

Shared: 问题重述, 假设, LSTM, 关键词.  
Different in the first-prize paper: explicit literature-model baseline table, hold-out 80/20, perturbation robustness table, feature-filter pipeline, and a later optimization with a named improved solver.

This is one pair, not a factorial design. Confidence: `medium`.

The 2024 participation vs 2024 star-champion reports are **not** a matched full-paper pair. Use them only to see that star-level C-problem writeups emphasize multi-factor interaction, a classical equation as baseline (Steinmetz), and a downstream optimizer. Confidence: `low` for paper-quality ranking, `medium` for method-family expectation.

## 4. Integrity and format observations

Published mirrors restore school / team IDs on the cover. Contest uploads must still keep identity off every page after the cover; several cached PDFs would be invalid if submitted as-is after page 1.

Abstracts in the sample stay near two pages and are Chinese-only.

AI disclosure was not visible in the 2022–2023 first-prize extracts (pre-annex or unused). For 2024+ the official rule is disclosure, not prohibition.

## 5. What the skill should copy

1. Restate each numbered question as an input–output contract.
2. Propose 2–3 method families and keep a written rejection.
3. Attach one test to every headline number.
4. Plan figures by job before drawing.
5. Write the abstract last, as a numbered-question story with numbers.
6. Never invent official point weights.
## 6. 48-paper lexical screen (not a discriminator)

On 2026-08-30 the full deep sample was downloaded: 48 first-prize PDFs + 3 controls. Readable extracts: 45 first-prize (`ok`). Garbled: 3 (see `coding-adjudication.md`).

Among the 45 readable first-prize extracts, keyword rates:

| Token family | Share of 45 |
|---|---|
| 关键词 | 88.9% |
| 灵敏 / 鲁棒 / 扰动 / 敏感性 | 42.2% |
| 基线 / 对照 / 现有模型 | 28.9% |
| RMSE / MAE / CSI | 28.9% |
| 技术路线 | 15.6% |

These are **entry-ticket frequencies**. They do not replace the human contrast in §2–3. Heuristic scores can even rank a strong 2025 second-prize self-archive above 2022–2023 first prizes; that is a screen failure, not a jury result.

Adjudication of all `|delta|≥2` cells between human (15) and heuristic: human gold wins. See `coding-adjudication.md`.

## 7. 2024 first-prize layer (local ingest, n=24 files / 12 readable coded)

Source: `D:\BaiduNetdiskDownload\2024年研究生数学建模竞赛优秀论文选`, all 24 filenames match `CPMCM-Awards/2024.csv` 一等奖 after stripping A–F. Census is **24/242**, not a full year dump.

Readable extracts used for this section (2 per letter where CJK count is high). Compact sheet: `coding-sheet-2024.csv`.

- A `A24102940057`, `A24103350007`
- B `B24102860287`, `B24104760033`
- C `C24103860012`, `C24104220149` (`C24102890089` extract is encoding-garbled)
- D `D24103850092`, `D24104250063` (`D24106570027` nearly no CJK)
- E `E24101480006`, `E24102870008`
- F `F24102870082`, `F24910020063` (`F24103360083` weak extract)

### Still true

Abstracts still run 针对问题一/二… with keywords. Discriminators still are **numbers + named baseline + a check**, not the skeleton.

- A `A24102940057` pp. 2–3: rejects offline rainflow for real-time use; reports 0.739 s; shaft torque error 6% vs tower thrust 20%; RL allocation with a safety layer; cumulative damage −10%, load-variance −30%.
- A `A24103350007` p. 2: compares Rainflow-Miner / Rainflow-Goodman-Miner / TW-Rainflow-Goodman-Miner; BiLSTM + sparse NSGA-II; 70/30 split on WF1.
- B `B24102860287` p. 2: 2AP vs 3AP systems; random-forest importance 87.96% / 74.94%; CNN (MCS,NSS) 86.73%; CDF accuracy >95%.
- B `B24104760033` p. 2: logistic vs RF; 2AP MSE 10.412 vs 3AP 43.869; MCS/NSS classifiers named with Accuracy/F1.
- C `C24104220149` p. 2: Steinmetz vs temperature-corrected fit; R 0.041 vs 0.9955; SVM/graph models 100% waveform accuracy on the stated task.
- E `E24101480006` pp. 2–3: YOLO/Deepsort vs later LSTM vs Greenberg; historical-average/SVM/tree named and killed.
- F `F24102870082` p. 2: positions in km and km/s; geometric delay 277.92 s vs refined 473.90 s with named Roemer/Shapiro terms.

### 2024-specific caution

Several 2024 PDFs extract as mojibake. Do not code garbled files. Independent second coder on a fresh 10-paper draw is still open. Confidence for 2024 discriminators: `medium` on the 12 readable papers, `low` for year-wide rates.
