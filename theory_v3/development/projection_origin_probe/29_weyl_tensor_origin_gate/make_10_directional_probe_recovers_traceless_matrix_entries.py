#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('10_directional_probe_recovers_traceless_matrix_entries.md')
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

a,b=sp.symbols('a b')
S=sp.Matrix([[a,b],[b,-a]])
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1])
def Q(v): return (v.T*S*v)[0]
a_rec=sp.simplify((Q(e1)-Q(e2))/2)
b_rec=sp.simplify((Q(e1+e2)-Q(e1)-Q(e2))/2)
require_zero(a_rec-a,'a rec'); require_zero(b_rec-b,'b rec')
md = f"""# 10. Directional probe recovers traceless matrix entries

For

```text
S = [[a,b],[b,-a]],
```

directional probes recover both traceless components:

```text
(Q(e1)-Q(e2))/2 = {sp.sstr(a_rec)}
(Q(e1+e2)-Q(e1)-Q(e2))/2 = {sp.sstr(b_rec)}
```

So the missing traceless sector is recoverable from directional quadratic data, not from scalar trace data.
"""

write_md(md)
