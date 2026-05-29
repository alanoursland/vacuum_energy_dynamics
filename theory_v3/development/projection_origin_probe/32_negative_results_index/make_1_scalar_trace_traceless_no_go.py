import os
os.chdir(os.path.dirname(__file__))

import sympy as sp
from pathlib import Path

a,b,c=sp.symbols('a b c')
T=sp.diag(a,b,-a-b)
trace=sp.trace(T)
norm=sp.trace(T*T)
assert sp.simplify(trace)==0
assert sp.simplify(norm - (a**2+b**2+(a+b)**2))==0
md=f"""# 1. Scalar Trace / Traceless No-Go

A scalar trace channel cannot reconstruct traceless tensor data.

Use a symmetric traceless witness

```text
T = diag(a, b, -a-b).
```

SymPy verifies

```text
tr(T) = {sp.simplify(trace)}
tr(T^2) = {sp.simplify(norm)}
```

The trace scalar is zero while the tensor can still be nonzero. Thus scalar
trace data kills exactly the sector needed for shear/Weyl-like information.

## Closed result

```text
trace(T) = 0 does not imply T = 0.
```

The scalar ladder cannot recover traceless tensor data.
"""
Path('1_scalar_trace_traceless_no_go.md').write_text(md)
