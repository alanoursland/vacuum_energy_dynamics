#!/usr/bin/env python3
"""
make_94_static_green_solution_for_bar_h00.py

Validate the static Green solution for the trace-reversed metric component:

    -1/2 Delta bar_h_00 = 8*pi*G rho

For a point mass M:

    bar_h_00 = 4GM/r.

Output:
    94_static_green_solution_for_bar_h00.md
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

bar_h00 = 4 * Gconst * M / r
lap_bar = sp.diff(bar_h00, r, 2) + 2 * sp.diff(bar_h00, r) / r
require_zero("bar_h00 harmonic off source", lap_bar)
checks.append("bar_h00 harmonic off source")

bar_flux = -4 * pi * r**2 * sp.diff(bar_h00, r)
require_equal("bar_h00 boundary flux", bar_flux, 16 * pi * Gconst * M)
checks.append("bar_h00 boundary flux")

mass_from_bar_flux = bar_flux / (16 * pi * Gconst)
require_equal("mass from bar_h00 flux", mass_from_bar_flux, M)
checks.append("mass from bar_h00 flux")

Phi = -Gconst * M / r
u = -Phi
h00 = -2 * Phi
require_equal("bar_h00 relation to scalar bridge", bar_h00, 4 * u)
checks.append("bar_h00 relation to scalar bridge")
require_equal("h00 relation to scalar bridge", h00, 2 * u)
checks.append("h00 relation to scalar bridge")

# Static de Donder field equation normalization outside source.
operator_value = -sp.Rational(1, 2) * lap_bar
require_zero("static de Donder operator off source", operator_value)
checks.append("static de Donder operator off source")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 94: Static Green Solution for `bar h_00`

## Purpose

This report validates the static Green solution for the trace-reversed metric
component in the Newtonian sector.

## Validated Checks

{validation_bullets}

## de Donder Equation

In de Donder gauge:

```text
G_ab = -1/2 box bar h_ab.
```

For a static source:

```text
-1/2 Delta bar h_00 = 8*pi*G rho.
```

For a point mass `M`, the exterior solution is:

```text
bar h_00 = 4GM/r.
```

## Boundary Flux

SymPy verifies:

```text
-integral partial_n bar h_00 dA = 16*pi*G M.
```

Therefore:

```text
M = [-integral partial_n bar h_00 dA]/(16*pi*G).
```

## Scalar Bridge Relation

With:

```text
u = GM/r,
```

one has:

```text
h_00 = 2u
bar h_00 = 4u.
```
"""

out = Path(__file__).with_name("94_static_green_solution_for_bar_h00.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
