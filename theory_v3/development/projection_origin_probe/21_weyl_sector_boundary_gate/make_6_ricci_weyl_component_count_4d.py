#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('6_ricci_weyl_component_count_4d.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


D=sp.symbols('D', integer=True, positive=True)
riem=D**2*(D**2-1)/12
ricci=D*(D+1)/2
weyl=sp.simplify(riem-ricci)
weyl_formula=sp.simplify(D*(D+1)*(D+2)*(D-3)/12)
require_zero(weyl-weyl_formula, 'Weyl count formula')
require_zero(riem.subs(D,4)-20,'Riemann 4D')
require_zero(ricci.subs(D,4)-10,'Ricci 4D')
require_zero(weyl.subs(D,4)-10,'Weyl 4D')


md = f"""# 6. Riemann/Ricci/Weyl component count in 4D

## Checked identities

The algebraic component split in `D` dimensions was checked:

```text
Riemann = D^2(D^2-1)/12,
Ricci symmetric = D(D+1)/2,
Weyl = D(D+1)(D+2)(D-3)/12.
```

In `D=4`, this gives `20 = 10 + 10`.

## Conclusion

The Weyl sector is an independent curvature sector not determined by Ricci/trace data alone.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
