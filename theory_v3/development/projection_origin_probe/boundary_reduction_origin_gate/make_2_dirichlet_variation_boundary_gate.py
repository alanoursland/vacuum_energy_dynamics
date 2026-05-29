#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '2_dirichlet_variation_boundary_gate.md'

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


x=sp.symbols('x')
u=sp.Function('u')
v=sp.Function('v')
# variation of 1/2 int u'^2: integrand u'v'; integrate by parts u'v'=(u'v)'-u''v
expr=sp.diff(sp.diff(u(x),x)*v(x),x)-sp.diff(u(x),x)*sp.diff(v(x),x)-sp.diff(u(x),x,2)*v(x)
# rearranged: u'v' = (u'v)' - u''v
require_zero(expr,'variation integration by parts identity')
report=f"""# 2. Dirichlet variation boundary gate

This script checks the standard variation identity behind a Dirichlet energy.

For

```text
E[u] = 1/2 ∫ (u')^2 dx,
```

the first variation contains `u' v'`. Integration by parts gives

```text
u' v' = (u' v)' - u'' v.
```

The first term becomes boundary variation data; the second term gives the bulk
Euler-Lagrange equation.

SymPy check:

```text
(u'v)' - u'v' - u''v = {sp.simplify(expr)}
```

Conclusion: the boundary term is the variational ledger of a bulk energy, not a
separate ontology.
"""


write_report(report)
