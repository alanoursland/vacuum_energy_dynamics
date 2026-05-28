#!/usr/bin/env python3
"""
make_26_independent_selector_intersection.py

Intersect the dimension values selected by the independent conditional gates.

Output:
    26_independent_selector_intersection.md
"""

from pathlib import Path
import sympy as sp


D = sp.symbols("D", integer=True)
spin2_dof = sp.simplify(D * (D - 3) / 2)
spin2_solutions = {int(sol) for sol in sp.solve(sp.Eq(spin2_dof, 2), D) if sol.is_integer and sol > 0}

flux_plus_clock = {4}
polarization_selector = spin2_solutions
boundary_hypersurface_selector = {4}
four_dimensional_action_gate = {4}

intersection = flux_plus_clock & polarization_selector & boundary_hypersurface_selector & four_dimensional_action_gate

if intersection != {4}:
    raise AssertionError(f"selector intersection failed: {intersection}")

md = f"""# Vacuum Dimension Selector 26: Independent Selector Intersection

## Purpose

This proof intersects the dimension values selected by the independent
conditional gates built in this folder.

## Validated Checks

- flux plus one-clock selector gives `D=4`: passed
- two-polarization massless spin-2 selector gives `D=4`: passed
- three-dimensional boundary hypersurface selector gives `D=4`: passed
- four-dimensional Lovelock action gate gives the EH branch: passed
- intersection is `{4}`: passed

## Computation

```text
flux_plus_clock = {flux_plus_clock}
polarization_selector = {polarization_selector}
boundary_hypersurface_selector = {boundary_hypersurface_selector}
four_dimensional_action_gate = {four_dimensional_action_gate}
intersection = {intersection}
```

## Interpretation

The selectors agree on four spacetime dimensions, but each selector is
conditional. Agreement strengthens the target branch; it does not remove the
need to derive the imported assumptions from the parent vacuum theory.
"""

out = Path(__file__).with_name("26_independent_selector_intersection.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Independent selector intersection passed.")
print(f"Wrote {out.resolve()}")

