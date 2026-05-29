#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('18_boundary_symplectic_needed_for_radiative_weyl.md')
def require_zero(expr, name='expr'):
    if sp.simplify(expr) != 0:
        raise AssertionError(f"{name} not zero: {sp.simplify(expr)}")
def require(cond, name='condition'):
    if not bool(cond):
        raise AssertionError(f"failed: {name}")
def write_md(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text.strip() + "\n", encoding='utf-8')
    tmp.replace(OUT)

Omega = sp.Matrix([[0,1],[-1,0]])
D=sp.det(Omega)
require_zero(D-1,'det')
md = f"""# 18. Boundary symplectic needed for radiative Weyl

Radiative boundary data requires canonical phase-space pairing, modeled by

```text
Omega = [[0,1],[-1,0]], det(Omega) = {D}.
```

A scalar charge ledger supplies one configuration channel, not a nondegenerate radiative phase-space pair.

So Weyl/TT radiation requires boundary symplectic data or equivalent tensor transport data.
"""

write_md(md)
