#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('15_bondi_news_tracefree_witness.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


cp,cx=sp.symbols('c_plus c_cross')
C=sp.Matrix([[cp,cx],[cx,-cp]])
require_zero(sp.trace(C),'2D shear trace')
invar=sp.simplify(sp.trace(C*C))
require_zero(invar-2*(cp**2+cx**2),'shear invariant')


md = f"""# 15. Bondi-news-like tracefree shear witness

## Checked identities

A two-dimensional boundary shear/news witness

```text
[[c_+, c_x], [c_x, -c_+]]
```

has zero trace but nonzero invariant `2(c_+^2+c_x^2)`.

## Conclusion

Radiative boundary shear/news can be trace-free and therefore invisible to scalar charge ledgers.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
