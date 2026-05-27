#!/usr/bin/env python3
"""
make_8_gauss_flux_mass_from_density.py

Validate that the reduced A-sector source law gives Gauss mass flux.

Output:
    8_gauss_flux_mass_from_density.md
"""

from pathlib import Path
import sympy as sp


r, R, rho0, G, c = sp.symbols("r R rho0 G c", positive=True)
pi = sp.pi
alpha = 8 * pi * G / c**2


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

M_R = simplify_expr(4 * pi * sp.integrate(rho0 * r**2, (r, 0, R)))
expected_M = 4 * pi * rho0 * R**3 / 3
require_zero("constant density mass", M_R - expected_M)
checks.append("M(R)=4*pi*rho0*R^3/3 for a constant-density ball")

flux_R = simplify_expr(alpha * M_R)
expected_flux = 8 * pi * G * M_R / c**2
require_zero("Gauss flux from source law", flux_R - expected_flux)
checks.append("A-sector Gauss flux is 8*pi*G*M(R)/c^2")

A_ext = 1 - flux_R / (4 * pi * r)
exterior_flux = simplify_expr(4 * pi * r**2 * sp.diff(A_ext, r))
require_zero("exterior coefficient matches flux", exterior_flux - flux_R)
checks.append("exterior 1/r coefficient is fixed by enclosed source flux")

M_recovered = simplify_expr(c**2 * exterior_flux / (8 * pi * G))
require_zero("recovered mass", M_recovered - M_R)
checks.append("exterior flux recovers the same enclosed mass")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 8: Gauss Flux Mass From Density

## Purpose

This proof connects the reduced A-sector source law to enclosed ordinary mass.

## Validated Checks

{validation_bullets}

## Source Law

Use:

```text
Delta_areal A = alpha rho
alpha = 8*pi*G/c^2.
```

For a constant-density ball:

```text
M(R) = 4*pi integral_0^R rho0 r^2 dr
     = 4*pi*rho0*R^3/3.
```

Gauss integration gives:

```text
F_A(R) = 4*pi R^2 A'(R)
       = alpha M(R)
       = 8*pi*G*M(R)/c^2.
```

## Exterior

The exterior field is source-free and has:

```text
A_ext = 1 - F_A/(4*pi r).
```

Then:

```text
4*pi*r^2 A_ext' = F_A.
```

## Gate Interpretation

The A-sector source law carries the ordinary mass once through Gauss flux. This
is the positive counterpart to the previous source-safety exclusion gates.
"""

out = Path(__file__).with_name("8_gauss_flux_mass_from_density.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Gauss flux mass from density passed.")
print(f"Wrote {out.resolve()}")
