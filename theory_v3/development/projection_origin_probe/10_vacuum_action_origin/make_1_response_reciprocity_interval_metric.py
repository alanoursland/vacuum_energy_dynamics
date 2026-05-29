#!/usr/bin/env python3
"""
make_1_response_reciprocity_interval_metric.py

Validate that a smooth reciprocal local response cost has a symmetric
quadratic leading term, giving a metric candidate.

Output:
    1_response_reciprocity_interval_metric.md
"""

from pathlib import Path
import sympy as sp


d0, d1 = sp.symbols("d0 d1")
c0, l0, l1 = sp.symbols("c0 l0 l1")
m00, m01, m10, m11, a01 = sp.symbols("m00 m01 m10 m11 a01")


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

d = sp.Matrix([d0, d1])
M = sp.Matrix([[m00, m01], [m10, m11]])
S = (M + M.T) / 2
A = (M - M.T) / 2

# Local response expansion through quadratic order.
response = c0 + l0 * d0 + l1 * d1 + sp.Rational(1, 2) * (d.T * M * d)[0]

require_equal("self-response normalization", response.subs({d0: 0, d1: 0}), c0)
checks.append("self-response normalization")

zero_self_solution = sp.solve([sp.Eq(response.subs({d0: 0, d1: 0}), 0)], [c0], dict=True)
if zero_self_solution != [{c0: 0}]:
    raise AssertionError(f"zero self-response did not force c0=0: {zero_self_solution}")
checks.append("zero self-response removes constant term")

odd_part = simplify_expr(response - response.subs({d0: -d0, d1: -d1}))
require_equal("reciprocity odd part", odd_part, 2 * (l0 * d0 + l1 * d1))
checks.append("reciprocity odd part")

odd_coeffs = [sp.Poly(odd_part, d0, d1).coeff_monomial(d0), sp.Poly(odd_part, d0, d1).coeff_monomial(d1)]
reciprocal_solution = sp.solve([sp.Eq(coeff, 0) for coeff in odd_coeffs], [l0, l1], dict=True)
if reciprocal_solution != [{l0: 0, l1: 0}]:
    raise AssertionError(f"reciprocity did not force l0=l1=0: {reciprocal_solution}")
checks.append("reciprocity removes linear term")

quadratic = sp.Rational(1, 2) * (d.T * M * d)[0]
require_equal("antisymmetric part invisible to quadratic interval", sp.Rational(1, 2) * (d.T * A * d)[0], 0)
checks.append("antisymmetric part invisible to quadratic interval")

require_equal("quadratic interval equals symmetric part", quadratic, sp.Rational(1, 2) * (d.T * S * d)[0])
checks.append("quadratic interval equals symmetric part")

hessian = sp.hessian(quadratic, (d0, d1))
require_equal("Hessian recovers symmetric response metric", hessian, S)
checks.append("Hessian recovers symmetric response metric")

explicit_antisym = sp.Matrix([[0, a01], [-a01, 0]])
require_equal("explicit antisymmetric response gives zero interval", (d.T * explicit_antisym * d)[0], 0)
checks.append("explicit antisymmetric response gives zero interval")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 1: Response Reciprocity to Metric Candidate

## Purpose

This report validates the first action-origin gate:

```text
smooth local response cost
  + zero self-cost
  + reciprocity under displacement reversal
  -> symmetric quadratic leading term.
```

That symmetric quadratic leading term is the metric candidate.

## Validated Checks

{validation_bullets}

## Local Response Expansion

Write the local response cost for a small displacement `d` as:

```text
C(d) = c0 + l_a d^a + (1/2) M_ab d^a d^b + higher terms.
```

Zero self-cost gives:

```text
C(0) = 0 -> c0 = 0.
```

Reciprocity means:

```text
C(d) = C(-d).
```

SymPy verifies that the odd part is:

```text
C(d) - C(-d) = 2 l_a d^a.
```

So reciprocity forces:

```text
l_a = 0.
```

## Metric Candidate

Every matrix decomposes as:

```text
M = S + A
S = (M + M^T)/2
A = (M - M^T)/2.
```

SymPy verifies:

```text
d^T A d = 0
d^T M d = d^T S d.
```

The Hessian of the quadratic response is:

```text
partial_a partial_b C = S_ab.
```

## Interpretation

If vacuum response supplies a smooth reciprocal local cost between nearby
states, the leading nontrivial local observable is necessarily a symmetric
bilinear form. This does not yet determine signature or dynamics, but it gives
the metric as the natural macroscopic configuration variable.
"""

out = Path(__file__).with_name("1_response_reciprocity_interval_metric.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
