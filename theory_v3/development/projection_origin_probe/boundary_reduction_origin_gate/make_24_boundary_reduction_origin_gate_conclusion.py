#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '24_boundary_reduction_origin_gate_conclusion.md'

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


expected=[f"{i}_" for i in range(1,24)]
existing=[p.name for p in ROOT.glob('*.md')]
missing=[]
for prefix in expected:
    if not any(name.startswith(prefix) for name in existing):
        missing.append(prefix)
if missing:
    raise AssertionError(f"Missing earlier reports: {missing}")
report="""# 24. Boundary reduction origin gate conclusion

This proof group closes the interpretive gate:

```text
r_k is part of standard boundary/admissibility analysis.
```

It appears through:

- moment cancellation;
- endpoint contact;
- integration by parts;
- primitive regularity;
- compactified endpoint analysis;
- flux and boundary-source ledgers.

But this does **not** mean the underlying physics is literally the boundary.
The boundary appears because local/bulk/relational physics is reduced to
surface data, endpoint conditions, asymptotic charges, or finite projection
kernels.

Final status:

```text
boundary = reduction / ledger / admissibility interface;
physics = the local or relational structure that generates the boundary data.
```

The scalar projection ladder should therefore be presented as a boundary-reduced
admissibility object. It is a real and useful shadow of the deeper structure,
but not the complete ontology by itself.
"""


write_report(report)
