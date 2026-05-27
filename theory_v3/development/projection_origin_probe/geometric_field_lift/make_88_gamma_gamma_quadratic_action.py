#!/usr/bin/env python3
"""
make_88_gamma_gamma_quadratic_action.py

Validate algebraic features of the quadratic Gamma-Gamma density:

    L_GG = eta^mn( Gamma^a_{m b} Gamma^b_{n a}
                   - Gamma^a_{m n} Gamma^b_{a b} )

for linearized Christoffel symbols.

The script evaluates the expression on controlled derivative ansatzes to show
that the geometric quadratic action is not the same as naive componentwise
positive Dirichlet strain.

Output:
    88_gamma_gamma_quadratic_action.md
"""

from pathlib import Path
import sympy as sp


dim = 4
eta = [-1, 1, 1, 1]
p = sp.symbols("p0:4", real=True)
a = sp.symbols("a", real=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def gamma_gamma_from_derivatives(dh):
    """dh[c][a][b] = partial_c h_ab, with h_ab symmetric."""

    def Gamma(up, low1, low2):
        return sp.Rational(1, 2) * eta[up] * (
            dh[low1][up][low2]
            + dh[low2][up][low1]
            - dh[up][low1][low2]
        )

    expr = 0
    for m in range(dim):
        for n in range(dim):
            eta_mn = eta[m] if m == n else 0
            if eta_mn == 0:
                continue
            term1 = sum(
                Gamma(aidx, m, bidx) * Gamma(bidx, n, aidx)
                for aidx in range(dim)
                for bidx in range(dim)
            )
            term2 = sum(
                Gamma(aidx, m, n) * Gamma(bidx, aidx, bidx)
                for aidx in range(dim)
                for bidx in range(dim)
            )
            expr += eta_mn * (term1 - term2)
    return sp.simplify(sp.factor(expr))


def componentwise_strain_from_derivatives(dh):
    expr = 0
    for c in range(dim):
        for i in range(dim):
            for j in range(dim):
                expr += sp.Rational(1, 2) * eta[c] * dh[c][i][j] * dh[c][i][j]
    return sp.simplify(sp.factor(expr))


checks = []

# Conformal ansatz h_ab = psi eta_ab, so partial_c h_ab = p_c eta_ab.
dh_conf = [
    [
        [
            p[c] * (eta[i] if i == j else 0)
            for j in range(dim)
        ]
        for i in range(dim)
    ]
    for c in range(dim)
]

gg_conf = gamma_gamma_from_derivatives(dh_conf)
strain_conf = componentwise_strain_from_derivatives(dh_conf)
p_sq = sum(eta[c] * p[c] ** 2 for c in range(dim))

require_equal("Gamma-Gamma conformal coefficient", gg_conf, sp.Rational(3, 2) * p_sq)
checks.append("Gamma-Gamma conformal coefficient")
require_equal("componentwise conformal strain coefficient", strain_conf, 2 * p_sq)
checks.append("componentwise conformal strain coefficient")
require_equal("conformal coefficient mismatch", strain_conf - gg_conf, sp.Rational(1, 2) * p_sq)
checks.append("conformal coefficient mismatch")

# Single off-diagonal perturbation h_12=h_21 with derivative along x^0 only.
zero = sp.Integer(0)
dh_off = [[[zero for _ in range(dim)] for _ in range(dim)] for _ in range(dim)]
dh_off[0][1][2] = a
dh_off[0][2][1] = a

gg_off = gamma_gamma_from_derivatives(dh_off)
strain_off = componentwise_strain_from_derivatives(dh_off)

require_equal("Gamma-Gamma offdiagonal time-gradient term", gg_off, sp.Rational(1, 2) * a**2)
checks.append("Gamma-Gamma offdiagonal time-gradient term")
require_equal("componentwise offdiagonal time-gradient term", strain_off, -a**2)
checks.append("componentwise offdiagonal time-gradient term")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 88: Gamma-Gamma Quadratic Action

## Purpose

This report validates controlled algebraic features of the quadratic
Gamma-Gamma density:

```text
L_GG = eta^mn(
  Gamma^a_mb Gamma^b_na
  - Gamma^a_mn Gamma^b_ab
).
```

The goal is not to derive the full action here. The goal is to compare the
geometric quadratic structure against naive componentwise strain.

## Validated Checks

{validation_bullets}

## Conformal Test

For:

```text
h_ab = psi eta_ab,
p_c = partial_c psi,
p^2 = eta^cd p_c p_d,
```

SymPy verifies:

```text
L_GG = (3/2)p^2.
```

The naive componentwise strain gives:

```text
L_component = 2 p^2.
```

So the coefficients differ.

## Off-Diagonal Test

For a single off-diagonal perturbation with time derivative:

```text
partial_0 h_12 = partial_0 h_21 = a,
```

SymPy verifies:

```text
L_GG = +a^2/2
L_component = -a^2.
```

## Interpretation

The geometric quadratic action is not the naive positive componentwise
Dirichlet strain. The scalar bridge can match the Newtonian sector, but the
full geometric lift needs the connection/Fierz-Pauli structure.
"""

out = Path(__file__).with_name("88_gamma_gamma_quadratic_action.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
