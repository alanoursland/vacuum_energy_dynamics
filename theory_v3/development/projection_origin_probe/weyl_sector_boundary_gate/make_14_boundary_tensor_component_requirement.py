#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('14_boundary_tensor_component_requirement.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


m=sp.symbols('m', integer=True, positive=True)
tensor=m*(m+1)/2
scalar=1
need=sp.simplify(tensor-scalar)
require_zero(need.subs(m,3)-5,'boundary 3D missing components')


md = f"""# 14. Boundary tensor component requirement

## Checked identities

On an `m`-dimensional boundary, a symmetric induced tensor has

```text
m(m+1)/2
```

components. Scalar trace supplies only `1`; for `m=3`, five components remain.

## Conclusion

Full boundary geometry requires tensor boundary data beyond scalar flux.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
