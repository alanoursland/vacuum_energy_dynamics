#!/usr/bin/env python3
"""
make_14_common_conformal_scale_gate.py

Validate the consistency condition for multiple non-null scale calibrations.

Output:
    14_common_conformal_scale_gate.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


c, q1, q2, m1, m2 = sp.symbols("c q1 q2 m1 m2", nonzero=True)

scale_from_first = sp.solve(sp.Eq(c * q1, m1), c)[0]
scale_from_second = sp.solve(sp.Eq(c * q2, m2), c)[0]

consistency = simplify_expr(scale_from_first - scale_from_second)
cleared_consistency = simplify_expr(sp.together(consistency) * q1 * q2)
require_zero("cleared consistency", cleared_consistency - (m1 * q2 - m2 * q1))

calibrated_second_error = simplify_expr(scale_from_first * q2 - m2)
require_zero(
    "calibrated second error",
    calibrated_second_error - (m1 * q2 - m2 * q1) / q1,
)

md = f"""# Vacuum Interval Directional Probe Origin 14: Common Conformal Scale Gate

## Purpose

This proof strengthens the scale-calibration result.

One non-null interval fixes the conformal factor. Multiple non-null intervals
must agree on the same factor, or the data is not described by a single metric
scale.

## Validated Checks

- first calibration gives `c = m1/q1`: passed
- second calibration gives `c = m2/q2`: passed
- consistency requires a single shared scale: passed

## Consistency Equation

For baseline non-null interval values:

```text
q1, q2
```

and measured values:

```text
m1, m2
```

a single conformal scale requires:

```text
m1/q1 = m2/q2.
```

Equivalently:

```text
m1 q2 - m2 q1 = 0.
```

Sympy obtains the cleared consistency expression:

```text
{cleared_consistency}
```

## Interpretation

The vacuum ontology cannot assign independent scales to different directions
and still claim a single metric interval. Directional calibrations must share
one conformal factor locally unless the excess scale data is treated as an
additional field.
"""

out = Path(__file__).with_name("14_common_conformal_scale_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Common conformal scale gate passed.")
print(f"Wrote {out.resolve()}")

