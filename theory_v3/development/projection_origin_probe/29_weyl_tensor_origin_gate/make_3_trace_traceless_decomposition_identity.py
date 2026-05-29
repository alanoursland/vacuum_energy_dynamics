#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('3_trace_traceless_decomposition_identity.md')
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

a,b,c=sp.symbols('a b c')
H=sp.Matrix([[a,b],[b,c]])
n=2
tr=sp.trace(H)
I=sp.eye(2)
TF=sp.simplify(H - tr/n*I)
require_zero(sp.trace(TF),'trace-free part trace')
recon=sp.simplify(tr/n*I + TF - H)
for entry in recon:
    require_zero(entry,'reconstruction')
md = """# 3. Trace/traceless decomposition identity

For a symmetric matrix `H`, the split

```text
H = (tr H / n) I + H_TF
H_TF = H - (tr H / n) I
```

has `tr(H_TF)=0`, and the script verifies exact reconstruction.

Interpretation:

```text
scalar trace channel -> isotropic part;
directional tensor channel -> traceless shear part.
```
"""

write_md(md)
