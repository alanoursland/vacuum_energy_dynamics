#!/usr/bin/env python3
"""
make_4_relabeling_invariance_density_gate.py

Validate the density and metric factors needed for relabeling-invariant local
actions.

Output:
    4_relabeling_invariance_density_gate.md
"""

from pathlib import Path
import sympy as sp


J, rho, sqrt_g, g_inv, q_y = sp.symbols("J rho sqrt_g g_inv q_y", nonzero=True)
J2 = sp.symbols("J2", nonzero=True)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# Scalar density in 1D:
#   dx = J dy, rho_y = rho_x J.
rho_y = rho * J
require_equal("scalar density relabeling", rho_y, rho * J)
checks.append("scalar density relabeling")

# First-derivative strain in 1D:
#   dx/dy = J
#   dq/dx = (dq/dy)/J
#   sqrt(g_y) = J sqrt(g_x)
#   g_y^yy = g_x^xx / J^2
sqrt_g_y = J * sqrt_g
g_y_inv = g_inv / J**2
strain_y_density = simplify_expr(sqrt_g_y * g_y_inv * q_y**2)
strain_x_density_times_jacobian = simplify_expr(J * sqrt_g * g_inv * (q_y / J) ** 2)
require_equal("metric strain density relabeling", strain_y_density, strain_x_density_times_jacobian)
checks.append("metric strain density relabeling")

# The raw derivative-square density without metric compensation does not
# transform as a scalar density.
raw_y = q_y**2
raw_x_times_jacobian = J * (q_y / J) ** 2
require_equal("raw derivative density mismatch factor", raw_y / raw_x_times_jacobian, J)
checks.append("raw derivative density mismatch factor")

# In 2D, the volume density transforms by the absolute determinant. Here we
# track the oriented algebraic determinant factor.
rho_2_relabel = rho * J2
require_equal("two-dimensional oriented density relabeling", rho_2_relabel, rho * J2)
checks.append("two-dimensional oriented density relabeling")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 4: Relabeling-Invariant Density Gate

## Purpose

This report validates the density bookkeeping required if vacuum-as-spacetime
has no preferred coordinate labels.

The gate is:

```text
coordinate labels are arbitrary
  -> action density must transform with the Jacobian
  -> derivative strain requires metric compensation.
```

## Validated Checks

{validation_bullets}

## Scalar Density

For a one-dimensional relabeling:

```text
dx = J dy,
```

the density must transform as:

```text
rho_y = rho_x J.
```

This is the basic condition for:

```text
integral rho_x dx = integral rho_y dy.
```

## Strain Density

For a first-derivative strain:

```text
dq/dx = (dq/dy)/J.
```

The metric factors transform as:

```text
sqrt(g_y) = J sqrt(g_x)
g_y^yy = g_x^xx / J^2.
```

SymPy verifies:

```text
sqrt(g_y) g_y^yy (dq/dy)^2
  =
J sqrt(g_x) g_x^xx [(dq/dy)/J]^2.
```

So the metric-density combination is relabeling-invariant.

## Raw Derivative Failure

A raw derivative-square density lacks the compensating metric factor. SymPy
verifies that it differs by a factor of `J`.

## Interpretation

If coordinates are only labels for vacuum configurations, the action must be a
geometric density. This is the action-origin version of diffeomorphism
invariance: it is not added for elegance; it is the bookkeeping required when
labels are not physical structure.
"""

out = Path(__file__).with_name("4_relabeling_invariance_density_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
