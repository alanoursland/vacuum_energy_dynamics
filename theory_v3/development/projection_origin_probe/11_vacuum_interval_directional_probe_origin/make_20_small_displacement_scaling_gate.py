#!/usr/bin/env python3
"""
make_20_small_displacement_scaling_gate.py

Validate small-displacement scaling diagnostics for separating quadratic,
cubic, and quartic response channels.

Output:
    20_small_displacement_scaling_gate.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


lam, Q, C, R, alpha, beta = sp.symbols("lam Q C R alpha beta")

F = lam**2 * Q + alpha * lam**3 * C + beta * lam**4 * R
homogeneity_residual = simplify_expr(F - lam**2 * F.subs(lam, 1))
expected_residual = simplify_expr(alpha * (lam**3 - lam**2) * C + beta * (lam**4 - lam**2) * R)
require_zero("homogeneity residual", homogeneity_residual - expected_residual)

quadratic_extractor = simplify_expr(sp.diff(F, lam, 2).subs(lam, 0) / 2)
cubic_extractor = simplify_expr(sp.diff(F, lam, 3).subs(lam, 0) / 6)
quartic_extractor = simplify_expr(sp.diff(F, lam, 4).subs(lam, 0) / 24)

require_zero("quadratic extractor", quadratic_extractor - Q)
require_zero("cubic extractor", cubic_extractor - alpha * C)
require_zero("quartic extractor", quartic_extractor - beta * R)

md = f"""# Vacuum Interval Directional Probe Origin 20: Small-Displacement Scaling Gate

## Purpose

This proof gives a diagnostic for separating the metric quadratic branch from
higher-order directional response.

## Validated Checks

- pure quadratic response is homogeneous of degree 2: passed
- cubic and quartic corrections produce a scaling residual: passed
- second, third, and fourth derivatives isolate their channels: passed

## Model

Use:

```text
F(lambda) = lambda^2 Q + alpha lambda^3 C + beta lambda^4 R.
```

The degree-2 homogeneity residual is:

```text
F(lambda) - lambda^2 F(1)
= {homogeneity_residual}.
```

The channel extractors are:

```text
F''(0)/2   = {quadratic_extractor}
F'''(0)/6  = {cubic_extractor}
F''''(0)/24 = {quartic_extractor}
```

## Interpretation

The metric interval branch is the degree-2 response. Higher-order response may
exist, but it is not metric data unless separately reduced or routed. Small
displacement scaling is the operational test that separates these channels.
"""

out = Path(__file__).with_name("20_small_displacement_scaling_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Small-displacement scaling gate passed.")
print(f"Wrote {out.resolve()}")

