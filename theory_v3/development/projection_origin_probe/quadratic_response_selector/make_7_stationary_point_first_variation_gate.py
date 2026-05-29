#!/usr/bin/env python3
"""
Validate that the first variation vanishes only under stationarity assumptions.

Output:
    7_stationary_point_first_variation_gate.md
"""
from pathlib import Path
import sympy as sp

x,y = sp.symbols('x y')
px, py, h11, h12, h22 = sp.symbols('px py h11 h12 h22')
F = px*x + py*y + sp.Rational(1,2)*(h11*x**2 + 2*h12*x*y + h22*y**2)
grad0 = sp.Matrix([sp.diff(F,x), sp.diff(F,y)]).subs({x:0,y:0})
stationary_grad = grad0.subs({px:0, py:0})
if grad0 != sp.Matrix([px,py]):
    raise AssertionError(f'unexpected gradient: {grad0}')
if stationary_grad != sp.Matrix([0,0]):
    raise AssertionError(f'stationary gradient did not vanish: {stationary_grad}')

md = f"""# Quadratic Response Selector 7: Stationary Point First Variation Gate

## Purpose

This proof records that a Hessian metric-like sector is clean only after the
first variation has been routed or set to zero by stationarity.

## Validated Computation

For a local expansion with linear part:

```text
F = px x + py y + quadratic terms,
```

SymPy computes:

```text
grad F at 0 = {sp.sstr(grad0)}
```

Under the stationarity condition `px=py=0`, this becomes:

```text
{sp.sstr(stationary_grad)}
```

## Interpretation

The Hessian branch is not automatically the whole local response. A nonzero
first variation is a separate force/source/drift channel and must be routed
rather than hidden inside metric data.
"""

out = Path(__file__).with_name('7_stationary_point_first_variation_gate.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Stationary first variation gate passed.')
print(f'Wrote {out.resolve()}')
