#!/usr/bin/env python3
"""
make_96_linearized_action_reduced_source_sign.py

Validate the reduced-action attraction sign and coefficient in the linearized
trace-reversed Newtonian sector.

For B = bar_h_00 and A=-Delta:

    E[B] = (1/(128*pi*G)) <B,A B> - (1/4)<rho,B>

gives:

    A B = 16*pi*G rho.

Eliminating B yields the standard Newtonian cross interaction:

    E_cross = -G M1 M2/d.

Output:
    96_linearized_action_reduced_source_sign.md
"""

from pathlib import Path
import sympy as sp


Gconst, M1, M2, d = sp.symbols("G M1 M2 d", positive=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# Action coefficients for B=bar_h_00:
# E = 1/2 c <B,A B> - alpha <rho,B>
c = 1 / (64 * pi * Gconst)
alpha = sp.Rational(1, 4)

field_coupling = sp.simplify(alpha / c)
require_equal("trace-reversed field equation coefficient", field_coupling, 16 * pi * Gconst)
checks.append("trace-reversed field equation coefficient")

Green_d = 1 / (4 * pi * d)
B_from_M2_at_1 = field_coupling * M2 * Green_d
require_equal("bar_h00 Green field from M2", B_from_M2_at_1, 4 * Gconst * M2 / d)
checks.append("bar_h00 Green field from M2")

# Reduced action cross coefficient:
# E_red = -1/2 (alpha^2/c) J G J.
# Off-diagonal cross term is - (alpha^2/c) M1 M2 G(d).
cross_prefactor = sp.simplify(alpha**2 / c)
require_equal("reduced action cross prefactor", cross_prefactor, 4 * pi * Gconst)
checks.append("reduced action cross prefactor")

E_cross = -cross_prefactor * M1 * M2 * Green_d
require_equal("Newtonian reduced cross energy", E_cross, -Gconst * M1 * M2 / d)
checks.append("Newtonian reduced cross energy")

F_d = -sp.diff(E_cross, d)
require_equal("Newtonian attractive separation derivative", F_d, -Gconst * M1 * M2 / d**2)
checks.append("Newtonian attractive separation derivative")

# Relation to scalar bridge reduced action:
# Q_i = 4*pi*G M_i, scalar E=-Q1Q2/(4*pi d) times 1/(4*pi G)?
Q1 = 4 * pi * Gconst * M1
Q2 = 4 * pi * Gconst * M2
scalar_reduced = -Q1 * Q2 / (4 * pi * d)
require_equal("Newtonian energy from scalar reduced action normalization", scalar_reduced / (4 * pi * Gconst), E_cross)
checks.append("Newtonian energy from scalar reduced action normalization")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 96: Linearized Action Reduced Source Sign

## Purpose

This report validates that the scalar reduced-action attraction mechanism lifts
with the correct coefficient to the linearized trace-reversed Newtonian sector.

## Validated Checks

{validation_bullets}

## Trace-Reversed Variable

Let:

```text
B = bar h_00
A = -Delta.
```

Use the static quadratic/source action:

```text
E[B] =
  (1/(128*pi*G)) <B,A B>
  - (1/4)<rho,B>.
```

Equivalently:

```text
c = 1/(64*pi*G)
alpha = 1/4
E = 1/2 c <B,A B> - alpha<rho,B>.
```

The field equation is:

```text
A B = (alpha/c) rho = 16*pi*G rho.
```

This matches:

```text
-1/2 Delta bar h_00 = 8*pi*G rho.
```

## Reduced Interaction

The reduced cross term is:

```text
E_cross = -(alpha^2/c) M1 M2 G(d),
```

where:

```text
G(d)=1/(4*pi*d).
```

SymPy verifies:

```text
E_cross = -G M1 M2/d.
```

Therefore:

```text
F_d = -dE/dd = -G M1 M2/d^2.
```

## Scalar Bridge Normalization

With:

```text
Q_i = 4*pi*G M_i,
```

the scalar reduced action:

```text
-Q1 Q2/(4*pi*d)
```

becomes the Newtonian energy after dividing by `4*pi*G`.

## Interpretation

The reduced-action attraction mechanism is not only scalar. With the correct
linearized-gravity normalization, it reproduces the Newtonian interaction
energy and force sign.
"""

out = Path(__file__).with_name("96_linearized_action_reduced_source_sign.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
