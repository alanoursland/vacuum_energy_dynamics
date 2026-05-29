#!/usr/bin/env python3
"""
make_20_connection_not_tensor_curvature_field_strength.py

Validate that connection coefficients can be nonzero from coordinate choice
alone, while curvature detects the tensorial field strength of connection
strain.

Output:
    20_connection_not_tensor_curvature_field_strength.md
"""

from pathlib import Path
import sympy as sp


y, r, th = sp.symbols("y r theta", positive=True)
coords = (r, th)
dim = 2


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# One-dimensional nonlinear relabeling X=y^2/2. A zero old connection becomes
# nonzero in y coordinates:
#   Gamma^y_yy = (dy/dX) d^2X/dy^2 = X''/X'.
X_prime = y
X_second = 1
Gamma_y = simplify_expr(X_second / X_prime)
require_equal("nonlinear relabeling creates connection coefficient", Gamma_y, 1 / y)
checks.append("nonlinear relabeling creates connection coefficient")

# Flat Euclidean plane in polar coordinates has nonzero Christoffels but zero
# curvature.
g = sp.diag(1, r**2)
g_inv = sp.diag(1, r**-2)


def Gamma(a, b, c):
    return simplify_expr(
        sp.Rational(1, 2)
        * sum(
            g_inv[a, d]
            * (
                sp.diff(g[d, c], coords[b])
                + sp.diff(g[d, b], coords[c])
                - sp.diff(g[b, c], coords[d])
            )
            for d in range(dim)
        )
    )


require_equal("polar Gamma r theta theta", Gamma(0, 1, 1), -r)
checks.append("polar Gamma r theta theta")
require_equal("polar Gamma theta r theta", Gamma(1, 0, 1), 1 / r)
checks.append("polar Gamma theta r theta")
require_equal("polar Gamma theta theta r", Gamma(1, 1, 0), 1 / r)
checks.append("polar Gamma theta theta r")


def Riemann(a, b, c, d):
    return simplify_expr(
        sp.diff(Gamma(a, b, d), coords[c])
        - sp.diff(Gamma(a, b, c), coords[d])
        + sum(Gamma(a, e, c) * Gamma(e, b, d) - Gamma(a, e, d) * Gamma(e, b, c) for e in range(dim))
    )


for a in range(dim):
    for b in range(dim):
        for c in range(dim):
            for d in range(dim):
                require_zero(f"polar flat Riemann {a}{b}{c}{d}", Riemann(a, b, c, d))

checks.append("polar flat connection has zero curvature")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 20: Connection Is Not Tensor, Curvature Is Field Strength

## Purpose

This report validates the next gate:

```text
connection coefficients are local comparison data,
not tensorial field strength.
curvature is the tensorial obstruction to flat comparison.
```

## Validated Checks

{validation_bullets}

## Connection Can Be Coordinate-Created

In one dimension, start with zero connection in coordinate `X` and relabel:

```text
X = y^2/2.
```

The transformed connection coefficient is:

```text
Gamma^y_yy = (dy/dX) d^2X/dy^2 = 1/y.
```

So a nonzero connection coefficient can arise from relabeling alone.

## Polar Flat Plane

For the flat plane:

```text
ds^2 = dr^2 + r^2 dtheta^2,
```

SymPy verifies nonzero connection coefficients:

```text
Gamma^r_thetatheta = -r
Gamma^theta_rtheta = 1/r
Gamma^theta_thetar = 1/r.
```

But SymPy verifies all Riemann components vanish.

## Interpretation

The connection is the local comparison rule, but it is not itself a tensorial
field strength. The curvature is the invariant obstruction to removing
connection strain by coordinate choice. This is the action-origin reason the
metric action must be built from curvature or from a connection-strain density
with explicit boundary bookkeeping.
"""

out = Path(__file__).with_name("20_connection_not_tensor_curvature_field_strength.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
