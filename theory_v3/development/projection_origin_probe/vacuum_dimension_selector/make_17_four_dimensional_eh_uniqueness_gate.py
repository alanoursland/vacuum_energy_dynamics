#!/usr/bin/env python3
"""
make_17_four_dimensional_eh_uniqueness_gate.py

Validate that in D=4 the only non-topological Lovelock curvature term with
local second-order metric dynamics is the Einstein-Hilbert term.

Output:
    17_four_dimensional_eh_uniqueness_gate.md
"""

from pathlib import Path


def lovelock_status(D, p):
    if D < 2 * p:
        return "vanishes"
    if D == 2 * p:
        return "topological"
    return "dynamical"


D = 4
statuses = {p: lovelock_status(D, p) for p in range(0, 6)}

if statuses[0] != "dynamical":
    raise AssertionError("cosmological term status failed")
if statuses[1] != "dynamical":
    raise AssertionError("Einstein-Hilbert term status failed")
if statuses[2] != "topological":
    raise AssertionError("Gauss-Bonnet topological status failed")
for p in range(3, 6):
    if statuses[p] != "vanishes":
        raise AssertionError(f"higher Lovelock term p={p} should vanish")

dynamic_curvature_orders = [p for p in statuses if p >= 1 and statuses[p] == "dynamical"]
if dynamic_curvature_orders != [1]:
    raise AssertionError(f"expected only p=1 dynamical curvature order, got {dynamic_curvature_orders}")

md = f"""# Vacuum Dimension Selector 17: Four-Dimensional EH Uniqueness Gate

## Purpose

This proof isolates the Lovelock consequence of `D=4`.

## Validated Checks

- `p=0` cosmological term is allowed: passed
- `p=1` Einstein-Hilbert term is dynamical: passed
- `p=2` Gauss-Bonnet term is topological: passed
- `p>=3` Lovelock terms vanish in four dimensions: passed
- the only dynamical curvature Lovelock order in `D=4` is `p=1`: passed

## Computation

```text
D = 4
statuses = {statuses}
dynamical curvature orders = {dynamic_curvature_orders}
```

## Interpretation

Under the assumptions of locality, diffeomorphism invariance, metric variables,
and second-order Lovelock field equations, four dimensions select the
Einstein-Hilbert curvature term as the unique local dynamical curvature term.
The cosmological term remains separately allowed.
"""

out = Path(__file__).with_name("17_four_dimensional_eh_uniqueness_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Four-dimensional EH uniqueness gate passed.")
print(f"Wrote {out.resolve()}")

