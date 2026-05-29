#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('6_tracefree_tidal_vacuum_witness.md')
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

x,y,z,a=sp.symbols('x y z a')
Phi = a*(x**2 - y**2)/2
lap = sp.diff(Phi,x,2)+sp.diff(Phi,y,2)+sp.diff(Phi,z,2)
H=sp.hessian(Phi,(x,y,z))
require_zero(lap,'laplacian vacuum')
require_zero(sp.trace(H),'trace H')
md = f"""# 6. Trace-free tidal vacuum witness

Take

```text
Phi = a (x^2-y^2)/2.
```

Then

```text
Delta Phi = {sp.sstr(lap)}
```

but the Hessian is nonzero:

```text
H = {sp.sstr(H)}.
```

So a vacuum scalar trace equation can have nonzero trace-free tidal data.

This is the Newtonian analogue of the Ricci/Weyl separation:

```text
trace/source channel can vanish while tidal/free data remains.
```
"""

write_md(md)
