#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('7_directional_probe_detects_vacuum_tidal_shear.md')
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

a=sp.symbols('a')
H=sp.Matrix([[a,0,0],[0,-a,0],[0,0,0]])
e1=sp.Matrix([1,0,0]); e2=sp.Matrix([0,1,0])
def Q(v): return (v.T*H*v)[0]
diff=sp.simplify(Q(e1)-Q(e2))
require_zero(diff-2*a,'directional shear')
md = f"""# 7. Directional probe detects vacuum tidal shear

For trace-free tidal matrix

```text
H = diag(a,-a,0),
```

scalar trace gives zero, but directional probes give

```text
Q(e1)-Q(e2) = {sp.sstr(diff)}.
```

Thus directional interval probes detect the data the scalar ledger misses.
"""

write_md(md)
