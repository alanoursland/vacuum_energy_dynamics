#!/usr/bin/env python3
"""
make_82_linearized_ricci_tensor.py

Validate the linearized Ricci tensor formula from the linearized Christoffel
symbol in flat Minkowski background.

Output:
    82_linearized_ricci_tensor.md
"""

from pathlib import Path
import sympy as sp


t, x, y, z = sp.symbols("t x y z", real=True)
coords = (t, x, y, z)
eta = [-1, 1, 1, 1]
dim = 4


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def hsym(a, b):
    i, j = sorted((a, b))
    return sp.Function(f"h{i}{j}")(*coords)


def d_up(a, expr):
    return eta[a] * sp.diff(expr, coords[a])


def box(expr):
    return sum(eta[a] * sp.diff(expr, coords[a], 2) for a in range(dim))


checks = []

h = [[hsym(a, b) for b in range(dim)] for a in range(dim)]
trace_h = sum(eta[a] * h[a][a] for a in range(dim))


def Gamma(up, low1, low2):
    return sp.Rational(1, 2) * eta[up] * (
        sp.diff(h[up][low2], coords[low1])
        + sp.diff(h[up][low1], coords[low2])
        - sp.diff(h[low1][low2], coords[up])
    )


def Ricci_from_gamma(a, b):
    return sum(
        sp.diff(Gamma(c, a, b), coords[c]) - sp.diff(Gamma(c, a, c), coords[b])
        for c in range(dim)
    )


def Ricci_formula(a, b):
    term1 = sum(d_up(c, sp.diff(h[b][c], coords[a])) for c in range(dim))
    term2 = sum(d_up(c, sp.diff(h[a][c], coords[b])) for c in range(dim))
    return sp.Rational(1, 2) * (
        term1 + term2 - box(h[a][b]) - sp.diff(trace_h, coords[a], coords[b])
    )


for a in range(dim):
    for b in range(dim):
        require_equal(
            f"linearized Ricci formula component {a}{b}",
            Ricci_from_gamma(a, b),
            Ricci_formula(a, b),
        )

checks.append("linearized Ricci formula verified for all 16 components")

for a in range(dim):
    for b in range(dim):
        require_equal(f"Ricci symmetry {a}{b}", Ricci_formula(a, b), Ricci_formula(b, a))

checks.append("linearized Ricci symmetry verified")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 82: Linearized Ricci Tensor

## Purpose

This report validates the standard linearized Ricci tensor formula from the
linearized Christoffel symbol on a flat Minkowski background.

## Validated Checks

{validation_bullets}

## Linearized Christoffel Symbol

```text
Gamma^a_bc
  =
  1/2 eta^ad(
    partial_b h_dc
    + partial_c h_db
    - partial_d h_bc
  ).
```

## Linearized Ricci Tensor

Starting from:

```text
R_ab = partial_c Gamma^c_ab - partial_b Gamma^c_ac,
```

SymPy verifies:

```text
R_ab
  =
  1/2(
    partial^c partial_a h_bc
    + partial^c partial_b h_ac
    - box h_ab
    - partial_a partial_b h
  ).
```

## Interpretation

This is the first real geometric operator in the lift. The naive componentwise
Laplacian from proof `76` is not the Ricci tensor; Ricci mixes trace and
divergence terms.
"""

out = Path(__file__).with_name("82_linearized_ricci_tensor.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
