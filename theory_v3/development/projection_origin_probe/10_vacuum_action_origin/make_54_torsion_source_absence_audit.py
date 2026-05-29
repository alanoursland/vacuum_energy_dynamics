#!/usr/bin/env python3
"""
make_54_torsion_source_absence_audit.py

Validate the torsion-source absence gate as a physical selector rather than an
algebraic identity.

Output:
    54_torsion_source_absence_audit.md
"""

from pathlib import Path
import sympy as sp


tau, mu, J_spin, J_defect, J_aux = sp.symbols("tau mu J_spin J_defect J_aux")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

J_total = J_spin + J_defect + J_aux
E = 12 * mu * tau**2 - J_total * tau
variation = sp.diff(E, tau)
require_zero("torsion variation", variation - (24 * mu * tau - J_total))
checks.append("torsion variation is 24*mu*tau-J_total")

stationary_tau = sp.solve([sp.Eq(variation, 0)], [tau], dict=True)
if stationary_tau != [{tau: J_total / (24 * mu)}]:
    raise AssertionError(f"unexpected torsion stationary point: {stationary_tau}")
checks.append("stationary torsion is proportional to total torsion source")

torsion_free_residual = simplify_expr(variation.subs(tau, 0))
require_zero("torsion-free residual", torsion_free_residual + J_total)
checks.append("torsion-free branch is stationary only when total torsion source vanishes")

source_condition = sp.solve([sp.Eq(J_total, 0)], [J_aux], dict=True)
if source_condition != [{J_aux: -J_defect - J_spin}]:
    raise AssertionError(f"unexpected torsion source cancellation condition: {source_condition}")
checks.append("torsion-free can be obtained by source absence or exact cancellation")

positive_no_source_energy = simplify_expr(E.subs({J_spin: 0, J_defect: 0, J_aux: 0}))
require_zero("positive no-source torsion energy", positive_no_source_energy - 12 * mu * tau**2)
checks.append("with no source, positive torsion stiffness minimizes at tau=0")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 54: Torsion Source Absence Audit

## Purpose

This proof restates the torsion-free branch as a source selector.

Torsion-free geometry is not forced by metric compatibility alone. It is
selected when the total torsion source is absent, or when sources cancel by a
separate physical mechanism.

## Validated Checks

{validation_bullets}

## Torsion Source Ledger

Let:

```text
J_total = J_spin + J_defect + J_aux.
```

Use the reduced torsion energy:

```text
E = 12 mu tau^2 - J_total tau.
```

The variation is:

```text
dE/dtau = 24 mu tau - J_total.
```

So:

```text
tau = J_total/(24 mu).
```

## Torsion-Free Branch

At:

```text
tau = 0,
```

the residual is:

```text
-J_total.
```

Therefore torsion-free stationarity requires:

```text
J_total = 0.
```

## Interpretation

The remaining physical selector is not mathematical. The theory must explain
why spin/defect/auxiliary torsion sources vanish or cancel. Without that, the
natural action branch is torsion-extended rather than pure EH.
"""

out = Path(__file__).with_name("54_torsion_source_absence_audit.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Torsion source absence audit passed.")
print(f"Wrote {out.resolve()}")
