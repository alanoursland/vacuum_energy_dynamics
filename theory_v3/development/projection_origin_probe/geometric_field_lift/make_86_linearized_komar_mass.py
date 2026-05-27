#!/usr/bin/env python3
"""
make_86_linearized_komar_mass.py

Validate the weak-field Komar-like boundary mass expression:

    N = sqrt(-g_00) ~= 1 + Phi
    M = (1/(4*pi*G)) integral partial_n N dA

For Phi=-GM/r, this gives M in the weak-field limit.

Output:
    86_linearized_komar_mass.md
"""

from pathlib import Path
import sympy as sp


eps, phi = sp.symbols("eps phi", real=True)
r, Gconst, M = sp.symbols("r G M", positive=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# Weak field lapse N=sqrt(1+2 eps phi).
N_eps = sp.sqrt(1 + 2 * eps * phi)
N_linear_coeff = sp.diff(N_eps, eps).subs(eps, 0)
require_equal("linear lapse perturbation", N_linear_coeff, phi)
checks.append("linear lapse perturbation")

Phi = -Gconst * M / r
N_weak = 1 + Phi

mass_from_lapse = (1 / (4 * pi * Gconst)) * 4 * pi * r**2 * sp.diff(N_weak, r)
require_equal("weak-field Komar mass from lapse", mass_from_lapse, M)
checks.append("weak-field Komar mass from lapse")

h00 = -2 * Phi
mass_from_h00 = -(1 / (8 * pi * Gconst)) * 4 * pi * r**2 * sp.diff(h00, r)
require_equal("weak-field Komar mass from h00", mass_from_h00, M)
checks.append("weak-field Komar mass from h00")

u = -Phi
scalar_flux = -4 * pi * r**2 * sp.diff(u, r)
require_equal("scalar bridge flux in Komar normalization", scalar_flux, 4 * pi * Gconst * M)
checks.append("scalar bridge flux in Komar normalization")

require_equal("Komar mass from scalar bridge flux", scalar_flux / (4 * pi * Gconst), M)
checks.append("Komar mass from scalar bridge flux")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 86: Linearized Komar Mass

## Purpose

This report validates the weak-field boundary mass expression associated with
the lapse:

```text
N = sqrt(-g_00).
```

## Validated Checks

{validation_bullets}

## Linearized Lapse

For:

```text
g_00 = -(1+2 Phi),
```

the lapse is:

```text
N = sqrt(1+2 Phi) = 1 + Phi + higher order terms.
```

SymPy verifies the linear coefficient.

## Boundary Mass

For:

```text
Phi(r) = -GM/r,
N = 1 + Phi,
```

the weak-field boundary mass expression gives:

```text
M = (1/(4*pi*G)) integral partial_n N dA.
```

Equivalently:

```text
M = -(1/(8*pi*G)) integral partial_n h_00 dA.
```

## Scalar Bridge Normalization

With:

```text
u = -Phi = GM/r,
```

the scalar bridge flux is:

```text
Q = -integral partial_n u dA = 4*pi*G M.
```

So the scalar boundary charge is the weak-field mass multiplied by `4*pi*G`.
"""

out = Path(__file__).with_name("86_linearized_komar_mass.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
