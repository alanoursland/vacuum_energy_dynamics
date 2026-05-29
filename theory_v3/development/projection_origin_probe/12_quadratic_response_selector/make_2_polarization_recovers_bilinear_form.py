#!/usr/bin/env python3
"""
Validate that polarization recovers the symmetric bilinear form for a quadratic response.

Output:
    2_polarization_recovers_bilinear_form.md
"""
from pathlib import Path
import sympy as sp

u1,u2,v1,v2 = sp.symbols('u1 u2 v1 v2')
a,b,c = sp.symbols('a b c')

def Q(x1,x2):
    return a*x1**2 + 2*b*x1*x2 + c*x2**2

B = sp.expand((Q(u1+v1,u2+v2) - Q(u1,u2) - Q(v1,v2))/2)
expected = a*u1*v1 + b*(u1*v2 + u2*v1) + c*u2*v2
residual = sp.simplify(B - expected)
if residual != 0:
    raise AssertionError(f'polarization failed: {residual}')

md = f"""# Quadratic Response Selector 2: Polarization Recovers Bilinear Form

## Purpose

This proof validates that the polarization formula reconstructs a fixed
symmetric bilinear form from an exact quadratic response.

## Computation

For

```text
Q(x1,x2) = a x1^2 + 2 b x1 x2 + c x2^2,
```

define

```text
B(u,v) = [Q(u+v) - Q(u) - Q(v)] / 2.
```

SymPy obtains:

```text
B(u,v) = {sp.sstr(B)}
```

and verifies that this equals:

```text
{sp.sstr(expected)}
```

## Interpretation

If the local response is exactly quadratic, the metric tensor is not an extra
object. It is reconstructed from directional interval probes by polarization.
"""

out = Path(__file__).with_name('2_polarization_recovers_bilinear_form.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Polarization recovery passed.')
print(f'Wrote {out.resolve()}')
