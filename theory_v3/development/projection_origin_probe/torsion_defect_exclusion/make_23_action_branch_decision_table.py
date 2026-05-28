#!/usr/bin/env python3
"""
make_23_action_branch_decision_table.py

Validate the reduced action branch table for EH, sourced torsion, and excluded
torsion.

Output:
    23_action_branch_decision_table.md
"""

from pathlib import Path
import sympy as sp


L_EH, tau, mu = sp.symbols("L_EH tau mu")
J_spin, J_defect, J_aux = sp.symbols("J_spin J_defect J_aux")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


J_total = J_spin + J_defect + J_aux
action = L_EH + 12 * mu * tau**2 - J_total * tau
variation = simplify_expr(sp.diff(action, tau))
stationary_tau = simplify_expr(J_total / (24 * mu))
reduced_action = simplify_expr(action.subs(tau, stationary_tau))

eh_branch_action = simplify_expr(action.subs({tau: 0, J_spin: 0, J_defect: 0, J_aux: 0}))
excluded_branch_source = simplify_expr(J_total.subs({J_spin: 0, J_defect: 0, J_aux: 0}))
source_survives_residual = simplify_expr(variation.subs(tau, 0))

require_zero("EH branch action", eh_branch_action - L_EH)
require_zero("excluded branch source", excluded_branch_source)
require_zero("reduced sourced action", reduced_action - (L_EH - J_total**2 / (48 * mu)))
require_zero("source survives residual", source_survives_residual + J_total)

md = f"""# Torsion Defect Exclusion 23: Action Branch Decision Table

## Purpose

This proof records the reduced action branch table.

## Validated Checks

- no-source zero-contorsion branch reduces to `L_EH`: passed
- sourced torsion branch reduces to `L_EH - J_total^2/(48 mu)`: passed
- nonzero source makes `tau = 0` nonstationary: passed
- excluding all source routes gives `J_total = 0`: passed

## Reduced Action

Use:

```text
J_total = J_spin + J_defect + J_aux
L_total = L_EH + 12 mu tau^2 - J_total tau.
```

The variation is:

```text
dL_total/dtau = {variation}.
```

## Branch Table

```text
EH branch:
  J_spin = J_defect = J_aux = 0
  tau = 0
  L_total = {eh_branch_action}

sourced torsion branch:
  tau = J_total/(24 mu)
  L_reduced = {reduced_action}

invalid hidden-source EH branch:
  tau = 0
  residual = {source_survives_residual}
```

## Interpretation

There are only three honest choices:

```text
exclude torsion sources and recover EH;
route torsion as a sourced extension;
prove structural cancellation.
```

Leaving a nonzero source while calling the branch EH is inconsistent.
"""

out = Path(__file__).with_name("23_action_branch_decision_table.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Action branch decision table passed.")
print(f"Wrote {out.resolve()}")

