# Coverage gaps

`as_of`: 2026-09-01

This file records what this package has **not** ingested. Missing sources are not silently treated as covered.

## Blocked or gated

| Item | Why blocked | Effect |
|---|---|---|
| Official 优秀作品 KDocs | User-confirmed promotional PPTX, not papers | Do not ingest. Use GitHub/netdisk locators in `download-excellent-works.md` |
| Official 2025 Attachment 2/3/4 binaries | `sysFile/downFile.do` returns binary and is not reliably text-renderable here | Readable transcriptions from cmathc used with explicit `transcription` label |
| 系列微课 videos | WeChat-hosted | Not transcribed; skill points to official landing page only |
| 2026 opening notice, template, AI annex | Not published as of 2026-08-30 (portal re-fetch; `year_gate.py` sees invitation only) | Skill must re-check official portal before any 2026 contest run |
| 2025 full-paper census | No stable public dump; author-posted repos only | Recency layer remains reports + author controls |
| 2022–2024 123pan pack | Link invalid 2026-08-31 | Dropped from recommended locators |

## Incomplete verification

| Item | Status |
|---|---|
| Exact official award-list PDFs for 2022-2025 | Secondary transcription (`CPMCM-Awards`) used; team IDs matched, but original attachments were not re-downloaded |
| Paper titles inside 2022-2023 PDFs | Manifest stores official **problem** titles; individual paper titles filled only after local ingest |
| 48-paper deep sample PDFs (2022–2023) | All 48 IDs (seed `20260829`) plus 3 controls downloaded 2026-08-30. **45** first-prize extracts are readable; 3 garbled (`2022-F22105330345`, `2023-A23102480015`, `2023-E23102550019`). Original PDFs remain gitignored. |
| 2024 first-prize local ingest | **24/24** files team-id-matched 一等奖; census **24/242**. Weak/garbled extracts: `2024-C24102890089` (cjk=0), `2024-D24106570027`, `2024-F24103360083`, `2024-F24104860143`. Human coding uses 12 readable papers (2 per letter). |
| Lower-tier matched controls for every year-letter cell | Only a few public controls located; do not overclaim contrast coverage |
| Double coding of 20% of the deep sample | Human sheet covers 15 records (2022–2023). Independent second human coder on a fresh 10-paper draw is still open. 2024 coding is first-pass-single. |

## Deliberately excluded

- Official 优秀作品 KDocs promotional PPTX
- CSDN paid dumps and Baidu-disk “2004-2023 优秀论文合集”
- Undergraduate CUMCM 评阅要点 as if they were Huawei Cup national score sheets
- CUMCM 2010–2025 优秀论文网盘 (wrong contest)
- Blog “A-F 评分细则” pages
- Any claim of a universal official percentage rubric
- Other modeling skills’ “国一 ≥ 85” or “至少 8 张图” as Huawei Cup rules
- Second/third prize papers as “顶级” distillation gold
