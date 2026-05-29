#!/usr/bin/env python3
"""
make_13_interval_field_self_reference_gate.py

Validate the self-reference gate: a metric response variable changes the local
interval used to measure displacements, while a scalar field on a fixed metric
does not.

Output:
    13_interval_field_self_reference_gate.md
"""

from pathlib import Path
import sympy as sp


d0, d1 = sp.symbols("d0 d1")
h00, h01, h11, sigma, q = sp.symbols("h00 h01 h11 sigma q")


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

d = sp.Matrix([d0, d1])
eta = sp.Matrix([[-1, 0], [0, 1]])
h = sp.Matrix([[h00, h01], [h01, h11]])

interval_background = simplify_expr((d.T * eta * d)[0])
interval_metric = simplify_expr((d.T * (eta + h) * d)[0])
delta_interval_metric = simplify_expr(interval_metric - interval_background)

require_equal("metric perturbation changes interval by h contraction", delta_interval_metric, (d.T * h * d)[0])
checks.append("metric perturbation changes interval by h contraction")

require_equal("interval Hessian recovers metric perturbation", sp.hessian(delta_interval_metric, (d0, d1)) / 2, h)
checks.append("interval Hessian recovers metric perturbation")

scalar_fixed_background_interval = interval_background
require_equal("fixed-background scalar does not change interval", sp.diff(scalar_fixed_background_interval, q), 0)
checks.append("fixed-background scalar does not change interval")

h_conformal = 2 * sigma * eta
delta_interval_conformal = simplify_expr((d.T * h_conformal * d)[0])
require_equal("conformal response rescales background interval", delta_interval_conformal, 2 * sigma * interval_background)
checks.append("conformal response rescales background interval")

require_equal("conformal response has no shear component", h_conformal[0, 1], 0)
checks.append("conformal response has no shear component")

shear_interval = simplify_expr(delta_interval_metric.subs({h00: 0, h11: 0}))
require_equal("general metric perturbation can carry shear interval response", shear_interval, 2 * h01 * d0 * d1)
checks.append("general metric perturbation can carry shear interval response")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 13: Interval Field Self-Reference Gate

## Purpose

This report tests the next lift:

```text
response field on a metric
  vs.
response field that is the metric.
```

## Validated Checks

{validation_bullets}

## Metric Response

For a displacement `d` and background interval:

```text
I_0(d) = d^T eta d,
```

let the response be a metric perturbation `h`.

Then:

```text
I(d) = d^T(eta+h)d
delta I = d^T h d.
```

SymPy verifies that:

```text
(1/2) Hessian_d(delta I) = h.
```

So the metric response is self-referential: the response changes the local
measurement rule itself.

## Scalar on Fixed Background

If `q` is a scalar living on a fixed interval:

```text
I_0(d) = d^T eta d,
```

SymPy verifies:

```text
partial I_0 / partial q = 0.
```

The scalar can have energy, but it does not by itself change the local interval.

## Conformal Limitation

A conformal response:

```text
h_ab = 2 sigma eta_ab
```

only rescales the background interval:

```text
delta I = 2 sigma I_0.
```

It has no shear component. A general metric perturbation can carry:

```text
2 h_01 d0 d1.
```

## Interpretation

The action-origin path to gravity requires the vacuum response variable to
modify the interval itself, not merely live on a fixed interval. A scalar action
is a useful prototype, but the gravitational lift begins when response becomes
metric self-reference.
"""

out = Path(__file__).with_name("13_interval_field_self_reference_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
