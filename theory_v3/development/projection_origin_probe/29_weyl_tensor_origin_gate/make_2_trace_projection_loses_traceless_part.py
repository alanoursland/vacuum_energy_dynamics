#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('2_trace_projection_loses_traceless_part.md')
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

s = sp.symbols('s')
S = sp.Matrix([[s,0],[0,-s]])
tr = sp.trace(S)
require_zero(tr, 'trace')
md = f"""# 2. Trace projection loses traceless part

Take the nonzero shear matrix

```text
S = [[s,0],[0,-s]].
```

Its trace is

```text
tr(S) = {sp.sstr(tr)}.
```

So scalar trace projection annihilates it even though `S != 0` when `s != 0`.

Closed result:

```text
trace/monopole scalar data cannot reconstruct traceless shear.
```
"""

write_md(md)
