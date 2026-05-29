#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("15_diffeomorphism_variation_conservation_gate.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

# One-dimensional integration-by-parts witness for the conservation route.
x=sp.symbols('x')
T=sp.Function('T')(x)
xi=sp.Function('xi')(x)
expr=T*sp.diff(xi,x)
# T xi' = (T xi)' - T' xi
rhs=sp.diff(T*xi,x)-sp.diff(T,x)*xi
require_zero(sp.simplify(expr-rhs), 'IBP conservation identity')


content = r"""# Diffeomorphism Variation Conservation Gate

A diffeomorphism variation of a metric matter action routes conservation by
integration by parts.  The symbolic witness checks

```text
T ξ' = (T ξ)' - T' ξ.
```

In tensor form, the same structure yields the bulk condition

```text
∇_a T^{ab}=0
```

up to boundary flux terms.  This is a compatibility gate, not a microscopic
matter-origin theorem.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
