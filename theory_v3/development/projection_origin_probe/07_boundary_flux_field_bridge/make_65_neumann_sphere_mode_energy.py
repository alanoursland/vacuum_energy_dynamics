#!/usr/bin/env python3
"""
make_65_neumann_sphere_mode_energy.py

Validate fixed-flux spherical harmonic mode energy for the exterior sphere.

Assume unit-sphere angular normalization:

    integral_{S^2} Y_lm^2 dOmega = 1.

For boundary flux density amplitude q_l:

    q_l = ((l+1)/R) U_l

and:

    E_red[q_l] = -R^3 q_l^2 / (2(l+1)).

Output:
    65_neumann_sphere_mode_energy.md
"""

from pathlib import Path
import sympy as sp


R, q, Q = sp.symbols("R q Q", positive=True)
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
U_from_q = q / lambda_l

# With angular normalization int Y^2 dOmega=1, physical boundary area measure
# contributes R^2.  Energy = 1/2 int U q dA.
stored_energy = sp.simplify(sp.Rational(1, 2) * R**2 * U_from_q * q)
reduced_action = -stored_energy

require_equal("Neumann mode boundary potential amplitude", U_from_q, R * q / (l + 1))
checks.append("Neumann mode boundary potential amplitude")
require_equal("Neumann mode stored energy", stored_energy, R**3 * q**2 / (2 * (l + 1)))
checks.append("Neumann mode stored energy")
require_equal("Neumann mode reduced action", reduced_action, -R**3 * q**2 / (2 * (l + 1)))
checks.append("Neumann mode reduced action")

# Monopole check against total flux Q.  For Y_00=1/sqrt(4*pi),
# q_density amplitude q = Q/(R^2 sqrt(4*pi)).
q_mono = Q / (R**2 * sp.sqrt(4 * pi))
mono_energy = stored_energy.subs({l: 0, q: q_mono})
require_equal("monopole fixed-flux energy", mono_energy, Q**2 / (8 * pi * R))
checks.append("monopole fixed-flux energy")

mono_reduced = reduced_action.subs({l: 0, q: q_mono})
require_equal("monopole fixed-flux reduced action", mono_reduced, -Q**2 / (8 * pi * R))
checks.append("monopole fixed-flux reduced action")

for ell in range(0, 8):
    require_equal(
        f"explicit Neumann mode energy l={ell}",
        stored_energy.subs(l, ell),
        R**3 * q**2 / (2 * (ell + 1)),
    )

checks.append("explicit Neumann mode energies for l=0..7")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 65: Neumann Sphere Mode Energy

## Purpose

This report validates fixed-flux spherical harmonic mode bookkeeping for the
exterior sphere.

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

Therefore:

```text
U_l = R q_l/(l+1).
```

## Stored Energy

Using:

```text
E = 1/2 integral_boundary U q dA,
```

and `dA=R^2 dOmega`, the mode energy is:

```text
E_l = R^3 q_l^2/[2(l+1)].
```

## Reduced Source Action

The source-coupled reduced action has the opposite sign:

```text
E_red,l = -R^3 q_l^2/[2(l+1)].
```

## Monopole Check

For total monopole flux `Q`:

```text
q_0 = Q/(R^2 sqrt(4*pi)).
```

The stored energy becomes:

```text
E_0 = Q^2/(8*pi*R),
```

matching the earlier radial proof.
"""

out = Path(__file__).with_name("65_neumann_sphere_mode_energy.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
