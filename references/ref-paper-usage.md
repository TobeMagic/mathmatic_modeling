# Reference papers (Skill repo only)

Load when the user asks how a first-prize paper is written, or when surveying neighbours.

## Location

All reference PDFs live in **this Skill repo**:

```text
ref-papers/pdf/{year}-{tier}-{team_id}-{title}.pdf
```

`tier` is `first` | `second` | `third` | `participation` | `report`.  
`team_id` includes the letter, e.g. `A24102940057`.

These files are **other teams’ papers**. They are never the contest-repo `paper/` manuscript.

## Agent rules

1. When opening a path under `ref-papers/`, prefix every claim with `[参考] {filename} p.N`.
2. Do not write 本文, 我们, 本队, 摘要已完成 about a `ref-papers/` file.
3. Do not copy sentences into `paper/sections/`.
4. Do not save a reference PDF into the contest repo.
5. If a filename does not match `{year}-{tier}-{team_id}-`, treat it as unlabeled and do not use it as gold.

## How to cite in planning

In contest `plans/CONTEXT.md` list the filenames actually used, e.g.:

```text
[参考] 2024-first-A24102940057-风电场有功功率优化分配.pdf p.2
```
