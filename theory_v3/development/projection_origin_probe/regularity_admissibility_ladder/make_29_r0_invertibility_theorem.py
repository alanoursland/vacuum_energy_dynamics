#!/usr/bin/env python3
"""
make_29_r0_invertibility_theorem.py

Prove the R=0 balanced projection invertibility mechanism:

    psi_1..psi_N and B_1..B_N are two bases of the same first-admissibility
    kernel, so their positive inner-product cross Gram matrix is invertible.

Output:
    29_r0_invertibility_theorem.md
"""

from pathlib import Path
import sympy as sp


y = sp.symbols("y", real=True)
x = sp.symbols("x", real=True)
a = 1 - x**2


def psi_y(k):
    r = sp.Rational(2 * k - 1, 2 * k + 3)
    return sp.expand(y**k - r * y ** (k - 1))


def c_q(q):
    return sp.Rational(3, (2 * q + 1) * (2 * q + 3))


def B_y(q):
    return sp.expand(y**q - c_q(q))


def coeff_vector(poly, degree):
    p = sp.Poly(sp.expand(poly), y)
    return sp.Matrix([p.coeff_monomial(y**j) for j in range(degree + 1)])


def integrate_y(poly):
    return sp.integrate(sp.expand(poly * (1 - y) ** 4 * y ** sp.Rational(-1, 2)), (y, 0, 1))


checks = []
rows = []

for N in range(1, 9):
    Psi = sp.Matrix([list(coeff_vector(psi_y(k), N).T) for k in range(1, N + 1)])
    Bal = sp.Matrix([list(coeff_vector(B_y(q), N).T) for q in range(1, N + 1)])

    if Psi.rank() != N:
        raise AssertionError(f"Psi rank failed N={N}")
    if Bal.rank() != N:
        raise AssertionError(f"Balanced rank failed N={N}")

    # Both live in the first-admissibility coefficient kernel.
    adm = sp.Matrix([sp.Rational(2, (2 * j + 1) * (2 * j + 3)) for j in range(N + 1)])
    for i in range(N):
        if sp.simplify((Psi[i, :] * adm)[0]) != 0:
            raise AssertionError(f"Psi not in kernel N={N} i={i}")
        if sp.simplify((Bal[i, :] * adm)[0]) != 0:
            raise AssertionError(f"Balanced not in kernel N={N} i={i}")

    # Cross Gram under positive Jacobi weight (1-y)^4 y^-1/2.
    G = sp.Matrix(
        [
            [sp.factor(integrate_y(psi_y(k) * B_y(q))) for q in range(1, N + 1)]
            for k in range(1, N + 1)
        ]
    )
    detG = sp.factor(G.det())
    if detG == 0:
        raise AssertionError(f"cross Gram determinant failed N={N}")

    rows.append((N, detG))

checks.append("psi and balanced rows both span first-admissibility kernel for N=1..8")
checks.append("R=0 cross Gram determinants are nonzero for N=1..8")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
row_lines = "\n".join(f"N={N}: det={detG}" for N, detG in rows)

md = f"""# Synthesis Proof 29: R=0 Invertibility Mechanism

## Purpose

This report isolates why the original balanced projection signatures are
invertible in the first-admissibility class.

## Validated Checks

{validation_bullets}

## Mechanism

In `y=x^2`, the original row functions are:

```text
psi_k(y) = y^k - ((2k-1)/(2k+3))y^(k-1).
```

The first balanced source basis is:

```text
B_q(y) = y^q - 3/((2q+1)(2q+3)).
```

Both families span the same finite coefficient-space kernel:

```text
ker[S -> integral_0^1 aS dx].
```

The projection matrix is their cross Gram matrix under the positive weight:

```text
(1-y)^4 y^(-1/2).
```

Because a positive inner product is nondegenerate on this finite kernel, the
cross Gram matrix between two bases of the same kernel is invertible.

## Determinant Evidence

```text
{row_lines}
```

## Interpretation

This gives a conceptual invertibility proof for the `R=0` balanced source
class. The original `psi_k` rows are exactly adapted to the first
admissibility condition.
"""

out = Path(__file__).with_name("29_r0_invertibility_theorem.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")


