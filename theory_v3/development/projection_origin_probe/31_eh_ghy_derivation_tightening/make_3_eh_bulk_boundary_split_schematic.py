#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("3_eh_bulk_boundary_split_schematic.md")
TITLE = 'EH variation has bulk plus boundary derivative terms'
DESC = 'a second-derivative variation decomposes into Euler bulk plus total derivative leakage.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

x=sp.symbols('x')
eta=sp.Function('eta')(x); A=sp.Function('A')(x)
res=A*sp.diff(eta,x,2) - (sp.diff(A*sp.diff(eta,x)-sp.diff(A,x)*eta,x)+sp.diff(A,x,2)*eta)
require_zero(res,'IBP split')
md=f"""# {TITLE}

{DESC}

Toy identity:

```text
A eta'' = d(A eta' - A' eta)/dx + A'' eta
```

Residual: `{sp.simplify(res)}`

This models the EH variation split into bulk plus boundary derivative terms.
"""
write_report(md)
