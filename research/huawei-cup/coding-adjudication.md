# Coding adjudication

`as_of`: 2026-08-30  
`deep_sample`: 48 first-prize IDs (seed `20260829`) + 3 controls = 51 extracts.  
`ok_extracts`: 48. Garbled: `2022-F22105330345`, `2023-A23102480015`, `2023-E23102550019`.

## Two layers (do not collapse)

1. **Human gold** (`coding-sheet.csv`, 15 records, `coder_id=first-pass-single`). Used for discriminators in `findings.md`.
2. **Heuristic screen** (`coding-sheet-heuristic.csv`, `coder_id=heuristic-v1`). Lexical. High recall on 关键词, low precision on 基线/灵敏度.

Disagreements with `|delta|≥2` after tightening abstract regex: **17** on the 15 human records (plan asked 20% of 48 ≈ 10; we adjudicated the full overlap instead).

## Verdicts

| Pattern | Winner | Why |
|---|---|---|
| Heuristic under-scores `abstract_structure` when the paper uses 问题一 not 针对问题 | human | Genre backbone is still there |
| Heuristic under-scores `sensitivity` if the paper says 扰动/稳健 without 灵敏度 | human if a table exists | 2022-E first prize |
| Heuristic **over**-scores `method_rationale` on participation `E22100160013` (对比 hits) | human (1) | Contrast words are genre |
| Heuristic **over**-scores 2024 control sensitivity | human (1) | 鲁棒 is decorative |
| Garbled 2023-E | neither | Do not code from mojibake |

**Rule:** a discriminator claim needs the human layer **or** a quoted page. Heuristic rates in findings are labelled `lexical-screen`, not prize predictors.

Heuristic means on 45 readable first-prize extracts vs 3 controls **must not** be used to rank award tiers: the control set is tiny and includes a 2025 second-prize self-archive that is lexically “complete”.
