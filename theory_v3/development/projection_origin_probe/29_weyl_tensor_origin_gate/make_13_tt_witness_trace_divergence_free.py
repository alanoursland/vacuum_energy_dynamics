#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('13_tt_witness_trace_divergence_free.md')
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

A=sp.symbols('A')
h=sp.Matrix([[A,0,0],[0,-A,0],[0,0,0]])
require_zero(sp.trace(h),'trace')
x,y,z=sp.symbols('x y z')
coords=[x,y,z]
divs=[]
for j in range(3):
    divs.append(sum(sp.diff(h[i,j], coords[i]) for i in range(3)))
for d in divs: require_zero(d,'div')
md = """# 13. TT witness: trace-free and divergence-free

The constant plus-polarization witness

```text
h = diag(A,-A,0)
```

has

```text
trace(h) = 0
partial_i h_ij = 0
```

but is not zero. This is a minimal algebraic witness that TT-like data is not scalar trace data.
"""

write_md(md)
