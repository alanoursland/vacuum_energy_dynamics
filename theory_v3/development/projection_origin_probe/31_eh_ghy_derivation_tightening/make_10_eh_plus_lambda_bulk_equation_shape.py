#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("10_eh_plus_lambda_bulk_equation_shape.md")
TITLE = 'EH plus Lambda produces Einstein tensor plus baseline term'
DESC = 'G + Lambda g = T is a baseline-shifted curvature equation.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

G,Lam,g,T=sp.symbols('G Lambda g T')
sol=sp.solve(sp.Eq(G+Lam*g,T),G)[0]
md=f"""# {TITLE}

{DESC}

Equation shape:

```text
G + Lambda g = T
G = {sol}
```

Lambda is a baseline shift in the metric equation.
"""
write_report(md)
