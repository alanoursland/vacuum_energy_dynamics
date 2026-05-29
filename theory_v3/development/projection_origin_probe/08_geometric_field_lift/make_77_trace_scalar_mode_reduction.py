#!/usr/bin/env python3
"""
make_77_trace_scalar_mode_reduction.py

Validate the scalar trace-mode reduction of the componentwise strain model:

    h_ij = 2 phi delta_ij
    S_ij = 2 rho delta_ij

In three spatial dimensions this reduces the component equations to:

    -Delta phi = rho.

Output:
    77_trace_scalar_mode_reduction.md
"""

from pathlib import Path
import sympy as sp


x, y, z = sp.symbols("x y z", real=True)
coords = (x, y, z)
phi = sp.Function("phi")(x, y, z)
rho = sp.Function("rho")(x, y, z)
eta = sp.Function("eta")(x, y, z)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def lap(expr):
    return sum(sp.diff(expr, c, 2) for c in coords)


def grad_dot(a, b):
    return sum(sp.diff(a, c) * sp.diff(b, c) for c in coords)


checks = []

spatial_dim = 3

# h_ij = 2 phi delta_ij, S_ij = 2 rho delta_ij.
strain_density = sp.Rational(1, 2) * spatial_dim * grad_dot(2 * phi, 2 * phi)
source_density = spatial_dim * (2 * rho) * (2 * phi)
reduced_density = strain_density - source_density

require_equal("trace-mode strain density", strain_density, 6 * grad_dot(phi, phi))
checks.append("trace-mode strain density")
require_equal("trace-mode source density", source_density, 12 * rho * phi)
checks.append("trace-mode source density")
require_equal("trace-mode reduced density", reduced_density, 6 * grad_dot(phi, phi) - 12 * rho * phi)
checks.append("trace-mode reduced density")

# First variation:
#   delta[6 |grad phi|^2 - 12 rho phi]
#     = 12 grad phi.grad eta - 12 rho eta
#     = div(12 eta grad phi) + 12(-Delta phi - rho)eta.
variation_density = 12 * grad_dot(phi, eta) - 12 * rho * eta
boundary_density = sum(sp.diff(12 * eta * sp.diff(phi, c), c) for c in coords)
bulk_density = 12 * (-lap(phi) - rho) * eta

require_zero("trace-mode scalar variation identity", variation_density - boundary_density - bulk_density)
checks.append("trace-mode scalar variation identity")

# Component equation check:
#   -Delta h_ii = S_ii  => -Delta(2phi)=2rho.
require_equal("component equation reduces to scalar Poisson", -lap(2 * phi) - 2 * rho, 2 * (-lap(phi) - rho))
checks.append("component equation reduces to scalar Poisson")

trace_h = spatial_dim * 2 * phi
trace_S = spatial_dim * 2 * rho
require_equal("trace equation reduction", -lap(trace_h) - trace_S, 6 * (-lap(phi) - rho))
checks.append("trace equation reduction")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 77: Trace Scalar Mode Reduction

## Purpose

This report validates that the isotropic trace mode of the componentwise
weak-field strain model reduces to the scalar bridge equation.

## Validated Checks

{validation_bullets}

## Ansatz

Use the isotropic spatial perturbation:

```text
h_ij = 2 phi delta_ij
```

and isotropic source:

```text
S_ij = 2 rho delta_ij.
```

In three spatial dimensions, the componentwise strain density reduces to:

```text
1/2 sum_ij |grad h_ij|^2 = 6 |grad phi|^2.
```

The source coupling reduces to:

```text
sum_ij S_ij h_ij = 12 rho phi.
```

## Scalar Equation

The first variation gives:

```text
12(-Delta phi - rho) = 0.
```

Equivalently:

```text
-Delta phi = rho.
```

## Interpretation

The scalar boundary-flux bridge appears as the isotropic trace sector of the
naive componentwise metric perturbation model, with explicit normalization.
"""

out = Path(__file__).with_name("77_trace_scalar_mode_reduction.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
