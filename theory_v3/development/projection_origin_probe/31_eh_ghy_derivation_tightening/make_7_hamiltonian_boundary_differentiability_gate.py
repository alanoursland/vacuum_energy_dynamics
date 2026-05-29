#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("7_hamiltonian_boundary_differentiability_gate.md")
TITLE = 'Hamiltonian differentiability requires boundary generator cancellation'
DESC = 'Hamiltonian variation has the same bulk-plus-boundary cancellation shape.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

B,c=sp.symbols('B c')
res=B-c*B
sol=sp.solve(sp.Eq(res,0),c)[0]
require_zero(res.subs(c,sol),'Hamiltonian boundary')
md=f"""# {TITLE}

{DESC}

Model Hamiltonian variation:

```text
delta H = bulk + B - cB
```

Differentiability fixes `c = {sol}`.
"""
write_report(md)
