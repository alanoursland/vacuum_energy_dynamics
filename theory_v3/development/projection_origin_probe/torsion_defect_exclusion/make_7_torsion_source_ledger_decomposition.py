#!/usr/bin/env python3
"""
make_7_torsion_source_ledger_decomposition.py

Validate the torsion source ledger and cancellation condition.

Output:
    7_torsion_source_ledger_decomposition.md
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
energy = 12 * mu * tau**2 - J_total * tau
variation = simplify_expr(sp.diff(energy, tau))
stationary_tau = sp.solve([sp.Eq(variation, 0)], [tau], dict=True)
cancellation = sp.solve([sp.Eq(J_total, 0)], [J_aux], dict=True)

require_zero("variation", variation - (24 * mu * tau - J_total))
if stationary_tau != [{tau: J_total / (24 * mu)}]:
    raise AssertionError(f"unexpected stationary tau: {stationary_tau}")
if cancellation != [{J_aux: -J_defect - J_spin}]:
    raise AssertionError(f"unexpected cancellation condition: {cancellation}")

source_absence = simplify_expr(J_total.subs({J_spin: 0, J_defect: 0, J_aux: 0}))
require_zero("source absence", source_absence)

md = f"""# Torsion Defect Exclusion 7: Torsion Source Ledger Decomposition

## Purpose

This proof defines the torsion-source ledger used by the rest of the folder.

## Validated Checks

- total torsion source decomposes into spin, defect, and auxiliary routes: passed
- stationary torsion is controlled by the total source: passed
- torsion-free cancellation condition is explicit: passed
- full source absence gives `J_total = 0`: passed

## Ledger

Use:

```text
J_total = J_spin + J_defect + J_aux.
```

The reduced torsion energy is:

```text
E_T = 12 mu tau^2 - J_total tau.
```

The variation is:

```text
dE_T/dtau = {variation}.
```

So:

```text
tau = J_total/(24 mu).
```

## Cancellation Condition

The torsion-free branch requires:

```text
J_total = 0.
```

Solving for the auxiliary route gives:

```text
J_aux = -J_spin - J_defect.
```

## Interpretation

This ledger makes the selector explicit. The EH branch is selected by source
absence or structural cancellation, not by relabeling torsion as part of the
metric branch.
"""

out = Path(__file__).with_name("7_torsion_source_ledger_decomposition.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Torsion source ledger decomposition passed.")
print(f"Wrote {out.resolve()}")

