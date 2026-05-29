#!/usr/bin/env python3
"""
make_9_weak_limit_newtonian_source_match.py

Validate the weak-limit normalization connecting A to the Newtonian potential.

Output:
    9_weak_limit_newtonian_source_match.md
"""

from pathlib import Path
import sympy as sp


G, c, rho = sp.symbols("G c rho", positive=True)
lap_phi = sp.symbols("Delta_Phi")
lap_A = sp.symbols("Delta_A")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

poisson_phi = sp.Eq(lap_phi, 4 * sp.pi * G * rho)
relation = sp.Eq(lap_A, 2 * lap_phi / c**2)
derived_lap_A = simplify_expr(relation.rhs.subs(lap_phi, poisson_phi.rhs))
expected_lap_A = 8 * sp.pi * G * rho / c**2
require_zero("A-sector weak-limit source normalization", derived_lap_A - expected_lap_A)
checks.append("A=1+2Phi/c^2 maps Poisson to Delta A=8*pi*G*rho/c^2")

r, M = sp.symbols("r M", positive=True)
Phi_ext = -G * M / r
A_ext = 1 + 2 * Phi_ext / c**2
expected_A = 1 - 2 * G * M / (c**2 * r)
require_zero("Schwarzschild weak exterior A", A_ext - expected_A)
checks.append("Phi=-GM/r maps to A=1-2GM/(c^2 r)")

u = -Phi_ext
h00 = 2 * u
bar_h00 = 4 * u
require_zero("linearized h00 normalization", h00 - 2 * G * M / r)
require_zero("linearized trace-reversed h00 normalization", bar_h00 - 4 * G * M / r)
checks.append("linearized normalization matches u=-Phi, h00=2u, bar_h00=4u")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 9: Weak-Limit Newtonian Source Match

## Purpose

This proof checks the source normalization against the Newtonian weak-field
limit.

## Validated Checks

{validation_bullets}

## Newtonian Match

Use the weak-field relation:

```text
A = 1 + 2 Phi/c^2.
```

If:

```text
Delta Phi = 4*pi*G rho,
```

then:

```text
Delta A = 2 Delta Phi/c^2
        = 8*pi*G rho/c^2.
```

This matches the reduced A-sector source law.

## Exterior

For:

```text
Phi = -GM/r,
```

the A-field is:

```text
A = 1 - 2GM/(c^2 r).
```

## Gate Interpretation

The reduced A-sector source normalization is not arbitrary inside the current
chain. It is the weak-limit normalization required by ordinary Newtonian
gravity. This still does not prove the full covariant matter action, but it
anchors the reduced source coefficient.
"""

out = Path(__file__).with_name("9_weak_limit_newtonian_source_match.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Weak-limit Newtonian source match passed.")
print(f"Wrote {out.resolve()}")
