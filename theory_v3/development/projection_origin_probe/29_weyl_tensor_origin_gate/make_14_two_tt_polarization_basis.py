#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('14_two_tt_polarization_basis.md')
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

A,B=sp.symbols('A B')
plus=sp.Matrix([[1,0,0],[0,-1,0],[0,0,0]])
cross=sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])
h=A*plus+B*cross
require_zero(sp.trace(h),'trace')
md = """# 14. Two TT polarization basis

A wave propagating in the z direction has transverse trace-free basis tensors

```text
plus  = diag(1,-1,0)
cross = [[0,1,0],[1,0,0],[0,0,0]].
```

A linear combination

```text
h = A plus + B cross
```

has trace zero and contains two independent amplitudes `A` and `B`.

Scalar trace data sees neither amplitude.
"""

write_md(md)
