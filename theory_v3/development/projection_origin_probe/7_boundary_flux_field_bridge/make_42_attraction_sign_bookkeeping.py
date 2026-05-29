#!/usr/bin/env python3
"""
make_42_attraction_sign_bookkeeping.py

Track the sign needed for attractive same-sign masses in a scalar boundary-flux
Dirichlet model.

Output:
    42_attraction_sign_bookkeeping.md
"""

from pathlib import Path
import sympy as sp


d = sp.symbols("d", positive=True)
K = sp.symbols("K", positive=True)
M1, M2 = sp.symbols("M1 M2", positive=True)
s = sp.symbols("s", real=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

E = s * K * M1 * M2 / d
F_sep = -sp.diff(E, d)

require_equal("separation force from signed interaction", F_sep, s * K * M1 * M2 / d**2)
checks.append("separation force from signed interaction")

E_dirichlet_cross = K * M1 * M2 / d
F_dirichlet_cross = -sp.diff(E_dirichlet_cross, d)
require_equal("positive cross energy gives repulsive separation force", F_dirichlet_cross, K * M1 * M2 / d**2)
checks.append("positive cross energy gives repulsive separation force")

E_attractive = -K * M1 * M2 / d
F_attractive = -sp.diff(E_attractive, d)
require_equal("negative interaction gives attractive separation force", F_attractive, -K * M1 * M2 / d**2)
checks.append("negative interaction gives attractive separation force")

# Charge-sign alternative: E=K q1 q2/d is attractive for opposite signs.
q1 = M1
q2 = -M2
E_opposite_charges = K * q1 * q2 / d
F_opposite_charges = -sp.diff(E_opposite_charges, d)
require_equal("opposite scalar charges attract", F_opposite_charges, -K * M1 * M2 / d**2)
checks.append("opposite scalar charges attract")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 42: Attraction Sign Bookkeeping

## Purpose

This report isolates the sign issue in the scalar boundary-flux bridge.

The minimal Dirichlet cross term has the form:

```text
E_cross(d) = K Q1 Q2 / d.
```

That is Coulomb-like. Same-sign scalar charges repel unless an additional sign
choice or interpretation is introduced.

## Validated Checks

{validation_bullets}

## Separation Force Convention

Let:

```text
E(d) = s K M1 M2 / d
```

with positive `K`, `M1`, and `M2`.

The force on the separation coordinate is:

```text
F_d = -dE/dd = s K M1 M2 / d^2.
```

Under this convention:

```text
F_d > 0  means increasing separation, repulsion
F_d < 0  means decreasing separation, attraction
```

## Consequence

For same-sign positive masses:

```text
E = +K M1 M2/d  -> repulsive
E = -K M1 M2/d  -> attractive
```

Therefore a gravitational interpretation must supply one of the following:

```text
1. physical interaction energy is the negative of the scalar cross-strain;
2. positive mass maps to opposite scalar boundary charges in the relevant
   interaction channel;
3. the scalar model is only a magnitude model and the tensor/nonlinear theory
   supplies the attractive sign.
```

## Interpretation

The inverse-square scaling is established by the previous bridge scripts, but
the attractive sign is not automatic. It is an independent physical requirement
that must be derived, not assumed.
"""

out = Path(__file__).with_name("42_attraction_sign_bookkeeping.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
