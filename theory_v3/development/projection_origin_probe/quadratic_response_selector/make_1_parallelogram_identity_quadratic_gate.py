#!/usr/bin/env python3
"""
Validate that a symmetric quadratic response satisfies the parallelogram law.

Output:
    1_parallelogram_identity_quadratic_gate.md
"""
from pathlib import Path
import sympy as sp

x1, x2, y1, y2 = sp.symbols('x1 x2 y1 y2')
a, b, c = sp.symbols('a b c')

def Q(u1, u2):
    return a*u1**2 + 2*b*u1*u2 + c*u2**2

residual = sp.expand(Q(x1+y1, x2+y2) + Q(x1-y1, x2-y2) - 2*Q(x1, x2) - 2*Q(y1, y2))
if sp.simplify(residual) != 0:
    raise AssertionError(f'parallelogram residual not zero: {residual}')

md = f"""# Quadratic Response Selector 1: Parallelogram Identity Quadratic Gate

## Purpose

This proof validates the algebraic gate that any symmetric quadratic response
obeys the parallelogram law.

Let

```text
Q(x1,x2) = a x1^2 + 2 b x1 x2 + c x2^2.
```

The metric branch requires:

```text
Q(x+y) + Q(x-y) - 2 Q(x) - 2 Q(y) = 0.
```

## Validated Check

SymPy expands the residual and verifies it vanishes identically.

```text
residual = {sp.sstr(residual)}
```

## Interpretation

A quadratic directional interval response passes the parallelogram gate. This
is the exact algebraic condition needed before polarization can reconstruct a
fixed symmetric bilinear metric tensor.
"""

out = Path(__file__).with_name('1_parallelogram_identity_quadratic_gate.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Parallelogram identity quadratic gate passed.')
print(f'Wrote {out.resolve()}')
