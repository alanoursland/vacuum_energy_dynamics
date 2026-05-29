#!/usr/bin/env python3
"""
make_28_hidden_dimension_assumption_witness.py

Show the difference between assuming D=4 and solving a selector equation.

Output:
    28_hidden_dimension_assumption_witness.md
"""

from pathlib import Path
import sympy as sp


D = sp.symbols("D", integer=True)
spin2_dof = sp.simplify(D * (D - 3) / 2)
assumed_value = sp.simplify(spin2_dof.subs(D, 4))
solutions = sp.solve(sp.Eq(spin2_dof, 2), D)
positive_solutions = [sol for sol in solutions if sol.is_integer and sol > 0]

if assumed_value != 2:
    raise AssertionError("D=4 evaluation failed")
if positive_solutions != [4]:
    raise AssertionError(f"selector solve failed: {positive_solutions}")

md = f"""# Vacuum Dimension Selector 28: Hidden Dimension Assumption Witness

## Purpose

This proof distinguishes two different moves:

```text
evaluate a formula after assuming D=4
solve a selector equation whose positive solution is D=4
```

## Validated Checks

- assuming `D=4` gives two spin-2 degrees of freedom: passed
- solving `D(D-3)/2 = 2` gives positive solution `D=4`: passed

## Computation

Assumption route:

```text
N_spin2(4) = {assumed_value}
```

Selector route:

```text
N_spin2(D) = {spin2_dof}
N_spin2(D) = 2
solutions = {solutions}
positive solution = {positive_solutions[0]}
```

## Interpretation

The folder should prefer selector equations over post-hoc evaluation whenever
possible. Where a report assumes `D=4`, it should label that assumption rather
than presenting the result as a dimension derivation.
"""

out = Path(__file__).with_name("28_hidden_dimension_assumption_witness.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Hidden dimension assumption witness passed.")
print(f"Wrote {out.resolve()}")

