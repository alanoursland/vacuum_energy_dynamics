#!/usr/bin/env python3
"""
make_17_conformal_boundary_flux_to_metric_boundary.py

Validate in a conformal sector that the metric curvature action has a boundary
flux term plus a first-derivative strain density.

Output:
    17_conformal_boundary_flux_to_metric_boundary.md
"""

from pathlib import Path
import sympy as sp


x, D = sp.symbols("x D", positive=True)
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

E = sp.exp((D - 2) * s)
spx = sp.diff(s, x)
spp = sp.diff(s, x, 2)

sqrt_g_R_1d = -2 * (D - 1) * E * spp - (D - 1) * (D - 2) * E * spx**2
boundary_flux_density = -2 * (D - 1) * E * spx
boundary_divergence = sp.diff(boundary_flux_density, x)
bulk_strain = (D - 1) * (D - 2) * E * spx**2

require_equal("conformal metric boundary plus strain split", sqrt_g_R_1d - boundary_divergence, bulk_strain)
checks.append("conformal metric boundary plus strain split")

require_equal("four-dimensional boundary flux density", boundary_flux_density.subs(D, 4), -6 * sp.exp(2 * s) * spx)
checks.append("four-dimensional boundary flux density")

require_equal("four-dimensional bulk conformal strain", bulk_strain.subs(D, 4), 6 * sp.exp(2 * s) * spx**2)
checks.append("four-dimensional bulk conformal strain")

require_equal("two-dimensional bulk conformal strain vanishes", bulk_strain.subs(D, 2), 0)
checks.append("two-dimensional bulk conformal strain vanishes")

linearized_flux_D4 = sp.diff(boundary_flux_density.subs(D, 4), spx).subs(s, 0)
require_equal("linearized D4 flux momentum coefficient", linearized_flux_D4, -6)
checks.append("linearized D4 flux momentum coefficient")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 17: Conformal Boundary Flux to Metric Boundary

## Purpose

This report strengthens the boundary-flux bridge in a metric sector.

For a conformal metric:

```text
g_ab = exp(2s) eta_ab,
```

the curvature density separates into:

```text
boundary flux + first-derivative metric strain.
```

## Validated Checks

{validation_bullets}

## One-Dimensional Conformal Sector

The conformal curvature density along one coordinate has the form:

```text
sqrt(g)R =
  -2(D-1) exp((D-2)s) s''
  -(D-1)(D-2) exp((D-2)s)(s')^2.
```

Define the boundary flux density:

```text
F_boundary = -2(D-1) exp((D-2)s) s'.
```

SymPy verifies:

```text
sqrt(g)R - dF_boundary/dx
  =
  (D-1)(D-2) exp((D-2)s)(s')^2.
```

## Four-Dimensional Case

For `D=4`:

```text
F_boundary = -6 exp(2s) s'
bulk strain = 6 exp(2s)(s')^2.
```

The linearized boundary momentum coefficient is:

```text
-6.
```

## Interpretation

This is the conformal metric analogue of the scalar boundary-flux variational
source. The EH/GHY boundary structure is not an unrelated add-on: in this
sector it is exactly the boundary-flux completion of metric strain.
"""

out = Path(__file__).with_name("17_conformal_boundary_flux_to_metric_boundary.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
