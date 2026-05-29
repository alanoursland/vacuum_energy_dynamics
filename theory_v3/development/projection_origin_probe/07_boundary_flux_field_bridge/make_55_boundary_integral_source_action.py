#!/usr/bin/env python3
"""
make_55_boundary_integral_source_action.py

Validate the boundary-integral version of the source-coupled action:

    E[u] = 1/2 integral_Omega |grad u|^2 dV - integral_boundary q u dA.

For an exterior spherical domain this gives the natural boundary condition:

    partial_n u = q_density,

where the outward normal of the exterior domain at the inner sphere points
toward decreasing r.

Output:
    55_boundary_integral_source_action.md
"""

from pathlib import Path
import sympy as sp


r, R, Q = sp.symbols("r R Q", positive=True)
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

# Radial first variation identity:
# integral_R^infty 4*pi*r^2 u' v' dr
#   = [4*pi*r^2 u' v]_R^infty - integral_R^infty d/dr(4*pi*r^2 u') v dr.
identity_density = 4 * pi * r**2 * u_r * v_r
rhs_density = sp.diff(4 * pi * r**2 * u_r * v(r), r) - sp.diff(4 * pi * r**2 * u_r, r) * v(r)
require_equal("radial boundary-action variation identity", identity_density, rhs_density)
checks.append("radial boundary-action variation identity")

# Boundary source density for total Q over the inner sphere.
q_density = Q / (4 * pi * R**2)
u_Q = Q / (4 * pi * r)

# Exterior domain inner boundary outward normal is n=-e_r, so partial_n u=-u_r.
normal_derivative_inner = -sp.diff(u_Q, r).subs(r, R)
require_equal("natural boundary density condition", normal_derivative_inner, q_density)
checks.append("natural boundary density condition")

total_boundary_flux = 4 * pi * R**2 * normal_derivative_inner
require_equal("total boundary flux condition", total_boundary_flux, Q)
checks.append("total boundary flux condition")

bulk_operator = sp.diff(4 * pi * r**2 * sp.diff(u_Q, r), r)
require_zero("source-free exterior bulk equation", bulk_operator)
checks.append("source-free exterior bulk equation")

boundary_coupling = -Q * u_Q.subs(r, R)
strain_energy = sp.integrate(
    sp.Rational(1, 2) * 4 * pi * r**2 * sp.diff(u_Q, r) ** 2,
    (r, R, sp.oo),
)
require_equal("boundary-integral reduced action", strain_energy + boundary_coupling, -Q**2 / (8 * pi * R))
checks.append("boundary-integral reduced action")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 55: Boundary-Integral Source Action

## Purpose

This report upgrades the point boundary coupling to an actual boundary integral:

```text
E[u] = 1/2 integral_Omega |grad u|^2 dV
       - integral_boundary q u dA.
```

## Validated Checks

{validation_bullets}

## Variation

In the radial exterior domain:

```text
integral 4*pi*r^2 u'v' dr
  =
  [4*pi*r^2 u'v]_R^infty
  - integral d/dr[4*pi*r^2u'] v dr.
```

The bulk equation is:

```text
d/dr[4*pi*r^2u'] = 0.
```

At the inner boundary of an exterior domain, the outward normal points toward
decreasing `r`, so:

```text
partial_n u = -u'(R).
```

The boundary source density is:

```text
q = Q/(4*pi*R^2).
```

The natural boundary condition is:

```text
partial_n u = q.
```

## Flux-Normalized Solution

For:

```text
u(r)=Q/(4*pi*r),
```

SymPy verifies:

```text
partial_n u = Q/(4*pi*R^2)
integral_boundary partial_n u dA = Q.
```

## Interpretation

The source-coupled reduced-action sign is compatible with a genuine boundary
source action. Mass-like source strength can be represented as boundary flux
density, not only as an idealized point charge.
"""

out = Path(__file__).with_name("55_boundary_integral_source_action.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
