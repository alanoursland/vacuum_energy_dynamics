#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '1_integration_by_parts_boundary_gate.md'

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
f=sp.Function('f')
g=sp.Function('g')
# product rule: (f g)' = f' g + f g'
identity=sp.diff(f(x)*g(x),x)-sp.diff(f(x),x)*g(x)-f(x)*sp.diff(g(x),x)
require_zero(identity,'product rule decomposition')
report=f"""# 1. Integration by parts boundary gate

This script checks the algebraic origin of a boundary term.

For smooth functions `f` and `g`,

```text
(f g)' = f' g + f g'
```

so

```text
f' g = (f g)' - f g'.
```

After integration over an interval, the total derivative becomes endpoint data.
This is the smallest model of the boundary-reduction idea: the boundary term is
created by rewriting a bulk derivative, not by declaring the boundary to be the
underlying physics.

SymPy check:

```text
(f*g)' - f'*g - f*g' = {sp.simplify(identity)}
```

Conclusion: boundary terms are produced by bulk differential identities.
"""


write_report(report)
