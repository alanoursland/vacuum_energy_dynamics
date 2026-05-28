#!/usr/bin/env python3
"""
make_19_lower_dimension_spin2_obstruction.py

Validate the lower-dimensional obstruction for propagating massless spin-2
degrees of freedom.

Output:
    19_lower_dimension_spin2_obstruction.md
"""

from pathlib import Path
import sympy as sp


D = sp.symbols("D", integer=True, positive=True)
spin2_dof = sp.simplify(D * (D - 3) / 2)


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed: {result}")


require_zero("D=3 local spin2 degrees", spin2_dof.subs(D, 3))
require_zero("D=4 local spin2 degrees", spin2_dof.subs(D, 4) - 2)

md = f"""# Vacuum Dimension Selector 19: Lower-Dimension Spin-2 Obstruction

## Purpose

This proof records why the lower-dimensional metric branch does not reproduce
the standard two-polarization weak-field GR lift.

## Validated Checks

- `D=3` gives zero local massless spin-2 degrees of freedom: passed
- `D=4` gives two local massless spin-2 degrees of freedom: passed

## Computation

```text
N_spin2(D) = {spin2_dof}
N_spin2(3) = {spin2_dof.subs(D, 3)}
N_spin2(4) = {spin2_dof.subs(D, 4)}
```

## Interpretation

Three-dimensional spacetime gravity can have global or topological structure,
but it does not carry the same local propagating spin-2 content as the standard
four-dimensional weak-field GR branch.
"""

out = Path(__file__).with_name("19_lower_dimension_spin2_obstruction.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Lower-dimension spin-2 obstruction check passed.")
print(f"Wrote {out.resolve()}")

