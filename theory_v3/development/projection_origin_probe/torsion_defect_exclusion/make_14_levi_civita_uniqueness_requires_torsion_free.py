#!/usr/bin/env python3
"""
make_14_levi_civita_uniqueness_requires_torsion_free.py

Validate that metric compatibility plus torsion-free uniquely selects the
Levi-Civita connection for a symbolic diagonal 2D metric.

Output:
    14_levi_civita_uniqueness_requires_torsion_free.md
"""

from pathlib import Path
import sympy as sp


A, B, Ax, Ay, Bx, By = sp.symbols("A B Ax Ay Bx By")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


g = sp.Matrix([[A, 0], [0, B]])
ginv = sp.Matrix([[1 / A, 0], [0, 1 / B]])

derivs = {
    (0, 0, 0): Ax,
    (1, 0, 0): Ay,
    (0, 1, 1): Bx,
    (1, 1, 1): By,
    (0, 0, 1): 0,
    (1, 0, 1): 0,
    (0, 1, 0): 0,
    (1, 1, 0): 0,
}

G000, G001, G011, G100, G101, G111 = sp.symbols("G000 G001 G011 G100 G101 G111")


def Gamma(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return G000
    if a == 0 and {b, c} == {0, 1}:
        return G001
    if a == 0 and b == 1 and c == 1:
        return G011
    if a == 1 and b == 0 and c == 0:
        return G100
    if a == 1 and {b, c} == {0, 1}:
        return G101
    if a == 1 and b == 1 and c == 1:
        return G111
    raise ValueError((a, b, c))


equations = []
for c in range(2):
    for a in range(2):
        for b in range(2):
            residual = derivs[(c, a, b)]
            for d in range(2):
                residual -= Gamma(d, c, a) * g[d, b]
                residual -= Gamma(d, c, b) * g[a, d]
            equations.append(sp.Eq(simplify_expr(residual), 0))

unknowns = [G000, G001, G011, G100, G101, G111]
solution = sp.solve(equations, unknowns, dict=True)
if len(solution) != 1:
    raise AssertionError(f"expected unique solution, got {solution}")
solution = solution[0]


def d(coord, i, j):
    return derivs[(coord, i, j)]


expected = {}
for a in range(2):
    for b in range(2):
        for c in range(2):
            expr = 0
            for e in range(2):
                expr += ginv[a, e] * (d(b, e, c) + d(c, e, b) - d(e, b, c)) / 2
            expected[(a, b, c)] = simplify_expr(expr)

checks = {
    G000: expected[(0, 0, 0)],
    G001: expected[(0, 0, 1)],
    G011: expected[(0, 1, 1)],
    G100: expected[(1, 0, 0)],
    G101: expected[(1, 0, 1)],
    G111: expected[(1, 1, 1)],
}

for symbol, expr in checks.items():
    require_zero(f"Levi-Civita component {symbol}", solution[symbol] - expr)

md = f"""# Torsion Defect Exclusion 14: Levi-Civita Uniqueness Requires Torsion-Free

## Purpose

This proof records the positive connection selector.

Metric compatibility plus torsion-free uniquely selects the Levi-Civita
connection.

## Validated Checks

- symbolic metric-compatibility equations have one torsion-free solution: passed
- solution equals the Levi-Civita formula: passed

## Model

Use a symbolic diagonal 2D metric:

```text
g = diag(A,B)
```

with independent derivatives:

```text
A_x, A_y, B_x, B_y.
```

Starting with six torsion-free connection components, Sympy solves:

```text
nabla_c g_ab = 0.
```

The unique solution equals:

```text
Gamma^a_bc = 1/2 g^ad(
  partial_b g_dc
  + partial_c g_db
  - partial_d g_bc
).
```

For example:

```text
Gamma^0_00 = {solution[G000]}
Gamma^0_01 = {solution[G001]}
Gamma^1_01 = {solution[G101]}
Gamma^1_11 = {solution[G111]}
```

## Interpretation

Levi-Civita is not selected by metric data alone. It is selected by metric
compatibility together with the torsion-free gate.
"""

out = Path(__file__).with_name("14_levi_civita_uniqueness_requires_torsion_free.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Levi-Civita uniqueness gate passed.")
print(f"Wrote {out.resolve()}")

