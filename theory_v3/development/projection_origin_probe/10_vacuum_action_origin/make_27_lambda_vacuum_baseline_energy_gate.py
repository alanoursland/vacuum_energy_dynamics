#!/usr/bin/env python3
"""
make_27_lambda_vacuum_baseline_energy_gate.py

Validate that a vacuum baseline energy density varies as a metric-proportional
term and appears as a separate Lambda branch.

Output:
    27_lambda_vacuum_baseline_energy_gate.md
"""

from pathlib import Path
import sympy as sp


A, B, Lambda = sp.symbols("A B Lambda", positive=True)
r, Gconst, M = sp.symbols("r G M", positive=True)


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

sqrt_g = sp.sqrt(A * B)
g_inv_A = 1 / A
g_inv_B = 1 / B

require_equal("volume variation with respect to A", sp.diff(sqrt_g, A), sp.Rational(1, 2) * sqrt_g * g_inv_A)
checks.append("volume variation with respect to A")

require_equal("volume variation with respect to B", sp.diff(sqrt_g, B), sp.Rational(1, 2) * sqrt_g * g_inv_B)
checks.append("volume variation with respect to B")

L_lambda = -2 * Lambda * sqrt_g
require_equal("Lambda variation with respect to A", sp.diff(L_lambda, A), -Lambda * sqrt_g * g_inv_A)
checks.append("Lambda variation with respect to A")

require_equal("Lambda variation with respect to B", sp.diff(L_lambda, B), -Lambda * sqrt_g * g_inv_B)
checks.append("Lambda variation with respect to B")

Phi_lambda = -Lambda * r**2 / 6
require_equal("Lambda Newtonian potential Laplacian", radial_laplacian(Phi_lambda), -Lambda)
checks.append("Lambda Newtonian potential Laplacian")

Phi_mass = -Gconst * M / r
require_equal("mass potential is source-free off origin", radial_laplacian(Phi_mass), 0)
checks.append("mass potential is source-free off origin")

Phi_total = Phi_mass + Phi_lambda
require_equal("mass plus Lambda exterior equation", radial_laplacian(Phi_total), -Lambda)
checks.append("mass plus Lambda exterior equation")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 27: Lambda as Vacuum Baseline Energy Gate

## Purpose

This report validates the role of a vacuum baseline energy density.

The gate is:

```text
constant vacuum baseline density
  -> metric-proportional field-equation term
  -> separate Lambda branch.
```

## Validated Checks

{validation_bullets}

## Volume Variation

For a diagonal two-dimensional metric:

```text
sqrt(g) = sqrt(A B),
```

SymPy verifies:

```text
partial sqrt(g)/partial A = (1/2)sqrt(g) g^AA
partial sqrt(g)/partial B = (1/2)sqrt(g) g^BB.
```

For:

```text
L_Lambda = -2 Lambda sqrt(g),
```

the variation is metric-proportional:

```text
partial L_Lambda/partial A = -Lambda sqrt(g) g^AA
partial L_Lambda/partial B = -Lambda sqrt(g) g^BB.
```

## Newtonian Branch

The potential:

```text
Phi_Lambda = -Lambda r^2/6
```

satisfies:

```text
Delta Phi_Lambda = -Lambda.
```

The mass potential remains harmonic off source:

```text
Delta(-GM/r) = 0.
```

So outside localized matter:

```text
Delta[-GM/r - Lambda r^2/6] = -Lambda.
```

## Interpretation

Lambda is not connection strain. It is baseline vacuum energy. The earlier EH
tests correctly treated it as an allowed but separate branch: compatible with
the action gates, but not forced by the boundary-flux inverse-square bridge.
"""

out = Path(__file__).with_name("27_lambda_vacuum_baseline_energy_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
