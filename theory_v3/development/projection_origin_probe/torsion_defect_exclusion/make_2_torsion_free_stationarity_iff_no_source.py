#!/usr/bin/env python3
"""
make_2_torsion_free_stationarity_iff_no_source.py

Validate that tau = 0 is stationary if and only if the total torsion source
vanishes.

Output:
    2_torsion_free_stationarity_iff_no_source.md
"""

from pathlib import Path
import sympy as sp


tau, mu, J_total = sp.symbols("tau mu J_total")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


energy = 12 * mu * tau**2 - J_total * tau
variation = simplify_expr(sp.diff(energy, tau))
torsion_free_residual = simplify_expr(variation.subs(tau, 0))

require_zero("variation", variation - (24 * mu * tau - J_total))
require_zero("torsion-free residual", torsion_free_residual + J_total)

source_condition = sp.solve([sp.Eq(torsion_free_residual, 0)], [J_total], dict=True)
if source_condition != [{J_total: 0}]:
    raise AssertionError(f"unexpected source condition: {source_condition}")

stationary_tau = sp.solve([sp.Eq(variation, 0)], [tau], dict=True)
if stationary_tau != [{tau: J_total / (24 * mu)}]:
    raise AssertionError(f"unexpected stationary tau: {stationary_tau}")

md = f"""# Torsion Defect Exclusion 2: Torsion-Free Stationarity Iff No Source

## Purpose

This proof records the exact no-source condition for the torsion-free branch.

## Validated Checks

- torsion variation is `24 mu tau - J_total`: passed
- residual at `tau = 0` is `-J_total`: passed
- stationarity at `tau = 0` requires `J_total = 0`: passed
- stationary torsion is `J_total/(24 mu)`: passed

## Computation

Use:

```text
E_T = 12 mu tau^2 - J_total tau.
```

Then:

```text
dE_T/dtau = {variation}.
```

At the torsion-free branch:

```text
(dE_T/dtau)|tau=0 = {torsion_free_residual}.
```

Thus:

```text
tau = 0 is stationary iff J_total = 0.
```

## Interpretation

Torsion-free geometry is not a default consequence of metric data. It is a
source selector. A hidden nonzero `J_total` makes the torsion-free branch
nonstationary.
"""

out = Path(__file__).with_name("2_torsion_free_stationarity_iff_no_source.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Torsion-free stationarity iff no source passed.")
print(f"Wrote {out.resolve()}")

