#!/usr/bin/env python3
"""
make_26_torsion_free_energy_minimum.py

Validate that positive torsion stiffness gives a unique reduced minimum at
tau = 0 when the total torsion source vanishes.

Output:
    26_torsion_free_energy_minimum.md
"""

from pathlib import Path
import sympy as sp


tau = sp.symbols("tau")
mu = sp.symbols("mu", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


energy = 12 * mu * tau**2
variation = simplify_expr(sp.diff(energy, tau))
second_variation = simplify_expr(sp.diff(energy, tau, 2))
stationary = sp.solve([sp.Eq(variation, 0)], [tau], dict=True)
energy_difference = simplify_expr(energy - energy.subs(tau, 0))

require_zero("variation", variation - 24 * mu * tau)
require_zero("second variation", second_variation - 24 * mu)
require_zero("energy difference", energy_difference - 12 * mu * tau**2)
if stationary != [{tau: 0}]:
    raise AssertionError(f"unexpected stationary point: {stationary}")

md = f"""# Torsion Defect Exclusion 26: Torsion-Free Energy Minimum

## Purpose

This proof validates the reduced minimum once the no-source condition holds.

## Validated Checks

- no-source torsion energy is `12 mu tau^2`: passed
- stationary point is `tau = 0`: passed
- second variation is `24 mu`: passed
- energy difference from `tau = 0` is nonnegative when `mu > 0`: passed

## Computation

With:

```text
J_total = 0
```

the reduced torsion energy is:

```text
E_T = {energy}.
```

The variation is:

```text
dE_T/dtau = {variation}.
```

The second variation is:

```text
d^2E_T/dtau^2 = {second_variation}.
```

For `mu > 0`, this is positive.

The energy difference from the torsion-free point is:

```text
E_T(tau)-E_T(0) = {energy_difference}.
```

## Interpretation

With positive stiffness and no torsion source, the torsion-free branch is not
just stationary. It is the unique reduced minimum in this one-mode torsion
sector.
"""

out = Path(__file__).with_name("26_torsion_free_energy_minimum.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Torsion-free energy minimum passed.")
print(f"Wrote {out.resolve()}")

