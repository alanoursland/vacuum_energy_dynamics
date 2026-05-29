#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("5_scalar_field_stress_gate.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

# Flat 2D symbolic scalar-field stress from inverse-metric variation.
rho, V = sp.symbols('rho V')
phi0, phi1 = sp.symbols('phi0 phi1')
# Euclidean signature witness for algebraic stress formula.
g00,g11=sp.symbols('g00 g11', positive=True)
X = g00*phi0**2 + g11*phi1**2
L = -sp.Rational(1,2)*X - V
# T_ab = -2 dL/dg^{ab} + g_ab L; in diagonal inverse variables g00,g11.
T00_cov = -2*sp.diff(L,g00) + sp.symbols('G00')*L
# The kinetic derivative part is phi0^2.
require_equal(-2*sp.diff(L,g00), phi0**2, 'scalar kinetic stress derivative 00')
require_equal(-2*sp.diff(L,g11), phi1**2, 'scalar kinetic stress derivative 11')


content = r"""# Scalar Field Stress Gate

A scalar matter action coupled through `g^{ab} ∂_a φ ∂_b φ` sources the
metric by differentiating with respect to the inverse metric.  The kinetic
part contributes

```text
∂_a φ ∂_b φ
```

to the stress tensor.  This is an example witness: once a matter field uses the
shared metric contraction, its stress route is fixed by variation.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
