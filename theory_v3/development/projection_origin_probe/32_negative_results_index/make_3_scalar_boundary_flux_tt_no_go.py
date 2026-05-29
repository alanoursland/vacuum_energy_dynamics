import os
os.chdir(os.path.dirname(__file__))

import sympy as sp
from pathlib import Path
hplus,hcross=sp.symbols('hplus hcross')
H=sp.Matrix([[hplus,hcross,0],[hcross,-hplus,0],[0,0,0]])
trace=sp.trace(H)
norm=sp.trace(H.T*H)
assert trace==0
md=f"""# 3. Scalar Boundary Flux / TT No-Go

A transverse-traceless witness can carry nonzero tensor amplitude with zero
scalar trace.

```text
H = [[h_+, h_x, 0], [h_x, -h_+, 0], [0, 0, 0]]
```

SymPy verifies

```text
tr(H) = {trace}
tr(H^T H) = {norm}
```

## Closed result

Scalar boundary charge/trace data does not encode TT radiative amplitude.
"""
Path('3_scalar_boundary_flux_tt_no_go.md').write_text(md)
