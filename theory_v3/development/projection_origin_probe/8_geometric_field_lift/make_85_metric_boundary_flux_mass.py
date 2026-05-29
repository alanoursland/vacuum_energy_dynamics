#!/usr/bin/env python3
"""
make_85_metric_boundary_flux_mass.py

Validate the weak-field boundary mass/flux relation:

    Phi(r) = -G M/r
    h_00 = -2 Phi = 2GM/r

Then:

    M = (1/(4*pi*G)) integral partial_n Phi dA
      = -(1/(8*pi*G)) integral partial_n h_00 dA.

Output:
    85_metric_boundary_flux_mass.md
"""

from pathlib import Path
import sympy as sp


r, Gconst, M = sp.symbols("r G M", positive=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

Phi = -Gconst * M / r
h00 = -2 * Phi
u = -Phi

lap_phi = sp.diff(Phi, r, 2) + 2 * sp.diff(Phi, r) / r
require_zero("Newtonian potential harmonic off source", lap_phi)
checks.append("Newtonian potential harmonic off source")

mass_from_phi_flux = (1 / (4 * pi * Gconst)) * 4 * pi * r**2 * sp.diff(Phi, r)
require_equal("mass from Phi boundary flux", mass_from_phi_flux, M)
checks.append("mass from Phi boundary flux")

mass_from_h00_flux = -(1 / (8 * pi * Gconst)) * 4 * pi * r**2 * sp.diff(h00, r)
require_equal("mass from h00 boundary flux", mass_from_h00_flux, M)
checks.append("mass from h00 boundary flux")

scalar_bridge_flux = -4 * pi * r**2 * sp.diff(u, r)
require_equal("scalar bridge flux", scalar_bridge_flux, 4 * pi * Gconst * M)
checks.append("scalar bridge flux")

require_equal("mass from scalar bridge flux", scalar_bridge_flux / (4 * pi * Gconst), M)
checks.append("mass from scalar bridge flux")

require_equal("h00 scalar bridge relation", h00, 2 * u)
checks.append("h00 scalar bridge relation")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 85: Metric Boundary Flux Mass

## Purpose

This report connects the scalar boundary-flux source strength to the weak-field
metric/Newtonian mass flux.

## Validated Checks

{validation_bullets}

## Newtonian Exterior

For positive mass `M`:

```text
Phi(r) = -G M/r.
```

The weak-field metric perturbation is:

```text
h_00 = -2 Phi = 2GM/r.
```

The positive scalar bridge variable is:

```text
u = -Phi = GM/r.
```

## Boundary Flux Mass

SymPy verifies:

```text
M = (1/(4*pi*G)) integral partial_n Phi dA
```

and equivalently:

```text
M = -(1/(8*pi*G)) integral partial_n h_00 dA.
```

For the scalar bridge flux:

```text
Q = -integral partial_n u dA,
```

one gets:

```text
Q = 4*pi*G M.
```

## Interpretation

The scalar boundary-flux source strength maps cleanly to weak-field geometric
mass flux:

```text
Q_scalar = 4*pi*G M.
```

This is the first direct bridge between the scalar boundary-flux model and
linearized gravitational mass bookkeeping.
"""

out = Path(__file__).with_name("85_metric_boundary_flux_mass.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
