#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('5_hessian_trace_poisson_sector.md')
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

x,y,z,k=sp.symbols('x y z k')
Phi = k*(x**2+y**2+z**2)/2
lap = sp.diff(Phi,x,2)+sp.diff(Phi,y,2)+sp.diff(Phi,z,2)
require_zero(lap-3*k,'laplacian')
md = f"""# 5. Hessian trace is the Poisson sector

For

```text
Phi = k (x^2+y^2+z^2)/2,
```

the Laplacian is the trace of the Hessian:

```text
Delta Phi = {sp.sstr(lap)}.
```

This is the scalar Poisson/trace channel. It does not encode the trace-free Hessian.
"""

write_md(md)
