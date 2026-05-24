#!/usr/bin/env python3
"""
make_22_psi_adapted_balanced_basis.py

Construct finite psi-adapted balanced source bases by inverting the balanced
projection signature matrix.

Output:
    22_psi_adapted_balanced_basis.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
a = 1 - x**2
w = a**4


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


def B_Rq(R, q):
    return sp.expand(a**R * (x ** (2 * q) - c_Rq(R, q)))


def projection(S, k):
    return sp.factor(integrate_poly(psi(k) * S * w))


checks = []
reports = []

for R in range(0, 4):
    N = 4
    B = [B_Rq(R, q) for q in range(1, N + 1)]
    P = sp.Matrix([[projection(B[q - 1], k) for q in range(1, N + 1)] for k in range(1, N + 1)])
    if P.det() == 0:
        raise AssertionError(f"projection signature not invertible R={R}")

    # Columns of C give combinations of B_q that produce unit psi signatures.
    C = P.inv()
    D = []
    for ell in range(N):
        D_ell = sp.expand(sum(C[q, ell] * B[q] for q in range(N)))
        D.append(D_ell)

    signature = sp.Matrix([[projection(D[ell], k) for ell in range(N)] for k in range(1, N + 1)])
    for i in range(N):
        for j in range(N):
            require_zero(f"adapted signature R={R} i={i} j={j}", signature[i, j] - (1 if i == j else 0))

    # These adapted basis elements should remain admissible.
    for ell, D_ell in enumerate(D):
        require_zero(f"adapted admissibility R={R} ell={ell}", integrate_poly(a * D_ell))

    reports.append((R, P, C, D, signature))

checks.append("finite psi-adapted balanced bases constructed for R=0..3, N=4")
checks.append("adapted basis has identity psi signature matrix")
checks.append("adapted basis remains first-admissible")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
report_lines = []
for R, P, C, D, signature in reports:
    d_lines = "\n".join(f"D_{ell + 1}(x) = {sp.factor(expr)}" for ell, expr in enumerate(D))
    report_lines.append(
        f"R={R}\nP=\n{P}\nC=P^-1=\n{C}\nAdapted basis:\n{d_lines}\nSignature=\n{signature}"
    )

md = f"""# Synthesis Proof 22: Psi-Adapted Balanced Basis

## Purpose

This report constructs finite balanced source bases adapted to the `psi_k`
projection diagnostics.

Given balanced sources:

```text
B_(R,q) = a^R[x^(2q)-c_(R,q)],
```

and signature matrix:

```text
P[k,q] = integral psi_k B_(R,q) a^4 dx,
```

define:

```text
D = B P^(-1).
```

Then:

```text
integral psi_k D_l a^4 = delta_(k,l).
```

## Validated Checks

{validation_bullets}

## Results

The construction was performed exactly for `R=0..3`, `N=4`.

```text
{chr(10).join(report_lines)}
```

## Interpretation

Although the naive balanced basis is not triangular under `psi_k` projection,
finite psi-adapted balanced bases exist by exact inversion of the full-rank
signature matrix.

This means the projection hierarchy can be used as coordinates on finite
balanced admissible source spaces.
"""

out = Path("22_psi_adapted_balanced_basis.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
