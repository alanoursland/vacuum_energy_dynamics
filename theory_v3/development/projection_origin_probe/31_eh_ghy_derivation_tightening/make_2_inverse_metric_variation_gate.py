#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("2_inverse_metric_variation_gate.md")
TITLE = 'Variation of the inverse metric'
DESC = 'inverse metric variation carries the minus sign needed in metric variations.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

g,h=sp.symbols('g h', nonzero=True)
res=sp.diff(1/g,g)*h + h/g**2
require_zero(res,'inverse variation')
md=f"""# {TITLE}

{DESC}

Validated identity:

```text
delta(g^-1) = - g^-2 delta g
```

Residual: `{sp.simplify(res)}`
"""
write_report(md)
