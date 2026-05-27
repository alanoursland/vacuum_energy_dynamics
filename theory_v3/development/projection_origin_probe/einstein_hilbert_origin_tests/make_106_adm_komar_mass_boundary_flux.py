#!/usr/bin/env python3
"""
make_106_adm_komar_mass_boundary_flux.py

Validate weak-field ADM and Komar boundary mass flux normalizations for the
Newtonian exterior metric.

Output:
    106_adm_komar_mass_boundary_flux.md
"""

from pathlib import Path
import sympy as sp


r, Gconst, M = sp.symbols("r G M", positive=True)
pi = sp.pi


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

Phi = -Gconst * M / r
u = -Phi
H_spatial = -2 * Phi  # g_ij = delta_ij + H_spatial delta_ij.
h00 = -2 * Phi

# ADM integrand for h_ij = H(r) delta_ij:
#   (partial_j h_ij - partial_i h_jj)n^i = -2 H'(r).
adm_integrand = -2 * sp.diff(H_spatial, r)
adm_mass = (1 / (16 * pi * Gconst)) * 4 * pi * r**2 * adm_integrand
require_equal("weak-field ADM mass", adm_mass, M)
checks.append("weak-field ADM mass")

# Komar/lapse mass in weak field:
#   N=1+Phi, M=(1/(4*piG)) integral partial_n N dA.
N = 1 + Phi
komar_mass = (1 / (4 * pi * Gconst)) * 4 * pi * r**2 * sp.diff(N, r)
require_equal("weak-field Komar mass", komar_mass, M)
checks.append("weak-field Komar mass")

mass_from_h00 = -(1 / (8 * pi * Gconst)) * 4 * pi * r**2 * sp.diff(h00, r)
require_equal("mass from h00 flux", mass_from_h00, M)
checks.append("mass from h00 flux")

scalar_flux = -4 * pi * r**2 * sp.diff(u, r)
require_equal("scalar bridge flux normalization", scalar_flux, 4 * pi * Gconst * M)
checks.append("scalar bridge flux normalization")

require_equal("ADM equals Komar in weak static exterior", adm_mass, komar_mass)
checks.append("ADM equals Komar in weak static exterior")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 106: ADM/Komar Mass Boundary Flux

## Purpose

This report validates weak-field ADM and Komar boundary mass normalizations for
the Newtonian exterior metric.

## Validated Checks

{validation_bullets}

## Newtonian Exterior Metric

Use:

```text
Phi = -GM/r
g_00 = -(1+2Phi)
g_ij = (1-2Phi)delta_ij.
```

The spatial perturbation is:

```text
h_ij = -2Phi delta_ij.
```

## ADM Mass

For this isotropic perturbation:

```text
(partial_j h_ij - partial_i h_jj)n^i = -2 d(-2Phi)/dr.
```

SymPy verifies:

```text
M_ADM = M.
```

## Komar/Lapse Mass

With:

```text
N = 1 + Phi,
```

SymPy verifies:

```text
M_Komar = (1/(4*pi*G)) integral partial_n N dA = M.
```

## Scalar Bridge Flux

With:

```text
u = -Phi,
```

the scalar flux is:

```text
Q_scalar = 4*pi*G M.
```

## Interpretation

The scalar boundary-flux normalization is consistent with standard weak-field
ADM/Komar mass bookkeeping.
"""

out = Path(__file__).with_name("106_adm_komar_mass_boundary_flux.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
