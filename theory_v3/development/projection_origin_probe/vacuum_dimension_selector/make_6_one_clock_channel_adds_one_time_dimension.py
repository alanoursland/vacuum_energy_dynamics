#!/usr/bin/env python3
"""
make_6_one_clock_channel_adds_one_time_dimension.py

Validate the simple counting gate: three spatial dimensions plus one clock
channel gives four spacetime dimensions.

Output:
    6_one_clock_channel_adds_one_time_dimension.md
"""

from pathlib import Path
import sympy as sp


n, t = sp.symbols("n t", integer=True, positive=True)
D = n + t


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed: {result}")


one_clock_D = sp.simplify(D.subs(t, 1))
four_dimensional_case = sp.simplify(D.subs({n: 3, t: 1}))

require_zero("one-clock dimension relation", one_clock_D - (n + 1))
require_zero("three-space plus one clock", four_dimensional_case - 4)

md = f"""# Vacuum Dimension Selector 6: One Clock Channel Adds One Time Dimension

## Purpose

This proof records a deliberately small counting gate. If the scalar flux
bridge selects `n=3` spatial dimensions and the dynamics imports exactly one
clock channel, then the resulting spacetime dimension is four.

## Validated Checks

- `D = n + t`: passed
- `t = 1` gives `D = n + 1`: passed
- `n = 3`, `t = 1` gives `D = 4`: passed

## Computation

```text
D = n + t
t = 1
D = {one_clock_D}
```

With the inverse-square spatial selector:

```text
n = 3
D = {four_dimensional_case}
```

## Interpretation

This does not derive time. It records the handoff condition needed to move from
the scalar boundary-flux bridge to a spacetime field theory: exactly one clock
channel turns three selected spatial dimensions into four spacetime dimensions.
"""

out = Path(__file__).with_name("6_one_clock_channel_adds_one_time_dimension.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("One-clock channel dimension count passed.")
print(f"Wrote {out.resolve()}")

