#!/usr/bin/env python3
"""
make_1_a_sector_mass_flux_normalization.py

Validate the reduced A-sector mass flux normalization.

Output:
    1_a_sector_mass_flux_normalization.md
"""

from pathlib import Path
import sympy as sp


r, G, M, c = sp.symbols("r G M c", positive=True)
pi = sp.pi


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

A_ext = 1 - 2 * G * M / (c**2 * r)
lap_areal = simplify_expr((1 / r**2) * sp.diff(r**2 * sp.diff(A_ext, r), r))
require_zero("source-free exterior A equation", lap_areal)
checks.append("A_ext is source-free under the areal radial Laplacian")

flux_A = simplify_expr(4 * pi * r**2 * sp.diff(A_ext, r))
expected_flux = 8 * pi * G * M / c**2
require_zero("A flux normalization", flux_A - expected_flux)
checks.append("A-sector flux equals 8*pi*G*M/c^2")

M_A = simplify_expr(c**2 * flux_A / (8 * pi * G))
require_zero("A-sector recovered mass", M_A - M)
checks.append("A-sector flux recovers exactly one mass M")

Q = sp.symbols("Q")
A_flux_solution = 1 - Q / (4 * pi * r)
flux_solution = simplify_expr(4 * pi * r**2 * sp.diff(A_flux_solution, r))
require_zero("generic inverse-radius flux", flux_solution - Q)
checks.append("1/r exterior coefficient is fixed by boundary flux")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 1: A-Sector Mass Flux Normalization

## Purpose

This proof isolates the ordinary reduced mass channel already present in the
archive:

```text
Delta_areal A = (8*pi*G/c^2) rho.
```

It verifies that the exterior A-sector solution carries exactly one ordinary
mass parameter through boundary flux.

## Validated Checks

{validation_bullets}

## Exterior Solution

Use:

```text
A_ext(r) = 1 - 2GM/(c^2 r).
```

SymPy verifies:

```text
(1/r^2) d/dr [r^2 A_ext'] = 0
```

for `r > R`, so the exterior is source-free.

## Flux Normalization

The A-sector flux is:

```text
F_A = 4*pi*r^2 A_ext'
    = 8*pi*G*M/c^2.
```

Therefore the reduced mass ledger:

```text
M_A = (c^2/(8*pi*G)) F_A
```

returns:

```text
M_A = M.
```

## Gate Interpretation

This is the ordinary mass channel. Any later residual, projection, trace, or
boundary object must not add an independent copy of this same mass unless a new
source-routing theorem explicitly allows it.
"""

out = Path(__file__).with_name("1_a_sector_mass_flux_normalization.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("A-sector mass flux normalization passed.")
print(f"Wrote {out.resolve()}")
