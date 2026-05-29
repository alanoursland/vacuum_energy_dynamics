#!/usr/bin/env python3
"""
make_36_boundary_flux_variation.py

Validate the boundary-charge variational form:

    E_Q[u] = 1/2 integral_R^infty 4*pi*r^2 (u')^2 dr - Q*u(R)

whose variation gives:

    (r^2 u')' = 0          in the bulk
    -4*pi*R^2*u'(R) = Q    at the boundary.

Output:
    36_boundary_flux_variation.md
"""

from pathlib import Path
import sympy as sp


r = sp.symbols("r", positive=True)
R = sp.symbols("R", positive=True)
Q = sp.symbols("Q", real=True)
pi = sp.pi

u = sp.Function("u")
v = sp.Function("v")


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

u_r = sp.diff(u(r), r)
v_r = sp.diff(v(r), r)

# First-variation integration-by-parts identity:
#
#   4*pi*r^2 u' v'
#     =
#   d/dr(4*pi*r^2 u' v) - d/dr(4*pi*r^2 u') v.
variation_density = 4 * pi * r**2 * u_r * v_r
boundary_derivative = sp.diff(4 * pi * r**2 * u_r * v(r), r)
bulk_operator = sp.diff(4 * pi * r**2 * u_r, r)

require_equal(
    "radial first-variation integration by parts",
    variation_density,
    boundary_derivative - bulk_operator * v(r),
)
checks.append("radial first-variation integration by parts")

# Boundary charge term -Q*u(R) contributes -Q*v(R). The lower integration
# boundary contributes -4*pi*R^2*u'(R)*v(R). Stationarity therefore requires:
#
#   -4*pi*R^2*u'(R) - Q = 0.
u_Q = Q / (4 * pi * r)
boundary_condition = -4 * pi * R**2 * sp.diff(u_Q, r).subs(r, R) - Q
require_zero("boundary flux condition for u=Q/(4*pi*r)", boundary_condition)
checks.append("boundary flux condition for u=Q/(4*pi*r)")

# The bulk operator vanishes for the flux-normalized solution.
bulk_for_u_Q = sp.diff(4 * pi * r**2 * sp.diff(u_Q, r), r)
require_zero("bulk equation for flux solution", bulk_for_u_Q)
checks.append("bulk equation for flux solution")

# The boundary-coupled functional evaluated on u_Q.
strain_energy = sp.integrate(
    sp.Rational(1, 2) * 4 * pi * r**2 * sp.diff(u_Q, r) ** 2,
    (r, R, sp.oo),
)
boundary_coupling = -Q * u_Q.subs(r, R)
reduced_action = sp.simplify(strain_energy + boundary_coupling)

require_equal("strain energy", strain_energy, Q**2 / (8 * pi * R))
checks.append("strain energy")
require_equal("boundary-coupled reduced functional", reduced_action, -Q**2 / (8 * pi * R))
checks.append("boundary-coupled reduced functional")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Radial Boundary Field Bridge 36: Boundary Flux Variation

## Purpose

This report validates the boundary-charge action:

```text
E_Q[u]
  =
  1/2 integral_R^infty 4*pi*r^2 (u')^2 dr
  - Q u(R).
```

The point is to represent mass/source strength as a boundary constraint, not as
a bulk density in the exterior vacuum region.

## Validated Checks

{validation_bullets}

## Variation Identity

SymPy verifies:

```text
4*pi*r^2 u'v'
  =
  d/dr[4*pi*r^2 u'v]
  - d/dr[4*pi*r^2 u'] v.
```

Therefore stationarity gives the bulk equation:

```text
d/dr[4*pi*r^2 u'] = 0,
```

and the boundary condition at the inner sphere:

```text
-4*pi*R^2*u'(R) = Q.
```

## Flux-Normalized Solution

The solution:

```text
u(r) = Q/(4*pi*r)
```

satisfies both:

```text
d/dr[4*pi*r^2 u'] = 0
```

and:

```text
-4*pi*R^2*u'(R) = Q.
```

## Reduced Boundary Functional

For the flux-normalized solution:

```text
strain energy = Q^2/(8*pi*R)
```

and:

```text
E_Q[u_Q] = -Q^2/(8*pi*R).
```

The sign depends on whether the boundary term is included as a source coupling
or whether one keeps only positive stored strain energy. The field equation and
boundary flux normalization are unaffected by that bookkeeping choice.

## Interpretation

This is the field-equation bridge from the admissibility work:

```text
nonzero endpoint defect
  -> controlled boundary flux
  -> source-free bulk equation
  -> exterior harmonic field.
```
"""

out = Path(__file__).with_name("36_boundary_flux_variation.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
