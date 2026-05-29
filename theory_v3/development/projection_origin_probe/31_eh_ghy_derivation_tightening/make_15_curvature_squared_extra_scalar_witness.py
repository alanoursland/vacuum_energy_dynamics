#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("15_curvature_squared_extra_scalar_witness.md")
TITLE = 'Curvature-squared branch carries an extra scalar witness'
DESC = 'a toy characteristic factor exposes an additional mode.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

k,m=sp.symbols('k m')
poly=sp.factor(k**2*(k**2+m**2))
md=f"""# {TITLE}

{DESC}

Toy characteristic factor:

```text
{poly}
```

The extra factor beyond `k^2=0` witnesses an additional mode.
"""
write_report(md)
