#!/usr/bin/env python3
"""
make_8_projection_matrix_closed_form.py

Validate closed-form expressions for the projection matrix entries and their
IBP pullback form.

Output:
    8_projection_matrix_closed_form.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
k = sp.symbols("k", integer=True, positive=True)
j = sp.symbols("j", integer=True, nonnegative=True)

a = 1 - x**2
w = a**4
r_k = sp.simplify((2 * k - 1) / (2 * k + 3))


def simplify_expr(expr):
    out = sp.simplify(expr)
    out = sp.factor(out)
    out = sp.powsimp(out, force=True)
    out = sp.cancel(out)
    out = sp.factor(out)
    out = sp.powsimp(out, force=True)
    out = sp.simplify(out)
    return out


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def moment_poly(n, power):
    return sp.simplify(
        sum(
            sp.binomial(power, ell) * (-1) ** ell / (n + 2 * ell + 1)
            for ell in range(power + 1)
        )
    )


def L_monomial_even(J):
    """L[x^(2J)] in expanded monomial form."""
    return 2 * J * x ** (2 * J - 1) - (2 * J + 6) * x ** (2 * J + 1)


checks = []

# A[k,j] = 2 int psi_k x^(2j) a^4 dx.
A_closed = 2 * (
    moment_poly(2 * k + 2 * j, 4)
    - r_k * moment_poly(2 * k + 2 * j - 2, 4)
)

lower_moment = moment_poly(2 * k + 2 * j - 2, 4)
ratio_part = (k + j - sp.Rational(1, 2)) / (k + j + sp.Rational(9, 2)) - r_k
A_factored = 2 * lower_moment * ratio_part
require_equal("closed form factored source signature", A_closed, A_factored)
checks.append("closed form factored source signature")

# Pullback form:
#
#   A[k,j] = 2/(2k+3) int x^(2k-1) a^4 L[x^(2j)] dx.
pullback_closed = sp.Rational(2, 1) / (2 * k + 3) * (
    2 * j * moment_poly(2 * k + 2 * j - 2, 4)
    - (2 * j + 6) * moment_poly(2 * k + 2 * j, 4)
)
require_equal("projection matrix pullback closed form", A_closed, pullback_closed)
checks.append("projection matrix pullback closed form")

# Direct finite checks against SymPy integration.
sample_rows = []
for K in range(1, 7):
    row = []
    for J in range(0, 6):
        rK = sp.Rational(2 * K - 1, 2 * K + 3)
        psiK = x ** (2 * K) - rK * x ** (2 * K - 2)
        direct = 2 * sp.integrate(sp.expand(psiK * x ** (2 * J) * w), (x, 0, 1))
        closed = A_closed.subs({k: K, j: J})
        pullback = pullback_closed.subs({k: K, j: J})
        require_equal(f"direct closed K={K} J={J}", direct, closed)
        require_equal(f"direct pullback K={K} J={J}", direct, pullback)
        row.append(sp.factor(direct))
    sample_rows.append(row)
checks.append("direct finite matrix grid K=1..6 J=0..5")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
matrix_lines = "\n".join(str(row) for row in sample_rows)

md = f"""# Synthesis Proof 8: Projection Matrix Closed Form

## Purpose

This report validates exact closed forms for:

```text
A[k,j] = 2 integral_0^1 psi_k(x) x^(2j) a^4 dx
```

and for the IBP pullback expression:

```text
A[k,j] = 2/(2k+3) integral_0^1 x^(2k-1) a^4 L[x^(2j)] dx.
```

## Validated Identities

{validation_bullets}

## Closed Form

Let:

```text
M(n,p) = integral_0^1 x^n (1-x^2)^p dx.
```

Then:

```text
A[k,j] = 2[M(2k+2j,4) - r_k M(2k+2j-2,4)].
```

Equivalently:

```text
A[k,j]
  = 2 M(2k+2j-2,4)
    [ (k+j-1/2)/(k+j+9/2) - (2k-1)/(2k+3) ].
```

The pullback form uses:

```text
L[x^(2j)] = 2j x^(2j-1) - (2j+6)x^(2j+1).
```

## Sample Exact Matrix

Rows are `k=1..6`; columns are `j=0..5`.

```text
{matrix_lines}
```
"""

out = Path(__file__).with_name("8_projection_matrix_closed_form.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")


