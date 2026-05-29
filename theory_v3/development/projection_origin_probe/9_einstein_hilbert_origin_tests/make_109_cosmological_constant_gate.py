#!/usr/bin/env python3
"""
make_109_cosmological_constant_gate.py

Validate the Newtonian-sector role of a cosmological constant term.

Output:
    109_cosmological_constant_gate.md
"""

from pathlib import Path
import sympy as sp


r, Gconst, M, Lambda = sp.symbols("r G M Lambda", positive=True)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def radial_laplacian(expr):
    return simplify_expr((1 / r**2) * sp.diff(r**2 * sp.diff(expr, r), r))


checks = []

Phi_mass = -Gconst * M / r
Phi_lambda = -Lambda * r**2 / 6
Phi_total = Phi_mass + Phi_lambda

require_equal("off-source mass potential is harmonic", radial_laplacian(Phi_mass), 0)
checks.append("off-source mass potential is harmonic")

require_equal("cosmological potential solves modified vacuum Poisson equation", radial_laplacian(Phi_lambda), -Lambda)
checks.append("cosmological potential solves modified vacuum Poisson equation")

require_equal("combined exterior equation", radial_laplacian(Phi_total), -Lambda)
checks.append("combined exterior equation")

acceleration = -sp.diff(Phi_total, r)
require_equal("radial acceleration with Lambda", acceleration, -Gconst * M / r**2 + Lambda * r / 3)
checks.append("radial acceleration with Lambda")

require_equal("scalar bridge recovered at Lambda equals zero", radial_laplacian(Phi_total.subs(Lambda, 0)), 0)
checks.append("scalar bridge recovered at Lambda equals zero")

lambda_limit = sp.limit(Phi_lambda, r, sp.oo)
if lambda_limit != -sp.oo:
    raise AssertionError(f"positive Lambda potential limit failed: {lambda_limit}")
checks.append("positive Lambda potential is not asymptotically flat")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 109: Cosmological Constant Gate

## Purpose

This report tests the Newtonian-sector effect of the allowed Lovelock `p=0`
term.

The cosmological constant is allowed by the Lovelock gate, but it is not part
of the asymptotically flat scalar boundary-flux bridge unless it is set to
zero or treated as a separate background branch.

## Validated Checks

{validation_bullets}

## Radial Potentials

For the mass term:

```text
Phi_M = -GM/r,
```

SymPy verifies off source:

```text
Delta Phi_M = 0.
```

For the cosmological term:

```text
Phi_Lambda = -Lambda r^2/6,
```

SymPy verifies:

```text
Delta Phi_Lambda = -Lambda.
```

So:

```text
Phi = -GM/r - Lambda r^2/6
```

satisfies:

```text
Delta Phi = -Lambda
```

outside localized matter.

## Acceleration

The radial acceleration is:

```text
-dPhi/dr = -GM/r^2 + Lambda r/3.
```

Positive `Lambda` adds an outward term and destroys asymptotic flatness.

## Interpretation

The cosmological term is a legitimate four-dimensional Lovelock option, but
it is a separate vacuum-background parameter. The scalar boundary-flux bridge
selects the `Lambda=0` asymptotically flat sector unless a nonzero vacuum
curvature background is independently supplied.
"""

out = Path(__file__).with_name("109_cosmological_constant_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
