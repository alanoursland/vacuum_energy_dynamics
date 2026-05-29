#!/usr/bin/env python3
"""
make_21_gamma_gamma_strain_action_candidate.py

Validate that the Einstein-Hilbert density splits into a local quadratic
connection-strain density plus a boundary divergence on a controlled nonlinear
metric.

Output:
    21_gamma_gamma_strain_action_candidate.md
"""

from pathlib import Path
import sympy as sp


x, y, z = sp.symbols("x y z", real=True)
coords = (x, y, z)
dim = 3
A = sp.Function("A")(x)
B = sp.Function("B")(x)
C = sp.Function("C")(x)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


g = sp.diag(A, B, C)
g_inv = sp.simplify(g.inv())
sqrt_g = sp.sqrt(A * B * C)


def Gamma(a, b, c):
    return simplify_expr(
        sp.Rational(1, 2)
        * sum(
            g_inv[a, d]
            * (
                sp.diff(g[d, c], coords[b])
                + sp.diff(g[d, b], coords[c])
                - sp.diff(g[b, c], coords[d])
            )
            for d in range(dim)
        )
    )


def Ricci(a, b):
    expr = 0
    for c in range(dim):
        expr += sp.diff(Gamma(c, a, b), coords[c]) - sp.diff(Gamma(c, a, c), coords[b])
        for d in range(dim):
            expr += Gamma(c, c, d) * Gamma(d, a, b) - Gamma(c, b, d) * Gamma(d, a, c)
    return simplify_expr(expr)


R = simplify_expr(sum(g_inv[a, b] * Ricci(a, b) for a in range(dim) for b in range(dim)))
eh_density = simplify_expr(sqrt_g * R)

gamma_gamma_density = 0
for a in range(dim):
    for b in range(dim):
        for c in range(dim):
            for d in range(dim):
                gamma_gamma_density += sqrt_g * g_inv[a, b] * (
                    Gamma(c, a, d) * Gamma(d, b, c)
                    - Gamma(c, a, b) * Gamma(d, c, d)
                )
gamma_gamma_density = simplify_expr(gamma_gamma_density)

V = []
for c in range(dim):
    term = 0
    for a in range(dim):
        for b in range(dim):
            term += g_inv[a, b] * Gamma(c, a, b) - g_inv[c, b] * Gamma(a, a, b)
    V.append(simplify_expr(sqrt_g * term))

boundary_divergence = simplify_expr(sum(sp.diff(V[c], coords[c]) for c in range(dim)))

checks = []

require_equal("EH equals Gamma-Gamma plus boundary divergence", eh_density, gamma_gamma_density + boundary_divergence)
checks.append("EH equals Gamma-Gamma plus boundary divergence")

expected_gamma_gamma = sqrt_g * sp.diff(B, x) * sp.diff(C, x) / (2 * A * B * C)
require_equal("Gamma-Gamma density is first-derivative strain", gamma_gamma_density, expected_gamma_gamma)
checks.append("Gamma-Gamma density is first-derivative strain")

for func in (A, B, C):
    if gamma_gamma_density.has(sp.diff(func, x, 2)):
        raise AssertionError("Gamma-Gamma density contains second derivatives")
checks.append("Gamma-Gamma density has no second metric derivatives")

if not eh_density.has(sp.diff(B, x, 2)) and not eh_density.has(sp.diff(C, x, 2)):
    raise AssertionError("EH density should contain second derivatives before boundary split")
checks.append("EH density contains second derivatives before boundary split")

require_equal("boundary vector only x component for warped ansatz", V[1] + V[2], 0)
checks.append("boundary vector only x component for warped ansatz")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 21: Gamma-Gamma Strain Action Candidate

## Purpose

This report validates the metric action candidate suggested by the origin
chain:

```text
connection strain squared
  + boundary bookkeeping
  = Einstein-Hilbert curvature density.
```

## Validated Checks

{validation_bullets}

## Nonlinear Test Metric

Use:

```text
g = diag(A(x), B(x), C(x)).
```

SymPy verifies:

```text
sqrt(g) R
  =
  sqrt(g) g^ab(
    Gamma^c_ad Gamma^d_bc
    - Gamma^c_ab Gamma^d_cd
  )
  + partial_c V^c.
```

## Connection-Strain Density

For this ansatz, the Gamma-Gamma density is:

```text
sqrt(g) B'(x) C'(x) / [2 A(x) B(x) C(x)].
```

It contains only first derivatives of the metric. The second derivatives in
`sqrt(g)R` are carried by the boundary divergence.

## Interpretation

This is the nonlinear metric analogue of the scalar strain/boundary split. The
bulk strain is quadratic in the local comparison rule, while the boundary term
keeps the curvature form variationally well-posed.
"""

out = Path(__file__).with_name("21_gamma_gamma_strain_action_candidate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
