#!/usr/bin/env python3
"""
make_1_torsion_norm_and_source_variation.py

Validate the reduced totally antisymmetric torsion mode and its source
variation.

Output:
    1_torsion_norm_and_source_variation.md
"""

from pathlib import Path
import sympy as sp


tau = sp.symbols("tau")
mu, J = sp.symbols("mu J")
dim = 3


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def eps(a, b, c):
    return sp.LeviCivita(a, b, c)


def torsion(a, b, c):
    # Gamma^a_bc = tau epsilon_abc, so T^a_bc = Gamma^a_bc - Gamma^a_cb.
    return simplify_expr(tau * eps(a, b, c) - tau * eps(a, c, b))


checks = []

torsion_norm = simplify_expr(
    sum(
        torsion(a, b, c) ** 2
        for a in range(dim)
        for b in range(dim)
        for c in range(dim)
    )
)
require_zero("torsion norm", torsion_norm - 24 * tau**2)
checks.append("reduced torsion norm is 24 tau^2")

energy = simplify_expr(mu * torsion_norm / 2 - J * tau)
require_zero("source energy", energy - (12 * mu * tau**2 - J * tau))
checks.append("source-coupled torsion energy reduces to 12 mu tau^2 - J tau")

variation = simplify_expr(sp.diff(energy, tau))
require_zero("torsion variation", variation - (24 * mu * tau - J))
checks.append("torsion variation is 24 mu tau - J")

stationary = sp.solve([sp.Eq(variation, 0)], [tau], dict=True)
if stationary != [{tau: J / (24 * mu)}]:
    raise AssertionError(f"unexpected stationary torsion solution: {stationary}")
checks.append("stationary torsion is J/(24 mu)")

validation_bullets = "\n".join(f"- {item}: passed" for item in checks)

md = f"""# Torsion Defect Exclusion 1: Torsion Norm And Source Variation

## Purpose

This proof restates the reduced torsion mode inside the selector folder.

The goal is to make the torsion-free branch a local theorem of this chain,
not an imported assumption.

## Validated Checks

{validation_bullets}

## Reduced Torsion Mode

Use the metric-compatible reduced connection component:

```text
Gamma^a_bc = tau epsilon_abc.
```

Then:

```text
T^a_bc = Gamma^a_bc - Gamma^a_cb.
```

Sympy verifies:

```text
T^a_bc T_a^bc = {torsion_norm}.
```

## Source-Coupled Energy

With stiffness `mu` and source `J`:

```text
E_T = (mu/2) T^2 - J tau
    = {energy}.
```

The variation is:

```text
dE_T/dtau = {variation}.
```

Therefore:

```text
tau = J/(24 mu).
```

## Interpretation

Torsion is not removed by algebra. It is controlled by its source. The
torsion-free branch can only be selected after the torsion source is absent or
structurally canceled.
"""

out = Path(__file__).with_name("1_torsion_norm_and_source_variation.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Torsion norm and source variation passed.")
print(f"Wrote {out.resolve()}")

