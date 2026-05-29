#!/usr/bin/env python3
"""
make_33_general_cross_gram_invertibility.py

Validate the general-R cross-Gram invertibility mechanism between:

    chi_(R,k)
    y^q - c_(R,q)

under the positive Jacobi weight:

    (1-y)^(R+4)y^(-1/2).

Output:
    33_general_cross_gram_invertibility.md
"""

from pathlib import Path
import sympy as sp


y = sp.symbols("y", real=True)


def integrate_y(expr):
    return sp.integrate(sp.expand(expr), (y, 0, 1))


def chi(R, k):
    ratio = sp.Rational(2 * k - 1, 2 * k + 2 * R + 3)
    return sp.expand(y**k - ratio * y ** (k - 1))


def c_Rq(R, q):
    return sp.factor(
        sp.beta(q + sp.Rational(1, 2), R + 2)
        / sp.beta(sp.Rational(1, 2), R + 2)
    )


def balanced(R, q):
    return sp.expand(y**q - c_Rq(R, q))


checks = []
rows = []

for R in range(0, 5):
    weight = (1 - y) ** (R + 4) * y ** sp.Rational(-1, 2)
    for N in range(1, 6):
        G = sp.Matrix(
            [
                [sp.factor(integrate_y(chi(R, k) * balanced(R, q) * weight)) for q in range(1, N + 1)]
                for k in range(1, N + 1)
            ]
        )
        detG = sp.factor(G.det())
        if detG == 0:
            raise AssertionError(f"cross Gram determinant vanished R={R} N={N}")

        if N <= 4:
            rows.append((R, N, detG))

checks.append("general-R chi/balanced cross Gram determinants nonzero for R=0..4 N=1..5")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
row_lines = "\n".join(f"R={R}, N={N}: det={detG}" for R, N, detG in rows)

md = f"""# Regularity Ladder Proof 33: General Cross-Gram Invertibility

## Purpose

This report tests the cross-Gram invertibility mechanism for the generalized
endpoint-contact row family.

## Objects

Rows:

```text
chi_(R,k)(y)
  = y^k - ((2k-1)/(2k+2R+3))y^(k-1).
```

Balanced source coordinates:

```text
B_(R,q)(y) = y^q - c_(R,q).
```

Pairing weight:

```text
(1-y)^(R+4)y^(-1/2).
```

## Validated Checks

{validation_bullets}

## Determinant Data

Small exact determinants:

```text
{row_lines}
```

## Interpretation

For each tested `R,N`, the generalized rows and balanced source coordinates
produce an invertible cross-Gram matrix.

Together with the kernel theorem, this supports the general picture:

```text
endpoint-contact level R
  -> adapted row family chi_(R,k)
  -> balanced source basis y^q-c_(R,q)
  -> nondegenerate finite coordinate pairing.
```
"""

out = Path(__file__).with_name("33_general_cross_gram_invertibility.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")


