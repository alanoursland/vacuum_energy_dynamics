#!/usr/bin/env python3
"""
make_95_boundary_flux_in_de_donder_variables.py

Validate boundary flux normalization in de Donder / trace-reversed variables.

Output:
    95_boundary_flux_in_de_donder_variables.md
"""

from pathlib import Path
import sympy as sp


r, Gconst, M = sp.symbols("r G M", positive=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

u = Gconst * M / r
h00 = 2 * u
bar_h00 = 4 * u

Q_u = -4 * pi * r**2 * sp.diff(u, r)
Q_h00 = -4 * pi * r**2 * sp.diff(h00, r)
Q_bar = -4 * pi * r**2 * sp.diff(bar_h00, r)

require_equal("scalar bridge flux", Q_u, 4 * pi * Gconst * M)
checks.append("scalar bridge flux")
require_equal("h00 flux", Q_h00, 8 * pi * Gconst * M)
checks.append("h00 flux")
require_equal("bar_h00 flux", Q_bar, 16 * pi * Gconst * M)
checks.append("bar_h00 flux")

require_equal("h00 flux relative to scalar", Q_h00, 2 * Q_u)
checks.append("h00 flux relative to scalar")
require_equal("bar_h00 flux relative to scalar", Q_bar, 4 * Q_u)
checks.append("bar_h00 flux relative to scalar")

require_equal("mass from scalar flux", Q_u / (4 * pi * Gconst), M)
checks.append("mass from scalar flux")
require_equal("mass from h00 flux", Q_h00 / (8 * pi * Gconst), M)
checks.append("mass from h00 flux")
require_equal("mass from bar_h00 flux", Q_bar / (16 * pi * Gconst), M)
checks.append("mass from bar_h00 flux")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 95: Boundary Flux in de Donder Variables

## Purpose

This report validates the boundary-flux normalization across the scalar,
metric, and trace-reversed weak-field variables.

## Validated Checks

{validation_bullets}

## Variable Relations

For a positive mass source:

```text
u = GM/r
h_00 = 2u
bar h_00 = 4u.
```

## Fluxes

SymPy verifies:

```text
Q_u       = 4*pi*G M
Q_h00     = 8*pi*G M
Q_bar_h00 = 16*pi*G M.
```

Thus:

```text
M = Q_u/(4*pi*G)
M = Q_h00/(8*pi*G)
M = Q_bar_h00/(16*pi*G).
```

## Interpretation

The same mass is represented by different boundary flux normalizations
depending on the chosen weak-field variable. The scalar bridge variable is the
quarter-normalized trace-reversed variable:

```text
u = bar h_00 / 4.
```
"""

out = Path(__file__).with_name("95_boundary_flux_in_de_donder_variables.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
