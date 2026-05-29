#!/usr/bin/env python3
"""
make_3_moment_matrix_entry_formula.py

Reconstruct the explicit moment-matrix entry formula from the weighted
projection integral.

Output:
    3_moment_matrix_entry_formula.md
"""

from pathlib import Path
import sympy as sp


j, k = sp.symbols("j k", positive=True, integer=True)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []


def beta_moment(s):
    return simplify_expr(
        768
        / (
            (2 * s + 1)
            * (2 * s + 3)
            * (2 * s + 5)
            * (2 * s + 7)
            * (2 * s + 9)
        )
    )


r_k = (2 * k - 1) / (2 * k + 3)
A_entry = simplify_expr(beta_moment(j + k) - r_k * beta_moment(j + k - 1))

closed_formula = simplify_expr(
    1536
    * (4 * j - 6 * k + 3)
    / (
        (2 * k + 3)
        * (2 * j + 2 * k - 1)
        * (2 * j + 2 * k + 1)
        * (2 * j + 2 * k + 3)
        * (2 * j + 2 * k + 5)
        * (2 * j + 2 * k + 7)
        * (2 * j + 2 * k + 9)
    )
)

require_equal("closed matrix entry formula", A_entry, closed_formula)
checks.append("closed matrix entry formula")

# Validate determinant nonzero/positive through N=6 using the closed formula.
det_values = []
for N in range(1, 7):
    matrix = sp.Matrix(
        [
            [closed_formula.subs({k: row, j: col}) for col in range(1, N + 1)]
            for row in range(1, N + 1)
        ]
    )
    det_N = simplify_expr(matrix.det())
    if det_N <= 0:
        raise AssertionError(f"determinant not positive for N={N}: {det_N}")
    det_values.append((N, det_N))

checks.append("closed formula determinants positive through N=6")

for N in range(2, 7):
    pivot_ratio = simplify_expr(det_values[N - 1][1] / det_values[N - 2][1])
    if pivot_ratio <= 0:
        raise AssertionError(f"pivot ratio not positive for N={N}: {pivot_ratio}")

checks.append("leading pivot ratios positive through N=6")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
det_lines = "\n".join(f"N={N}: det={det}" for N, det in det_values)

md = f"""# Field Search Survivor Audit 3: Moment Matrix Entry Formula

## Purpose

This report reconstructs the explicit matrix-entry formula from the weighted
projection integral.

## Validated Checks

{validation_bullets}

## Weighted Moment

The base moment is:

```text
M(s) = 2 integral_0^1 x^(2s)(1-x^2)^4 dx
     = 768 / [(2s+1)(2s+3)(2s+5)(2s+7)(2s+9)].
```

The projection entry is:

```text
A[k,j] = M(j+k) - r_k M(j+k-1).
```

with:

```text
r_k = (2k-1)/(2k+3).
```

## Closed Formula

SymPy verifies:

```text
A[k,j] =
1536(4j - 6k + 3)
/
[
(2k+3)
(2j+2k-1)
(2j+2k+1)
(2j+2k+3)
(2j+2k+5)
(2j+2k+7)
(2j+2k+9)
].
```

## Determinant Check

Using the closed formula, the leading determinants are positive through `N=6`:

```text
{det_lines}
```

## Interpretation

This is the archived determinant/moment result in compact form. It supports the
projection hierarchy as a real moment-pairing object, while preserving the
boundary that finite determinant checks are not an all-order theorem.
"""

out = Path(__file__).with_name("3_moment_matrix_entry_formula.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
