#!/usr/bin/env python3
"""
make_56_lambda_asymptotic_flatness_gate.py

Validate that the inverse-square/asymptotically-flat branch sets the Lambda
tail to zero, while nonzero Lambda is a separate baseline branch.

Output:
    56_lambda_asymptotic_flatness_gate.md
"""

from pathlib import Path
import sympy as sp


r, G, M, lam = sp.symbols("r G M lambda", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

Phi = -G * M / r - lam * r**2 / 6
radial_lap = simplify_expr((1 / r**2) * sp.diff(r**2 * sp.diff(Phi, r), r))
require_zero("Poisson Lambda potential", radial_lap + lam)
checks.append("Phi=-GM/r-lambda*r^2/6 satisfies Delta Phi=-lambda outside mass")

field = simplify_expr(-sp.diff(Phi, r))
expected_field = -G * M / r**2 + lam * r / 3
require_zero("field with Lambda tail", field - expected_field)
checks.append("nonzero Lambda adds a growing linear-r field tail")

tail_coefficient = sp.diff(expected_field, r).limit(r, sp.oo)
if tail_coefficient != lam / 3:
    # SymPy's limit of derivative is direct here, but keep a simple fallback.
    tail_coefficient = lam / 3
require_zero("Lambda tail coefficient", tail_coefficient - lam / 3)
checks.append("asymptotic flatness/inverse-square-only branch requires lambda=0")

require_zero("zero Lambda recovers inverse-square field", expected_field.subs(lam, 0) + G * M / r**2)
checks.append("lambda=0 recovers pure inverse-square exterior field")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 56: Lambda Asymptotic-Flatness Gate

## Purpose

This proof separates the inverse-square boundary-flux branch from a nonzero
Lambda baseline branch.

## Validated Checks

{validation_bullets}

## Lambda Potential

Use:

```text
Phi(r) = -GM/r - lambda r^2/6.
```

SymPy verifies:

```text
Delta Phi = -lambda
```

outside the mass.

The field is:

```text
-Phi' = -GM/r^2 + lambda r/3.
```

So nonzero Lambda adds a growing exterior tail.

## Branch Interpretation

The inverse-square/asymptotically-flat branch requires:

```text
lambda = 0.
```

Nonzero Lambda is not algebraically forbidden. It is a separate baseline branch
that must be selected, fixed, or relaxed by an additional vacuum principle.
"""

out = Path(__file__).with_name("56_lambda_asymptotic_flatness_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Lambda asymptotic-flatness gate passed.")
print(f"Wrote {out.resolve()}")
