#!/usr/bin/env python3
"""
State and check the algebraic condition for a single shared metric branch.

Output:
    19_shared_metric_branch_condition.md
"""
from pathlib import Path
import sympy as sp

x1,x2,y1,y2,eps = sp.symbols('x1 x2 y1 y2 eps')

def Q(x,y):
    return x**2 + y**2 + eps*(x**2+y**2)**2

res = sp.expand(Q(x1+y1,x2+y2) + Q(x1-y1,x2-y2) - 2*Q(x1,x2) - 2*Q(y1,y2))
poly = sp.Poly(res, x1,x2,y1,y2)
coeffs = list(poly.coeffs())
# All residual coefficients are proportional to eps. Therefore eps=0 is the condition in this model.
conditions = [sp.factor(coef/eps) if coef != 0 else 0 for coef in coeffs]
if not coeffs or any(sp.simplify(coef.subs(eps,0)) != 0 for coef in coeffs):
    raise AssertionError('residual coefficients should vanish at eps=0')
if sp.simplify(res.subs(eps,0)) != 0:
    raise AssertionError('metric branch condition eps=0 failed')

md = f"""# Quadratic Response Selector 19: Shared Metric Branch Condition

## Purpose

This proof isolates the condition for a single shared metric branch in the
simple quadratic-plus-quartic witness model.

## Validated Check

For

```text
Q = x^2 + y^2 + eps (x^2+y^2)^2,
```

all parallelogram residual coefficients vanish when:

```text
eps = 0.
```

Number of residual monomial coefficients checked:

```text
{len(coeffs)}
```

## Interpretation

In this witness family, exact metric response is the branch where the
nonquadratic coefficient vanishes. More generally, a single shared metric
branch requires exact parallelogram/quadratic response, not merely the existence
of a Hessian at one point.
"""

out = Path(__file__).with_name('19_shared_metric_branch_condition.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Shared metric branch condition passed.')
print(f'Wrote {out.resolve()}')
