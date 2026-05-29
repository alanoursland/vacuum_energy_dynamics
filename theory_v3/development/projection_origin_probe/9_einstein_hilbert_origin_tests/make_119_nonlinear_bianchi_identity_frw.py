#!/usr/bin/env python3
"""
make_119_nonlinear_bianchi_identity_frw.py

Validate the contracted Bianchi identity on a nonlinear flat-FRW metric.

Output:
    119_nonlinear_bianchi_identity_frw.md
"""

from pathlib import Path
import sympy as sp


t, x, y, z = sp.symbols("t x y z")
coords = (t, x, y, z)
dim = 4
scale = sp.Function("a")(t)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


g = sp.diag(-1, scale**2, scale**2, scale**2)
g_inv = sp.diag(-1, scale**-2, scale**-2, scale**-2)


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
    term1 = sum(sp.diff(Gamma(c, a, b), coords[c]) for c in range(dim))
    term2 = sum(sp.diff(Gamma(c, a, c), coords[b]) for c in range(dim))
    term3 = sum(Gamma(c, a, b) * Gamma(d, c, d) for c in range(dim) for d in range(dim))
    term4 = sum(Gamma(d, a, c) * Gamma(c, b, d) for c in range(dim) for d in range(dim))
    return simplify_expr(term1 - term2 + term3 - term4)


Ricci_cov = [[Ricci(a, b) for b in range(dim)] for a in range(dim)]
R_scalar = simplify_expr(sum(g_inv[a, b] * Ricci_cov[a][b] for a in range(dim) for b in range(dim)))
Einstein_cov = [
    [simplify_expr(Ricci_cov[a][b] - sp.Rational(1, 2) * g[a, b] * R_scalar) for b in range(dim)]
    for a in range(dim)
]
Einstein_mixed = [
    [simplify_expr(sum(g_inv[a, c] * Einstein_cov[c][b] for c in range(dim))) for b in range(dim)]
    for a in range(dim)
]


def covariant_divergence_mixed(b):
    # nabla_a G^a_b = partial_a G^a_b
    #                 + Gamma^a_ac G^c_b
    #                 - Gamma^c_ab G^a_c.
    derivative_term = sum(sp.diff(Einstein_mixed[a][b], coords[a]) for a in range(dim))
    upper_connection_term = sum(
        Gamma(a, a, c) * Einstein_mixed[c][b] for a in range(dim) for c in range(dim)
    )
    lower_connection_term = sum(
        Gamma(c, a, b) * Einstein_mixed[a][c] for a in range(dim) for c in range(dim)
    )
    return simplify_expr(derivative_term + upper_connection_term - lower_connection_term)


checks = []

for b in range(dim):
    require_zero(f"contracted Bianchi component b={b}", covariant_divergence_mixed(b))

checks.append("contracted Bianchi identity on flat-FRW metric")

G00_expected = 3 * sp.diff(scale, t) ** 2 / scale**2
require_zero("FRW G_00 component", Einstein_cov[0][0] - G00_expected)
checks.append("FRW G_00 component")

Gii_expected = -2 * scale * sp.diff(scale, t, 2) - sp.diff(scale, t) ** 2
for i in (1, 2, 3):
    require_zero(f"FRW spatial Einstein component {i}{i}", Einstein_cov[i][i] - Gii_expected)

checks.append("FRW spatial Einstein components")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 119: Nonlinear Bianchi Identity on FRW

## Purpose

This report validates the contracted Bianchi identity on a nonlinear metric:

```text
ds^2 = -dt^2 + a(t)^2(dx^2 + dy^2 + dz^2).
```

## Validated Checks

{validation_bullets}

## Einstein Tensor Components

SymPy computes:

```text
G_00 = 3(a')^2/a^2
G_ii = -2aa'' - (a')^2
```

for each spatial diagonal component.

## Contracted Bianchi Identity

Using the mixed tensor:

```text
G^a_b = g^ac G_cb,
```

SymPy verifies all four components of:

```text
nabla_a G^a_b = 0.
```

## Interpretation

This is a nonlinear consistency check on the action-to-source gate. The EH
field tensor has the covariant divergence identity required by
diffeomorphism-invariant source coupling.
"""

out = Path(__file__).with_name("119_nonlinear_bianchi_identity_frw.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
