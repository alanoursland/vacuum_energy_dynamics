#!/usr/bin/env python3
"""
Use parallelogram closure failure as an operational witness of nonmetric response.

Output:
    18_parallelogram_closure_obstruction.md
"""
from pathlib import Path
import sympy as sp

A,B,eps = sp.symbols('A B eps')
# Orthogonal two-step probes with lengths A and B in a Euclidean quadratic plus quartic correction.
def Q(x,y):
    return x**2 + y**2 + eps*(x**2+y**2)**2
closure = sp.factor(sp.expand(Q(A,B) + Q(A,-B) - 2*Q(A,0) - 2*Q(0,B)))
if closure != 4*A**2*B**2*eps:
    raise AssertionError(f'unexpected closure obstruction: {closure}')
if sp.simplify(closure.subs(eps,0)) != 0:
    raise AssertionError('metric limit should close')

md = f"""# Quadratic Response Selector 18: Parallelogram Closure Obstruction

## Purpose

This proof gives a simple operational witness for nonmetric response: a
parallelogram built from two interval probes fails the metric closure identity.

## Computation

For

```text
Q(x,y)=x^2+y^2+eps(x^2+y^2)^2,
```

SymPy evaluates the orthogonal parallelogram residual:

```text
Q(A,B)+Q(A,-B)-2Q(A,0)-2Q(0,B) = {sp.sstr(closure)}
```

## Interpretation

The residual vanishes in the metric branch and is nonzero for quartic response.
This makes parallelogram closure a direct diagnostic for whether directional
interval probes are metric-quadratic.
"""

out = Path(__file__).with_name('18_parallelogram_closure_obstruction.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Parallelogram closure obstruction passed.')
print(f'Wrote {out.resolve()}')
