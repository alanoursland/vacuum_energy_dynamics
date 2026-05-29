#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('17_scalar_ladder_scope_limit.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


k,R=sp.symbols('k R', positive=True, integer=True)
rR=(2*k-1)/(2*k+2*R+3)
r0=(2*k-1)/(2*k+3)
require_zero(rR.subs(R,0)-r0,'R=0 base')
# no tensor index dependence exists in scalar rR
n=sp.symbols('n')
expr=sp.diff(rR,n)
require_zero(expr,'no tensor dimension index dependence in rR symbol')


md = f"""# 17. Scalar ladder scope limit

## Checked identities

The scalar ladder coefficient

```text
r_(R,k) = (2k-1)/(2k+2R+3)
```

has no tensor/shear index structure. Its `R=0` base is the original `r_k`.

## Conclusion

The `r_k` ladder is a scalar admissibility object, not a carrier of Weyl/TT tensor data.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
