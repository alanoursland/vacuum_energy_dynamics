#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("9_cosmological_term_no_derivative_boundary.md")
TITLE = 'Cosmological term has no derivative boundary leakage'
DESC = 'Lambda is a volume baseline term with algebraic metric variation.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

g,Lam,h=sp.symbols('g Lambda h', positive=True)
var=sp.diff(Lam*sp.sqrt(g),g)*h
md=f"""# {TITLE}

{DESC}

One-component variation:

```text
delta(Lambda sqrt(g)) = {sp.simplify(var)}
```

No derivative of the metric variation appears, so Lambda introduces no GHY-like boundary leakage.
"""
write_report(md)
