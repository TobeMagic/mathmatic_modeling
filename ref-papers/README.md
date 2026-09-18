# Reference papers (NOT our contest manuscript)

Private-team library of **other teams’** Huawei Cup papers.

## Filename (mandatory)

```text
{year}-{tier}-{team_id}-{problem_title}.pdf
```

Examples:

- `2024-first-A24102940057-风电场有功功率优化分配.pdf`
- `2022-first-C22103190082-汽车制造涂装-总装缓冲出车调度优化研究.pdf`

`tier`: `first` | `second` | `third` | `participation` | `report`

Git tracks extracts and `manifest.csv`. Full PDFs in `pdf/` stay **local only** (gitignore) so a public clone does not redistribute contest papers. Rebuild from cache with `python scripts/migrate_ref_papers.py`.

## Agent contract

These files are **REFERENCE_ONLY**. Contest `paper/` is OUR draft.

Cite: `[参考] 2024-first-A24102940057-风电场有功功率优化分配.pdf p.2`  
Do not write 本文 / 我们 about these files. Do not copy sentences into a contest draft.

Copyright remains with authors and the organizer. Do not upload `pdf/` to a public remote.
