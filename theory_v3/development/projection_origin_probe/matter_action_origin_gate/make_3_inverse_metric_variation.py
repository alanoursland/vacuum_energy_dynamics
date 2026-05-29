#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("3_inverse_metric_variation.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

a,b,c = sp.symbols('a b c')
h00,h01,h11 = sp.symbols('h00 h01 h11')
g = sp.Matrix([[a,b],[b,c]])
h = sp.Matrix([[h00,h01],[h01,h11]])
ε=sp.symbols('ε')
ginv_eps=(g+ε*h).inv()
deriv=sp.diff(ginv_eps, ε).subs(ε,0)
expected= -g.inv()*h*g.inv()
for i in range(2):
    for j in range(2):
        require_zero(sp.factor(deriv[i,j]-expected[i,j]), f'inverse variation {i}{j}')


content = r"""# Inverse Metric Variation

Metric matter actions often contain `g^{ab}` rather than `g_ab`.  The
script verifies the standard identity

```text
δg^{ab} = -g^{ac} g^{bd} δg_cd.
```

This is the algebraic bridge between covariant and inverse-metric stress
normalizations.  The sign is a convention consequence, not a new physical
source route.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
