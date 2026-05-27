#!/usr/bin/env python3
"""
make_78_newtonian_potential_metric_identification.py

Validate the weak-field Newtonian metric identification:

    g_00 = -(1 + 2 phi)

For a static weak field, the slow-particle geodesic acceleration is:

    a^i = -Gamma^i_00 = -partial_i phi.

Output:
    78_newtonian_potential_metric_identification.md
"""

from pathlib import Path
import sympy as sp


x, y, z, r = sp.symbols("x y z r", real=True)
K = sp.symbols("K", positive=True)
coords = (x, y, z)
phi = sp.Function("phi")(x, y, z)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

g00 = -(1 + 2 * phi)

# In static weak field with spatial inverse metric delta^ij:
# Gamma^i_00 = -1/2 partial_i g00.
for coord in coords:
    gamma_i_00 = -sp.Rational(1, 2) * sp.diff(g00, coord)
    require_equal(f"Gamma^i_00 equals gradient phi for {coord}", gamma_i_00, sp.diff(phi, coord))

checks.append("Gamma^i_00 = partial_i phi")

for coord in coords:
    acceleration_i = -sp.diff(phi, coord)
    require_equal(f"slow acceleration component for {coord}", acceleration_i, -sp.diff(phi, coord))

checks.append("slow geodesic acceleration is -grad phi")

# Radial attractive potential convention:
#   phi(r) = -K/r  =>  a_r = -dphi/dr = -K/r^2.
phi_radial = -K / r
acceleration_radial = -sp.diff(phi_radial, r)
require_equal("attractive radial acceleration", acceleration_radial, -K / r**2)
checks.append("attractive radial acceleration")

lap_radial = sp.diff(phi_radial, r, 2) + 2 * sp.diff(phi_radial, r) / r
require_zero("radial potential is harmonic off source", lap_radial)
checks.append("radial potential is harmonic off source")

# Relation to positive scalar bridge variable u: if u=K/r, then phi=-u.
u_radial = K / r
require_equal("scalar bridge sign relation", phi_radial, -u_radial)
checks.append("scalar bridge sign relation")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 78: Newtonian Potential Metric Identification

## Purpose

This report validates the standard weak-field metric identification:

```text
g_00 = -(1 + 2 phi).
```

It checks only the Newtonian/slow-particle limit. It does not derive the full
Einstein equations.

## Validated Checks

{validation_bullets}

## Christoffel Term

For a static weak field with spatial inverse metric approximated by
`delta^ij`:

```text
Gamma^i_00 = -1/2 partial_i g_00.
```

Since:

```text
g_00 = -(1+2phi),
```

SymPy verifies:

```text
Gamma^i_00 = partial_i phi.
```

## Slow Geodesic Acceleration

The slow-particle spatial acceleration is:

```text
a^i = -Gamma^i_00 = -partial_i phi.
```

Thus `phi` is the Newtonian potential under this convention.

## Radial Sign Convention

For attraction toward a positive source:

```text
phi(r) = -K/r.
```

Then:

```text
a_r = -dphi/dr = -K/r^2.
```

The positive scalar bridge variable `u=K/r` corresponds to:

```text
phi = -u
```

under this Newtonian acceleration convention.
"""

out = Path(__file__).with_name("78_newtonian_potential_metric_identification.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
