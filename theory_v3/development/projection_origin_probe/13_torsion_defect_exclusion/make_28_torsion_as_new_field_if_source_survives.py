#!/usr/bin/env python3
"""
make_28_torsion_as_new_field_if_source_survives.py

Validate that surviving torsion source forces torsion to be treated as an
additional field branch with its own source and stiffness.

Output:
    28_torsion_as_new_field_if_source_survives.md
"""

from pathlib import Path
import sympy as sp


tau, mu, J_total, L_EH = sp.symbols("tau mu J_total L_EH")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


action = L_EH + 12 * mu * tau**2 - J_total * tau
equation = simplify_expr(sp.diff(action, tau))
stationary_tau = simplify_expr(J_total / (24 * mu))
reduced_action = simplify_expr(action.subs(tau, stationary_tau))
source_response = simplify_expr(sp.diff(stationary_tau, J_total))
stiffness_response = simplify_expr(sp.diff(stationary_tau, mu))

require_zero("field equation", equation - (24 * mu * tau - J_total))
require_zero("source response", source_response - 1 / (24 * mu))
require_zero("stiffness response", stiffness_response + J_total / (24 * mu**2))
require_zero("reduced action correction", reduced_action - (L_EH - J_total**2 / (48 * mu)))

md = f"""# Torsion Defect Exclusion 28: Torsion As New Field If Source Survives

## Purpose

This proof records the honest classification if a torsion source survives.

Torsion becomes an additional field branch with its own source and stiffness.

## Validated Checks

- surviving source gives a torsion field equation: passed
- stationary torsion responds to source strength: passed
- stationary torsion responds to torsion stiffness: passed
- reduced action contains an explicit source correction: passed

## Field Branch

Use:

```text
L_total = L_EH + 12 mu tau^2 - J_total tau.
```

The torsion equation is:

```text
{equation} = 0.
```

So:

```text
tau = {stationary_tau}.
```

Its sensitivities are:

```text
d tau / dJ_total = {source_response}
d tau / dmu      = {stiffness_response}.
```

The reduced action becomes:

```text
{reduced_action}.
```

## Interpretation

If `J_total` survives, torsion is not EH data. It is a separate field branch
with a source ledger, stiffness, boundary/current conditions, and reduced
action correction.
"""

out = Path(__file__).with_name("28_torsion_as_new_field_if_source_survives.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Torsion-as-new-field classification passed.")
print(f"Wrote {out.resolve()}")

