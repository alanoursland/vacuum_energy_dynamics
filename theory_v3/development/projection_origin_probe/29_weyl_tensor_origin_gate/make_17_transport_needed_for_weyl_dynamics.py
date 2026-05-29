#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('17_transport_needed_for_weyl_dynamics.md')
def require_zero(expr, name='expr'):
    if sp.simplify(expr) != 0:
        raise AssertionError(f"{name} not zero: {sp.simplify(expr)}")
def require(cond, name='condition'):
    if not bool(cond):
        raise AssertionError(f"failed: {name}")
def write_md(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text.strip() + "\n", encoding='utf-8')
    tmp.replace(OUT)

wamp,wt,c=sp.symbols('w wt c')
constraint = wt + c*wamp
require_zero(sp.diff(constraint, wt)-1,'derivative check')
md = """# 17. Transport needed for Weyl dynamics

Local directional data can supply a Weyl-like amplitude `w`, but dynamics requires a transport equation, schematically

```text
w_t + c w = 0
```

or its tensor/gauge-covariant analogue.

The local algebraic reconstruction of traceless data does not by itself supply this propagation law.

Closed result:

```text
directional probes can recover local traceless data;
Weyl dynamics still requires transport/constraint closure.
```
"""

write_md(md)
