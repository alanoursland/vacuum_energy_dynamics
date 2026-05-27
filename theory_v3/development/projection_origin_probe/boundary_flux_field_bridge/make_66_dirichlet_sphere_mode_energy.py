#!/usr/bin/env python3
"""
make_66_dirichlet_sphere_mode_energy.py

Validate fixed-potential spherical harmonic mode energy for the exterior sphere.

Assume unit-sphere angular normalization:

    integral_{S^2} Y_lm^2 dOmega = 1.

For boundary potential amplitude U_l:

    q_l = ((l+1)/R) U_l
    E_l = (l+1) R U_l^2 / 2.

Output:
    66_dirichlet_sphere_mode_energy.md
"""

from pathlib import Path
import sympy as sp


R, U, C = sp.symbols("R U C", positive=True)
l = sp.symbols("l", integer=True, nonnegative=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

lambda_l = (l + 1) / R
q_from_U = lambda_l * U
stored_energy = sp.simplify(sp.Rational(1, 2) * R**2 * U * q_from_U)

require_equal("Dirichlet mode flux amplitude", q_from_U, (l + 1) * U / R)
checks.append("Dirichlet mode flux amplitude")
require_equal("Dirichlet mode stored energy", stored_energy, (l + 1) * R * U**2 / 2)
checks.append("Dirichlet mode stored energy")

# Monopole check: a constant boundary potential C corresponds to
# U_0 = C sqrt(4*pi), since Y_00=1/sqrt(4*pi).
U_mono = C * sp.sqrt(4 * pi)
mono_flux_density_amp = q_from_U.subs({l: 0, U: U_mono})
total_flux = sp.simplify(mono_flux_density_amp * R**2 * sp.sqrt(4 * pi))
mono_energy = stored_energy.subs({l: 0, U: U_mono})

require_equal("constant-potential total flux", total_flux, 4 * pi * R * C)
checks.append("constant-potential total flux")
require_equal("constant-potential sphere energy", mono_energy, 2 * pi * R * C**2)
checks.append("constant-potential sphere energy")

for ell in range(0, 8):
    require_equal(
        f"explicit Dirichlet mode energy l={ell}",
        stored_energy.subs(l, ell),
        (ell + 1) * R * U**2 / 2,
    )

checks.append("explicit Dirichlet mode energies for l=0..7")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 66: Dirichlet Sphere Mode Energy

## Purpose

This report validates fixed-potential spherical harmonic mode bookkeeping for
the exterior sphere.

Assume:

```text
integral_S2 Y_lm^2 dOmega = 1.
```

## Validated Checks

{validation_bullets}

## Mode Relation

From proof `64`:

```text
q_l = ((l+1)/R) U_l.
```

## Stored Energy

Using:

```text
E = 1/2 integral_boundary U q dA,
```

and `dA=R^2 dOmega`, the mode energy is:

```text
E_l = (l+1) R U_l^2/2.
```

## Constant Potential Check

For constant boundary potential `C`, the normalized monopole amplitude is:

```text
U_0 = C sqrt(4*pi).
```

Then:

```text
Q = 4*pi R C
E = 2*pi R C^2,
```

matching the isolated fixed-potential sphere result.
"""

out = Path(__file__).with_name("66_dirichlet_sphere_mode_energy.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
