#!/usr/bin/env python3
"""
make_26_psi_missing_direction_closed_form.py

Prove the closed form of the coefficient-space direction missing from
span{psi_1,...,psi_N} in y=x^2 coordinates.

Output:
    26_psi_missing_direction_closed_form.md
"""

from pathlib import Path
import sympy as sp


y = sp.symbols("y", real=True)


def psi_y(k):
    r = sp.Rational(2 * k - 1, 2 * k + 3)
    return sp.expand(y**k - r * y ** (k - 1))


def coeff_vector(poly, degree):
    p = sp.Poly(sp.expand(poly), y)
    return sp.Matrix([p.coeff_monomial(y**j) for j in range(degree + 1)])


def missing_coeff(j):
    return sp.Rational(3, (2 * j + 1) * (2 * j + 3))


checks = []
rows = []

for N in range(1, 15):
    m = sp.Matrix([missing_coeff(j) for j in range(N + 1)])
    for k in range(1, N + 1):
        dot = (coeff_vector(psi_y(k), N).T * m)[0]
        if sp.simplify(dot) != 0:
            raise AssertionError(f"closed missing vector failed N={N} k={k}: {dot}")

    M = sp.Matrix([list(coeff_vector(psi_y(k), N).T) for k in range(1, N + 1)])
    null = M.nullspace()
    if len(null) != 1:
        raise AssertionError(f"expected one null direction N={N}, got {len(null)}")

    # SymPy's null vector should be proportional to m.
    null_vec = null[0]
    scale = sp.simplify(null_vec[0] / m[0])
    if any(sp.simplify(null_vec[j] - scale * m[j]) != 0 for j in range(N + 1)):
        raise AssertionError(f"null vector not proportional to closed form N={N}")

    missing_poly = sp.factor(sum(m[j] * y**j for j in range(N + 1)))
    rows.append((N, missing_poly))

checks.append("closed missing vector annihilates psi_1..psi_N for N=1..14")
checks.append("closed missing vector spans the one-dimensional complement")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
row_lines = "\n".join(f"N={N}: m_N(y)={poly}" for N, poly in rows)

md = f"""# Synthesis Proof 26: Closed Missing Direction of the `psi_k` Span

## Purpose

In `y=x^2` coordinates:

```text
psi_k(y) = y^k - ((2k-1)/(2k+3))y^(k-1).
```

For each finite degree `N`, the span of `psi_1,...,psi_N` has codimension one
inside polynomials of degree `<=N`. This report proves the missing coefficient
direction.

## Validated Checks

{validation_bullets}

## Closed Form

The missing coefficient vector is:

```text
m_j = 3 / ((2j+1)(2j+3)),  j=0..N.
```

Equivalently:

```text
sum_j c_j y^j
```

is in the `psi` coefficient span only if its coefficient vector is orthogonal
to `m_j`.

The identity is immediate from:

```text
m_k / m_(k-1) = (2k-1)/(2k+3).
```

This is exactly the ratio in `psi_k`, so:

```text
<coeff(psi_k), m> = m_k - r_k m_(k-1) = 0.
```

## Missing Polynomials

```text
{row_lines}
```
"""

out = Path(__file__).with_name("26_psi_missing_direction_closed_form.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")


