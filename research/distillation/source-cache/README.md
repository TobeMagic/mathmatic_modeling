# Source cache policy

Do not commit cloned third-party skill repos.

Pin commits in `provenance-cards.md` and `distillation-manifest.json`. If a maintainer clones a repo for re-read, put it here:

```text
research/distillation/source-cache/<owner-repo>@<sha>/
```

This directory is gitignored.
