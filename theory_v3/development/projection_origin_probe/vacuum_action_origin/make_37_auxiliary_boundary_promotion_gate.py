#!/usr/bin/env python3
"""
make_37_auxiliary_boundary_promotion_gate.py

Validate that adding an auxiliary projection/residual boundary term promotes it
to an explicit boundary field unless it decouples or is silent.

Output:
    37_auxiliary_boundary_promotion_gate.md
"""

from pathlib import Path
import sympy as sp


h, z, gamma, C, M = sp.symbols("h z gamma C M", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

E = C * sp.sqrt(h) - M * sp.sqrt(h) + gamma * z * sp.sqrt(h)
d_h = simplify_expr(sp.diff(E, h))
d_z = simplify_expr(sp.diff(E, z))
require_zero("auxiliary boundary h variation", d_h - (C - M + gamma * z) / (2 * sp.sqrt(h)))
require_zero("auxiliary boundary z variation", d_z - gamma * sp.sqrt(h))
checks.append("auxiliary boundary term contributes to both h and z variations")

require_zero("decoupled auxiliary boundary route", d_z.subs(gamma, 0))
checks.append("gamma=0 decouples the auxiliary boundary field")

require_zero("silent auxiliary value removes h normalization shift", (d_h - (C - M) / (2 * sp.sqrt(h))).subs(z, 0))
checks.append("z=0 removes the h-variation normalization shift")

if simplify_expr(d_z.subs({gamma: 1, h: 1})) == 0:
    raise AssertionError("nonzero gamma should source z boundary variation")
checks.append("nonzero gamma makes z an explicit boundary variable")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 37: Auxiliary Boundary Promotion Gate

## Purpose

This proof checks whether a projection/residual boundary term can be added
quietly to the action.

## Validated Checks

{validation_bullets}

## Setup

Let:

```text
E_boundary = C sqrt(h) - M sqrt(h) + gamma z sqrt(h).
```

Then:

```text
dE/dh = (C - M + gamma z)/(2 sqrt(h))
dE/dz = gamma sqrt(h).
```

## Consequence

If:

```text
gamma != 0,
```

then `z` is an explicit boundary field with its own variation equation. It is
not hidden projection bookkeeping.

Safe routes are:

```text
gamma = 0
```

or:

```text
z = 0
```

in the boundary sector being varied.

## Interpretation

Projection/admissibility boundary structures can only enter the nonlinear
action as explicit boundary fields or as silent/decoupled diagnostics. They
cannot be silently added to GHY without changing the variational problem.
"""

out = Path(__file__).with_name("37_auxiliary_boundary_promotion_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Auxiliary boundary promotion gate passed.")
print(f"Wrote {out.resolve()}")
