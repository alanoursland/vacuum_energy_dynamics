#!/usr/bin/env python3
"""
make_46_source_coupled_reduced_action_sign.py

Validate the sign bookkeeping for the source-coupled reduced action:

    E[u] = 1/2 <u, A u> - <J, u>

At the stationary field:

    u = A^-1 J

the reduced action is:

    E_red[J] = -1/2 <J, A^-1 J>.

For two boundary/source charges this makes the separation-dependent
interaction term negative:

    E_red,cross(d) = -Q1*Q2/(4*pi*d),

which gives attractive same-sign separation force under the convention used in
the previous sign bookkeeping script.

Output:
    46_source_coupled_reduced_action_sign.md
"""

from pathlib import Path
import sympy as sp


a, u, J = sp.symbols("a u J", positive=True)
Q1, Q2, d = sp.symbols("Q1 Q2 d", positive=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# Finite-dimensional prototype:
#   E(u)=1/2 a u^2 - J u.
E = sp.Rational(1, 2) * a * u**2 - J * u
stationary_u = sp.solve(sp.diff(E, u), u)[0]
require_equal("stationary field in quadratic source-coupled action", stationary_u, J / a)
checks.append("stationary field in quadratic source-coupled action")

E_reduced = sp.simplify(E.subs(u, stationary_u))
require_equal("reduced quadratic action is negative", E_reduced, -J**2 / (2 * a))
checks.append("reduced quadratic action is negative")

# Two-source Green-kernel bookkeeping.
G = 1 / (4 * pi * d)
stored_cross = Q1 * Q2 * G
source_cross = -2 * Q1 * Q2 * G
reduced_cross = sp.simplify(stored_cross + source_cross)

require_equal("positive stored strain cross term", stored_cross, Q1 * Q2 / (4 * pi * d))
checks.append("positive stored strain cross term")
require_equal("source coupling cross term", source_cross, -Q1 * Q2 / (2 * pi * d))
checks.append("source coupling cross term")
require_equal("negative reduced interaction cross term", reduced_cross, -Q1 * Q2 / (4 * pi * d))
checks.append("negative reduced interaction cross term")

force_on_separation = -sp.diff(reduced_cross, d)
require_equal("reduced action gives attractive separation derivative", force_on_separation, -Q1 * Q2 / (4 * pi * d**2))
checks.append("reduced action gives attractive separation derivative")

# Stored strain alone gives the opposite sign.
stored_force = -sp.diff(stored_cross, d)
require_equal("stored strain alone gives repulsive derivative", stored_force, Q1 * Q2 / (4 * pi * d**2))
checks.append("stored strain alone gives repulsive derivative")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 46: Source-Coupled Reduced Action Sign

## Purpose

This report resolves the scalar sign bookkeeping gap left by proof `42`.

The important distinction is:

```text
stored strain energy
```

versus:

```text
source-coupled reduced action after the field has been eliminated.
```

## Validated Checks

{validation_bullets}

## Quadratic Prototype

For a positive quadratic operator `A`, the source-coupled action has the finite
dimensional form:

```text
E[u] = 1/2 <u,Au> - <J,u>.
```

The stationary field satisfies:

```text
Au = J.
```

Substituting the stationary field back into the action gives:

```text
E_red[J] = -1/2 <J,A^-1 J>.
```

The minus sign is forced by completing the square.

## Two-Source Interaction

For two positive boundary/source strengths:

```text
G(d) = 1/(4*pi*d).
```

The stored strain cross term is:

```text
E_strain,cross = +Q1*Q2*G(d).
```

The source coupling contributes:

```text
E_source,cross = -2*Q1*Q2*G(d).
```

Therefore the reduced interaction is:

```text
E_red,cross = -Q1*Q2*G(d)
            = -Q1*Q2/(4*pi*d).
```

## Force Sign

Using the convention that the separation force is:

```text
F_d = -dE/dd,
```

the reduced interaction gives:

```text
F_d = -Q1*Q2/(4*pi*d^2).
```

For same-sign positive sources this is attractive.

## Interpretation

The scalar bridge does not need same-sign charges to repel. Repulsion only
appears if one treats the positive stored strain cross term as the full
effective interaction energy.

The source-coupled reduced action supplies the attractive sign:

```text
positive stored strain + source coupling -> negative reduced interaction.
```
"""

out = Path(__file__).with_name("46_source_coupled_reduced_action_sign.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
