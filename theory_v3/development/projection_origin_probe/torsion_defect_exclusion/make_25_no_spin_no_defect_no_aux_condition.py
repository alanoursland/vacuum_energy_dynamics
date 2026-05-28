#!/usr/bin/env python3
"""
make_25_no_spin_no_defect_no_aux_condition.py

Validate the sufficient condition for zero torsion source.

Output:
    25_no_spin_no_defect_no_aux_condition.md
"""

from pathlib import Path
import sympy as sp


tau, mu = sp.symbols("tau mu")
J_spin, J_defect, J_aux = sp.symbols("J_spin J_defect J_aux")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


J_total = J_spin + J_defect + J_aux
no_source_subs = {J_spin: 0, J_defect: 0, J_aux: 0}
J_no_source = simplify_expr(J_total.subs(no_source_subs))
variation = simplify_expr(24 * mu * tau - J_total)
variation_no_source = simplify_expr(variation.subs(no_source_subs))
stationary_no_source = sp.solve([sp.Eq(variation_no_source, 0)], [tau], dict=True)

require_zero("no source total", J_no_source)
require_zero("no source variation", variation_no_source - 24 * mu * tau)
if stationary_no_source != [{tau: 0}]:
    raise AssertionError(f"unexpected no-source stationary point: {stationary_no_source}")

md = """# Torsion Defect Exclusion 25: No Spin / No Defect / No Aux Condition

## Purpose

This proof states the sufficient no-source condition for the torsion-free EH
branch.

## Validated Checks

- setting spin, defect, and auxiliary torsion sources to zero gives `J_total = 0`: passed
- no-source torsion variation reduces to `24 mu tau`: passed
- no-source stationary torsion is `tau = 0`: passed

## Source Ledger

Use:

```text
J_total = J_spin + J_defect + J_aux.
```

The sufficient condition:

```text
J_spin = 0
J_defect = 0
J_aux = 0
```

gives:

```text
J_total = 0.
```

Then:

```text
dE_T/dtau = 24 mu tau.
```

So:

```text
tau = 0.
```

## Interpretation

This is sufficient, not automatic. The folder has shown that scalar projection
data and symmetric interval data do not themselves supply these sources. Any
independent spin, holonomy, or auxiliary channel must still be ruled out or
routed explicitly.
"""

out = Path(__file__).with_name("25_no_spin_no_defect_no_aux_condition.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("No spin/no defect/no aux condition passed.")
print(f"Wrote {out.resolve()}")

