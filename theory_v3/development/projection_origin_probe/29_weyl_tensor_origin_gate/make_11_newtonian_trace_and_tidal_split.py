#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('11_newtonian_trace_and_tidal_split.md')
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

rho,a=sp.symbols('rho a')
H=sp.Matrix([[rho/3+a,0,0],[0,rho/3-a,0],[0,0,rho/3]])
tr=sp.trace(H)
TF=sp.simplify(H-tr/3*sp.eye(3))
require_zero(tr-rho,'trace'); require_zero(sp.trace(TF),'tf trace')
md = f"""# 11. Newtonian trace and tidal split

A Hessian-like matrix can be split as

```text
H = (rho/3) I + Tidal_TF.
```

For the witness matrix, the trace is

```text
tr(H) = {sp.sstr(tr)}.
```

and the trace-free tidal part is

```text
{sp.sstr(TF)}.
```

The source/Poisson trace and free tidal data are distinct channels.
"""

write_md(md)
