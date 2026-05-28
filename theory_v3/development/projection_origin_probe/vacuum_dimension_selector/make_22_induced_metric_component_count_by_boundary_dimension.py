#!/usr/bin/env python3
"""
make_22_induced_metric_component_count_by_boundary_dimension.py

Validate induced metric component counts on boundary hypersurfaces.

Output:
    22_induced_metric_component_count_by_boundary_dimension.md
"""

from pathlib import Path
import sympy as sp


m = sp.symbols("m", integer=True, positive=True)
components = sp.simplify(m * (m + 1) / 2)


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed: {result}")


require_zero("m=3 induced metric components", components.subs(m, 3) - 6)
require_zero("m=2 induced metric components", components.subs(m, 2) - 3)

md = f"""# Vacuum Dimension Selector 22: Induced Metric Component Count By Boundary Dimension

## Purpose

This proof records how many components an induced metric has on an
`m`-dimensional boundary hypersurface.

## Validated Checks

- `m=3` induced metric has six components: passed
- `m=2` induced metric has three components: passed

## Computation

```text
N_induced(m) = m(m+1)/2 = {components}
N_induced(3) = {components.subs(m, 3)}
N_induced(2) = {components.subs(m, 2)}
```

## Interpretation

If the action bridge uses a three-dimensional boundary hypersurface, the natural
induced metric data has six independent components.
"""

out = Path(__file__).with_name("22_induced_metric_component_count_by_boundary_dimension.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Induced metric component count passed.")
print(f"Wrote {out.resolve()}")

