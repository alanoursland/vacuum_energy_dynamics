#!/usr/bin/env python3
"""
make_19_metric_comparison_forces_connection.py

Validate that preserving a self-referential metric interval under local
comparison forces metric compatibility, and with torsion-free comparison
selects the Levi-Civita connection.

Output:
    19_metric_comparison_forces_connection.md
"""

from pathlib import Path
import sympy as sp


v0, v1, dx0, dx1 = sp.symbols("v0 v1 dx0 dx1")
A, B = sp.symbols("A B", nonzero=True)
Ax, Ay, Bx, By = sp.symbols("A_x A_y B_x B_y")
dim = 2


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def is_zero(expr):
    expr = simplify_expr(expr)
    if isinstance(expr, sp.MatrixBase):
        return all(simplify_expr(entry) == 0 for entry in expr)
    return expr == 0


def require_zero(label, expr):
    result = simplify_expr(expr)
    if not is_zero(result):
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

g = sp.Matrix([[A, 0], [0, B]])
g_inv = sp.Matrix([[1 / A, 0], [0, 1 / B]])
v = [v0, v1]
dx = [dx0, dx1]


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


G_symbols = {}
for a in range(dim):
    for b in range(dim):
        for c in range(dim):
            G_symbols[(a, b, c)] = sp.symbols(f"G{a}{b}{c}")


def G(a, b, c):
    return G_symbols[(a, b, c)]


# Direct first-order change of I = g_ab v^a v^b under:
#   dg_ab = partial_c g_ab dx^c
#   dv^a = -Gamma^a_bc v^b dx^c.
direct_delta_interval = 0
compatibility_contraction = 0
for a in range(dim):
    for b in range(dim):
        for c in range(dim):
            direct_delta_interval += dg(a, b, c) * v[a] * v[b] * dx[c]

            dv_a = -sum(G(a, e, c) * v[e] * dx[c] for e in range(dim))
            dv_b = -sum(G(b, e, c) * v[e] * dx[c] for e in range(dim))
            direct_delta_interval += g[a, b] * dv_a * v[b] + g[a, b] * v[a] * dv_b

            compatibility_residual = (
                dg(a, b, c)
                - sum(G(e, a, c) * g[e, b] for e in range(dim))
                - sum(G(e, b, c) * g[a, e] for e in range(dim))
            )
            compatibility_contraction += compatibility_residual * v[a] * v[b] * dx[c]

require_equal(
    "interval preservation equals metric compatibility contraction",
    direct_delta_interval,
    compatibility_contraction,
)
checks.append("interval preservation equals metric compatibility contraction")

# Now impose torsion-free connection and metric compatibility for diagonal g.
unknowns = {}
unknown_list = []
for a in range(dim):
    for b in range(dim):
        for c in range(b, dim):
            symbol = sp.symbols(f"L{a}{b}{c}")
            unknowns[(a, b, c)] = symbol
            unknown_list.append(symbol)


def L(a, b, c):
    if b <= c:
        return unknowns[(a, b, c)]
    return unknowns[(a, c, b)]


equations = []
for c in range(dim):
    for a in range(dim):
        for b in range(a, dim):
            residual = (
                dg(a, b, c)
                - sum(L(e, a, c) * g[e, b] for e in range(dim))
                - sum(L(e, b, c) * g[a, e] for e in range(dim))
            )
            equations.append(sp.Eq(residual, 0))

solution = sp.solve(equations, unknown_list, dict=True)
if len(solution) != 1:
    raise AssertionError(f"expected unique torsion-free connection, got {len(solution)}")
solution = solution[0]


def LC(a, b, c):
    return simplify_expr(
        sp.Rational(1, 2)
        * sum(g_inv[a, e] * (dg(e, c, b) + dg(e, b, c) - dg(b, c, e)) for e in range(dim))
    )


for a in range(dim):
    for b in range(dim):
        for c in range(b, dim):
            require_equal(f"Levi-Civita component {a}{b}{c}", solution[L(a, b, c)], LC(a, b, c))

checks.append("torsion-free metric-compatible comparison selects Levi-Civita")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 19: Metric Comparison Forces Connection

## Purpose

This report validates the connection-origin gate:

```text
metric interval self-reference
  + local comparison of neighboring intervals
  + interval preservation
  -> metric-compatible connection.
```

With torsion-free comparison, the connection is uniquely Levi-Civita.

## Validated Checks

{validation_bullets}

## Interval Preservation

Let:

```text
I = g_ab v^a v^b.
```

Under local comparison:

```text
delta v^a = -Gamma^a_bc v^b dx^c
delta g_ab = partial_c g_ab dx^c.
```

SymPy verifies:

```text
delta I
  =
  (partial_c g_ab
   - Gamma^d_ac g_db
   - Gamma^d_bc g_ad)
  v^a v^b dx^c.
```

Therefore preserving the interval for arbitrary `v` and `dx` gives:

```text
nabla_c g_ab = 0.
```

## Levi-Civita Selection

For:

```text
g = diag(A, B),
```

SymPy solves the torsion-free metric-compatibility equations and verifies the
unique solution:

```text
Gamma^a_bc =
  1/2 g^ad(
    partial_b g_dc
    + partial_c g_db
    - partial_d g_bc
  ).
```

## Interpretation

Once the vacuum response changes the interval itself, comparing response states
at neighboring locations requires a connection. If comparison is required to
preserve the interval and has no independent torsion defect, the configuration
strain is the Levi-Civita connection.
"""

out = Path(__file__).with_name("19_metric_comparison_forces_connection.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
