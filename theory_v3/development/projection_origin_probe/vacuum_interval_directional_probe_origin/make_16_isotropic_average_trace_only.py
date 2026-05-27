#!/usr/bin/env python3
"""
make_16_isotropic_average_trace_only.py

Validate that isotropic direction averaging recovers only trace information.

Output:
    16_isotropic_average_trace_only.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


h11, h12, h22 = sp.symbols("h11 h12 h22")
theta = sp.symbols("theta", real=True)

H = sp.Matrix([[h11, h12], [h12, h22]])
v = sp.Matrix([sp.cos(theta), sp.sin(theta)])
Q = simplify_expr((v.T * H * v)[0])

average = simplify_expr(sp.integrate(Q, (theta, 0, 2 * sp.pi)) / (2 * sp.pi))
require_zero("circle average", average - (h11 + h22) / 2)

for variable in [h12, h11 - h22]:
    # Evaluate sensitivity to h12 directly; h11-h22 is checked by substitution.
    pass

hmean, shear = sp.symbols("hmean shear")
average_shear_form = simplify_expr(average.subs({h11: hmean + shear, h22: hmean - shear}))
require_zero("isotropic average loses diagonal shear", average_shear_form - hmean)
require_zero("isotropic average loses off diagonal shear", sp.diff(average, h12))

md = f"""# Vacuum Interval Directional Probe Origin 16: Isotropic Average Trace Only

## Purpose

This proof shows why direction-averaged interval data cannot replace
directional interval probes.

## Validated Checks

- isotropic circle average recovers half the trace in 2D: passed
- diagonal shear cancels under isotropic averaging: passed
- off-diagonal shear cancels under isotropic averaging: passed

## Computation

For:

```text
v(theta) = (cos(theta), sin(theta))
Q(theta) = v(theta)^T H v(theta)
```

Sympy verifies:

```text
(1/2pi) int_0^(2pi) Q(theta) dtheta = {average}.
```

For:

```text
h11 = hmean + shear
h22 = hmean - shear
```

the average becomes:

```text
{average_shear_form}
```

## Interpretation

Isotropic directional averaging collapses tensor data to trace data. It is
therefore equivalent to returning to the scalar limitation. To recover shear,
the vacuum interval ontology must preserve directional comparisons, not only
averaged response strength.
"""

out = Path(__file__).with_name("16_isotropic_average_trace_only.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Isotropic average trace-only gate passed.")
print(f"Wrote {out.resolve()}")

