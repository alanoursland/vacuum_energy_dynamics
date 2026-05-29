#!/usr/bin/env python3
"""
make_32_clock_only_data_limitation.py

Validate that clock-only data fixes only the temporal interval component and
does not determine the full local metric.

Output:
    32_clock_only_data_limitation.md
"""

from pathlib import Path
import sympy as sp


g00, g01, g11, h01, h11 = sp.symbols("g00 g01 g11 h01 h11")
dt, dx = sp.symbols("dt dx")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

Q = g00 * dt**2 + 2 * g01 * dt * dx + g11 * dx**2
clock_Q = simplify_expr(Q.subs(dx, 0))
require_zero("clock-only interval component", clock_Q - g00 * dt**2)
checks.append("clock-only data sees only g00")

Q2 = g00 * dt**2 + 2 * h01 * dt * dx + h11 * dx**2
clock_Q2 = simplify_expr(Q2.subs(dx, 0))
require_zero("same clock data with different spatial components", clock_Q2 - clock_Q)
checks.append("different spatial/cross components can share the same clock data")

difference_full = simplify_expr(Q2 - Q)
if difference_full == 0:
    raise AssertionError("full interval should differ when h01,h11 differ")
checks.append("clock-equivalent metrics need not agree on full interval")

rod_Q = simplify_expr(Q.subs(dt, 0))
require_zero("rod-only interval component", rod_Q - g11 * dx**2)
checks.append("rod/spatial data is required to fix spatial interval components")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 32: Clock-Only Data Limitation

## Purpose

This proof records a guardrail for interval-origin claims:

```text
clock redshift data alone does not determine the full local interval.
```

## Validated Checks

{validation_bullets}

## Setup

In a 1+1 local model:

```text
Q = g00 dt^2 + 2 g01 dt dx + g11 dx^2.
```

For a clock at rest:

```text
dx = 0,
```

so:

```text
Q_clock = g00 dt^2.
```

The cross and spatial components do not enter.

## Counterexample Form

Two intervals:

```text
Q  = g00 dt^2 + 2 g01 dt dx + g11 dx^2
Q2 = g00 dt^2 + 2 h01 dt dx + h11 dx^2
```

have identical clock-at-rest data but need not agree as full intervals.

## Gate Interpretation

Operational interval universality requires more than universal clock redshift.
It also requires rod/light/spatial propagation data sufficient to identify one
full local interval.
"""

out = Path(__file__).with_name("32_clock_only_data_limitation.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Clock-only data limitation passed.")
print(f"Wrote {out.resolve()}")
