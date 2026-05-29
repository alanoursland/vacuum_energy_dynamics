#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('1_directional_quadratic_reconstructs_symmetric_matrix.md')
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

a,b,c = sp.symbols('a b c')
H = sp.Matrix([[a,b],[b,c]])
e1 = sp.Matrix([1,0]); e2=sp.Matrix([0,1])
def Q(v): return (v.T*H*v)[0]
Buv = sp.simplify((Q(e1+e2)-Q(e1)-Q(e2))/2)
require_zero(Buv-b, 'off diagonal reconstruction')
md = f"""# 1. Directional quadratic reconstructs symmetric matrix

For a quadratic directional response `Q(v)=v^T H v`, polarization recovers the off-diagonal component:

```text
(Q(e1+e2)-Q(e1)-Q(e2))/2 = {sp.sstr(Buv)} = b.
```

Closed result:

```text
directional quadratic probe data -> full symmetric bilinear matrix data.
```

Scalar trace data alone cannot do this.
"""

write_md(md)
