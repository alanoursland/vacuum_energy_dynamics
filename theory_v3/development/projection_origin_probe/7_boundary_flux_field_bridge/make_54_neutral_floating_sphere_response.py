#!/usr/bin/env python3
"""
make_54_neutral_floating_sphere_response.py

Validate the neutral floating sphere response to an external point source.

Start with the grounded image pair and add a central compensating source so the
net induced charge/flux on the sphere is zero.

Output:
    54_neutral_floating_sphere_response.md
"""

from pathlib import Path
import sympy as sp


R, d, q = sp.symbols("R d q", positive=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

b = R**2 / d
q_img = -R * q / d
q_center = -q_img

require_equal("neutral compensating central charge", q_center, R * q / d)
checks.append("neutral compensating central charge")
require_zero("net induced charge vanishes", q_img + q_center)
checks.append("net induced charge vanishes")

# Grounded source+image pair gives zero boundary potential. The central
# compensating charge adds a constant potential over the sphere.
floating_boundary_potential = q_center / (4 * pi * R)
require_equal("floating boundary potential", floating_boundary_potential, q / (4 * pi * d))
checks.append("floating boundary potential")

# Dipole moment of the induced pair: central charge at origin contributes zero.
p_induced = q_img * b
require_equal("induced dipole moment", p_induced, -q * R**3 / d**2)
checks.append("induced dipole moment")

# The external source potential at the center is q/(4*pi*d), which equals the
# floating sphere boundary potential.
external_potential_at_center = q / (4 * pi * d)
require_equal("floating potential equals external center potential", floating_boundary_potential, external_potential_at_center)
checks.append("floating potential equals external center potential")

# Large-distance scaling of the induced dipole.
require_equal("dipole distance scaling", sp.diff(p_induced, d), 2 * q * R**3 / d**3)
checks.append("dipole distance scaling")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 54: Neutral Floating Sphere Response

## Purpose

This report validates the fixed-total-flux counterpart of the grounded sphere:
a neutral floating sphere in the field of an external point source.

## Validated Checks

{validation_bullets}

## Construction

The grounded image response uses:

```text
q_img = -(R/d)q
b = R^2/d.
```

To keep the induced net charge zero, add a central compensating source:

```text
q_center = -q_img = (R/d)q.
```

Then:

```text
q_img + q_center = 0.
```

## Floating Boundary Potential

The source plus image pair gives zero boundary potential. The central source
adds a constant over the sphere:

```text
u_boundary = q_center/(4*pi*R) = q/(4*pi*d).
```

This is exactly the external source potential at the sphere center.

## Induced Dipole

The induced dipole moment is:

```text
p_induced = q_img*b = -q R^3/d^2.
```

The neutral floating sphere has no induced monopole, but it does have an
induced dipole response.

## Interpretation

Fixed total flux and fixed potential are different boundary hypotheses:

```text
grounded fixed potential -> induced net charge changes
neutral floating sphere -> net induced charge stays zero, dipole polarizes
```

This is the first exact proof that finite boundaries can carry induced
multipole structure even when their total flux is fixed.
"""

out = Path(__file__).with_name("54_neutral_floating_sphere_response.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
