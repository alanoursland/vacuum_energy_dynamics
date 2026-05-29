#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("5_ghy_cancellation_toy_model.md")
TITLE = 'GHY-like boundary completion cancels derivative leakage'
DESC = 'a boundary counterterm coefficient is fixed by cancellation.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

b,c=sp.symbols('b c')
res=b-c*b
sol=sp.solve(sp.Eq(res,0),c)[0]
require_zero(res.subs(c,sol),'counterterm coefficient')
md=f"""# {TITLE}

{DESC}

Leakage plus counterterm:

```text
B_total = b - c b
```

Cancellation fixes `c = {sol}`.

The coefficient is not free once the leakage normalization is fixed.
"""
write_report(md)
