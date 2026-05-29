#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '23_boundary_reduction_status.md'

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} expected 0, got {simplified}")
    return simplified

def require_equal(a, b, label):
    return require_zero(sp.simplify(a-b), label)

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text)
    tmp.replace(OUT)


# Check expected files 1..22 exist after running earlier scripts if present; do not fail if not? For run_all order yes. We'll check.
expected=[f"{i}_" for i in range(1,23)]
existing=[p.name for p in ROOT.glob('*.md')]
missing=[]
for prefix in expected:
    if not any(name.startswith(prefix) for name in existing):
        missing.append(prefix)
if missing:
    raise AssertionError(f"Missing earlier reports: {missing}")
report="""# 23. Boundary reduction status

The preceding reports establish the role of boundary analysis in this chain.

Verified pieces:

- integration by parts creates endpoint terms;
- energy variation splits into bulk equations plus boundary ledgers;
- conserved flux is measured on movable enclosing surfaces;
- compactified endpoints can represent infinity or support boundaries;
- endpoint contact controls flux safety;
- `r_k` is a moment-kernel / primitive boundary-regular coefficient;
- the `R` ladder is a standard endpoint-contact family;
- scalar projection rows are finite representatives of boundary/admissibility test functions.

Status claim:

```text
boundary analysis exposes and constrains the reduced field/source ledger;
it is not, by itself, the underlying physical ontology.
```

The underlying dynamics remain in the bulk/local/relational interval structure
that generates the reduced boundary data.
"""


write_report(report)
