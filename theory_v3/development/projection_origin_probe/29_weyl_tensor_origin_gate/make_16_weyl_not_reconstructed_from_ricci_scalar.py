#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('16_weyl_not_reconstructed_from_ricci_scalar.md')
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

w1,w2=sp.symbols('w1 w2')
R_scalar = sp.Integer(0)
require_zero(R_scalar,'scalar')
md = """# 16. Weyl is not reconstructed from Ricci scalar

A scalar Ricci/trace channel value can be fixed, e.g.

```text
R_scalar = 0,
```

while independent Weyl amplitudes `w1`, `w2`, ... remain unconstrained.

This records the algebraic underdetermination:

```text
one scalar equation cannot solve independent traceless tensor amplitudes.
```
"""

write_md(md)
