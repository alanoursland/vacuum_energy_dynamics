#!/usr/bin/env python3
"""
make_30_generalized_admissibility_rows.py

Derive the row family adapted to the R-th endpoint-contact source class:

    chi_(R,k)(y) = y^k - ((2k-1)/(2k+2R+3)) y^(k-1).

Output:
    30_generalized_admissibility_rows.md
"""

from pathlib import Path
import sympy as sp


y = sp.symbols("y", real=True)


def chi(R, k):
    r = sp.Rational(2 * k - 1, 2 * k + 2 * R + 3)
    return sp.expand(y**k - r * y ** (k - 1))


def moment_coeff(R, j):
    """Coefficient vector for int a^(R+1) x^(2j) dx in y form."""
    # Use the polynomial expansion form so SymPy does not need to prove beta
    # recurrences symbolically.
    return sp.simplify(
        sum(
            sp.binomial(R + 1, ell) * (-1) ** ell / (2 * j + 2 * ell + 1)
            for ell in range(R + 2)
        )
    )


def coeff_vector(poly, degree):
    p = sp.Poly(sp.expand(poly), y)
    return sp.Matrix([p.coeff_monomial(y**j) for j in range(degree + 1)])


checks = []
rows = []

for R in range(0, 7):
    for N in range(1, 10):
        m = sp.Matrix([moment_coeff(R, j) for j in range(N + 1)])
        Chi = sp.Matrix([list(coeff_vector(chi(R, k), N).T) for k in range(1, N + 1)])

        if Chi.rank() != N:
            raise AssertionError(f"Chi rank failed R={R} N={N}")

        for i in range(N):
            dot = sp.simplify((Chi[i, :] * m)[0])
            if dot != 0:
                raise AssertionError(f"Chi not in R-kernel R={R} N={N} i={i}: {dot}")

        kernel_dim = len(sp.Matrix([list(m.T)]).nullspace())
        if kernel_dim != N:
            raise AssertionError(f"unexpected kernel dim R={R} N={N}: {kernel_dim}")

    rows.append((R, f"chi_(R,k)=y^k-((2k-1)/(2k+{2*R+3}))y^(k-1)"))

checks.append("generalized chi_(R,k) spans R-weighted first-admissibility kernel for R=0..6 N=1..9")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
row_lines = "\n".join(f"R={R}: {formula}" for R, formula in rows)

md = f"""# Synthesis Proof 30: Generalized Admissibility Rows

## Purpose

This report derives the row family adapted to the `R` endpoint-contact source
class.

For source class:

```text
S(y) = (1-y)^R P(y),
```

the first admissibility condition on `P` uses the moment weight:

```text
(1-y)^(R+1)y^(-1/2).
```

## Validated Checks

{validation_bullets}

## Generalized Row Family

The adapted row functions are:

```text
chi_(R,k)(y)
  =
  y^k - ((2k-1)/(2k+2R+3)) y^(k-1).
```

They span the finite coefficient-space kernel of:

```text
P -> integral_0^1 (1-y)^(R+1)y^(-1/2) P(y) dy.
```

Concrete rows:

```text
{row_lines}
```

## Interpretation

The original row family is the `R=0` case:

```text
psi_k = chi_(0,k).
```

Higher endpoint-contact classes have their own adapted row families, with the
denominator shifted from:

```text
2k+3
```

to:

```text
2k+2R+3.
```
"""

out = Path(__file__).with_name("30_generalized_admissibility_rows.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")


