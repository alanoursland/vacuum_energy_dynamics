#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('15_boundary_shear_from_directional_interval_difference.md')
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

s=sp.symbols('s')
H=sp.Matrix([[1+s,0],[0,1-s]])
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1])
def Q(v): return (v.T*H*v)[0]
s_rec=sp.simplify((Q(e1)-Q(e2))/2)
require_zero(s_rec-s,'shear')
md = f"""# 15. Boundary shear from directional interval difference

For boundary interval matrix

```text
H = diag(1+s, 1-s),
```

trace data is constant, but directional difference gives

```text
(Q(e1)-Q(e2))/2 = {sp.sstr(s_rec)}.
```

Boundary shear is directional interval data.
"""

write_md(md)
