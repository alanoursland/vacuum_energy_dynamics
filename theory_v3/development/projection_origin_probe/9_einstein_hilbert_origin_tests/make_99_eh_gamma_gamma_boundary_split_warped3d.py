#!/usr/bin/env python3
"""
make_99_eh_gamma_gamma_boundary_split_warped3d.py

Validate the Einstein-Hilbert / Gamma-Gamma plus boundary-divergence split on a
controlled nonlinear 3D metric:

    g = diag(A(x), B(x), C(x)).

This is a nontrivial symbolic check of:

    sqrt(g) R = sqrt(g) g^ab( Gamma^c_ad Gamma^d_bc
                             - Gamma^c_ab Gamma^d_cd )
                + partial_c V^c

with:

    V^c = sqrt(g)(g^ab Gamma^c_ab - g^cb Gamma^a_ab).

Output:
    99_eh_gamma_gamma_boundary_split_warped3d.md
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
require_equal("EH Gamma-Gamma boundary split", eh_density, gamma_gamma_density + boundary_divergence)
checks.append("EH density equals Gamma-Gamma density plus boundary divergence")

require_equal(
    "nonzero Gamma-Gamma density",
    gamma_gamma_density,
    sqrt_g * sp.diff(B, x) * sp.diff(C, x) / (2 * A * B * C),
)
checks.append("nonzero Gamma-Gamma density")

require_equal(
    "boundary vector only x component",
    V[1] + V[2],
    0,
)
checks.append("boundary vector only has x component for this ansatz")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 99: EH/Gamma-Gamma Boundary Split

## Purpose

This report validates the Einstein-Hilbert split into a quadratic connection
density plus a boundary divergence on a controlled nonlinear metric:

```text
g = diag(A(x), B(x), C(x)).
```

## Validated Checks

{validation_bullets}

## Identity Tested

SymPy verifies:

```text
sqrt(g) R
  =
  sqrt(g) g^ab(
    Gamma^c_ad Gamma^d_bc
    - Gamma^c_ab Gamma^d_cd
  )
  + partial_c V^c,
```

where:

```text
V^c =
  sqrt(g)(
    g^ab Gamma^c_ab
    - g^cb Gamma^a_ab
  ).
```

For the tested metric, the Gamma-Gamma density is nonzero:

```text
sqrt(g) B'(x) C'(x) / [2 A(x) B(x) C(x)].
```

## Interpretation

This is the first nonlinear action-origin bridge:

```text
Einstein-Hilbert curvature action
  =
  quadratic connection-strain action
  + boundary bookkeeping.
```

It supports treating the connection as the nonlinear geometric strain object,
while keeping boundary terms explicit.
"""

out = Path(__file__).with_name("99_eh_gamma_gamma_boundary_split_warped3d.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
