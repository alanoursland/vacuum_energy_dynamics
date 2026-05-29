#!/usr/bin/env python3
"""
Show the Hessian/effective metric depends on direction for quartic response.

Output:
    13_direction_dependent_metric_witness.md
"""
from pathlib import Path
import sympy as sp

x,y,eps = sp.symbols('x y eps')
a,c = sp.symbols('a c')
Q = a*x**2 + c*y**2 + eps*(x**2 + y**2)**2
H = sp.hessian(Q, (x,y))
H_origin = H.subs({x:0,y:0})
H_at_x = H.subs({x:1,y:0})
delta = sp.simplify(H_at_x - H_origin)
if delta == sp.zeros(2):
    raise AssertionError('direction/location dependent Hessian did not change')
if sp.simplify(delta.subs(eps,0)) != sp.zeros(2):
    raise AssertionError('quadratic limit should have no Hessian drift')

md = f"""# Quadratic Response Selector 13: Direction-Dependent Metric Witness

## Purpose

This proof checks whether a nonquadratic response can be represented by one
fixed metric tensor. It cannot: the Hessian depends on the direction/vector at
which it is evaluated.

## Computation

For

```text
Q = a x^2 + c y^2 + eps (x^2+y^2)^2,
```

SymPy computes:

```text
H(0,0) = {sp.sstr(H_origin)}
H(1,0) - H(0,0) = {sp.sstr(delta)}
```

## Interpretation

A fixed pseudo-Riemannian metric assigns one bilinear form at a point. A
quartic directional response produces an effective Hessian that changes with
vector direction/scale, which is Finsler-like rather than metric-like.
"""

out = Path(__file__).with_name('13_direction_dependent_metric_witness.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Direction-dependent metric witness passed.')
print(f'Wrote {out.resolve()}')
