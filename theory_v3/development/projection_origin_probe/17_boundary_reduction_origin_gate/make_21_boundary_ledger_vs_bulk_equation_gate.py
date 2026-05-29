#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '21_boundary_ledger_vs_bulk_equation_gate.md'

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


r,Q,Omega=sp.symbols('r Q Omega', positive=True)
F=Q/(Omega*r**2)
# Divergence radial in 3D: (1/r^2) d(r^2 F)/dr =0 source-free.
div=sp.simplify((1/r**2)*sp.diff(r**2*F,r))
require_zero(div,'source-free radial divergence')
flux=sp.simplify(Omega*r**2*F)
report=f"""# 21. Boundary ledger versus bulk equation gate

For a source-free exterior radial field

```text
F(r)=Q/(Omega r^2),
```

the bulk divergence is

```text
(1/r^2) d(r^2 F)/dr = {div}.
```

The boundary ledger is

```text
Omega r^2 F = {flux}.
```

Conclusion: the bulk equation says the exterior is source-free; the boundary
ledger records the integration constant. These are different roles.
"""


write_report(report)
