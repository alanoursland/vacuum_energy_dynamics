#!/usr/bin/env python3
"""
make_12_orthogonal_polynomial_nonidentification.py

Check that the Gegenbauer/Jacobi weight context does not directly identify
the row functions psi_k as the corresponding orthogonal polynomials.

Output:
    12_orthogonal_polynomial_nonidentification.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
y = sp.symbols("y", real=True)
lam = sp.Rational(9, 2)
a = 1 - x**2
w = a**4


def simplify_expr(expr):
    out = sp.simplify(expr)
    out = sp.factor(out)
    out = sp.cancel(out)
    out = sp.factor(out)
    return out


def require_not_zero(label, expr):
    result = simplify_expr(expr)
    if result == 0:
        raise AssertionError(f"{label} unexpectedly vanished")


def monic_in_x(poly):
    poly = sp.Poly(sp.expand(poly), x)
    return sp.expand(poly.as_expr() / poly.LC())


def monic_in_y(poly):
    poly = sp.Poly(sp.expand(poly), y)
    return sp.expand(poly.as_expr() / poly.LC())


def psi(k):
    r = sp.Rational(2 * k - 1, 2 * k + 3)
    return x ** (2 * k) - r * x ** (2 * k - 2)


def psi_y(k):
    r = sp.Rational(2 * k - 1, 2 * k + 3)
    return y**k - r * y ** (k - 1)


checks = []
rows = []

# Gegenbauer context on [-1,1] uses C_n^(9/2).  Compare monic psi_k to the
# even Gegenbauer polynomial C_(2k)^(9/2), not as a claim but as a guardrail.
for K in range(1, 5):
    psi_monic = monic_in_x(psi(K))
    geg_monic = monic_in_x(sp.gegenbauer(2 * K, lam, x))
    diff = simplify_expr(psi_monic - geg_monic)
    require_not_zero(f"psi_{K} not Gegenbauer C_{2*K}", diff)
    rows.append((f"psi_{K} vs C_{2*K}^(9/2)", diff))
checks.append("psi_k differs from monic Gegenbauer C_(2k)^(9/2) for k=1..4")

# In y=x^2, the induced weight is y^(-1/2)(1-y)^4 on [0,1].  The degree-k
# orthogonal polynomial is a shifted Jacobi polynomial with parameters
# alpha=4, beta=-1/2.  Compare monic forms.
for K in range(1, 5):
    psi_monic_y = monic_in_y(psi_y(K))
    shifted_jacobi = sp.jacobi(K, 4, sp.Rational(-1, 2), 1 - 2 * y)
    jacobi_monic_y = monic_in_y(shifted_jacobi)
    diff = simplify_expr(psi_monic_y - jacobi_monic_y)
    require_not_zero(f"psi_y_{K} not shifted Jacobi", diff)
    rows.append((f"psi_{K}(y) vs shifted Jacobi P_{K}^(4,-1/2)", diff))
checks.append("psi_k differs from shifted Jacobi family in y=x^2 for k=1..4")

# Same-weight orthogonality guardrail:
#
# psi_k is not the degree-k monic orthogonal polynomial under y^(-1/2)(1-y)^4
# because even the constant moment does not vanish in general.
moment_residuals = []
for K in range(1, 6):
    residual = sp.factor(sp.integrate(sp.expand(psi(K) * w), (x, 0, 1)))
    if residual == 0:
        raise AssertionError(f"same-weight constant residual vanished for K={K}")
    moment_residuals.append((K, residual))
checks.append("same-weight constant orthogonality fails for k=1..5")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
diff_lines = "\n".join(f"{label}: {diff}" for label, diff in rows)
moment_lines = "\n".join(f"k={K}: integral psi_k a^4 dx = {res}" for K, res in moment_residuals)

md = f"""# Synthesis Proof 12: Orthogonal-Polynomial Non-Identification

## Purpose

This report checks a guardrail from `speculative_synthesis.md`:

```text
w=a^4 lies near Gegenbauer/Jacobi structure, but psi_k is not directly
identified as the corresponding orthogonal-polynomial family.
```

## Validated Checks

{validation_bullets}

## Gegenbauer Comparison

The full-interval weight:

```text
(1-x^2)^4
```

corresponds to Gegenbauer parameter:

```text
lambda = 9/2.
```

Comparing monic forms gives nonzero differences:

```text
{diff_lines}
```

## Same-Weight Orthogonality Check

If `psi_k` were the direct same-weight degree-k orthogonal row in the
`y=x^2` picture, its constant moment under `a^4` would vanish. It does not:

```text
{moment_lines}
```

Thus the orthogonal-polynomial setting is contextual. It is not a direct
identification of the row functions.
"""

out = Path("12_orthogonal_polynomial_nonidentification.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
