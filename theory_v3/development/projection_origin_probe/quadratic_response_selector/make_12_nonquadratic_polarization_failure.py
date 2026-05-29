#!/usr/bin/env python3
"""
Show that polarization of a nonquadratic response is not a fixed bilinear form.

Output:
    12_nonquadratic_polarization_failure.md
"""
from pathlib import Path
import sympy as sp

u1,u2,v1,v2,eps = sp.symbols('u1 u2 v1 v2 eps')
a,c = sp.symbols('a c')

def Q(x1,x2):
    return a*x1**2 + c*x2**2 + eps*(x1**2 + x2**2)**2

P = sp.expand((Q(u1+v1,u2+v2) - Q(u1,u2) - Q(v1,v2))/2)
quadratic_bilinear = a*u1*v1 + c*u2*v2
extra = sp.factor(sp.expand(P - quadratic_bilinear))
# A bilinear expression has zero second derivative in the same argument variable u1 twice after subtracting no v dependence? Check extra has nonlinear u-dependence.
witness = sp.diff(extra, u1, 2)
if sp.simplify(witness) == 0:
    raise AssertionError('nonquadratic polarization extra unexpectedly bilinear')
if sp.simplify(extra.subs(eps,0)) != 0:
    raise AssertionError('extra term should vanish in quadratic limit')

md = f"""# Quadratic Response Selector 12: Nonquadratic Polarization Failure

## Purpose

This proof shows that applying the polarization formula to a nonquadratic
response does not recover a fixed bilinear tensor.

## Computation

For

```text
Q(v) = a v1^2 + c v2^2 + eps (v1^2+v2^2)^2,
```

polarization gives the ordinary bilinear part plus an extra term:

```text
extra = {sp.sstr(extra)}
```

SymPy verifies that this extra term has nonlinear dependence, for example:

```text
d^2(extra)/du1^2 = {sp.sstr(witness)}
```

## Interpretation

The polarization formula only reconstructs a bilinear metric when the response
is exactly quadratic. In the nonquadratic branch, polarization returns an
object contaminated by the chosen directions.
"""

out = Path(__file__).with_name('12_nonquadratic_polarization_failure.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Nonquadratic polarization failure passed.')
print(f'Wrote {out.resolve()}')
