#!/usr/bin/env python3
"""
make_18_projection_vs_admissibility_rowspace.py

Compare finite-truncation row spaces:

    projection rows:      S -> <psi_k, S>_w
    admissibility rows:   S -> int aS, S(1), S'(1), ...

This tests whether the projection hierarchy is equivalent to the regularity
admissibility ladder on even polynomial source spaces.

Output:
    18_projection_vs_admissibility_rowspace.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
a = 1 - x**2
w = a**4


def simplify_expr(expr):
    out = sp.simplify(expr)
    out = sp.factor(out)
    out = sp.cancel(out)
    out = sp.factor(out)
    return out


def integrate_poly(expr):
    return sp.integrate(sp.expand(expr), (x, 0, 1))


def psi(k):
    r = sp.Rational(2 * k - 1, 2 * k + 3)
    return x ** (2 * k) - r * x ** (2 * k - 2)


def projection_row(k, degree):
    return [sp.factor(integrate_poly(psi(k) * x ** (2 * j) * w)) for j in range(degree + 1)]


def admissibility_row(order, degree):
    """
    order=-1 gives int aS.
    order>=0 gives S^(order)(1).
    """
    if order == -1:
        return [sp.factor(integrate_poly(a * x ** (2 * j))) for j in range(degree + 1)]
    return [sp.diff(x ** (2 * j), x, order).subs(x, 1) for j in range(degree + 1)]


def rowspace_contains(row_basis, candidate):
    M = sp.Matrix(row_basis)
    before = M.rank()
    after = sp.Matrix(row_basis + [candidate]).rank()
    return before == after


def rowspace_rank(rows):
    return sp.Matrix(rows).rank()


def nullspace_basis(rows):
    return sp.Matrix(rows).nullspace()


checks = []
cases = []

for degree in range(2, 9):
    ncols = degree + 1

    # Use ncols projection rows k=1..ncols, enough to test full rank.
    P_rows = [projection_row(k, degree) for k in range(1, ncols + 1)]
    P_rank = rowspace_rank(P_rows)

    # Boundedness through C^R with R=degree-1 gives enough admissibility rows
    # to span the full dual space on degree-N even polynomials:
    #   int aS plus derivatives S^(m)(1), m=0..degree-1.
    A_rows_full = [admissibility_row(-1, degree)] + [
        admissibility_row(m, degree) for m in range(0, degree)
    ]
    A_rank_full = rowspace_rank(A_rows_full)

    if P_rank != ncols:
        raise AssertionError(f"projection rows lost rank at degree={degree}: {P_rank}")
    if A_rank_full != ncols:
        raise AssertionError(f"full admissibility rows lost rank at degree={degree}: {A_rank_full}")
    checks.append(f"degree {degree}: projection and full admissibility row spaces both full rank")

    # Minimal boundedness admissibility is just int aS on even polynomials.
    A0_rows = [admissibility_row(-1, degree)]
    A0_in_projection = rowspace_contains(P_rows, A0_rows[0])

    # C^R ladder row spaces for R=0..min(4,degree-1).
    ladder = []
    for R in range(0, min(5, degree)):
        A_R_rows = [admissibility_row(-1, degree)] + [
            admissibility_row(m, degree) for m in range(0, R)
        ]
        rank_R = rowspace_rank(A_R_rows)
        contained_in_projection = all(rowspace_contains(P_rows, row) for row in A_R_rows)
        projection_contained_in_AR = all(rowspace_contains(A_R_rows, row) for row in P_rows)
        ladder.append((R, rank_R, contained_in_projection, projection_contained_in_AR))

    # Compare first ncols admissibility rows against projection rowspace. Since
    # both are full rank, the full row spaces coincide with the whole dual
    # space, but the smaller ladder spaces do not.
    cases.append((degree, P_rank, A_rank_full, A0_in_projection, ladder))

# Direct non-equivalence at small ladder levels:
#
# On degree 4, projection rows are full rank with 5 rows, while C^0/C^1/C^2
# admissibility rows have ranks 1,2,3 respectively. Therefore the projection
# hierarchy is not the same as any low-order regularity ladder truncation.
degree = 4
P_rows = [projection_row(k, degree) for k in range(1, degree + 2)]
for R, expected_rank in [(0, 1), (1, 2), (2, 3)]:
    A_R_rows = [admissibility_row(-1, degree)] + [
        admissibility_row(m, degree) for m in range(0, R)
    ]
    if rowspace_rank(A_R_rows) != expected_rank:
        raise AssertionError(f"unexpected C^{R} rank")
    if rowspace_rank(P_rows) == expected_rank:
        raise AssertionError(f"projection rank unexpectedly equals C^{R} rank")
checks.append("low-order admissibility ladders are not equal to full projection rowspace")

# Kernel comparison on degree 6:
#
# C^R admissibility has a nontrivial nullspace until R reaches degree.
# Projection rows with degree+1 rows have zero nullspace.
degree = 6
P_rows = [projection_row(k, degree) for k in range(1, degree + 2)]
P_null_dim = len(nullspace_basis(P_rows))
if P_null_dim != 0:
    raise AssertionError(f"projection nullspace expected zero, got {P_null_dim}")

kernel_rows = []
for R in range(0, degree):
    A_R_rows = [admissibility_row(-1, degree)] + [
        admissibility_row(m, degree) for m in range(0, R)
    ]
    kernel_rows.append((R, len(nullspace_basis(A_R_rows))))
checks.append("kernel dimensions distinguish projection rows from finite regularity ladders")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
case_lines = "\n".join(
    (
        f"degree={degree}: P_rank={P_rank}, full_adm_rank={A_rank}, "
        f"C0 row in P rowspace? {A0_in_projection}, ladder={ladder}"
    )
    for degree, P_rank, A_rank, A0_in_projection, ladder in cases
)
kernel_lines = "\n".join(f"C^{R} admissibility nullity on degree 6: {dim}" for R, dim in kernel_rows)

md = f"""# Synthesis Proof 18: Projection vs. Admissibility Row Spaces

## Purpose

This report tests the proposed bridge:

```text
Are the psi_k projection rows equivalent to the regularity/admissibility rows?
```

The comparison is finite-dimensional, on even polynomial source spaces:

```text
S(x) = sum_j c_j x^(2j).
```

## Validated Checks

{validation_bullets}

## Row Families

Projection rows:

```text
P_k[S] = integral_0^1 psi_k(x) S(x) a^4 dx.
```

Admissibility rows:

```text
C_0[S] = integral_0^1 aS dx
C_1[S] = S(1)
C_2[S] = S'(1)
C_3[S] = S''(1)
...
```

where the regularity ladder uses:

```text
C^R f:
  integral aS = 0
  S vanishes to order R at x=1.
```

## Result

The projection rows are full rank on the tested even polynomial truncations.
The full admissibility row family is also full rank once enough endpoint
derivatives are included.

But the low-order regularity ladders are not equal to the projection rowspace.
They have smaller rank and larger nullspaces.

Exact row-space data:

```text
{case_lines}
```

Kernel comparison on degree 6:

```text
projection nullity on degree 6: {P_null_dim}
{kernel_lines}
```

## Interpretation

This is a partial negative result for the strongest bridge claim.

The `psi_k` hierarchy is not simply the same rowspace as the low-order
regularity/admissibility ladder:

```text
integral aS = 0,
S(1)=0,
S'(1)=0,
...
```

on finite even polynomial source spaces.

Instead:

```text
projection rows:
  full-rank moment diagnostics on the tested source space

admissibility rows:
  lower-rank boundary/regularity constraints until the full derivative tower is
  included
```

So the projection hierarchy is adjacent to the admissibility problem, and it
resolves admissible balanced source spaces, but it is not identical to the
low-order regularity ladder.
"""

out = Path("18_projection_vs_admissibility_rowspace.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
