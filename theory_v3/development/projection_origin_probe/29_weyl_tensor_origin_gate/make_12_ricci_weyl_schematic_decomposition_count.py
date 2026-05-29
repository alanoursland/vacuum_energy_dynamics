#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('12_ricci_weyl_schematic_decomposition_count.md')
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

D=4
riemann=D**2*(D**2-1)//12
ricci=D*(D+1)//2
weyl=riemann-ricci
require(riemann==20 and ricci==10 and weyl==10,'counts')
md = f"""# 12. Ricci/Weyl schematic decomposition count

In four dimensions:

```text
Riemann components = {riemann}
Ricci components   = {ricci}
Weyl components    = {weyl}
```

The Weyl sector is not a small correction to the scalar boundary ledger. It is an independent half of the local curvature component count.
"""

write_md(md)
