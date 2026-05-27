#!/usr/bin/env python3
"""
make_24_span_complement_tests.py

Test the span/complement structure of psi_k rows in y=x^2 coordinates.

Output:
    24_span_complement_tests.md
"""

from pathlib import Path
import sympy as sp


y = sp.symbols("y", real=True)


def psi_y(k):
    r = sp.Rational(2 * k - 1, 2 * k + 3)
    return sp.expand(y ** k - r * y ** (k - 1))


def poly_coeff_row(poly, degree):
    p = sp.Poly(sp.expand(poly), y)
    return [p.coeff_monomial(y**j) for j in range(degree + 1)]


checks = []
rows = []

for N in range(1, 11):
    # psi_1..psi_N live in polynomials of degree <= N with no constant-free
    # restriction? psi_1 includes y^0, and the family should span degree <=N
    # except possibly a one-dimensional complement depending on constraints.
    M = sp.Matrix([poly_coeff_row(psi_y(k), N) for k in range(1, N + 1)])
    rank = M.rank()

    if rank != N:
        raise AssertionError(f"psi span rank failed N={N}: {rank}")

    # Nullspace of coefficient matrix transpose gives the polynomial
    # coefficient vector orthogonal to psi span under raw coefficient pairing.
    # This identifies the missing direction in coefficient space.
    missing = M.nullspace()
    if len(missing) != 1:
        raise AssertionError(f"expected one missing coefficient direction N={N}, got {len(missing)}")

    missing_vec = missing[0]
    missing_poly = sp.expand(sum(missing_vec[j] * y**j for j in range(N + 1)))

    # Verify all psi_k have zero coefficient-dot against missing_vec.
    for k in range(1, N + 1):
        coeff = sp.Matrix(poly_coeff_row(psi_y(k), N))
        dot = (coeff.T * missing_vec)[0]
        if sp.simplify(dot) != 0:
            raise AssertionError(f"missing direction failed N={N} k={k}: {dot}")

    rows.append((N, rank, sp.factor(missing_poly)))

checks.append("psi_y span has dimension N inside degree <=N polynomials")
checks.append("one coefficient-space complement direction identified for N=1..10")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
row_lines = "\n".join(f"N={N}: rank={rank}, missing coefficient direction={poly}" for N, rank, poly in rows)

md = f"""# Synthesis Proof 24: Span and Complement Tests

## Purpose

This report tests the finite span of:

```text
psi_k(y) = y^k - ((2k-1)/(2k+3))y^(k-1)
```

inside the polynomial space of degree `<= N`.

## Validated Checks

{validation_bullets}

## Result

For each tested `N`, the family:

```text
psi_1, ..., psi_N
```

has rank `N` inside the `N+1` dimensional space of polynomials of degree
`<=N`.

Thus the row tests span a codimension-one subspace in this coefficient-space
sense.

The missing coefficient directions are:

```text
{row_lines}
```

## Interpretation

The `psi_k` family is not arbitrary: in `y` coordinates it forms a structured
degree-lowering row family with exactly one missing direction at each finite
degree.

This supports looking for a determinant/invertibility proof via polynomial
filtration and codimension-one balancing constraints.
"""

out = Path(__file__).with_name("24_span_complement_tests.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")


