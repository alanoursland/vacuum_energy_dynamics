#!/usr/bin/env python3
"""
Construct a quartic/Finsler-like obstruction to the parallelogram gate.

Output:
    11_quartic_finsler_obstruction_witness.md
"""
from pathlib import Path
import sympy as sp

x1,x2,y1,y2,eps = sp.symbols('x1 x2 y1 y2 eps')
a,c = sp.symbols('a c')

def Q(u1,u2):
    return a*u1**2 + c*u2**2 + eps*(u1**2 + u2**2)**2

residual = sp.factor(sp.expand(Q(x1+y1,x2+y2) + Q(x1-y1,x2-y2) - 2*Q(x1,x2) - 2*Q(y1,y2)))
expected = sp.factor(4*eps*(x1**4 + 2*x1**2*x2**2 + 6*x1**2*y1**2 + 2*x1**2*y2**2 + 8*x1*x2*y1*y2 + x2**4 + 2*x2**2*y1**2 + 6*x2**2*y2**2 + y1**4 + 2*y1**2*y2**2 + y2**4) - 0)
# Instead of asserting a hand-expanded expected expression, test a simple witness.
witness = sp.simplify(residual.subs({x1:1,x2:0,y1:1,y2:0}))
if witness != 12*eps:
    raise AssertionError(f'unexpected parallelogram witness: {witness}')
if sp.simplify(residual.subs(eps,0)) != 0:
    raise AssertionError('quadratic limit should pass parallelogram gate')

md = f"""# Quadratic Response Selector 11: Quartic/Finsler Obstruction Witness

## Purpose

This proof constructs an explicit nonquadratic directional response and shows
that it fails the parallelogram gate.

Take

```text
Q(v) = a v1^2 + c v2^2 + eps (v1^2+v2^2)^2.
```

## Validated Checks

- with `eps=0`, the parallelogram residual vanishes: passed
- at `x=(1,0), y=(1,0)`, the residual is:

```text
{sp.sstr(witness)}
```

## Interpretation

For nonzero `eps`, the response is not metric-quadratic. It may be a valid
higher directional response branch, but it cannot be silently treated as a
single pseudo-Riemannian metric tensor.
"""

out = Path(__file__).with_name('11_quartic_finsler_obstruction_witness.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Quartic Finsler obstruction witness passed.')
print(f'Wrote {out.resolve()}')
