#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '16_asymptotic_boundary_limit_gate.md'

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


r,Q=sp.symbols('r Q', positive=True)
phi=Q/r
lim_phi=sp.limit(phi,r,sp.oo)
lim_rphi=sp.limit(r*phi,r,sp.oo)
require_equal(lim_phi,0,'potential vanishes at infinity')
require_equal(lim_rphi,Q,'asymptotic coefficient')
report=f"""# 16. Asymptotic boundary is a limit gate

For a Coulomb/Newtonian asymptotic potential

```text
phi(r)=Q/r,
```

the boundary at infinity records the coefficient through a limit:

```text
lim phi(r) = {lim_phi}
lim r phi(r) = {lim_rphi}
```

Conclusion: asymptotic boundary data are limiting coefficients of bulk fields,
not a literal material wall at infinity.
"""


write_report(report)
