#!/usr/bin/env python3
"""
make_21_projection_determinant_evidence.py

Compute exact determinant evidence for original and balanced projection
matrices across finite truncations.

Output:
    21_projection_determinant_evidence.md
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


def c_Rq(R, q):
    return sp.factor(integrate_poly(a ** (R + 1) * x ** (2 * q)) / integrate_poly(a ** (R + 1)))


checks = []
original_rows = []
balanced_rows = []

for N in range(1, 9):
    A = sp.Matrix(
        [
            [sp.factor(2 * integrate_poly(psi(k) * x ** (2 * j) * w)) for j in range(0, N)]
            for k in range(1, N + 1)
        ]
    )
    detA = sp.factor(A.det())
    if detA == 0:
        raise AssertionError(f"original determinant vanished N={N}")
    original_rows.append((N, detA))

checks.append("original projection principal determinants nonzero for N=1..8")

for R in range(0, 6):
    for N in range(1, 8):
        P = sp.Matrix(
            [
                [
                    sp.factor(
                        integrate_poly(
                            psi(k) * a**R * (x ** (2 * q) - c_Rq(R, q)) * w
                        )
                    )
                    for q in range(1, N + 1)
                ]
                for k in range(1, N + 1)
            ]
        )
        detP = sp.factor(P.det())
        if detP == 0:
            raise AssertionError(f"balanced determinant vanished R={R} N={N}")
        balanced_rows.append((R, N, detP))

checks.append("balanced signature determinants nonzero for R=0..5 N=1..7")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
original_lines = "\n".join(f"N={N}: det={det}" for N, det in original_rows)
balanced_lines = "\n".join(f"R={R}, N={N}: det={det}" for R, N, det in balanced_rows)

md = f"""# Synthesis Proof 21: Projection Determinant Evidence

## Purpose

This report records exact determinant evidence for finite projection
truncations.

It does not claim a general determinant formula. It verifies nonzero exact
determinants over a substantial grid.

## Validated Checks

{validation_bullets}

## Original Projection Matrix

```text
A_N[k,j] = 2 integral psi_k x^(2j) a^4 dx
k=1..N, j=0..N-1
```

Exact principal determinants:

```text
{original_lines}
```

## Balanced Signature Matrices

```text
P_(R,N)[k,q] = integral psi_k a^R[x^(2q)-c_(R,q)] a^4 dx
k=1..N, q=1..N
```

Exact determinants:

```text
{balanced_lines}
```

## Interpretation

The tested truncations are exactly nonsingular. This supports the working
claim that the projection hierarchy is a full-rank diagnostic on both the
raw monomial space and the balanced admissible source classes.

A closed determinant formula remains a separate target.
"""

out = Path(__file__).with_name("21_projection_determinant_evidence.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All determinant checks passed.")
print(f"Wrote {out.resolve()}")


