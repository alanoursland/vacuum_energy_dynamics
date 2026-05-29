#!/usr/bin/env python3
"""
Validate that higher-order terms survive beyond the Hessian sector.

Output:
    8_higher_order_remainder_witness.md
"""
from pathlib import Path
import sympy as sp

x,y = sp.symbols('x y')
h11,h12,h22,c3,q4 = sp.symbols('h11 h12 h22 c3 q4')
F = sp.Rational(1,2)*(h11*x**2 + 2*h12*x*y + h22*y**2) + c3*x**2*y + q4*(x**2 + y**2)**2
H0 = sp.hessian(F, (x,y)).subs({x:0,y:0})
quad = sp.Rational(1,2)*sp.Matrix([x,y]).T*H0*sp.Matrix([x,y])
quad = sp.expand(quad[0])
remainder = sp.expand(F - quad)
expected = sp.expand(c3*x**2*y + q4*(x**2 + y**2)**2)
if sp.simplify(remainder - expected) != 0:
    raise AssertionError(f'remainder mismatch: {remainder}')
if remainder == 0:
    raise AssertionError('higher-order remainder unexpectedly vanished')

md = f"""# Quadratic Response Selector 8: Higher-Order Remainder Witness

## Purpose

This proof exhibits the difference between the Hessian metric sector and the
full local response.

## Validated Computation

For

```text
F = quadratic + c3 x^2 y + q4 (x^2+y^2)^2,
```

SymPy subtracts the Hessian quadratic sector and obtains the remainder:

```text
R = {sp.sstr(remainder)}
```

## Interpretation

A local Hessian does not erase higher-order directional response. Those terms
must be suppressed, shown irrelevant, or routed as a nonmetric branch.
"""

out = Path(__file__).with_name('8_higher_order_remainder_witness.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Higher-order remainder witness passed.')
print(f'Wrote {out.resolve()}')
