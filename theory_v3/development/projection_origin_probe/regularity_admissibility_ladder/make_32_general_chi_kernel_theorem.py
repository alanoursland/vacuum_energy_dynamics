#!/usr/bin/env python3
"""
make_32_general_chi_kernel_theorem.py

Prove the finite-dimensional theorem:

    span{chi_(R,1),...,chi_(R,N)}
      =
    ker[C_R]

where:

    C_R[P] = integral_0^1 P(y) (1-y)^(R+1)y^(-1/2) dy

on polynomials of degree <= N.

Output:
    32_general_chi_kernel_theorem.md
"""

from pathlib import Path
import sympy as sp


y = sp.symbols("y", real=True)


def moment(R, j):
    """C_R[y^j], up to the common positive factor 1/2 from x -> y."""
    return sp.simplify(
        sum(
            sp.binomial(R + 1, ell) * (-1) ** ell / (2 * j + 2 * ell + 1)
            for ell in range(R + 2)
        )
    )


def chi(R, k):
    ratio = sp.Rational(2 * k - 1, 2 * k + 2 * R + 3)
    return sp.expand(y**k - ratio * y ** (k - 1))


def coeff_vector(poly, degree):
    p = sp.Poly(sp.expand(poly), y)
    return sp.Matrix([p.coeff_monomial(y**j) for j in range(degree + 1)])


checks = []
rows = []

for R in range(0, 10):
    for N in range(1, 13):
        c_vec = sp.Matrix([moment(R, j) for j in range(N + 1)])
        rows_chi = sp.Matrix([list(coeff_vector(chi(R, k), N).T) for k in range(1, N + 1)])

        # chi rows are independent.
        if rows_chi.rank() != N:
            raise AssertionError(f"chi rank failed R={R} N={N}")

        # chi rows lie in ker C_R.
        for i in range(N):
            dot = sp.simplify((rows_chi[i, :] * c_vec)[0])
            if dot != 0:
                raise AssertionError(f"chi row not in C_R kernel R={R} N={N} i={i}: {dot}")

        # ker C_R has dimension N in degree <=N space.
        kernel_dim = len(sp.Matrix([list(c_vec.T)]).nullspace())
        if kernel_dim != N:
            raise AssertionError(f"C_R kernel dim failed R={R} N={N}: {kernel_dim}")

    rows.append((R, f"chi_(R,k)=y^k-((2k-1)/(2k+{2*R+3}))y^(k-1)"))

checks.append("span chi_(R,1..N)=ker C_R verified for R=0..9 N=1..12")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
row_lines = "\n".join(f"R={R}: {formula}" for R, formula in rows)

md = f"""# Regularity Ladder Proof 32: General `chi` Kernel Theorem

## Purpose

This report proves the finite-dimensional kernel theorem for the endpoint-contact
ladder row family.

## Theorem

For each `R >= 0`, define:

```text
C_R[P] = integral_0^1 P(y)(1-y)^(R+1)y^(-1/2) dy.
```

On polynomials of degree `<=N`,

```text
span{{chi_(R,1),...,chi_(R,N)}} = ker C_R,
```

where:

```text
chi_(R,k)(y)
  = y^k - ((2k-1)/(2k+2R+3))y^(k-1).
```

## Validated Checks

{validation_bullets}

## Row Family

```text
{row_lines}
```

## Proof Mechanism

The moment vector satisfies:

```text
C_R[y^k] / C_R[y^(k-1)]
  = (2k-1)/(2k+2R+3).
```

Therefore:

```text
C_R[chi_(R,k)] = 0.
```

The `N` rows `chi_(R,1)..chi_(R,N)` are independent because each has a unique
highest-degree term. Since `ker C_R` has dimension `N` inside the `N+1`
dimensional degree-`<=N` space, the rows span the whole kernel.
"""

out = Path(__file__).with_name("32_general_chi_kernel_theorem.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")


