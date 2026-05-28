#!/usr/bin/env python3
"""
make_10_auxiliary_torsion_routing_gate.py

Validate that auxiliary torsion channels must be explicit and cannot be hidden
inside scalar projection data.

Output:
    10_auxiliary_torsion_routing_gate.md
"""

from pathlib import Path
import sympy as sp


tau, mu, J_visible, eta, s = sp.symbols("tau mu J_visible eta s")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


J_aux = eta * s
J_total = J_visible + J_aux
stationary_tau = simplify_expr(J_total / (24 * mu))
aux_sensitivity = simplify_expr(sp.diff(stationary_tau, eta))

require_zero("aux sensitivity", aux_sensitivity - s / (24 * mu))
require_zero("aux channel removed", stationary_tau.subs(eta, 0) - J_visible / (24 * mu))

torsion_free_aux_condition = sp.solve([sp.Eq(J_total, 0)], [eta], dict=True)
if torsion_free_aux_condition != [{eta: -J_visible / s}]:
    raise AssertionError(f"unexpected auxiliary cancellation condition: {torsion_free_aux_condition}")

md = f"""# Torsion Defect Exclusion 10: Auxiliary Torsion Routing Gate

## Purpose

This proof checks the auxiliary route.

If an auxiliary carrier is allowed to convert scalar data into torsion source
data, that carrier is a separate routed field. It cannot remain hidden inside
the scalar projection ladder.

## Validated Checks

- auxiliary carrier changes stationary torsion: passed
- setting auxiliary carrier to zero removes its torsion contribution: passed
- torsion-free cancellation condition exposes the auxiliary carrier: passed

## Model

Let:

```text
J_aux = eta s
J_total = J_visible + eta s.
```

Then:

```text
tau = J_total/(24 mu)
    = {stationary_tau}.
```

The sensitivity to the auxiliary carrier is:

```text
d tau / d eta = {aux_sensitivity}.
```

Torsion-free cancellation would require:

```text
eta = -J_visible/s.
```

## Interpretation

An auxiliary torsion route is allowed only as an explicit branch. If `eta`
exists, it changes the torsion equation. If it does not exist or is constrained
to zero, the scalar `s` alone does not source torsion.
"""

out = Path(__file__).with_name("10_auxiliary_torsion_routing_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Auxiliary torsion routing gate passed.")
print(f"Wrote {out.resolve()}")

