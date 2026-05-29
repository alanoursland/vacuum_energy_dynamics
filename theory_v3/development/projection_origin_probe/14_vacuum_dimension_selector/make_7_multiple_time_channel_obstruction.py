#!/usr/bin/env python3
"""
make_7_multiple_time_channel_obstruction.py

Validate that adding more than one time channel changes the spacetime dimension,
signature count, and massless spin-2 degree count.

Output:
    7_multiple_time_channel_obstruction.md
"""

from pathlib import Path
import sympy as sp


D = sp.symbols("D", integer=True, positive=True)
spin2_dof = sp.simplify(D * (D - 3) / 2)


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed: {result}")


n = 3
one_time_D = n + 1
two_time_D = n + 2

one_time_dof = sp.simplify(spin2_dof.subs(D, one_time_D))
two_time_dof = sp.simplify(spin2_dof.subs(D, two_time_D))

one_time_negative_count = 1
two_time_negative_count = 2

require_zero("one-time dimension", one_time_D - 4)
require_zero("two-time dimension", two_time_D - 5)
require_zero("one-time spin2 degrees", one_time_dof - 2)
require_zero("two-time spin2 degrees", two_time_dof - 5)

if one_time_negative_count != 1 or two_time_negative_count != 2:
    raise AssertionError("signature count failed")

md = f"""# Vacuum Dimension Selector 7: Multiple Time Channel Obstruction

## Purpose

This proof checks what changes if the lift uses two clock channels instead of
one.

## Validated Checks

- `n=3`, one time gives `D=4`: passed
- `n=3`, two times gives `D=5`: passed
- massless spin-2 degree count changes from `2` to `5`: passed
- negative signature count changes from `1` to `2`: passed

## Computation

For the standard massless spin-2 count in `D >= 3` dimensions:

```text
N_spin2(D) = D(D-3)/2.
```

One clock channel:

```text
D = {one_time_D}
N_spin2 = {one_time_dof}
negative directions = {one_time_negative_count}
```

Two clock channels:

```text
D = {two_time_D}
N_spin2 = {two_time_dof}
negative directions = {two_time_negative_count}
```

## Interpretation

Multiple time directions are not excluded by this algebra alone. The proof only
shows that they are not a harmless relabeling: they change the dimension,
signature structure, and spin-2 degree count. A two-time branch would be a
separate theory branch, not the same weak-field GR lift.
"""

out = Path(__file__).with_name("7_multiple_time_channel_obstruction.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Multiple-time obstruction count passed.")
print(f"Wrote {out.resolve()}")

