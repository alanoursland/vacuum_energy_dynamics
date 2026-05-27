#!/usr/bin/env python3
"""
make_11_low_order_matrix_patterns.py

Generate exact low-order projection matrices and report simple algebraic
patterns: signs, rank, determinant, and pivots.

Output:
    11_low_order_matrix_patterns.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
a = 1 - x**2
w = a**4


def integrate_poly(expr):
    return sp.integrate(sp.expand(expr), (x, 0, 1))


def psi(k):
    r = sp.Rational(2 * k - 1, 2 * k + 3)
    return x ** (2 * k) - r * x ** (2 * k - 2)


def entry(k, j):
    return sp.factor(2 * integrate_poly(psi(k) * x ** (2 * j) * w))


def sign_of(q):
    q = sp.signsimp(q)
    if q > 0:
        return "+"
    if q < 0:
        return "-"
    return "0"


N = 8
A = sp.Matrix([[entry(k, j) for j in range(N)] for k in range(1, N + 1)])
sign_matrix = [[sign_of(A[i, j]) for j in range(N)] for i in range(N)]

ranks = []
dets = []
pivots = []
for n in range(1, N + 1):
    sub = A[:n, :n]
    ranks.append((n, sub.rank()))
    dets.append((n, sp.factor(sub.det())))
    pivots.append((n, sub.rref()[1]))

row_sums = [sp.factor(sum(A[i, j] for j in range(N))) for i in range(N)]
col_sums = [sp.factor(sum(A[i, j] for i in range(N))) for j in range(N)]

if A.rank() != N:
    raise AssertionError(f"expected full rank {N}, got {A.rank()}")

checks = [
    f"exact {N}x{N} projection matrix generated",
    f"full rank {N} verified",
    "principal determinants computed",
    "sign matrix computed",
]

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
sign_lines = "\n".join(" ".join(row) for row in sign_matrix)
rank_lines = "\n".join(f"n={n}: rank={rank}" for n, rank in ranks)
det_lines = "\n".join(f"n={n}: det={det}" for n, det in dets)
pivot_lines = "\n".join(f"n={n}: pivots={pivot}" for n, pivot in pivots)

md = f"""# Synthesis Proof 11: Low-Order Matrix Patterns

## Purpose

This report gives exact low-order data for the projection matrix:

```text
A[k,j] = 2 integral_0^1 psi_k(x) x^(2j) a^4 dx.
```

The data is exploratory, but all entries are exact rational values.

## Validated Computations

{validation_bullets}

## Exact Matrix

Rows are `k=1..{N}`; columns are `j=0..{N - 1}`.

```text
{A}
```

## Sign Pattern

```text
{sign_lines}
```

## Principal Ranks

```text
{rank_lines}
```

## Principal Determinants

```text
{det_lines}
```

## RREF Pivots

```text
{pivot_lines}
```

## Row Sums Over Displayed Columns

```text
{row_sums}
```

## Column Sums Over Displayed Rows

```text
{col_sums}
```
"""

out = Path(__file__).with_name("11_low_order_matrix_patterns.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All exact matrix checks passed.")
print(f"Wrote {out.resolve()}")


