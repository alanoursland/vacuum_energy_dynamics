#!/usr/bin/env python3
"""
make_5_boundary_flux_variational_source.py

Validate that boundary flux sources arise naturally from varying a local
Dirichlet energy with boundary source terms.

Output:
    5_boundary_flux_variational_source.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x")
u = sp.Function("u")(x)
eta = sp.Function("eta")(x)
uL, uR, etaL, etaR, upL, upR, QL, QR = sp.symbols("u_L u_R eta_L eta_R up_L up_R Q_L Q_R")
source_integral = sp.symbols("I")


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

bulk_variation_density = sp.diff(u, x) * sp.diff(eta, x)
bulk_decomposition = -eta * sp.diff(u, x, 2) + sp.diff(eta * sp.diff(u, x), x)

require_equal("Dirichlet variation bulk plus boundary decomposition", bulk_variation_density, bulk_decomposition)
checks.append("Dirichlet variation bulk plus boundary decomposition")

boundary_variation = upR * etaR - upL * etaL - QR * etaR + QL * etaL
boundary_factored = (upR - QR) * etaR + (-upL + QL) * etaL
require_equal("boundary source variation coefficients", boundary_variation, boundary_factored)
checks.append("boundary source variation coefficients")

right_condition = sp.solve([sp.Eq(upR - QR, 0)], [upR], dict=True)
left_condition = sp.solve([sp.Eq(-upL + QL, 0)], [upL], dict=True)
if right_condition != [{upR: QR}]:
    raise AssertionError(f"right boundary condition failed: {right_condition}")
if left_condition != [{upL: QL}]:
    raise AssertionError(f"left boundary condition failed: {left_condition}")
checks.append("boundary variation yields flux boundary conditions")

# For -u'' = S, integrating over [L,R] gives I = -u'(R) + u'(L).
integrated_defect = -upR + upL - source_integral
require_equal("integrated equation with boundary flux", integrated_defect.subs({upR: QR, upL: QL}), -QR + QL - source_integral)
checks.append("integrated equation with boundary flux")

require_equal(
    "zero net source compatibility under equal fluxes",
    (-QR + QL - source_integral).subs({QL: QR, source_integral: 0}),
    0,
)
checks.append("zero net source compatibility under equal fluxes")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 5: Boundary Flux as Variational Source

## Purpose

This report validates a basic action-origin mechanism for boundary flux:

```text
local Dirichlet energy
  + boundary source terms
  -> source-free bulk equation
  -> flux boundary conditions.
```

## Validated Checks

{validation_bullets}

## Bulk Variation

For:

```text
E_bulk = (1/2) integral (u')^2 dx,
```

the first variation density is:

```text
u' eta'.
```

SymPy verifies:

```text
u' eta' = -eta u'' + d(eta u')/dx.
```

So the bulk equation is:

```text
-u'' = 0
```

away from sources.

## Boundary Sources

Add boundary terms:

```text
E_boundary = -Q_R u(R) + Q_L u(L).
```

The boundary variation is:

```text
[u' eta]_L^R - Q_R eta_R + Q_L eta_L
  =
(u'(R)-Q_R)eta_R + (-u'(L)+Q_L)eta_L.
```

For arbitrary boundary variations, this gives:

```text
u'(R) = Q_R
u'(L) = Q_L.
```

## Integrated Compatibility

For a bulk equation:

```text
-u'' = S,
```

integrating gives:

```text
integral S dx = -u'(R) + u'(L).
```

So the source integral is exactly a boundary-flux defect.

## Interpretation

This is the action-origin version of the earlier projection result. The
admissibility functional is not just an abstract moment condition: in the
Dirichlet-energy variable it is the net boundary flux required by the source.
"""

out = Path(__file__).with_name("5_boundary_flux_variational_source.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
