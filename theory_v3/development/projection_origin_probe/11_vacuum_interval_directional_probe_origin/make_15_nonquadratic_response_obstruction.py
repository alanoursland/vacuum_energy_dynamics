#!/usr/bin/env python3
"""
make_15_nonquadratic_response_obstruction.py

Validate that non-quadratic directional response cannot be reconstructed as a
metric bilinear form by polarization.

Output:
    15_nonquadratic_response_obstruction.md
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
h11, h12, h22, eps = sp.symbols("h11 h12 h22 eps")

u = sp.Matrix([u1, u2])
v = sp.Matrix([v1, v2])
H = sp.Matrix([[h11, h12], [h12, h22]])


def Q_quad(z):
    return simplify_expr((z.T * H * z)[0])


def Q_nonquad(z):
    x, y = z[0], z[1]
    return simplify_expr(Q_quad(z) + eps * x**4)


polarized = simplify_expr((Q_nonquad(u + v) - Q_nonquad(u) - Q_nonquad(v)) / 2)
bilinear = simplify_expr((u.T * H * v)[0])
defect = simplify_expr(polarized - bilinear)

expected_defect = simplify_expr(eps * ((u1 + v1) ** 4 - u1**4 - v1**4) / 2)
require_zero("nonquadratic defect", defect - expected_defect)

# A bilinear expression has zero second derivative with respect to u1.
second_derivative_witness = simplify_expr(sp.diff(defect, u1, 2))
require_zero(
    "second derivative witness",
    second_derivative_witness - 6 * eps * (u1 + v1) ** 2 + 6 * eps * u1**2,
)

if simplify_expr(second_derivative_witness.subs({u1: 0, v1: 1})) == 0:
    raise AssertionError("nonquadratic witness unexpectedly vanished")

md = f"""# Vacuum Interval Directional Probe Origin 15: Nonquadratic Response Obstruction

## Purpose

This proof shows why the interval response must be genuinely quadratic if it
is to define metric tensor data.

## Validated Checks

- polarization of a quadratic response recovers a bilinear form: inherited
- adding a quartic directional term creates a polarization defect: passed
- the defect is not bilinear: passed

## Model

Let:

```text
Q_nonquad(v) = v^T H v + eps v1^4.
```

The polarization defect is:

```text
{defect}
```

A bilinear expression has zero second derivative with respect to one argument.
The defect witness is:

```text
d^2(defect)/du1^2 = {second_derivative_witness}
```

which is not identically zero.

## Interpretation

If the vacuum's directional response is Finsler-like, quartic, or otherwise
nonquadratic, polarization does not produce a metric tensor. Such data would
need a different field lift. The metric-action chain requires the quadratic
interval branch.
"""

out = Path(__file__).with_name("15_nonquadratic_response_obstruction.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Nonquadratic response obstruction passed.")
print(f"Wrote {out.resolve()}")

