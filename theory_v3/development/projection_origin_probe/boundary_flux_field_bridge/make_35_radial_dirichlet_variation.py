#!/usr/bin/env python3
"""
make_35_radial_dirichlet_variation.py

Validate the first 3D radial bridge:

    E[u] = 1/2 integral_R^infty 4*pi*r^2 (u')^2 dr

has source-free Euler-Lagrange equation:

    (r^2 u')' = 0,

with exterior solution u(r)=Q/(4*pi*r), conserved flux Q, and self-energy
Q^2/(8*pi*R).

Output:
    35_radial_dirichlet_variation.md
"""

from pathlib import Path
import sympy as sp


r = sp.symbols("r", positive=True)
R = sp.symbols("R", positive=True)
Q = sp.symbols("Q", real=True)
pi = sp.pi

u = sp.Function("u")


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

ur = sp.diff(u(r), r)

# The radial Dirichlet Lagrangian density after angular integration:
#   1/2 * 4*pi*r^2*u'^2 = 2*pi*r^2*u'^2.
lag = 2 * pi * r**2 * ur**2

euler_lagrange = sp.diff(sp.diff(lag, ur), r) - sp.diff(lag, u(r))
target_el = 4 * pi * sp.diff(r**2 * sp.diff(u(r), r), r)

require_equal("radial Euler-Lagrange operator", euler_lagrange, target_el)
checks.append("radial Euler-Lagrange operator")

# Radial Laplacian form:
radial_laplacian = sp.diff(u(r), r, 2) + 2 * sp.diff(u(r), r) / r
require_equal(
    "Euler-Lagrange equals radial Laplace equation",
    target_el / (4 * pi * r**2),
    radial_laplacian,
)
checks.append("Euler-Lagrange equals radial Laplace equation")

# Exterior harmonic solution normalized by total boundary flux Q.
u_Q = Q / (4 * pi * r)
lap_u_Q = sp.diff(u_Q, r, 2) + 2 * sp.diff(u_Q, r) / r
require_zero("u=Q/(4*pi*r) is harmonic for r>0", lap_u_Q)
checks.append("u=Q/(4*pi*r) is harmonic for r>0")

flux_Q = -4 * pi * r**2 * sp.diff(u_Q, r)
require_equal("conserved radial flux", flux_Q, Q)
checks.append("conserved radial flux")

energy_density = sp.Rational(1, 2) * 4 * pi * r**2 * sp.diff(u_Q, r) ** 2
energy = sp.integrate(energy_density, (r, R, sp.oo))
require_equal("exterior self-energy", energy, Q**2 / (8 * pi * R))
checks.append("exterior self-energy")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Radial Boundary Field Bridge 35: Radial Dirichlet Variation

## Purpose

This report validates the first 3D radial bridge from the one-dimensional
Dirichlet energy to a physical exterior-domain field.

The tested energy is:

```text
E[u] = 1/2 integral_R^infty 4*pi*r^2 (u')^2 dr.
```

## Validated Checks

{validation_bullets}

## Euler-Lagrange Equation

After angular integration, the radial Lagrangian density is:

```text
2*pi*r^2*(u')^2.
```

SymPy verifies that the Euler-Lagrange equation is:

```text
d/dr [4*pi*r^2 u'] = 0.
```

Equivalently:

```text
u'' + (2/r)u' = 0,
```

which is the source-free radial Laplace equation in 3D.

## Boundary Flux Solution

The exterior solution with total flux `Q` is:

```text
u(r) = Q/(4*pi*r).
```

It satisfies:

```text
Delta u = 0        for r > 0
-4*pi*r^2*u'(r) = Q.
```

So the `1/r` profile is not an extra assumption. It is the unique decaying
spherically symmetric minimizer with conserved boundary flux `Q`.

## Exterior Self-Energy

For an inner boundary sphere of radius `R`, SymPy verifies:

```text
E[u_Q] = Q^2/(8*pi*R).
```

This is a self-energy term. It depends on the source radius/cutoff `R`, not on
separation from another source.

## Interpretation

This proves the first physical bridge:

```text
Dirichlet strain energy in a 3D exterior domain
  -> source-free Laplace equation in the bulk
  -> conserved boundary flux
  -> exterior 1/r profile
  -> inverse-square field strength.
```
"""

out = Path(__file__).with_name("35_radial_dirichlet_variation.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
