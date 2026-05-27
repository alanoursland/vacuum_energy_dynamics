#!/usr/bin/env python3
"""
make_31_lambda_relaxation_baseline_alternatives.py

Validate simple algebraic alternatives for Lambda as fixed baseline, relaxed
baseline, or source-shifted baseline.

Output:
    31_lambda_relaxation_baseline_alternatives.md
"""

from pathlib import Path
import sympy as sp


lam, lam0, J = sp.symbols("lambda lambda_0 J")
kappa, r = sp.symbols("kappa r", positive=True)


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

U_relax = kappa * (lam - lam0) ** 2 / 2
variation_relax = sp.diff(U_relax, lam)
require_equal("relaxation potential variation", variation_relax, kappa * (lam - lam0))
checks.append("relaxation potential variation")

relax_solution = sp.solve([sp.Eq(variation_relax, 0)], [lam], dict=True)
if relax_solution != [{lam: lam0}]:
    raise AssertionError(f"relaxation solution failed: {relax_solution}")
checks.append("relaxation sets Lambda to baseline")

U_zero_relax = U_relax.subs(lam0, 0)
zero_relax_solution = sp.solve([sp.Eq(sp.diff(U_zero_relax, lam), 0)], [lam], dict=True)
if zero_relax_solution != [{lam: 0}]:
    raise AssertionError(f"zero relaxation solution failed: {zero_relax_solution}")
checks.append("zero-baseline relaxation sets Lambda to zero")

U_shifted = kappa * lam**2 / 2 - J * lam
variation_shifted = sp.diff(U_shifted, lam)
require_equal("source-shifted Lambda variation", variation_shifted, kappa * lam - J)
checks.append("source-shifted Lambda variation")

shifted_solution = sp.solve([sp.Eq(variation_shifted, 0)], [lam], dict=True)
if shifted_solution != [{lam: J / kappa}]:
    raise AssertionError(f"source-shifted solution failed: {shifted_solution}")
checks.append("source shifts Lambda baseline")

reduced_shifted_energy = simplify_expr(U_shifted.subs(lam, J / kappa))
require_equal("integrated-out Lambda shift energy", reduced_shifted_energy, -J**2 / (2 * kappa))
checks.append("integrated-out Lambda shift energy")

Phi_lambda = -lam * r**2 / 6
require_equal("Lambda potential equation", radial_laplacian(Phi_lambda), -lam)
checks.append("Lambda potential equation")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 31: Lambda Relaxation and Baseline Alternatives

## Purpose

This report separates three Lambda possibilities:

```text
fixed parameter;
relaxed vacuum baseline;
source-shifted baseline.
```

## Validated Checks

{validation_bullets}

## Relaxed Baseline

For:

```text
U(lambda) = (kappa/2)(lambda - lambda_0)^2,
```

SymPy verifies:

```text
dU/dlambda = kappa(lambda - lambda_0)
```

and stationarity gives:

```text
lambda = lambda_0.
```

If:

```text
lambda_0 = 0,
```

then relaxation sets:

```text
lambda = 0.
```

## Source-Shifted Baseline

For:

```text
U(lambda) = (kappa/2)lambda^2 - J lambda,
```

SymPy verifies:

```text
lambda = J/kappa.
```

Integrating out the baseline variable gives:

```text
U_reduced = -J^2/(2kappa).
```

## Newtonian Branch

The Lambda potential:

```text
Phi_lambda = -lambda r^2/6
```

satisfies:

```text
Delta Phi_lambda = -lambda.
```

## Interpretation

The proof chain cannot set Lambda by algebra alone. It can only classify the
branches:

```text
Lambda fixed     -> external baseline parameter;
Lambda relaxed   -> value selected by vacuum baseline potential;
Lambda shifted   -> value responds to an additional vacuum source variable.
```

The inverse-square boundary-flux bridge corresponds to the zero-Lambda
asymptotically flat sector.
"""

out = Path(__file__).with_name("31_lambda_relaxation_baseline_alternatives.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
