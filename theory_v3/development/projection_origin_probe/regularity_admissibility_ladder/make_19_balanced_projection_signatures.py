#!/usr/bin/env python3
"""
make_19_balanced_projection_signatures.py

Analyze psi_k projection signatures on the balanced regular source classes:

    B_(R,q)(x) = a^R [x^(2q) - c_(R,q)]

where c_(R,q) enforces:

    integral_0^1 a B_(R,q) dx = 0.

Output:
    19_balanced_projection_signatures.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
k = sp.symbols("k", integer=True, positive=True)
q = sp.symbols("q", integer=True, positive=True)
R = sp.symbols("R", integer=True, nonnegative=True)

a = 1 - x**2
w = a**4


def simplify_expr(expr):
    out = sp.simplify(expr)
    out = sp.factor(out)
    out = sp.powsimp(out, force=True)
    out = sp.cancel(out)
    out = sp.factor(out)
    return out


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def integrate_poly(expr):
    return sp.integrate(sp.expand(expr), (x, 0, 1))


def moment_poly(n, power):
    return sp.simplify(
        sum(
            sp.binomial(power, ell) * (-1) ** ell / (n + 2 * ell + 1)
            for ell in range(power + 1)
        )
    )


def psi(K):
    r = sp.Rational(2 * K - 1, 2 * K + 3)
    return x ** (2 * K) - r * x ** (2 * K - 2)


def c_Rq(R_value, Q):
    return sp.factor(moment_poly(2 * Q, R_value + 1) / moment_poly(0, R_value + 1))


def B_Rq(R_value, Q):
    return sp.expand(a ** R_value * (x ** (2 * Q) - c_Rq(R_value, Q)))


def projection_signature(R_value, Q, Kmax):
    B = B_Rq(R_value, Q)
    return [sp.factor(integrate_poly(psi(K) * B * w)) for K in range(1, Kmax + 1)]


checks = []

# 1. Validate the balancing coefficient and admissibility condition.
for R_value in range(0, 6):
    for Q in range(1, 8):
        B = B_Rq(R_value, Q)
        require_zero(
            f"balanced admissibility R={R_value} Q={Q}",
            integrate_poly(a * B),
        )
checks.append("balanced source classes satisfy integral aB=0")

# 2. Closed-form projection signature in moments:
#
# P_(R)[k,q] = int psi_k a^R [x^(2q)-c] a^4 dx
#             = M(2k+2q,R+4) - r_k M(2k+2q-2,R+4)
#               - c [M(2k,R+4) - r_k M(2k-2,R+4)].
for R_value in range(0, 6):
    for Q in range(1, 7):
        c = c_Rq(R_value, Q)
        for K in range(1, 7):
            rK = sp.Rational(2 * K - 1, 2 * K + 3)
            direct = integrate_poly(psi(K) * B_Rq(R_value, Q) * w)
            closed = (
                moment_poly(2 * K + 2 * Q, R_value + 4)
                - rK * moment_poly(2 * K + 2 * Q - 2, R_value + 4)
                - c * (
                    moment_poly(2 * K, R_value + 4)
                    - rK * moment_poly(2 * K - 2, R_value + 4)
                )
            )
            require_equal(
                f"balanced projection closed form R={R_value} Q={Q} K={K}",
                direct,
                closed,
            )
checks.append("balanced projection moment closed form grid R=0..5 Q,K=1..6")

# 3. Rank behavior of projection signatures on balanced regular source bases.
rank_rows = []
signature_matrices = {}
for R_value in range(0, 6):
    for N in range(2, 8):
        M = sp.Matrix(
            [
                projection_signature(R_value, Q, Kmax=N)
                for Q in range(1, N + 1)
            ]
        )
        rank = M.rank()
        if rank != N:
            raise AssertionError(f"signature rank failed R={R_value} N={N}: {rank}")
        rank_rows.append((R_value, N, rank))
        if N == 5:
            signature_matrices[R_value] = M
checks.append("balanced projection signatures full rank for R=0..5 N=2..7")

# 4. The balanced signature is not diagonal/triangular in the naive q,k order,
# so adaptation is full-rank diagnostic rather than simple modal decoupling.
triangular_rows = []
for R_value, M in signature_matrices.items():
    lower_zero = all(M[i, j] == 0 for i in range(5) for j in range(i + 1, 5))
    upper_zero = all(M[i, j] == 0 for i in range(5) for j in range(0, i))
    triangular_rows.append((R_value, lower_zero, upper_zero))
    if lower_zero or upper_zero:
        raise AssertionError(f"unexpected triangular signature R={R_value}")
checks.append("balanced signature matrices are full, not naively triangular")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
rank_lines = "\n".join(f"R={R_value}, N={N}: rank={rank}" for R_value, N, rank in rank_rows)
triangular_lines = "\n".join(
    f"R={R_value}: upper entries all zero? {lower_zero}; lower entries all zero? {upper_zero}"
    for R_value, lower_zero, upper_zero in triangular_rows
)
matrix_lines = "\n\n".join(
    f"R={R_value}, N=5 signature matrix rows q=1..5 cols k=1..5:\n{M}"
    for R_value, M in signature_matrices.items()
)

md = f"""# Synthesis Proof 19: Balanced Projection Signatures

## Purpose

This report analyzes how the `psi_k` projection diagnostics act on the
regular balanced source classes:

```text
B_(R,q)(x) = a^R [x^(2q) - c_(R,q)].
```

These classes satisfy the endpoint-contact/admissibility ladder conditions from the
transformed `u` problem.

## Validated Checks

{validation_bullets}

## Balanced Source Classes

The coefficient is chosen by:

```text
c_(R,q)
  =
  integral_0^1 x^(2q)a^(R+1) dx
  /
  integral_0^1 a^(R+1) dx.
```

Therefore:

```text
integral_0^1 a B_(R,q) dx = 0.
```

The factor `a^R` gives the endpoint vanishing needed for the `R`-fold boundary
contact class.

## Projection Signature Closed Form

For:

```text
P_R[k,q] = integral psi_k B_(R,q) a^4 dx,
```

the exact moment form is:

```text
P_R[k,q]
  =
  M(2k+2q,R+4) - r_k M(2k+2q-2,R+4)
  - c_(R,q)[M(2k,R+4) - r_k M(2k-2,R+4)].
```

where:

```text
M(n,p) = integral_0^1 x^n a^p dx.
```

## Rank Result

For tested truncations `R=0..5` and `N=2..7`, the matrix:

```text
rows: q=1..N
cols: k=1..N
entry: P_R[k,q]
```

has full rank.

```text
{rank_lines}
```

This means the projection hierarchy still resolves the balanced regular source
classes after the first admissibility constraint and its higher-contact
extensions are imposed.

## Shape

The signature matrices are not naively triangular in the tested `q,k` order:

```text
{triangular_lines}
```

So the relationship is not a simple mode-by-mode decoupling. The current best
description is:

```text
psi_k projections are full-rank diagnostics on the admissible balanced source
classes, not the same constraints as the admissibility ladder itself.
```

## Sample Signature Matrices

```text
{matrix_lines}
```
"""

out = Path(__file__).with_name("19_balanced_projection_signatures.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")


