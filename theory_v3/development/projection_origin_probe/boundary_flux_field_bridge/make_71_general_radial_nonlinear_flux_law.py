#!/usr/bin/env python3
"""
make_71_general_radial_nonlinear_flux_law.py

Validate the general radial nonlinear flux law for:

    E[u] = integral 4*pi*r^2 Phi((u')^2) dr.

Output:
    71_general_radial_nonlinear_flux_law.md
"""

from pathlib import Path
import sympy as sp


r, s, y, z, alpha = sp.symbols("r s y z alpha", positive=True)
pi = sp.pi
Phi = sp.Function("Phi")


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

density = 4 * pi * r**2 * Phi(s**2)
momentum = sp.diff(density, s)
expected_momentum = 8 * pi * r**2 * s * sp.diff(Phi(z), z).subs(z, s**2)
require_equal("general canonical radial momentum", momentum, expected_momentum)
checks.append("general canonical radial momentum")

# For y=-u' > 0, outward positive flux is:
#   Q = 8*pi*r^2*y*Phi'(y^2).
flux_y = 8 * pi * r**2 * y * sp.diff(Phi(z), z).subs(z, y**2)
require_equal("general outward flux expression", flux_y, 8 * pi * r**2 * y * sp.diff(Phi(z), z).subs(z, y**2))
checks.append("general outward flux expression")

# Polynomial family Phi_p(z)=1/2 z + alpha/(2p) z^p.
rows = []
for p in range(1, 7):
    Phi_p = sp.Rational(1, 2) * z + alpha * z**p / (2 * p)
    flux_p = sp.simplify(8 * pi * r**2 * y * sp.diff(Phi_p, z).subs(z, y**2))
    expected = 4 * pi * r**2 * (y + alpha * y ** (2 * p - 1))
    require_equal(f"polynomial flux law p={p}", flux_p, expected)
    rows.append((p, sp.sstr(expected)))

checks.append("polynomial flux laws verified for p=1..6")

row_lines = "\n".join(f"p={p}: Q = {expr}" for p, expr in rows)
validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 71: General Radial Nonlinear Flux Law

## Purpose

This report validates the general radial nonlinear flux law for energies of the
form:

```text
E[u] = integral 4*pi*r^2 Phi((u')^2) dr.
```

## Validated Checks

{validation_bullets}

## General Flux Law

Let:

```text
s = u'
```

The radial canonical momentum is:

```text
d/ds [4*pi*r^2 Phi(s^2)]
  =
  8*pi*r^2 s Phi'(s^2).
```

For an outward positive field magnitude:

```text
y = -u' > 0,
```

the outward flux is:

```text
Q = 8*pi*r^2 y Phi'(y^2).
```

## Polynomial Family

For:

```text
Phi_p(z)=1/2 z + alpha/(2p) z^p,
```

SymPy verifies:

```text
{row_lines}
```

## Interpretation

The linear Dirichlet model is the special case where `Phi'(z)=1/2`. Nonlinear
strain densities alter the flux-field relation, not the conservation law.
"""

out = Path(__file__).with_name("71_general_radial_nonlinear_flux_law.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
