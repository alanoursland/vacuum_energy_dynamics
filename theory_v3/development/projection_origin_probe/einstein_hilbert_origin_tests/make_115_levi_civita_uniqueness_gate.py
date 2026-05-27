#!/usr/bin/env python3
"""
make_115_levi_civita_uniqueness_gate.py

Validate that a torsion-free, metric-compatible connection is uniquely the
Levi-Civita connection for a nontrivial diagonal 2D metric.

Output:
    115_levi_civita_uniqueness_gate.md
"""

from pathlib import Path
import sympy as sp


A, B = sp.symbols("A B", nonzero=True)
Ax, Ay, Bx, By = sp.symbols("A_x A_y B_x B_y")
dim = 2


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


g = sp.Matrix([[A, 0], [0, B]])
g_inv = sp.Matrix([[1 / A, 0], [0, 1 / B]])


def dg(a, b, c):
    if (a, b, c) == (0, 0, 0):
        return Ax
    if (a, b, c) == (0, 0, 1):
        return Ay
    if (a, b, c) == (1, 1, 0):
        return Bx
    if (a, b, c) == (1, 1, 1):
        return By
    return sp.Integer(0)


unknowns = {}
unknown_list = []
for a in range(dim):
    for b in range(dim):
        for c in range(b, dim):
            symbol = sp.symbols(f"G{a}{b}{c}")
            unknowns[(a, b, c)] = symbol
            unknown_list.append(symbol)


def Gamma_unknown(a, b, c):
    if b <= c:
        return unknowns[(a, b, c)]
    return unknowns[(a, c, b)]


equations = []
for c in range(dim):
    for a in range(dim):
        for b in range(a, dim):
            metric_compatibility = (
                dg(a, b, c)
                - sum(Gamma_unknown(d, c, a) * g[d, b] for d in range(dim))
                - sum(Gamma_unknown(d, c, b) * g[a, d] for d in range(dim))
            )
            equations.append(sp.Eq(metric_compatibility, 0))

solution = sp.solve(equations, unknown_list, dict=True)
if len(solution) != 1:
    raise AssertionError(f"expected unique connection solution, got {len(solution)}")

solution = solution[0]
if set(solution.keys()) != set(unknown_list):
    missing = set(unknown_list) - set(solution.keys())
    raise AssertionError(f"connection solution is not complete: missing {missing}")


def Gamma_lc(a, b, c):
    return simplify_expr(
        sp.Rational(1, 2)
        * sum(
            g_inv[a, d]
            * (
                dg(d, c, b)
                + dg(d, b, c)
                - dg(b, c, d)
            )
            for d in range(dim)
        )
    )


checks = []

for a in range(dim):
    for b in range(dim):
        for c in range(b, dim):
            unknown = Gamma_unknown(a, b, c)
            require_equal(
                f"unique connection component {a}{b}{c}",
                solution[unknown],
                Gamma_lc(a, b, c),
            )

checks.append("torsion-free metric-compatible solution equals Levi-Civita")

for c in range(dim):
    for a in range(dim):
        for b in range(a, dim):
            residual = (
                dg(a, b, c)
                - sum(Gamma_lc(d, c, a) * g[d, b] for d in range(dim))
                - sum(Gamma_lc(d, c, b) * g[a, d] for d in range(dim))
            )
            require_zero(f"Levi-Civita metric compatibility {c}{a}{b}", residual)

checks.append("Levi-Civita solution satisfies metric compatibility")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 115: Levi-Civita Uniqueness Gate

## Purpose

This report validates a key geometry-selection gate:

```text
metric + torsion-free connection + metric compatibility
  -> unique Levi-Civita connection.
```

The check is performed on a symbolic diagonal 2D metric:

```text
g = diag(A, B)
```

with independent first derivatives `A_x`, `A_y`, `B_x`, and `B_y`.

## Validated Checks

{validation_bullets}

## Result

Starting from six independent torsion-free connection components:

```text
Gamma^a_bc = Gamma^a_cb,
```

the metric-compatibility equations:

```text
nabla_c g_ab = 0
```

have one unique solution.

SymPy verifies that this solution is exactly:

```text
Gamma^a_bc =
  1/2 g^ad(
    partial_b g_dc
    + partial_c g_db
    - partial_d g_bc
  ).
```

## Interpretation

Once the macroscopic vacuum configuration is represented by a metric, and once
the connection is required to preserve that metric without torsion, the
configuration-strain object is no longer arbitrary. It is the Levi-Civita
connection.
"""

out = Path(__file__).with_name("115_levi_civita_uniqueness_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
