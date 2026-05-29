#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '15_bulk_boundary_variation_split.md'

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
u,v=sp.Function('u'),sp.Function('v')
S=sp.Function('S')
# Energy: 1/2 u'^2 - S u. Variation integrand u'v' - S v = (u'v)' - (u''+S)v
expr=sp.diff(sp.diff(u(x),x)*v(x),x) - (sp.diff(u(x),x)*sp.diff(v(x),x) - S(x)*v(x)) - (sp.diff(u(x),x,2)+S(x))*v(x)
require_zero(expr,'bulk-boundary variation split')
report=f"""# 15. Bulk-boundary variation split

For

```text
E[u] = ∫ (1/2 u'^2 - S u) dx,
```

the variation integrand satisfies

```text
u'v' - S v = (u'v)' - (u'' + S)v.
```

SymPy check gives residual

```text
{sp.simplify(expr)}
```

Conclusion: the same variational operation produces both the bulk equation and
the boundary ledger. They are split faces of one local action variation.
"""


write_report(report)
