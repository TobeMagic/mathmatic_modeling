# Optimizer rounds (author eval, not live LLM)

`as_of`: 2026-09-01  
Mode: author-written with_skill vs weaker baseline; regex grader. Dry-run = 100% of live-model cells. **Do not claim measured LLM effectiveness.**

Static snapshot after HITL rewrite: see `audit-skill.json` produced by skill-optimizer `audit-skill.mjs`.

| Round | Target | Files touched | Result |
|---|---|---|---|
| 1 | 全题侦察 + G1 stop | `SKILL.md`, `references/letter-survey.md`, e11/e12 | with_skill PASS on survey/gate; no letter lock |
| 2 | baseline → experiment → incremental paper | `references/code-repro.md`, `experiments-validation.md`, `incremental-paper.md`, e13/e14/e17 | with_skill PASS; refuses skip-baseline and fake RMSE |
| 3 | source weight + training profiles | `references/profiles.md`, e09/e10/e15 | CUMCM quotas labeled profile; KDocs rejected; no M/C/W |

Independent review remaining: a second human coder on 10 papers; a live agent eval if the user authorizes it.
