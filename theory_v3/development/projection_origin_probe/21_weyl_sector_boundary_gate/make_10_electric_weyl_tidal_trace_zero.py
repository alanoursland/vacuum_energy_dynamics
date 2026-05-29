#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('10_electric_weyl_tidal_trace_zero.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


l1,l2=sp.symbols('lambda1 lambda2')
E=sp.diag(l1,l2,-l1-l2)
require_zero(sp.trace(E),'tidal trace')
invar=sp.simplify(sp.trace(E*E))
if invar == 0:
    raise AssertionError('tidal invariant collapsed')


md = f"""# 10. Electric Weyl/tidal trace-zero witness

## Checked identities

A vacuum tidal/electric-Weyl witness has eigenvalues

```text
lambda1, lambda2, -lambda1-lambda2
```

so its trace is zero while its quadratic invariant is generally nonzero.

## Conclusion

Vacuum tidal curvature can be present even when scalar trace/source data vanishes.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
