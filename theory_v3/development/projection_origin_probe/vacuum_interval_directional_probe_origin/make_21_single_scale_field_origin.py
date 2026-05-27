#!/usr/bin/env python3
"""
make_21_single_scale_field_origin.py

Validate that a single local interval-scale field forces a common conformal
calibration across all directions.

Output:
    21_single_scale_field_origin.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


beta, q1, q2, qp = sp.symbols("beta q1 q2 qp", nonzero=True)

m1 = beta * q1
m2 = beta * q2
mp = beta * qp

ratio12 = simplify_expr(m1 / q1 - m2 / q2)
ratiop1 = simplify_expr(mp / qp - m1 / q1)
consistency12 = simplify_expr(m1 * q2 - m2 * q1)
consistencyp1 = simplify_expr(mp * q1 - m1 * qp)

require_zero("ratio 12", ratio12)
require_zero("ratio p1", ratiop1)
require_zero("consistency 12", consistency12)
require_zero("consistency p1", consistencyp1)

md = """# Vacuum Interval Directional Probe Origin 21: Single Scale Field Origin

## Purpose

This proof records the positive origin of the common-scale gate.

If all local interval measurements are scaled by one local field `beta`, then
all non-null calibrations share one conformal factor automatically.

## Validated Checks

- `m1/q1 = beta`: passed
- `m2/q2 = beta`: passed
- `mp/qp = beta`: passed
- cross-calibration consistency equations vanish: passed

## Model

Let baseline interval probes be:

```text
q1, q2, qp
```

and measured probes be:

```text
m1 = beta q1
m2 = beta q2
mp = beta qp.
```

Then:

```text
m1/q1 = m2/q2 = mp/qp = beta.
```

Equivalently:

```text
m1 q2 - m2 q1 = 0
mp q1 - m1 qp = 0.
```

## Interpretation

A single local clock/interval scale field is sufficient to explain the common
conformal calibration required by the metric branch. Independent per-direction
scale factors would be a different tensor or auxiliary channel.
"""

out = Path(__file__).with_name("21_single_scale_field_origin.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Single scale field origin passed.")
print(f"Wrote {out.resolve()}")

