#!/usr/bin/env python3
"""
make_26_many_particle_source_functional.py

Validate many-particle source additivity from proper-time weak coupling.

Output:
    26_many_particle_source_functional.md
"""

from pathlib import Path
import sympy as sp


m1, m2, Phi1, Phi2, Phi0 = sp.symbols("m1 m2 Phi1 Phi2 Phi0")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

interaction = -(m1 * Phi1 + m2 * Phi2)
source1 = -sp.diff(interaction, Phi1)
source2 = -sp.diff(interaction, Phi2)
require_zero("particle 1 source weight", source1 - m1)
require_zero("particle 2 source weight", source2 - m2)
checks.append("variation of weak proper-time interaction gives each particle mass")

constant_field_interaction = simplify_expr(interaction.subs({Phi1: Phi0, Phi2: Phi0}))
total_mass = m1 + m2
require_zero("constant potential couples to total mass", constant_field_interaction + total_mass * Phi0)
checks.append("constant potential couples to total ordinary mass")

Phi_a, Phi_b = sp.symbols("Phi_a Phi_b")
linearity_error = simplify_expr(
    (-(m1 * (Phi1 + Phi_a) + m2 * (Phi2 + Phi_b)))
    - interaction
    + (m1 * Phi_a + m2 * Phi_b)
)
require_zero("source functional linearity", linearity_error)
checks.append("source functional is additive and linear in field perturbations")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 26: Many-Particle Source Functional

## Purpose

This proof records how the weak proper-time coupling becomes an ordinary source
functional for many particles.

## Validated Checks

{validation_bullets}

## Discrete Source Functional

For two particles, the weak interaction term is:

```text
L_int = -m_1 Phi(x_1) - m_2 Phi(x_2).
```

Varying with respect to the field values gives:

```text
-d L_int/d Phi(x_1) = m_1
-d L_int/d Phi(x_2) = m_2.
```

For a constant potential:

```text
L_int = -(m_1 + m_2) Phi_0.
```

So the source weight is the total ordinary mass.

## Continuum Reading

The continuum expression is the standard weak source functional:

```text
L_int = - integral rho(x) Phi(x) dV.
```

The proof above is its finite-particle version.

## Gate Interpretation

This explains how proper-time coupling produces the ordinary mass density
source used by the reduced A-sector law. It still assumes the interval coupling
already established in the previous gate.
"""

out = Path(__file__).with_name("26_many_particle_source_functional.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Many-particle source functional passed.")
print(f"Wrote {out.resolve()}")
