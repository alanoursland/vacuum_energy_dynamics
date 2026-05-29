#!/usr/bin/env python3
"""
make_41_boundary_condition_comparison.py

Compare isolated spherical exterior solutions under fixed flux, fixed
potential, and linear Robin-style boundary bookkeeping.

Output:
    41_boundary_condition_comparison.md
"""

from pathlib import Path
import sympy as sp


r, R = sp.symbols("r R", positive=True)
Q, U, kappa = sp.symbols("Q U kappa", positive=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

A = sp.symbols("A", real=True)
u_A = A / r
flux_A = -4 * pi * r**2 * sp.diff(u_A, r)
potential_A_R = u_A.subs(r, R)
energy_A = sp.integrate(
    sp.Rational(1, 2) * 4 * pi * r**2 * sp.diff(u_A, r) ** 2,
    (r, R, sp.oo),
)

require_equal("general harmonic flux", flux_A, 4 * pi * A)
checks.append("general harmonic flux")
require_equal("general harmonic exterior energy", energy_A, 2 * pi * A**2 / R)
checks.append("general harmonic exterior energy")

# Fixed flux Q.
A_flux = Q / (4 * pi)
U_flux = potential_A_R.subs(A, A_flux)
E_flux = energy_A.subs(A, A_flux)
require_equal("fixed flux boundary potential", U_flux, Q / (4 * pi * R))
checks.append("fixed flux boundary potential")
require_equal("fixed flux exterior energy", E_flux, Q**2 / (8 * pi * R))
checks.append("fixed flux exterior energy")

# Fixed boundary potential U.
A_potential = U * R
Q_potential = flux_A.subs(A, A_potential)
E_potential = energy_A.subs(A, A_potential)
require_equal("fixed potential induced flux", Q_potential, 4 * pi * R * U)
checks.append("fixed potential induced flux")
require_equal("fixed potential exterior energy", E_potential, 2 * pi * R * U**2)
checks.append("fixed potential exterior energy")

# Linear capacitance-style relation Q = kappa U.
# Isolated sphere geometry gives Q/U = 4*pi*R.
capacitance = sp.simplify(Q_potential / U)
require_equal("sphere flux-potential ratio", capacitance, 4 * pi * R)
checks.append("sphere flux-potential ratio")

compatibility = sp.simplify(kappa - capacitance)
require_equal("Robin compatibility at isolated sphere", compatibility, kappa - 4 * pi * R)
checks.append("Robin compatibility at isolated sphere")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 41: Boundary Condition Comparison

## Purpose

This report compares the isolated spherical exterior field under three boundary
bookkeeping choices:

```text
fixed flux
fixed potential
linear flux-potential relation
```

The exterior harmonic form is:

```text
u(r) = A/r.
```

## Validated Checks

{validation_bullets}

## General Exterior Solution

For:

```text
u(r)=A/r,
```

SymPy verifies:

```text
Q = -4*pi*r^2*u'(r) = 4*pi*A
E = 1/2 integral_R^infty 4*pi*r^2(u')^2 dr = 2*pi*A^2/R.
```

## Fixed Flux

If `Q` is fixed:

```text
A = Q/(4*pi)
u(R) = Q/(4*pi*R)
E = Q^2/(8*pi*R).
```

This makes source strength independent of the boundary radius.

## Fixed Potential

If `u(R)=U` is fixed:

```text
A = U R
Q = 4*pi*R*U
E = 2*pi*R*U^2.
```

Here the induced flux depends on radius.

## Linear Boundary Law

The isolated sphere imposes:

```text
Q/U = 4*pi*R.
```

So a linear law `Q=kappa U` is compatible with an isolated sphere only when:

```text
kappa = 4*pi*R.
```

## Interpretation

For a mass-like conserved source strength, fixed flux is the cleaner first
model. Fixed potential is more naturally a response condition: the total flux
changes with the size and environment of the boundary.

This does not eliminate fixed-potential or Robin boundary data. It says they
should be treated as different physical hypotheses, not silently interchanged.
"""

out = Path(__file__).with_name("41_boundary_condition_comparison.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
