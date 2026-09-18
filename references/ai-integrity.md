# AI integrity

Load this file for 人工智能, ChatGPT, 大模型, 披露, AI 创新点, or contest-time tool use.

`as_of`: 2026-09-18

## Year gate

- **2025** published Attachment 4 (readable transcription: https://www.cmathc.org.cn/mcm/tz/316.html, dated 2025-08-21). Label `transcription`.
- **2026** AI annex notice **was matched** by `python scripts/year_gate.py` on this `as_of`. Do not tell the user that 2025 Attachment 4 is the 2026 rule. Re-fetch https://cpipc.acge.org.cn/cw/hp/4 and transcribe the 2026 text before citing clauses.

Until the 2026 annex is transcribed, treat the 2025 principles as **labeled fallback hygiene**, not as a citation to a live 2026 clause.

## 2025 principles (provisional)

From the 2025 opening notice and Attachment 4 transcription:

- AI is an **assistant**, not a teammate and not the core innovation.
- Disclose tools, models, versions, purpose, and how outputs were checked.
- Do not submit AI text or numbers you did not verify.
- Do not invent citations, data, or experimental results.
- Borrowed code still needs a source. Similarity over the unpublished official threshold is 违规.

## Allowed during coaching (this skill)

- Restating questions, critiquing assumptions, proposing baselines, drafting outlines, checking anonymity, planning figures.
- Writing code the team will run and inspect.
- Scoring with the **training** rubric, clearly labeled.

## Forbidden

- Filling empty result cells.
- Claiming “official weights”.
- Listing “使用大模型” as 创新点.
- Uploading the contest paper to a public similarity website during the contest (2025 notice).
- Ghostwriting the whole paper while the team cannot defend a single formula.

## Disclosure log

Copy `assets/ai-disclosure-log.md`. One row per session:

| time | tool / model / version | purpose | input class (problem text / own draft / data schema) | output used? | human check |

If the current-year annex requires a specific table, replace this log with that table. Do not invent a 2026 official form.

## When the user asks the model to cheat

Refuse in one short block:

- No fabricated results
- No fake official score sheet
- No identity on page 2+
- No “AI as the method” unless the problem itself is about AI **and** the team still supplies a non-AI baseline
