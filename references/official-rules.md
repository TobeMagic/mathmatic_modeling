# Official rules

Load this file for any Huawei Cup / CPMCM formatting, submission, anonymity, or integrity question.

`as_of`: 2026-09-18 (`python scripts/year_gate.py` matched 2026 invitation, opening notice, and AI annex; Word-template notice still unmatched)

## Rule layers (do not collapse)

1. **Hard official rules** for the current year, from [研创网](https://cpipc.acge.org.cn/cw/hp/4).
2. **Fallback operational package**: 2025 opening notice, used only for items not yet confirmed on the 2026 portal (especially the Word template).
3. **Transcriptions** of those attachments (cmathc). Label them `transcription`.
4. **Training rubric** in `scoring-rubric.md`. Not official.

Before a contest run, re-fetch the official portal. The 2026 opening notice exists; where it conflicts with 2025 details below, the 2026 notice wins. Do not invent a 2026 filename or Word-template rule until that notice is transcribed.

## 2026 dates (official invitation, 2026-04-30)

- Contest: 2026-09-23 08:00 to 2026-09-27 12:00.
- Encrypted problem zip from 2026-09-22 08:00.
- Password from 2026-09-23 08:00.
- Use the official 《竞赛论文标准文档》.
- PDF MD5: 2026-09-26 12:00 to 2026-09-27 12:00.
- PDF upload: 2026-09-27 14:00 to 2026-09-28 24:00.
- Award ceilings: first / second / third at most 1.5% / 13% / 20% of submitted teams.
- Star finalists: at least 12 first-prize teams, normally two per problem, ranked by centralized-review paper score. Host exception may add one team.
- Star champion / runner-up / third are defense results, not a pure paper ranking.

Source: https://cpipc.acge.org.cn/cw/contestNews/detail/4/2c9080189dcfa24e019dddacc24a1314?page=0

## 2025 operational details (fallback)

Use these only for items not yet published for 2026. Tag every borrowed item `year=2025`.

Source: https://cpipc.acge.org.cn/cw/detail/4/2c90801b9914a68201994b1403512e96

- Uncompressed PDF.
- Filename: `{A-F}{team_id}.pdf`, e.g. `A25000010001.pdf`.
- Page 1 is the official cover; logos stay. Abstract starts on page 2.
- After the cover: no school, names, team ID, student ID.
- Unified abstract, Chinese, at most two pages. Must cover 建模思路, 主要方法, 模型, 结果与结论, 创新点.
- Three-stage submit: MD5 → PDF → optional `.rar` attachment ≤ 50 MB, same stem as the PDF, and declared in the paper.
- After MD5 is submitted the PDF must not change.
- Click the final 提交 control or the server never receives the file.
- No problem discussion with advisors or outsiders during the contest.
- Similarity above an unpublished threshold is generally 违规; borrowed code needs a source.
- Do not upload the contest paper to a public plagiarism site during the contest.
- 2025 added: AI only as assistant; disclose per Attachment 4 (see `ai-integrity.md`).

## Format transcription (2025 Attachment 2, via cmathc)

Label: `transcription`. https://www.cmathc.org.cn/mcm/tz/317.html

- Page numbers start at the abstract page, footer center, Arabic, from 1.
- No headers.
- Title: 三号黑体 centered. Level-1: 四号黑体 centered. Body: 小四宋体, single spacing.
- In-text citations `[1][3]`; books need page numbers.
- Reference order follows first appearance.
- Book / journal / URL forms are specified in that notice.
- Abstract generally ≤ 2 pages, no English translation required.
- Reviewers read both abstract and body.

## Community LaTeX

`latexstudio/GMCMthesis` and similar Overleaf classes are unofficial. If used, still match the official Word template of **that year** (cover, logos, abstract page, anonymity). Never tell the user the community class file is the official template.

## Excellent-works pointer

The 研创网 homepage card「优秀作品」is a promotional PPTX on KDocs. It is **not** a paper archive. Locators for real PDFs: `research/huawei-cup/download-excellent-works.md`. In this Skill repo, verified files live under `ref-papers/pdf/` with names `{year}-{tier}-{team_id}-{title}.pdf`. They are reference papers, not our manuscript.

## Agent checklist

1. Confirm year and fetch current official notice.
2. Lock filename, anonymity, abstract length, MD5 freeze.
3. Refuse to put identity on page 2+.
4. Refuse to invent a published official percentage rubric.
5. Run `python scripts/validate_submission.py` on the draft PDF when one exists.
6. After MD5, do not edit models or the PDF.
