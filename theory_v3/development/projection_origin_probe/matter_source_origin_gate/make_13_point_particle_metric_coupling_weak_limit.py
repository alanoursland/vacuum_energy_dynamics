#!/usr/bin/env python3
"""
make_13_point_particle_metric_coupling_weak_limit.py

Validate the weak-field point-particle matter coupling.

Output:
    13_point_particle_metric_coupling_weak_limit.md
"""

from pathlib import Path
import sympy as sp


eps, m, c, Phi, v2, q = sp.symbols("epsilon m c Phi v2 q", positive=True)
x = sp.symbols("x")
Phi_x = sp.Function("Phi")(x)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

# For g_00 = -(1+2 Phi/c^2), the nonrelativistic point-particle action gives
# L = -m c^2 sqrt(1 + 2 Phi/c^2 - v^2/c^2).  Use eps to make a controlled
# first-order expansion in Phi/c^2 and v^2/c^2.
L_eps = -m * c**2 * sp.sqrt(1 + eps * (2 * Phi / c**2 - v2 / c**2))
L_series = sp.series(L_eps, eps, 0, 2).removeO().subs(eps, 1)
expected_L = -m * c**2 - m * Phi + sp.Rational(1, 2) * m * v2
require_zero("weak point-particle Lagrangian", L_series - expected_L)
checks.append("point-particle action gives kinetic term plus potential -m Phi")

potential_energy = m * Phi_x
force = -sp.diff(potential_energy, x)
expected_force = -m * sp.diff(Phi_x, x)
require_zero("Newtonian force from potential energy", force - expected_force)
checks.append("potential energy m Phi gives force -m grad Phi")

u = -Phi
h00 = -2 * Phi / c**2
expected_h00 = 2 * u / c**2
require_zero("h00 and u relation", h00 - expected_h00)
checks.append("with u=-Phi, h00=2u/c^2")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 13: Point-Particle Metric Coupling Weak Limit

## Purpose

This proof checks the standard weak-field matter coupling at the point-particle
level.

It is a covariant-matter gate because it starts from the metric line element,
not from an imposed Poisson source.

## Validated Checks

{validation_bullets}

## Weak Metric

Use:

```text
g_00 = -(1 + 2 Phi/c^2).
```

For a slow particle:

```text
L = -m c^2 sqrt(1 + 2 Phi/c^2 - v^2/c^2).
```

Expanding to first order in `Phi/c^2` and `v^2/c^2` gives:

```text
L = -m c^2 + (1/2)m v^2 - m Phi.
```

Therefore the potential energy is:

```text
U = m Phi,
```

and the force is:

```text
F = -m grad Phi.
```

## Relation To The Bridge Variable

The earlier geometric lift used:

```text
u = -Phi.
```

With:

```text
h_00 = g_00 - eta_00,
```

one gets:

```text
h_00 = -2 Phi/c^2 = 2u/c^2.
```

## Gate Interpretation

This proves that ordinary matter couples to the weak metric in the way needed
to recover Newtonian motion. It does not yet derive the full vacuum action.
"""

out = Path(__file__).with_name("13_point_particle_metric_coupling_weak_limit.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Point-particle metric coupling weak limit passed.")
print(f"Wrote {out.resolve()}")
