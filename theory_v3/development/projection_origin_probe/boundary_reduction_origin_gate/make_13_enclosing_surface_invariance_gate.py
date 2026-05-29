#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '13_enclosing_surface_invariance_gate.md'

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


r1,r2,Q,Omega=sp.symbols('r1 r2 Q Omega', positive=True)
F=lambda r: Q/(Omega*r**2)
flux1=Omega*r1**2*F(r1)
flux2=Omega*r2**2*F(r2)
require_equal(flux1,flux2,'same flux across source-free shell')
report=f"""# 13. Enclosing-surface invariance gate

For a source-free shell surrounding charge `Q`, the flux through any enclosing
sphere is

```text
Omega r^2 F(r) = Q.
```

SymPy verifies

```text
flux(r1) - flux(r2) = {sp.simplify(flux1-flux2)}.
```

Conclusion: the boundary surface is movable when no source crosses it. This is
strong evidence that the boundary is an accounting surface, not the substance
being accounted for.
"""


write_report(report)
