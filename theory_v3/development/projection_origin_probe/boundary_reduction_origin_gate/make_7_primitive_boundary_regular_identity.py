#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '7_primitive_boundary_regular_identity.md'

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


x,k=sp.symbols('x k', positive=True, integer=True)
G=x**(2*k-1)*(1-x**2)**2
rk=(2*k-1)/(2*k+3)
psi=x**(2*k)-rk*x**(2*k-2)
identity=sp.simplify(sp.diff(G,x)+(2*k+3)*(1-x**2)*psi)
require_zero(identity,'primitive derivative identity')
G0=sp.simplify(G.subs(x,1))
require_zero(G0,'primitive vanishes at boundary x=1')
report=f"""# 7. Primitive boundary-regular identity

Define

```text
G_k(x) = x^(2k-1)(1-x^2)^2.
```

With

```text
psi_k(x) = x^(2k) - ((2k-1)/(2k+3)) x^(2k-2),
```

SymPy verifies

```text
G_k'(x) = -(2k+3)(1-x^2) psi_k(x).
```

Boundary contact check:

```text
G_k(1) = {G0}
```

Conclusion: the same ratio appears from a boundary-regular primitive identity.
This is integration-by-parts/admissibility structure, not a standalone physical
source law.
"""


write_report(report)
