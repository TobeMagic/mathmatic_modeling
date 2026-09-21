# Per-writer ledgers

Do not share `results/result-ledger.csv`. Each person writes only `results/ledger/<slug>.csv`.

```text
python scripts/writer_id.py --contest . --init
```

S6 reads every `*.csv` here. Optional local concat is gitignored; do not commit a merged table.

Header: `run_id,question,claim,baseline,slice,metric,value,script,seed,status,paper_eligible,writer`
