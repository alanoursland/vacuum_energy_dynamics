#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("21_scalar_boundary_cannot_set_full_matter_coupling.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

# Rank witness: in 4D symmetric stress has 10 components; scalar trace gives 1.
D=4
sym=D*(D+1)//2
trace=1
gap=sym-trace
require_equal(sym, 10, '4D symmetric stress components')
require_equal(gap, 9, 'trace rank gap')


content = r"""# Scalar Boundary Cannot Set Full Matter Coupling

A scalar boundary ledger cannot determine full matter coupling.  In four
dimensions a symmetric stress tensor has

```text
D(D+1)/2 = 10
```

components, while the trace channel supplies one scalar.  The rank gap is 9.
Thus matter coupling requires tensor metric variation, not only the scalar
`r_k` boundary sector.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
