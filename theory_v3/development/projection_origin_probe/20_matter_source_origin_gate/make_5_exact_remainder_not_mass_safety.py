#!/usr/bin/env python3
"""
make_5_exact_remainder_not_mass_safety.py

Validate that flat exactness of a total derivative is not enough to prove
weighted/geometric mass safety.

Output:
    5_exact_remainder_not_mass_safety.md
"""

from pathlib import Path
import sympy as sp


y = sp.symbols("y")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_nonzero(label, expr):
    result = simplify_expr(expr)
    if result == 0:
        raise AssertionError(f"{label} unexpectedly vanished")
    return result


checks = []

Xi = (1 - y**2) ** 3
window = (1 - y**2) ** 2
J = simplify_expr(window * sp.diff(Xi, y))
rho = simplify_expr(sp.diff(J, y))

flat_charge = simplify_expr(sp.integrate(rho, (y, -1, 1)))
require_zero("flat exactness charge", flat_charge)
checks.append("rho=dJ/dy with endpoint-vanishing J has zero flat integral")

rho_at_origin = simplify_expr(rho.subs(y, 0))
require_zero("local rho value", rho_at_origin + 6)
checks.append("flat exactness does not imply local inertness")

y2_weighted_charge = simplify_expr(sp.integrate(y**2 * rho, (y, -1, 1)))
nonzero_y2 = require_nonzero("y^2 weighted charge", y2_weighted_charge)
checks.append("flat exactness does not imply weighted neutrality")

window_weighted_charge = simplify_expr(sp.integrate((1 - y**2) * rho, (y, -1, 1)))
nonzero_window = require_nonzero("window weighted charge", window_weighted_charge)
checks.append("flat exactness does not imply geometric-window neutrality")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 5: Exact Remainder Is Not Mass Safety

## Purpose

This proof records an archive lesson that matters for source origin:

```text
flat exactness is not the same as physical source neutrality.
```

An exact derivative can have zero total integral while still having nonzero
local value and nonzero weighted/geometric moments.

## Validated Checks

{validation_bullets}

## Setup

Use the reduced exactness witness:

```text
Xi = (1-y^2)^3
window = (1-y^2)^2
J = window * Xi'
rho = J'.
```

Because `J` vanishes at both endpoints:

```text
integral_-1^1 rho dy = J(1)-J(-1) = 0.
```

SymPy verifies the flat charge vanishes.

## Failure Of Local Inertness

At the origin:

```text
rho(0) = -6.
```

So exactness does not mean pointwise silence.

## Failure Of Weighted Neutrality

Weighted witnesses are nonzero:

```text
integral_-1^1 y^2 rho dy = {nonzero_y2}
integral_-1^1 (1-y^2) rho dy = {nonzero_window}
```

## Gate Interpretation

An exact residual can be algebraically useful without being a safe matter
source or a safe neutral correction. To promote such an object, the theory
must prove the relevant weighted, boundary, and far-zone neutrality conditions,
not just flat exactness.
"""

out = Path(__file__).with_name("5_exact_remainder_not_mass_safety.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Exact remainder mass-safety warning passed.")
print(f"Wrote {out.resolve()}")
