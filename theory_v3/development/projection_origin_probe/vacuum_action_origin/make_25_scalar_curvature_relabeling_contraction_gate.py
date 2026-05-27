#!/usr/bin/env python3
"""
make_25_scalar_curvature_relabeling_contraction_gate.py

Validate that contracting the Ricci curvature with the inverse metric gives a
relabeling-invariant scalar.

Output:
    25_scalar_curvature_relabeling_contraction_gate.md
"""

from pathlib import Path
import sympy as sp


a, b, c = sp.symbols("a b c")
r00, r01, r11 = sp.symbols("R00 R01 R11")
p, q, r, s = sp.symbols("p q r s")


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

G_inv = sp.Matrix([[a, b], [b, c]])
Ricci = sp.Matrix([[r00, r01], [r01, r11]])
J = sp.Matrix([[p, q], [r, s]])

Ricci_prime = J.T * Ricci * J
G_inv_prime = J.inv() * G_inv * J.inv().T

scalar_R = simplify_expr(sp.trace(G_inv * Ricci))
scalar_R_prime = simplify_expr(sp.trace(G_inv_prime * Ricci_prime))

require_equal("Ricci inverse-metric contraction is relabeling invariant", scalar_R_prime, scalar_R)
checks.append("Ricci inverse-metric contraction is relabeling invariant")

swap = sp.Matrix([[0, 1], [1, 0]])
Ricci_swap = swap.T * Ricci * swap
G_inv_swap = swap.inv() * G_inv * swap.inv().T

require_equal("coordinate swap sends R00 to R11", Ricci_swap[0, 0], r11)
checks.append("coordinate swap sends R00 to R11")

require_equal("scalar curvature invariant under coordinate swap", sp.trace(G_inv_swap * Ricci_swap), scalar_R)
checks.append("scalar curvature invariant under coordinate swap")

diagonal_G_inv = sp.diag(a, c)
diagonal_scalar = sp.trace(diagonal_G_inv * Ricci)
require_equal("diagonal scalar curvature contraction", diagonal_scalar, a * r00 + c * r11)
checks.append("diagonal scalar curvature contraction")

offdiag_contribution = simplify_expr(scalar_R - diagonal_scalar)
require_equal("off-diagonal curvature contribution", offdiag_contribution, 2 * b * r01)
checks.append("off-diagonal curvature contribution")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 25: Scalar Curvature Relabeling Contraction Gate

## Purpose

This report validates the scalar-curvature action-selection gate:

```text
linear curvature scalar
  =
  inverse metric contracted with Ricci curvature.
```

## Validated Checks

{validation_bullets}

## Relabeling-Invariant Contraction

Let `R_ab` be a covariant Ricci-like curvature tensor and `g^ab` be the inverse
metric. Under a coordinate relabeling with Jacobian `J`:

```text
R' = J^T R J
g'^(-1) = J^(-1) g^(-1) J^(-T).
```

SymPy verifies:

```text
trace(g'^(-1) R') = trace(g^(-1) R).
```

This is:

```text
R = g^ab R_ab.
```

## Component Non-Invariance

A coordinate swap sends:

```text
R_00 -> R_11.
```

So individual curvature components are not scalar action densities.

## Interpretation

Once curvature is the invariant field strength, a local action term linear in
that curvature must contract indices to make a scalar. The inverse metric gives
the natural contraction:

```text
sqrt(g) g^ab R_ab = sqrt(g) R.
```

This does not yet prove uniqueness among all higher-curvature scalars; it
identifies the relabeling-invariant linear curvature term.
"""

out = Path(__file__).with_name("25_scalar_curvature_relabeling_contraction_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
