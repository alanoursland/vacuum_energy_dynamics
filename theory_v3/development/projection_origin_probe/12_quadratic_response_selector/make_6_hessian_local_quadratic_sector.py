#!/usr/bin/env python3
"""
Validate that a smooth local response has a Hessian-defined quadratic sector.

Output:
    6_hessian_local_quadratic_sector.md
"""
from pathlib import Path
import sympy as sp

x,y = sp.symbols('x y')
f0, px, py, h11, h12, h22, t = sp.symbols('f0 px py h11 h12 h22 t')
F = f0 + px*x + py*y + sp.Rational(1,2)*(h11*x**2 + 2*h12*x*y + h22*y**2) + t*x**3
H = sp.hessian(F, (x,y))
H_at_0 = H.subs({x:0,y:0})
expected = sp.Matrix([[h11,h12],[h12,h22]])
if sp.simplify(H_at_0 - expected) != sp.zeros(2):
    raise AssertionError(f'Hessian mismatch: {H_at_0}')
quad = sp.Rational(1,2)*sp.Matrix([x,y]).T*expected*sp.Matrix([x,y])
quad = sp.expand(quad[0])
if sp.simplify(quad - sp.Rational(1,2)*(h11*x**2 + 2*h12*x*y + h22*y**2)) != 0:
    raise AssertionError('quadratic sector mismatch')

md = f"""# Quadratic Response Selector 6: Hessian Local Quadratic Sector

## Purpose

This proof separates exact metric response from local second-variation data.
A smooth response has a Hessian-defined quadratic sector at a reference point,
even if the full response contains higher-order terms.

## Validated Computation

For

```text
F = f0 + px x + py y + 1/2(h11 x^2 + 2 h12 xy + h22 y^2) + t x^3,
```

SymPy computes the Hessian at the origin:

```text
H(0) = {sp.sstr(H_at_0)}
```

and verifies that it equals the symmetric matrix:

```text
{sp.sstr(expected)}
```

## Interpretation

A Hessian supplies local quadratic data. It does not by itself prove that the
entire interval-response functional is exactly quadratic.
"""

out = Path(__file__).with_name('6_hessian_local_quadratic_sector.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Hessian local quadratic sector passed.')
print(f'Wrote {out.resolve()}')
