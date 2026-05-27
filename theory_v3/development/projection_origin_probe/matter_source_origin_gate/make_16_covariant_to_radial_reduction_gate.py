#!/usr/bin/env python3
"""
make_16_covariant_to_radial_reduction_gate.py

Validate the radial reduction used by the covariant weak-field source lift.

Output:
    16_covariant_to_radial_reduction_gate.md
"""

from pathlib import Path
import sympy as sp


r, G, c, rho = sp.symbols("r G c rho", positive=True)
Phi = sp.Function("Phi")(r)
A = sp.Function("A")(r)
C0, C1 = sp.symbols("C0 C1")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

radial_lap_A = simplify_expr(sp.diff(A, r, 2) + 2 * sp.diff(A, r) / r)
div_form_A = simplify_expr((1 / r**2) * sp.diff(r**2 * sp.diff(A, r), r))
require_zero("radial Laplacian divergence form", radial_lap_A - div_form_A)
checks.append("radial Laplacian equals (1/r^2)(r^2 f')'")

A_from_phi = 1 + 2 * Phi / c**2
lap_A_from_phi = simplify_expr(
    (sp.diff(A_from_phi, r, 2) + 2 * sp.diff(A_from_phi, r) / r)
)
lap_phi = sp.diff(Phi, r, 2) + 2 * sp.diff(Phi, r) / r
require_zero("A-Phi radial source scaling", lap_A_from_phi - 2 * lap_phi / c**2)
checks.append("A=1+2Phi/c^2 scales the radial source by 2/c^2")

source_A = simplify_expr((2 / c**2) * 4 * sp.pi * G * rho)
require_zero("Newtonian Poisson to A-sector", source_A - 8 * sp.pi * G * rho / c**2)
checks.append("Delta Phi=4*pi*G*rho gives Delta A=8*pi*G*rho/c^2")

exterior = C0 + C1 / r
lap_exterior = simplify_expr(sp.diff(exterior, r, 2) + 2 * sp.diff(exterior, r) / r)
require_zero("source-free radial exterior", lap_exterior)
checks.append("C0+C1/r is the source-free radial exterior")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 16: Covariant To Radial Reduction Gate

## Purpose

This proof records the radial reduction used when the weak covariant matter
coupling is compared to the reduced A-sector source law.

## Validated Checks

{validation_bullets}

## Radial Laplacian

For a radial field:

```text
Delta f = f'' + 2f'/r
        = (1/r^2) d/dr [r^2 f'].
```

## A-Sector Scaling

With:

```text
A = 1 + 2 Phi/c^2,
```

one has:

```text
Delta A = 2 Delta Phi/c^2.
```

Therefore:

```text
Delta Phi = 4*pi*G rho
```

implies:

```text
Delta A = 8*pi*G rho/c^2.
```

## Exterior

The source-free radial exterior is:

```text
C0 + C1/r.
```

That is the origin of the flux ledger used in the reduced proof chain.
"""

out = Path(__file__).with_name("16_covariant_to_radial_reduction_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Covariant-to-radial reduction gate passed.")
print(f"Wrote {out.resolve()}")
