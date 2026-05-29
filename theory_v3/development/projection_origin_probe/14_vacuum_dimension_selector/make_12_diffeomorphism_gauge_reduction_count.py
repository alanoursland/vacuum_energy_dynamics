#!/usr/bin/env python3
"""
make_12_diffeomorphism_gauge_reduction_count.py

Validate the standard massless spin-2 degree count after diffeomorphism-type
gauge/constraint reduction.

Output:
    12_diffeomorphism_gauge_reduction_count.md
"""

from pathlib import Path
import sympy as sp


D = sp.symbols("D", integer=True, positive=True)
components = D * (D + 1) / 2
reduced = sp.simplify(components - 2 * D)
expected = sp.simplify(D * (D - 3) / 2)


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed: {result}")


require_zero("spin-2 reduction formula", reduced - expected)
require_zero("D=4 spin-2 degrees", expected.subs(D, 4) - 2)
require_zero("D=3 spin-2 degrees", expected.subs(D, 3))
require_zero("D=5 spin-2 degrees", expected.subs(D, 5) - 5)

md = f"""# Vacuum Dimension Selector 12: Diffeomorphism Gauge Reduction Count

## Purpose

This proof records the standard massless spin-2 degree count used by the
weak-field GR lift.

## Validated Checks

- symmetric components minus gauge/constraint count reduces to `D(D-3)/2`:
  passed
- `D=4` gives two propagating degrees of freedom: passed
- `D=3` gives zero local spin-2 degrees of freedom: passed
- `D=5` gives five propagating degrees of freedom: passed

## Computation

```text
D(D+1)/2 - 2D = {reduced}
```

So:

```text
N_spin2(D) = {expected}
N_spin2(4) = {expected.subs(D, 4)}
N_spin2(3) = {expected.subs(D, 3)}
N_spin2(5) = {expected.subs(D, 5)}
```

## Interpretation

This is imported weak-field spin-2 bookkeeping. It is valid under the assumption
of a local massless spin-2 metric lift with diffeomorphism-type gauge freedom.
"""

out = Path(__file__).with_name("12_diffeomorphism_gauge_reduction_count.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Diffeomorphism gauge reduction count passed.")
print(f"Wrote {out.resolve()}")

