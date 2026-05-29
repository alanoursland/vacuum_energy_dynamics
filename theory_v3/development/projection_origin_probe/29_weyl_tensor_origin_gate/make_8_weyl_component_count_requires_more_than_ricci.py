#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('8_weyl_component_count_requires_more_than_ricci.md')
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

D=sp.symbols('D', integer=True, positive=True)
riemann = D**2*(D**2-1)/12
ricci = D*(D+1)/2
weyl = sp.simplify(riemann-ricci)
weyl4=sp.simplify(weyl.subs(D,4))
require(weyl4==10,'weyl4 count')
md = f"""# 8. Weyl component count requires more than Ricci

The component counts are

```text
Riemann(D) = D^2(D^2-1)/12
Ricci(D)   = D(D+1)/2
Weyl(D)    = Riemann - Ricci = {sp.sstr(weyl)}.
```

In `D=4`,

```text
Weyl(4) = {weyl4}.
```

So Ricci/source/trace data does not exhaust curvature data in four dimensions.
"""

write_md(md)
