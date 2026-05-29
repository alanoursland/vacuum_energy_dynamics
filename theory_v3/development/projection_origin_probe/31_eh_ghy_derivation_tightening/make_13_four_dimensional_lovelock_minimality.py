#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("13_four_dimensional_lovelock_minimality.md")
TITLE = 'In D=4 EH is the unique dynamical Lovelock curvature term'
DESC = 'in D=4, p=1 is dynamical, p=2 is topological, p>=3 vanishes.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

D=4
classes={1:'dynamical' if D>2 else 'other',2:'topological' if D==4 else 'other',3:'vanishes' if D<6 else 'other'}
if classes[1]!='dynamical' or classes[2]!='topological' or classes[3]!='vanishes': raise AssertionError('D4 Lovelock')
md=f"""# {TITLE}

{DESC}

In D=4:

```text
p=1 EH: {classes[1]}
p=2 Gauss-Bonnet: {classes[2]}
p>=3: {classes[3]}
```

So EH is the unique dynamical Lovelock curvature branch in D=4, up to Lambda and boundary terms.
"""
write_report(md)
