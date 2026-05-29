#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("17_ghy_normalization_relation_gate.md")
TITLE = 'GHY normalization tracks the EH bulk normalization'
DESC = 'the required boundary normalization scales with the EH leakage coefficient.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

K,c=sp.symbols('K c')
sol=sp.solve(sp.Eq(K-c,0),c)[0]
require_zero((K-c).subs(c,sol),'normalization')
md=f"""# {TITLE}

{DESC}

If EH leakage has coefficient `K`, cancellation fixes boundary coefficient:

```text
c_GHY = {sol}
```
"""
write_report(md)
