#!/usr/bin/env python3
"""
make_9_torsion_defect_mode_action_gate.py

Validate that torsion behaves as an independent defect/source mode in a simple
metric-compatible connection sector.

Output:
    9_torsion_defect_mode_action_gate.md
"""

from pathlib import Path
import sympy as sp


tau = sp.symbols("tau")
mu, J = sp.symbols("mu J", positive=True)
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
    # Gamma^a_bc = tau epsilon_abc, so T^a_bc = Gamma^a_bc - Gamma^a_cb.
    return simplify_expr(tau * eps(a, b, c) - tau * eps(a, c, b))


checks = []

torsion_norm = simplify_expr(sum(torsion(a, b, c) ** 2 for a in range(dim) for b in range(dim) for c in range(dim)))
require_equal("totally antisymmetric torsion norm", torsion_norm, 24 * tau**2)
checks.append("totally antisymmetric torsion norm")

E_no_source = mu / 2 * torsion_norm
variation_no_source = sp.diff(E_no_source, tau)
require_equal("torsion no-source variation", variation_no_source, 24 * mu * tau)
checks.append("torsion no-source variation")

no_source_solution = sp.solve([sp.Eq(variation_no_source, 0)], [tau], dict=True)
if no_source_solution != [{tau: 0}]:
    raise AssertionError(f"torsion no-source solution failed: {no_source_solution}")
checks.append("positive torsion stiffness with no source sets torsion to zero")

E_with_source = E_no_source - J * tau
variation_with_source = sp.diff(E_with_source, tau)
require_equal("torsion source variation", variation_with_source, 24 * mu * tau - J)
checks.append("torsion source variation")

source_solution = sp.solve([sp.Eq(variation_with_source, 0)], [tau], dict=True)
if source_solution != [{tau: J / (24 * mu)}]:
    raise AssertionError(f"torsion source solution failed: {source_solution}")
checks.append("torsion source produces algebraic defect mode")

reduced_energy = simplify_expr(E_with_source.subs(tau, J / (24 * mu)))
require_equal("integrated-out torsion source energy", reduced_energy, -J**2 / (48 * mu))
checks.append("integrated-out torsion source energy")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 9: Torsion Defect Mode Action Gate

## Purpose

This report tests what torsion means in an action-origin language.

The result is not that torsion must exist. The result is sharper:

```text
torsion-free is a real physical gate.
```

If torsion is allowed, it behaves as an additional defect/source mode.

## Validated Checks

{validation_bullets}

## Torsion Sector

Use a metric-compatible toy connection:

```text
Gamma^a_bc = tau epsilon_abc.
```

Its torsion is:

```text
T^a_bc = Gamma^a_bc - Gamma^a_cb.
```

SymPy verifies:

```text
T^a_bc T_a^bc = 24 tau^2.
```

## No-Source Gate

For a positive torsion stiffness:

```text
E_T = (mu/2) T^2,
```

SymPy verifies:

```text
dE_T/dtau = 24 mu tau.
```

So without a torsion source:

```text
tau = 0.
```

## Defect Source

With a source-like defect coupling:

```text
E_T = (mu/2)T^2 - J tau,
```

SymPy verifies:

```text
tau = J/(24 mu).
```

Integrating out torsion gives:

```text
E_reduced = -J^2/(48 mu).
```

## Interpretation

Pure Einstein-Hilbert corresponds to the branch where no independent torsion
defect mode is present. If the vacuum ontology has rotational, spin-like, or
defect-like response variables, then torsion is a real extension gate rather
than a harmless convention.
"""

out = Path(__file__).with_name("9_torsion_defect_mode_action_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
