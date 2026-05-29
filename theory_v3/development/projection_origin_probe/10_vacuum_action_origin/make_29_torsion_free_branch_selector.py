#!/usr/bin/env python3
"""
make_29_torsion_free_branch_selector.py

Validate the torsion-free branch selector: with positive torsion stiffness,
torsion vanishes exactly when no torsion/defect source is present.

Output:
    29_torsion_free_branch_selector.md
"""

from pathlib import Path
import sympy as sp


tau = sp.symbols("tau")
mu = sp.symbols("mu", positive=True)
J = sp.symbols("J")
dim = 3


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def eps(a, b, c):
    return sp.LeviCivita(a, b, c)


def torsion(a, b, c):
    return simplify_expr(tau * eps(a, b, c) - tau * eps(a, c, b))


checks = []

torsion_norm = simplify_expr(sum(torsion(a, b, c) ** 2 for a in range(dim) for b in range(dim) for c in range(dim)))
require_equal("torsion norm", torsion_norm, 24 * tau**2)
checks.append("torsion norm")

E_torsion = mu * torsion_norm / 2 - J * tau
variation = sp.diff(E_torsion, tau)
require_equal("torsion branch variation", variation, 24 * mu * tau - J)
checks.append("torsion branch variation")

source_solution = sp.solve([sp.Eq(variation, 0)], [tau], dict=True)
if source_solution != [{tau: J / (24 * mu)}]:
    raise AssertionError(f"torsion source solution failed: {source_solution}")
checks.append("torsion source solution")

no_source_solution = sp.solve([sp.Eq(variation.subs(J, 0), 0)], [tau], dict=True)
if no_source_solution != [{tau: 0}]:
    raise AssertionError(f"torsion no-source solution failed: {no_source_solution}")
checks.append("no-source branch sets torsion to zero")

torsion_free_residual = simplify_expr(variation.subs(tau, 0))
require_equal("torsion-free residual", torsion_free_residual, -J)
checks.append("torsion-free residual")

source_absence_condition = sp.solve([sp.Eq(torsion_free_residual, 0)], [J], dict=True)
if source_absence_condition != [{J: 0}]:
    raise AssertionError(f"torsion-free source condition failed: {source_absence_condition}")
checks.append("torsion-free branch requires no torsion source")

positive_energy_no_source = simplify_expr(E_torsion.subs(J, 0))
require_equal("positive no-source torsion energy", positive_energy_no_source, 12 * mu * tau**2)
checks.append("positive no-source torsion energy")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 29: Torsion-Free Branch Selector

## Purpose

This report sharpens the torsion result into a branch selector.

The question is not whether torsion can be written down. It can. The question
is when the pure Einstein-Hilbert branch is selected.

## Validated Checks

{validation_bullets}

## Torsion Sector

Use the same metric-compatible torsion model:

```text
Gamma^a_bc = tau epsilon_abc
T^a_bc = Gamma^a_bc - Gamma^a_cb.
```

SymPy verifies:

```text
T^a_bc T_a^bc = 24 tau^2.
```

With positive stiffness and a possible torsion source:

```text
E_T = (mu/2)T^2 - J tau.
```

The variation is:

```text
dE_T/dtau = 24 mu tau - J.
```

So:

```text
tau = J/(24 mu).
```

## Torsion-Free Branch

If there is no torsion source:

```text
J = 0,
```

then:

```text
tau = 0.
```

Conversely, imposing:

```text
tau = 0
```

leaves the residual:

```text
-J.
```

So the torsion-free branch is stationary only when no torsion source is present.

## Interpretation

Pure Einstein-Hilbert is selected by the no-torsion-source branch. If the
vacuum ontology contains independent spin, rotational defect, or torsion-source
structure, the natural action is no longer pure EH; it moves toward a torsion
extension. This branch point is physical, not algebraic.
"""

out = Path(__file__).with_name("29_torsion_free_branch_selector.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
