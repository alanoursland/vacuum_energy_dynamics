#!/usr/bin/env python3
"""
make_20_action_dimension_status.py

Summarize the action-dimension gate.

Output:
    20_action_dimension_status.md
"""

from pathlib import Path


base = Path(__file__).resolve().parent
required = [
    "16_lovelock_order_dimension_table.md",
    "17_four_dimensional_eh_uniqueness_gate.md",
    "18_higher_dimension_lovelock_branch.md",
    "19_lower_dimension_spin2_obstruction.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Vacuum Dimension Selector 20: Action Dimension Status

## Status

The action-dimension gate is closed conditionally.

## What Was Proved

- Lovelock order `p` is dynamical only when `D > 2p`
- in `D=4`, the Einstein-Hilbert term is the only dynamical Lovelock curvature
  term
- higher dimensions open additional Lovelock curvature branches
- lower dimensions do not carry the same local spin-2 content as `D=4`

## What Was Not Proved

This does not derive diffeomorphism invariance, metric variables, or second-order
locality. It classifies the action once those assumptions are admitted.

## Gate Result

```text
D = 4
+ local metric action
+ diffeomorphism invariance
+ second-order Lovelock field equations
=> Einstein-Hilbert curvature term is uniquely dynamical.
```

The remaining work is to connect the dimension selectors back to boundary data
and then intersect the independent gates.
"""

out = base / "20_action_dimension_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Action-dimension status report validated.")
print(f"Wrote {out}")

