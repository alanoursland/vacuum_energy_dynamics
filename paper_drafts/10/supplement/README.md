# Supplementary symbolic verification

These scripts reproduce the algebraic checks reported in Sec. 8 without
depending on the research repository or its internal archive tooling.

Requirements:

- Python 3.11 or newer
- SymPy 1.12 or newer

From this directory, run:

```text
python -m pip install -r requirements.txt
python verify_family.py
python verify_pg.py
```

The expected summaries are `21/21 checks passed` and
`11/11 checks passed`. Both scripts recompute their results on every run
and write no files.
