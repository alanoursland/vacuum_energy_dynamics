#!/usr/bin/env python3
"""
make_13_two_polarization_selector.py

Validate that the standard massless spin-2 degree count equals two only at
D=4 among positive physical dimensions.

Output:
    13_two_polarization_selector.md
"""

from pathlib import Path
import sympy as sp


D = sp.symbols("D", integer=True)
spin2_dof = sp.simplify(D * (D - 3) / 2)
solutions = sp.solve(sp.Eq(spin2_dof, 2), D)
positive_solutions = [sol for sol in solutions if sol.is_integer and sol > 0]

if positive_solutions != [4]:
    raise AssertionError(f"expected only positive solution D=4, got {positive_solutions}")

md = f"""# Vacuum Dimension Selector 13: Two-Polarization Selector

## Purpose

This proof checks the dimension selected by the standard massless spin-2
two-polarization requirement.

## Validated Checks

- solving `D(D-3)/2 = 2` gives `D=4` and `D=-1`: passed
- the only positive physical solution is `D=4`: passed

## Computation

```text
D(D-3)/2 = 2
solutions = {solutions}
positive solution = {positive_solutions[0]}
```

## Interpretation

Under the assumption of a local massless spin-2 lift with the standard
weak-field GR polarization count, the two-polarization condition selects four
spacetime dimensions.
"""

out = Path(__file__).with_name("13_two_polarization_selector.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Two-polarization selector passed.")
print(f"Wrote {out.resolve()}")

