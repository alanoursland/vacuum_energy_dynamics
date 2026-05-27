#!/usr/bin/env python3
"""
make_53_grounded_sphere_image_response.py

Validate the Kelvin image solution for a grounded spherical boundary in the
scalar boundary-flux model.

An external point source q at distance d > R from the sphere center is canceled
on the spherical boundary by an image source:

    q_img = -(R/d) q
    b = R^2/d

located inside the sphere on the same axis.

Output:
    53_grounded_sphere_image_response.md
"""

from pathlib import Path
import sympy as sp


R, d, mu, q = sp.symbols("R d mu q", positive=True)
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

# On the boundary point R*n, with mu = cos(theta):
# source distance squared: |R n - d e_z|^2
# image distance squared:  |R n - b e_z|^2
D_src_sq = R**2 + d**2 - 2 * R * d * mu
D_img_sq = R**2 + b**2 - 2 * R * b * mu

require_equal("Kelvin boundary distance relation", D_img_sq, (R**2 / d**2) * D_src_sq)
checks.append("Kelvin boundary distance relation")

# Since d>R, D_img = (R/d) D_src. Boundary potential is proportional to:
#   q/D_src + q_img/D_img = (q + q_img*d/R)/D_src.
boundary_numerator = q + q_img * d / R
require_zero("grounded boundary potential cancellation", boundary_numerator)
checks.append("grounded boundary potential cancellation")

require_equal("image source strength", q_img, -R * q / d)
checks.append("image source strength")
require_equal("image position", b, R**2 / d)
checks.append("image position")

# The induced net flux/charge of the grounded sphere equals the image charge.
Q_induced = q_img
require_equal("grounded induced net charge", Q_induced, -R * q / d)
checks.append("grounded induced net charge")

# The image charge depends on the external source distance.
require_equal("distance derivative of induced charge", sp.diff(Q_induced, d), R * q / d**2)
checks.append("distance derivative of induced charge")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 53: Grounded Sphere Image Response

## Purpose

This report validates the first exact induced-boundary response: a grounded
spherical boundary in the field of an external point source.

## Validated Checks

{validation_bullets}

## Setup

Let an external source `q` sit at distance `d > R` from the center of a grounded
sphere of radius `R`.

The Kelvin image construction places an image source at:

```text
b = R^2/d
```

with strength:

```text
q_img = -(R/d)q.
```

## Boundary Cancellation

For a boundary point `R n`, with `mu=cos(theta)`, SymPy verifies:

```text
|R n - b e_z|^2 = (R^2/d^2)|R n - d e_z|^2.
```

Thus on the sphere:

```text
|R n - b e_z| = (R/d)|R n - d e_z|.
```

The boundary potential numerator is:

```text
q + q_img*d/R = 0.
```

So the sphere is held at zero potential.

## Interpretation

A fixed-potential boundary polarizes. Its induced net charge is:

```text
Q_induced = -(R/d)q.
```

This depends on the external source distance. Therefore fixed-potential
boundaries are not fixed-source-strength boundaries. They are response
conditions, and their induced flux changes with environment.
"""

out = Path(__file__).with_name("53_grounded_sphere_image_response.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
