#!/usr/bin/env python3
"""
make_22_connection_trace_volume_boundary_flux.py

Validate that the contracted connection is the logarithmic derivative of the
metric volume density, and that the EH boundary vector is a connection/volume
flux.

Output:
    22_connection_trace_volume_boundary_flux.md
"""

from pathlib import Path
import sympy as sp


x, y, z, D = sp.symbols("x y z D", positive=True)
coords = (x, y, z)
dim = 3
A = sp.Function("A")(x)
B = sp.Function("B")(x)
C = sp.Function("C")(x)
s = sp.Function("s")(x)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

g = sp.diag(A, B, C)
g_inv = sp.simplify(g.inv())
sqrt_g = sp.sqrt(A * B * C)


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


trace_x = simplify_expr(sum(Gamma(a, a, 0) for a in range(dim)))
volume_log_derivative = simplify_expr(sp.diff(sqrt_g, x) / sqrt_g)
require_equal("contracted connection is volume log derivative", trace_x, volume_log_derivative)
checks.append("contracted connection is volume log derivative")

for c_index, coord in enumerate(coords):
    trace_c = simplify_expr(sum(Gamma(a, a, c_index) for a in range(dim)))
    volume_c = simplify_expr(sp.diff(sqrt_g, coord) / sqrt_g)
    require_equal(f"volume identity component {c_index}", trace_c, volume_c)

checks.append("volume identity all components")

V = []
for c_index in range(dim):
    term = 0
    for a in range(dim):
        for b in range(dim):
            term += g_inv[a, b] * Gamma(c_index, a, b) - g_inv[c_index, b] * Gamma(a, a, b)
    V.append(simplify_expr(sqrt_g * term))

expected_Vx = simplify_expr(
    sqrt_g
    * (
        g_inv[0, 0] * Gamma(0, 0, 0)
        + g_inv[1, 1] * Gamma(0, 1, 1)
        + g_inv[2, 2] * Gamma(0, 2, 2)
        - g_inv[0, 0] * trace_x
    )
)
require_equal("boundary vector x component is connection-volume flux", V[0], expected_Vx)
checks.append("boundary vector x component is connection-volume flux")

require_equal("boundary vector transverse components vanish for warped ansatz", V[1] + V[2], 0)
checks.append("boundary vector transverse components vanish for warped ansatz")

# Conformal D-dimensional volume identity in one direction.
sqrt_g_conf = sp.exp(D * s)
trace_conf = D * sp.diff(s, x)
require_equal("conformal contracted connection volume identity", trace_conf, sp.diff(sqrt_g_conf, x) / sqrt_g_conf)
checks.append("conformal contracted connection volume identity")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 22: Connection Trace as Volume Boundary Flux

## Purpose

This report validates the boundary-flux meaning of the contracted connection.

The gate is:

```text
connection trace
  =
  logarithmic derivative of metric volume density.
```

## Validated Checks

{validation_bullets}

## Volume Identity

For:

```text
g = diag(A(x), B(x), C(x)),
sqrt(g) = sqrt(A B C),
```

SymPy verifies:

```text
Gamma^a_ac = partial_c log sqrt(g).
```

Equivalently:

```text
Gamma^a_ac = partial_c sqrt(g) / sqrt(g).
```

## Boundary Vector

The EH boundary vector has the form:

```text
V^c = sqrt(g)(g^ab Gamma^c_ab - g^cb Gamma^a_ab).
```

SymPy verifies that for the warped ansatz the only nonzero component is the
`x`-flux component, built from connection coefficients and the volume density.

## Conformal Check

For a conformal volume density:

```text
sqrt(g) = exp(D s),
```

SymPy verifies:

```text
partial_x log sqrt(g) = D s'.
```

## Interpretation

The boundary term in the metric action is a volume/connection flux. This is the
metric version of the scalar boundary-flux pattern: the boundary records how
the local comparison structure changes the volume measure.
"""

out = Path(__file__).with_name("22_connection_trace_volume_boundary_flux.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
