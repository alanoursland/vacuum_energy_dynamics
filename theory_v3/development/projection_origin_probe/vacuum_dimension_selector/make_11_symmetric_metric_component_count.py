#!/usr/bin/env python3
"""
make_11_symmetric_metric_component_count.py

Validate symmetric rank-2 component counts in D dimensions and in a
three-dimensional boundary hypersurface.

Output:
    11_symmetric_metric_component_count.md
"""

from pathlib import Path
import sympy as sp


D, m = sp.symbols("D m", integer=True, positive=True)
sym_components = lambda z: sp.simplify(z * (z + 1) / 2)

metric_components_D4 = sym_components(4)
boundary_components_m3 = sym_components(3)


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed: {result}")


require_zero("four-dimensional symmetric metric components", metric_components_D4 - 10)
require_zero("three-boundary induced metric components", boundary_components_m3 - 6)

md = f"""# Vacuum Dimension Selector 11: Symmetric Metric Component Count

## Purpose

This proof records the component count for a symmetric rank-2 field.

## Validated Checks

- symmetric rank-2 field in `D=4` has `10` components: passed
- symmetric induced metric on a `3`-dimensional hypersurface has `6`
  components: passed

## Computation

For a symmetric rank-2 tensor:

```text
N_sym(z) = z(z+1)/2.
```

Thus:

```text
N_sym(4) = {metric_components_D4}
N_sym(3) = {boundary_components_m3}
```

## Interpretation

This is a counting proof only. It supports the metric lift bookkeeping but does
not by itself force a metric ontology.
"""

out = Path(__file__).with_name("11_symmetric_metric_component_count.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Symmetric metric component count passed.")
print(f"Wrote {out.resolve()}")

