#!/usr/bin/env python3
"""
make_19_eh_branch_with_zero_contorsion.py

Validate that zero contorsion returns the torsion-free EH/Levi-Civita branch in
the reduced action model.

Output:
    19_eh_branch_with_zero_contorsion.md
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


torsion_norm = 24 * tau**2
action = L_EH + mu * torsion_norm / 2 - J * tau
eh_branch = simplify_expr(action.subs({tau: 0, J: 0}))
variation = simplify_expr(sp.diff(action, tau))
eh_variation = simplify_expr(variation.subs({tau: 0, J: 0}))
torsion_norm_zero = simplify_expr(torsion_norm.subs(tau, 0))

require_zero("EH branch action", eh_branch - L_EH)
require_zero("EH branch variation", eh_variation)
require_zero("zero contorsion torsion norm", torsion_norm_zero)

md = f"""# Torsion Defect Exclusion 19: EH Branch With Zero Contorsion

## Purpose

This proof validates the reduced action branch where contorsion is absent.

## Validated Checks

- zero contorsion gives zero torsion norm: passed
- zero torsion source and zero contorsion reduce the action to `L_EH`: passed
- torsion variation vanishes on the no-source zero-contorsion branch: passed

## Reduced Model

Use:

```text
L_total = L_EH + (mu/2) T^2 - J tau
T^2 = 24 tau^2.
```

So:

```text
L_total = {action}.
```

On the branch:

```text
tau = 0
J = 0
```

Sympy verifies:

```text
L_total = {eh_branch}
dL_total/dtau = {eh_variation}.
```

## Interpretation

The pure Einstein-Hilbert branch is recovered when the contorsion/torsion mode
is absent and no torsion source is present. This is the clean EH selector
inside the reduced torsion model.
"""

out = Path(__file__).with_name("19_eh_branch_with_zero_contorsion.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("EH branch with zero contorsion passed.")
print(f"Wrote {out.resolve()}")

