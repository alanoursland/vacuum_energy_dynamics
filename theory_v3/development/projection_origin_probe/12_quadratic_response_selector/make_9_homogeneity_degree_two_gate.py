#!/usr/bin/env python3
"""
Validate degree-two homogeneity for metric response and its failure with quartic corrections.

Output:
    9_homogeneity_degree_two_gate.md
"""
from pathlib import Path
import sympy as sp

x,y,lam,eps = sp.symbols('x y lam eps')
a,c = sp.symbols('a c')
Q2 = a*x**2 + c*y**2
Q4 = Q2 + eps*(x**2 + y**2)**2
res2 = sp.expand(Q2.subs({x:lam*x, y:lam*y}) - lam**2*Q2)
res4 = sp.factor(sp.expand(Q4.subs({x:lam*x, y:lam*y}) - lam**2*Q4))
if sp.simplify(res2) != 0:
    raise AssertionError(f'quadratic homogeneity failed: {res2}')
if sp.simplify(res4) == 0:
    raise AssertionError('quartic homogeneity obstruction unexpectedly vanished')

md = f"""# Quadratic Response Selector 9: Homogeneity Degree-Two Gate

## Purpose

This proof checks exact degree-two homogeneity, a necessary property of a
metric quadratic response.

## Validated Checks

For `Q2 = a x^2 + c y^2`:

```text
Q2(lambda v) - lambda^2 Q2(v) = {sp.sstr(res2)}
```

For `Q4 = Q2 + eps (x^2+y^2)^2`:

```text
Q4(lambda v) - lambda^2 Q4(v) = {sp.sstr(res4)}
```

## Interpretation

Quartic directional response introduces scale-dependent interval behavior. It
cannot be represented by one fixed metric tensor unless the quartic coefficient
vanishes or is routed outside the metric branch.
"""

out = Path(__file__).with_name('9_homogeneity_degree_two_gate.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Homogeneity degree-two gate passed.')
print(f'Wrote {out.resolve()}')
