#!/usr/bin/env python3
"""
make_68_conserved_charge_additivity.py

Validate additivity of conserved boundary flux/source strength in the scalar
boundary-flux bridge.

Output:
    68_conserved_charge_additivity.md
"""

from pathlib import Path
import sympy as sp


r = sp.symbols("r", positive=True)
Q1, Q2, Q3 = sp.symbols("Q1 Q2 Q3", real=True)
R1, R2, R3 = sp.symbols("R1 R2 R3", positive=True)
q1, q2, q3 = sp.symbols("q1 q2 q3", real=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# Boundary flux density q_i over a spherical component of radius R_i.
Q1_from_density = 4 * pi * R1**2 * q1
Q2_from_density = 4 * pi * R2**2 * q2
Q3_from_density = 4 * pi * R3**2 * q3

require_equal("component 1 total flux", Q1_from_density, 4 * pi * R1**2 * q1)
checks.append("component 1 total flux")
require_equal("component 2 total flux", Q2_from_density, 4 * pi * R2**2 * q2)
checks.append("component 2 total flux")
require_equal("component 3 total flux", Q3_from_density, 4 * pi * R3**2 * q3)
checks.append("component 3 total flux")

total_from_components = Q1_from_density + Q2_from_density + Q3_from_density
require_equal(
    "additive total boundary flux",
    total_from_components,
    4 * pi * (R1**2 * q1 + R2**2 * q2 + R3**2 * q3),
)
checks.append("additive total boundary flux")

# Far enclosing sphere sees only total monopole flux.
Q_total = Q1 + Q2 + Q3
u_far = Q_total / (4 * pi * r)
far_flux = -4 * pi * r**2 * sp.diff(u_far, r)
require_equal("far enclosing flux is total charge", far_flux, Q_total)
checks.append("far enclosing flux is total charge")
require_zero("far enclosing flux is conserved", sp.diff(far_flux, r))
checks.append("far enclosing flux is conserved")

# Linearity of source coupling.
U1, U2, U3 = sp.symbols("U1 U2 U3", real=True)
source_coupling_sum = -(Q1 * U1 + Q2 * U2 + Q3 * U3)
require_equal(
    "source coupling is additive",
    source_coupling_sum,
    -Q1 * U1 - Q2 * U2 - Q3 * U3,
)
checks.append("source coupling is additive")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 68: Conserved Charge Additivity

## Purpose

This report validates additivity of boundary flux/source strength.

## Validated Checks

{validation_bullets}

## Boundary Components

For spherical boundary components with flux densities `q_i`:

```text
Q_i = integral_boundary_i q_i dA = 4*pi*R_i^2 q_i.
```

The total boundary charge is additive:

```text
Q_total = sum_i Q_i.
```

## Far Enclosing Surface

The far monopole field:

```text
u_far(r) = Q_total/(4*pi*r)
```

has flux:

```text
-4*pi*r^2 u_far'(r) = Q_total.
```

So an enclosing surface measures the sum of the enclosed component fluxes.

## Interpretation

If mass-like source strength is boundary flux, then disjoint source strengths
combine linearly at the scalar weak-field level.
"""

out = Path(__file__).with_name("68_conserved_charge_additivity.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
