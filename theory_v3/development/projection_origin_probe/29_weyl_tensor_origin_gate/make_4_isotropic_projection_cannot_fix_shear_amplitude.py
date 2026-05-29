#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name('4_isotropic_projection_cannot_fix_shear_amplitude.md')
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

lam,s=sp.symbols('lambda s')
H1=sp.Matrix([[lam+s,0],[0,lam-s]])
H2=sp.Matrix([[lam+2*s,0],[0,lam-2*s]])
require_zero(sp.trace(H1)-sp.trace(H2),'same trace')
md = """# 4. Isotropic projection cannot fix shear amplitude

Two different matrices

```text
H1 = diag(lambda+s, lambda-s)
H2 = diag(lambda+2s, lambda-2s)
```

have the same trace, but different shear amplitudes.

Therefore scalar trace data cannot determine the traceless sector.
"""

write_md(md)
