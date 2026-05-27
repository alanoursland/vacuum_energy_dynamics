#!/usr/bin/env python3
"""
make_9_nonnull_scale_calibration.py

Validate that null-cone data alone leaves conformal scale free, while one
non-null interval calibration fixes the scale factor.

Output:
    9_nonnull_scale_calibration.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


c, measured = sp.symbols("c measured", nonzero=True)
t, x = sp.symbols("t x")

Q0 = -t**2 + x**2
Q = c * Q0

# A non-null clock calibration at (1,0).
calibration_value = simplify_expr(Q.subs({t: 1, x: 0}))
c_solution = sp.solve(sp.Eq(calibration_value, measured), c)[0]
require_zero("scale solution", c_solution + measured)

recovered_Q = simplify_expr(Q.subs(c, c_solution))
require_zero("calibrated clock value", recovered_Q.subs({t: 1, x: 0}) - measured)

# The null equation is unchanged by c, so it cannot determine c.
require_zero("null relation baseline", Q0.subs(x, t))
require_zero("null relation scaled", Q.subs(x, t))

md = f"""# Vacuum Interval Directional Probe Origin 9: Non-Null Scale Calibration

## Purpose

This proof records the additional datum needed after null-cone structure.

Null probes determine causal/conformal structure. A non-null interval
calibration fixes the missing scale.

## Validated Checks

- null-cone equation is unchanged by conformal scaling: passed
- one non-null calibration solves for the scale factor: passed
- calibrated interval reproduces the measured non-null value: passed

## Model

Use:

```text
Q0(t,x) = -t^2 + x^2
Q(t,x) = c Q0(t,x).
```

Both forms have the same null line:

```text
x = t.
```

Add one clock-like non-null calibration:

```text
Q(1,0) = measured.
```

Since:

```text
Q(1,0) = -c
```

the scale is fixed:

```text
c = -measured.
```

## Interpretation

The directional interval selector needs more than null ordering. To recover a
metric rather than only a conformal class, the ontology must supply a clock,
rod, or equivalent non-null interval scale.
"""

out = Path(__file__).with_name("9_nonnull_scale_calibration.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Non-null scale calibration passed.")
print(f"Wrote {out.resolve()}")

