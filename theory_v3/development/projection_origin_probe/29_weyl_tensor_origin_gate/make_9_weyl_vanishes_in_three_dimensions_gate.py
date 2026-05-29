#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('9_weyl_vanishes_in_three_dimensions_gate.md')
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

D=sp.symbols('D')
weyl = sp.simplify(D*(D+1)*(D+2)*(D-3)/12)
require_zero(weyl.subs(D,3),'D=3 Weyl')
md = f"""# 9. Weyl vanishes in three dimensions

The Weyl count is

```text
Weyl(D) = {sp.sstr(weyl)}.
```

At `D=3`, this becomes zero.

This supports the dimension-selector story: local free Weyl curvature requires at least four spacetime dimensions.
"""

write_md(md)
