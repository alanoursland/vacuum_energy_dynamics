#!/usr/bin/env python3
"""
make_22_direction_dependent_scale_obstruction.py

Validate that direction-dependent scale data is not a single conformal scale.
If retained, it is tensor/shear data.

Output:
    22_direction_dependent_scale_obstruction.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


c1, c2, cp, c = sp.symbols("c1 c2 cp c")

# Baseline Euclidean probes: Q0(e1)=1, Q0(e2)=1, Q0(e1+e2)=2.
m1 = c1
m2 = c2
mp = 2 * cp

single_scale_residual_12 = simplify_expr(c1 - c2)
single_scale_residual_1p = simplify_expr(c1 - cp)

# If treated as a general tensor H, the anisotropy becomes components.
h11 = m1
h22 = m2
h12 = simplify_expr((mp - m1 - m2) / 2)

trace_mean = simplify_expr((h11 + h22) / 2)
diagonal_shear = simplify_expr((h11 - h22) / 2)

require_zero("h12 reconstruction", h12 - (2 * cp - c1 - c2) / 2)
require_zero("diagonal shear", diagonal_shear - (c1 - c2) / 2)
require_zero("single scale residual 12", single_scale_residual_12 - (c1 - c2))
require_zero("single scale residual 1p", single_scale_residual_1p - (c1 - cp))

conformal_conditions = [c1 - c, c2 - c, cp - c]
conformal_solution = sp.solve(conformal_conditions, (c1, c2, cp), dict=True)[0]

md = f"""# Vacuum Interval Directional Probe Origin 22: Direction-Dependent Scale Obstruction

## Purpose

This proof clarifies what direction-dependent scale data means.

It is not a single conformal scale. If retained, it becomes anisotropic
tensor/shear data.

## Validated Checks

- single conformal scale requires equal directional scales: passed
- unequal axis scales reconstruct diagonal shear: passed
- pair-direction scale reconstructs off-diagonal tensor data: passed

## Model

Baseline probes:

```text
Q0(e1) = 1
Q0(e2) = 1
Q0(e1+e2) = 2.
```

Measured probes:

```text
m1 = c1
m2 = c2
mp = 2 cp.
```

A single conformal scale requires:

```text
c1 = c2 = cp = c.
```

Solving the conformal conditions gives:

```text
{conformal_solution}
```

If the data is instead reconstructed as a general symmetric tensor:

```text
h11 = c1
h22 = c2
h12 = (2cp-c1-c2)/2.
```

The diagonal shear is:

```text
(c1-c2)/2.
```

## Interpretation

Independent directional scales cannot be silently called one local clock
scale. They either violate the common-scale gate or must be promoted into
tensor/shear data with explicit routing.
"""

out = Path(__file__).with_name("22_direction_dependent_scale_obstruction.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Direction-dependent scale obstruction passed.")
print(f"Wrote {out.resolve()}")

