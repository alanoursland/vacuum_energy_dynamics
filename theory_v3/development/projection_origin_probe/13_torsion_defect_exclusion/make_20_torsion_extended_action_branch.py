#!/usr/bin/env python3
"""
make_20_torsion_extended_action_branch.py

Validate that nonzero torsion creates an explicit torsion-sector action branch.

Output:
    20_torsion_extended_action_branch.md
"""

from pathlib import Path
import sympy as sp


L_EH, tau, mu, J = sp.symbols("L_EH tau mu J")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


torsion_sector = 12 * mu * tau**2 - J * tau
action = L_EH + torsion_sector
variation = simplify_expr(sp.diff(action, tau))
source_sensitivity = simplify_expr(sp.diff(action, J))
stiffness_sensitivity = simplify_expr(sp.diff(action, mu))
stationary_tau = J / (24 * mu)
reduced_action = simplify_expr(action.subs(tau, stationary_tau))

require_zero("variation", variation - (24 * mu * tau - J))
require_zero("source sensitivity", source_sensitivity + tau)
require_zero("stiffness sensitivity", stiffness_sensitivity - 12 * tau**2)
require_zero("reduced action", reduced_action - (L_EH - J**2 / (48 * mu)))

md = f"""# Torsion Defect Exclusion 20: Torsion-Extended Action Branch

## Purpose

This proof validates the opposite branch from proof `19`.

If torsion is nonzero or sourced, it is an explicit action sector, not a
notation change inside Einstein-Hilbert.

## Validated Checks

- torsion variation is `24 mu tau - J`: passed
- action depends explicitly on torsion source `J`: passed
- action depends explicitly on torsion stiffness `mu`: passed
- integrating out torsion leaves a reduced source correction: passed

## Reduced Action

Use:

```text
L_total = L_EH + 12 mu tau^2 - J tau.
```

The torsion variation is:

```text
dL_total/dtau = {variation}.
```

The sensitivities are:

```text
dL_total/dJ  = {source_sensitivity}
dL_total/dmu = {stiffness_sensitivity}.
```

At:

```text
tau = J/(24 mu),
```

the reduced action is:

```text
{reduced_action}.
```

## Interpretation

A sourced torsion branch is a real extension. It changes the reduced action by
`-J^2/(48 mu)`. Pure EH is recovered only when this sector is absent, excluded,
or structurally canceled.
"""

out = Path(__file__).with_name("20_torsion_extended_action_branch.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Torsion-extended action branch passed.")
print(f"Wrote {out.resolve()}")

