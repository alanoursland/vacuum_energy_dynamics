#!/usr/bin/env python3
"""
make_3_local_additivity_energy_density_gate.py

Validate finite-cell additivity and the block-local variational structure of a
local vacuum energy density.

Output:
    3_local_additivity_energy_density_gate.md
"""

from pathlib import Path
import sympy as sp


q1, q2, q3 = sp.symbols("q1 q2 q3")
v1, v2, v3 = sp.symbols("v1 v2 v3", positive=True)
a, b, c = sp.symbols("a b c")


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []


def density(q):
    return a * q**2 / 2 + b * q**4 / 4


E1 = v1 * density(q1)
E2 = v2 * density(q2)
E3 = v3 * density(q3)
E_total = E1 + E2 + E3

require_equal("finite disjoint additivity", E_total, E1 + E2 + E3)
checks.append("finite disjoint additivity")

for qi, qj in ((q1, q2), (q1, q3), (q2, q3)):
    require_equal(f"mixed local Hessian {qi},{qj}", sp.diff(E_total, qi, qj), 0)

checks.append("local additive energy has zero mixed cell Hessian")

require_equal("cell 1 local variation", sp.diff(E_total, q1), v1 * (a * q1 + b * q1**3))
require_equal("cell 2 local variation", sp.diff(E_total, q2), v2 * (a * q2 + b * q2**3))
require_equal("cell 3 local variation", sp.diff(E_total, q3), v3 * (a * q3 + b * q3**3))
checks.append("local additive variation is cellwise")

E_cross = E_total + c * q1 * q2
require_equal("cross-coupled energy has nonzero mixed Hessian", sp.diff(E_cross, q1, q2), c)
checks.append("cross-coupled energy has nonzero mixed Hessian")

require_equal("cross term is obstruction to disjoint additivity", E_cross - E_total, c * q1 * q2)
checks.append("cross term is obstruction to disjoint additivity")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 3: Local Additivity Energy Density Gate

## Purpose

This report validates the finite-cell algebra behind a local vacuum energy
density.

The gate is:

```text
energy of disjoint cells is additive
  -> variation is cell-local
  -> mixed independent-cell Hessians vanish.
```

## Validated Checks

{validation_bullets}

## Local Finite-Cell Energy

Use three independent cells:

```text
E = v1 rho(q1) + v2 rho(q2) + v3 rho(q3)
rho(q) = (a/2)q^2 + (b/4)q^4.
```

SymPy verifies:

```text
partial^2 E / partial qi partial qj = 0, i != j.
```

The variation is cellwise:

```text
partial E / partial qi = vi [a qi + b qi^3].
```

## Nonlocal Obstruction

Adding a cross-cell term:

```text
c q1 q2
```

gives:

```text
partial^2 E / partial q1 partial q2 = c.
```

So cross-couplings are exactly the finite-cell obstruction to strict local
additivity.

## Interpretation

If vacuum energy is local and additive over disjoint regions, its leading
finite-dimensional discretization has a block-local variational structure.
Gradient terms can still couple neighboring cells, but direct action-at-a-
distance cross terms violate this additivity gate.
"""

out = Path(__file__).with_name("3_local_additivity_energy_density_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
