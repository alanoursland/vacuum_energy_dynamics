#!/usr/bin/env python3
"""
make_2_metric_signature_invariance_gate.py

Validate that metric signature data is invariant under invertible coordinate
changes and is therefore not a coordinate artifact.

Output:
    2_metric_signature_invariance_gate.md
"""

from pathlib import Path
import sympy as sp


p, q, r, s = sp.symbols("p q r s")
dx0, dx1 = sp.symbols("dx0 dx1")


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def is_zero(expr):
    expr = simplify_expr(expr)
    if isinstance(expr, sp.MatrixBase):
        return all(simplify_expr(entry) == 0 for entry in expr)
    return expr == 0


def require_zero(label, expr):
    result = simplify_expr(expr)
    if not is_zero(result):
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

J = sp.Matrix([[p, q], [r, s]])
det_J = simplify_expr(J.det())

G_euclidean = sp.diag(1, 1)
G_lorentzian = sp.diag(-1, 1)

G_e_prime = simplify_expr(J.T * G_euclidean * J)
G_l_prime = simplify_expr(J.T * G_lorentzian * J)

require_equal("Euclidean determinant transforms by det(J)^2", G_e_prime.det(), det_J**2 * G_euclidean.det())
checks.append("Euclidean determinant transforms by det(J)^2")

require_equal("Lorentzian determinant transforms by det(J)^2", G_l_prime.det(), det_J**2 * G_lorentzian.det())
checks.append("Lorentzian determinant transforms by det(J)^2")

require_equal("Euclidean determinant sign expression", G_e_prime.det(), det_J**2)
checks.append("Euclidean determinant sign expression")

require_equal("Lorentzian determinant sign expression", G_l_prime.det(), -det_J**2)
checks.append("Lorentzian determinant sign expression")

d = sp.Matrix([dx0, dx1])
require_equal("Euclidean interval for equal displacement", (d.T * G_euclidean * d)[0].subs({dx0: 1, dx1: 1}), 2)
checks.append("Euclidean interval for equal displacement")

require_equal("Lorentzian null displacement", (d.T * G_lorentzian * d)[0].subs({dx0: 1, dx1: 1}), 0)
checks.append("Lorentzian null displacement")

require_equal("Lorentzian timelike displacement", (d.T * G_lorentzian * d)[0].subs({dx0: 1, dx1: 0}), -1)
checks.append("Lorentzian timelike displacement")

require_equal("Lorentzian spacelike displacement", (d.T * G_lorentzian * d)[0].subs({dx0: 0, dx1: 1}), 1)
checks.append("Lorentzian spacelike displacement")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 2: Metric Signature Invariance Gate

## Purpose

This report validates that the signature of the local interval is not a
coordinate artifact.

It does not derive Lorentzian signature. It proves that once signature is
present, invertible relabeling cannot remove it.

## Validated Checks

{validation_bullets}

## Coordinate Change

For an invertible local coordinate change with Jacobian `J`, the metric
transforms as:

```text
G' = J^T G J.
```

SymPy verifies:

```text
det(G') = det(J)^2 det(G).
```

So the sign of `det(G)` is invariant under invertible relabeling.

## Two-Dimensional Gate

In two dimensions:

```text
G = diag(1,1)  -> det(G) =  1
G = diag(-1,1) -> det(G) = -1.
```

After relabeling:

```text
det(G'_Euclidean)  =  det(J)^2
det(G'_Lorentzian) = -det(J)^2.
```

So an invertible coordinate change cannot turn one into the other.

## Interpretation

The previous proof gives a symmetric local bilinear form. This proof shows that
its signature is physical structure, not coordinate convention. A vacuum-origin
derivation must therefore explain why the response interval is Lorentzian
rather than positive definite if the target is relativistic spacetime.
"""

out = Path(__file__).with_name("2_metric_signature_invariance_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
