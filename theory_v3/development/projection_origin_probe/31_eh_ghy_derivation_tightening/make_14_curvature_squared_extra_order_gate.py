#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("14_curvature_squared_extra_order_gate.md")
TITLE = 'Curvature-squared terms raise derivative order'
DESC = 'generic curvature-squared branches carry higher derivative order.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

EH=2; R2=4
extra=R2-EH
if extra<=0: raise AssertionError('order gate')
md=f"""# {TITLE}

{DESC}

Schematic field-equation derivative orders:

```text
EH: {EH}
curvature-squared: {R2}
extra: {extra}
```

Higher-curvature branches add higher-derivative data unless specially routed.
"""
write_report(md)
