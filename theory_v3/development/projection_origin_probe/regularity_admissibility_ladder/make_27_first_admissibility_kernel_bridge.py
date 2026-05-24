#!/usr/bin/env python3
"""
make_27_first_admissibility_kernel_bridge.py

Prove that, on finite even-polynomial coefficient spaces, span{psi_1..psi_N}
is the coefficient-space kernel of the first admissibility functional:

    S -> integral_0^1 aS dx.

Output:
    27_first_admissibility_kernel_bridge.md
"""

from pathlib import Path
import sympy as sp


x, y = sp.symbols("x y", real=True)
a = 1 - x**2


def integrate_poly(expr):
    return sp.integrate(sp.expand(expr), (x, 0, 1))


def psi_y(k):
    r = sp.Rational(2 * k - 1, 2 * k + 3)
    return sp.expand(y**k - r * y ** (k - 1))


def coeff_vector(poly, degree):
    p = sp.Poly(sp.expand(poly), y)
    return sp.Matrix([p.coeff_monomial(y**j) for j in range(degree + 1)])


def admissibility_moment(j):
    return sp.factor(integrate_poly(a * x ** (2 * j)))


def missing_coeff(j):
    return sp.Rational(3, (2 * j + 1) * (2 * j + 3))


checks = []
rows = []

# int_0^1 a x^(2j) dx = 2/((2j+1)(2j+3)) = (2/3)m_j.
for j in range(0, 20):
    moment = admissibility_moment(j)
    expected = sp.Rational(2, (2 * j + 1) * (2 * j + 3))
    if sp.simplify(moment - expected) != 0:
        raise AssertionError(f"moment closed form failed j={j}: {moment}")
    if sp.simplify(moment - sp.Rational(2, 3) * missing_coeff(j)) != 0:
        raise AssertionError(f"moment/missing proportionality failed j={j}")
checks.append("first admissibility moment vector is proportional to psi missing direction")

for N in range(1, 14):
    Psi = sp.Matrix([list(coeff_vector(psi_y(k), N).T) for k in range(1, N + 1)])
    adm = sp.Matrix([admissibility_moment(j) for j in range(N + 1)])

    # Every psi row is in the coefficient kernel of the first admissibility
    # vector.
    for k in range(N):
        dot = (Psi[k, :] * adm)[0]
        if sp.simplify(dot) != 0:
            raise AssertionError(f"psi not in admissibility kernel N={N} row={k}: {dot}")

    if Psi.rank() != N:
        raise AssertionError(f"psi rank failed N={N}")

    # The kernel of adm^T has dimension N. Since psi rows are N independent
    # vectors in that kernel, they span it.
    adm_kernel_dim = len(sp.Matrix([list(adm.T)]).nullspace())
    if adm_kernel_dim != N:
        raise AssertionError(f"unexpected admissibility kernel dim N={N}: {adm_kernel_dim}")

    rows.append((N, Psi.rank(), adm_kernel_dim))

checks.append("span psi_1..psi_N equals first-admissibility coefficient kernel for N=1..13")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
row_lines = "\n".join(f"N={N}: rank(span psi)={rank}, dim(kernel C0)={dim}" for N, rank, dim in rows)

md = f"""# Synthesis Proof 27: First Admissibility Kernel Bridge

## Purpose

This report proves a precise bridge between the `psi_k` rows and the first
regularity/admissibility condition.

The first admissibility functional is:

```text
C0[S] = integral_0^1 aS dx.
```

On finite even-polynomial source spaces:

```text
S(x) = sum_j s_j x^(2j),
```

this is a coefficient functional.

## Validated Checks

{validation_bullets}

## Key Identity

For the coefficient of `x^(2j)`:

```text
integral_0^1 a x^(2j) dx
  = 2 / ((2j+1)(2j+3)).
```

This is proportional to the missing direction of the `psi_k` span:

```text
m_j = 3 / ((2j+1)(2j+3)).
```

Therefore the codimension-one direction missing from:

```text
span{{psi_1,...,psi_N}}
```

is exactly the first admissibility functional.

## Finite-Dimensional Result

For each tested `N`:

```text
span{{psi_1,...,psi_N}}
  =
ker(C0)
```

inside the coefficient space of degree `<=N` even polynomials.

```text
{row_lines}
```

## Interpretation

This is stronger than the earlier row-space comparison.

The full projected moment matrix is not identical to the low-order regularity
ladder under the `a^4` pairing, but the polynomial shape of the `psi_k` rows is
exactly adapted to the first admissibility condition:

```text
integral_0^1 aS dx = 0.
```

The row functions themselves span the finite coefficient-space kernel of this
condition.
"""

out = Path("27_first_admissibility_kernel_bridge.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
