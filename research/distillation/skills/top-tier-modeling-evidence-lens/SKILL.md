---
name: top-tier-modeling-evidence-lens
description: >-
  Apply a top-tier contest-paper evidence lens: tests, baselines, rejections,
  and abstract numbers. Use when scoring or planning a Huawei Cup / CPMCM
  section and the user asks what a first-prize paper would show. Do not use
  for SCI journal voice, CUMCM undergraduate quotas, or to invent official
  jury weights.
category: research
subcategory: knowledge-distillation
tags:
  - huawei-cup
  - evidence
  - contest-paper
---

# Top-tier modeling evidence lens

## Decision Outcome

Decide whether a draft claim is first-prize texture (baseline + metric + falsifier + page) or only genre padding.

## Inputs And Preconditions

1. Required input: a problem letter, a section draft, or a planned experiment row.
2. Assumption to confirm: Huawei Cup first-prize team ids outrank CUMCM/MCM Outstanding papers for abstract contents.
3. Stop condition: garbled extract, unverified second prize, or missing page.

## Source-Grounded Model

First-prize Huawei papers pay with a named baseline, a killed alternative, and a number in the abstract (`E-HC-findings`; 2024-A `A24102940057` p.2 rainflow rejected + 0.739 s). Public contest skills pay with stage machines and stop markers (`E-SK-handsomeZR-stage01`). Combine them as evidence-before-prose, not as foreign page quotas.

## Worked Application

2022-C first prize reports PBS vs all-lane-4 with named scores (`E-HC-2022-C22103190082`). A method-only abstract would fail this lens: it has no comparator and no falsifier.

## Execution

1. Classify the ask as factual / framework / mixed.
   - Completion evidence: one label.
   - Branch: if factual about official notices, route to `huawei-cup-modeling` year gate; do not use this lens.
2. Prefer Huawei Cup first-prize team ids.
   - Completion evidence: team_id + page.
   - Branch: if only CUMCM/MCM exists, label `cross-contest` and downgrade confidence.
3. Ask: baseline, metric, slice, falsifier?
   - Completion evidence: four yes/no.
   - Branch: if any no, output `status=not-run` holes instead of adjectives.
4. Emit missing tests, not a rewritten paper.
   - Completion evidence: a short list.
   - Branch: never paste cached paper sentences.

## Failure Handling

| Trigger | First response | Fallback |
|---|---|---|
| Extract garbled | Do not code | `confidence=low`; skip the file |
| User wants 官方 85 分 | Refuse | Point to training_score isolation |
| User wants SCI tone | Non-trigger | `academic-paper-workflow` |
| Second-prize labeled 顶级 | Downgrade to control | Keep first-prize gold |

## Boundaries

- Non-triggers: SCI discussion tone; undergraduate CUMCM format; inventing jury weights.
- Known failure modes: treating 数模之星 defense rank as paper rank.
- Source blind spots: 2024 census is 24/242; some PDFs do not extract Chinese.
- Neighbor: `huawei-cup-modeling` owns stage routing; this lens only scores evidence texture.

## Relationships

- requires: `research/huawei-cup/findings.md` when present
- contrasts-with: `academic-paper-workflow`
- combines-with: `huawei-cup-modeling` S1 and S7
- escalates-to: `huawei-cup-modeling` when a contest stage must run

## Output Contract

A short list of missing tests with team_id/page pointers, or explicit `not-run` holes. Not a rewritten paper.
