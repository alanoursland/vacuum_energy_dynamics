#!/usr/bin/env python3
"""
make_13_parallelogram_metricity_gate.py

Validate the parallelogram identity as a metricity gate for interval probes.

Output:
    13_parallelogram_metricity_gate.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


u1, u2, v1, v2 = sp.symbols("u1 u2 v1 v2")
h11, h12, h22 = sp.symbols("h11 h12 h22")
c0, l1, l2, cubic = sp.symbols("c0 l1 l2 cubic")

u = sp.Matrix([u1, u2])
v = sp.Matrix([v1, v2])
H = sp.Matrix([[h11, h12], [h12, h22]])


def Q_quad(z):
    return simplify_expr((z.T * H * z)[0])


def Q_bad(z):
    x, y = z[0], z[1]
    return simplify_expr(Q_quad(z) + c0 + l1 * x + l2 * y + cubic * x**3)


def parallelogram_residual(Q):
    return simplify_expr(Q(u + v) + Q(u - v) - 2 * Q(u) - 2 * Q(v))


quad_residual = parallelogram_residual(Q_quad)
bad_residual = parallelogram_residual(Q_bad)

require_zero("quadratic parallelogram residual", quad_residual)

expanded_bad_residual = sp.expand(bad_residual)
constant_witness = simplify_expr(expanded_bad_residual.coeff(c0))
linear_witness = simplify_expr(expanded_bad_residual.coeff(l1))
cubic_witness = simplify_expr(expanded_bad_residual.coeff(cubic))

require_zero("constant witness", constant_witness + 2)
require_zero("linear witness", linear_witness + 2 * v1)
require_zero("cubic witness", cubic_witness - (6 * u1 * v1**2 - 2 * v1**3))

md = f"""# Vacuum Interval Directional Probe Origin 13: Parallelogram Metricity Gate

## Purpose

This proof records a necessary gate for treating interval probes as metric
quadratic-form data.

Metric interval data obeys the parallelogram identity:

```text
Q(u+v)+Q(u-v)-2Q(u)-2Q(v) = 0.
```

## Validated Checks

- quadratic interval data satisfies the parallelogram identity: passed
- constant contamination violates the identity: passed
- linear directional contamination violates the identity: passed
- cubic directional contamination violates the identity: passed

## Witnesses

For:

```text
Q_bad = Q_quad + c0 + l1 x + l2 y + cubic x^3
```

the residual contains:

```text
c0 witness    = {constant_witness}
l1 witness    = {linear_witness}
cubic witness = {cubic_witness}
```

## Interpretation

The vacuum interval selector cannot use arbitrary directional labels. To
produce metric tensor data, the local interval response must be quadratic
enough to satisfy the parallelogram gate. Constant offsets, odd drift, and
higher-order directional contamination are separate nonmetric channels unless
they are explicitly routed elsewhere.
"""

out = Path(__file__).with_name("13_parallelogram_metricity_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Parallelogram metricity gate passed.")
print(f"Wrote {out.resolve()}")
