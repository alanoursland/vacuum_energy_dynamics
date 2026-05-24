#!/usr/bin/env python3
"""
make_20_balanced_signature_factorization.py

Factor the balanced projection signature matrix as:

    P_R = M_R T_R

where M_R is the projection matrix on raw monomials under weight a^(R+4), and
T_R is the balancing transform x^(2q) -> x^(2q) - c_(R,q).

Output:
    20_balanced_signature_factorization.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
a = 1 - x**2


def integrate_poly(expr):
    return sp.integrate(sp.expand(expr), (x, 0, 1))


def simplify_expr(expr):
    out = sp.simplify(expr)
    out = sp.factor(out)
    out = sp.cancel(out)
    out = sp.factor(out)
    return out


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def psi(k):
    r = sp.Rational(2 * k - 1, 2 * k + 3)
    return x ** (2 * k) - r * x ** (2 * k - 2)


def c_Rq(R, q):
    return sp.factor(integrate_poly(a ** (R + 1) * x ** (2 * q)) / integrate_poly(a ** (R + 1)))


checks = []
factor_rows = []

for R in range(0, 5):
    for N in range(2, 6):
        # M_R rows k=1..N, raw columns j=0..N.
        M = sp.Matrix(
            [
                [sp.factor(integrate_poly(psi(k) * x ** (2 * j) * a ** (R + 4))) for j in range(0, N + 1)]
                for k in range(1, N + 1)
            ]
        )

        # T_R columns q=1..N, representing x^(2q)-c_(R,q).
        T = sp.zeros(N + 1, N)
        for q in range(1, N + 1):
            T[0, q - 1] = -c_Rq(R, q)
            T[q, q - 1] = 1

        P_factored = M * T
        P_direct = sp.Matrix(
            [
                [
                    sp.factor(
                        integrate_poly(
                            psi(k) * a**R * (x ** (2 * q) - c_Rq(R, q)) * a**4
                        )
                    )
                    for q in range(1, N + 1)
                ]
                for k in range(1, N + 1)
            ]
        )

        diff = P_factored - P_direct
        for entry_index, entry in enumerate(diff):
            require_zero(f"factorization R={R} N={N} entry={entry_index}", entry)

        if T.rank() != N:
            raise AssertionError(f"T lost rank R={R} N={N}: {T.rank()}")
        if P_direct.rank() != N:
            raise AssertionError(f"P lost rank R={R} N={N}: {P_direct.rank()}")

        factor_rows.append((R, N, M.rank(), T.rank(), P_direct.rank()))

checks.append("P_R = M_R T_R verified for R=0..4 N=2..5")
checks.append("balancing transform T_R has full column rank")
checks.append("balanced projection signatures have full tested rank")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
factor_lines = "\n".join(
    f"R={R}, N={N}: rank(M_R)={m_rank}, rank(T_R)={t_rank}, rank(P_R)={p_rank}"
    for R, N, m_rank, t_rank, p_rank in factor_rows
)

md = f"""# Synthesis Proof 20: Balanced Signature Factorization

## Purpose

This report factors the balanced source projection signatures.

Balanced sources are:

```text
B_(R,q) = a^R [x^(2q) - c_(R,q)].
```

The signature matrix is:

```text
P_R[k,q] = integral psi_k B_(R,q) a^4 dx.
```

## Validated Checks

{validation_bullets}

## Factorization

Define the raw projection matrix:

```text
M_R[k,j] = integral psi_k x^(2j) a^(R+4) dx
```

with `j=0..N`, and define the balancing transform `T_R` by:

```text
T_R[:,q] = e_q - c_(R,q)e_0.
```

Then:

```text
P_R = M_R T_R.
```

This explains the balanced signatures as ordinary monomial projection rows
after a source-space balancing transform.

## Rank Data

```text
{factor_lines}
```

## Interpretation

The balanced projection signatures do not require a new projection mechanism.
They are the original moment/projection mechanism composed with the
admissibility balancing transform.
"""

out = Path("20_balanced_signature_factorization.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
