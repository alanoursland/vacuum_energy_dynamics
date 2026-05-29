#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("8_traceless_stress_invisible_to_conformal.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

sigma,sqrtg,A=sp.symbols('sigma sqrtg A')
T00=A; T11=-A
h00=2*sigma; h11=2*sigma
dS=sp.Rational(1,2)*sqrtg*(T00*h00+T11*h11)
require_zero(dS, 'traceless stress conformal invisibility')


content = r"""# Traceless Stress Invisible to Conformal Perturbation

A traceless source can be nonzero while a conformal metric variation sees
nothing.  The witness

```text
T = diag(A, -A)
```

has zero trace, and the conformal variation vanishes.  This is the matter-side
analogue of the scalar ladder's trace limitation.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
