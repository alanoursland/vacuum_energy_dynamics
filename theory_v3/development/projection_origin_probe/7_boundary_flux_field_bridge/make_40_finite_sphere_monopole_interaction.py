#!/usr/bin/env python3
"""
make_40_finite_sphere_monopole_interaction.py

Validate the leading finite-radius boundary interaction:

For a sphere of radius R1 whose center is distance d from a second monopole
source with d > R1, the spherical average of the second source's potential over
the first sphere equals the value at the first sphere's center.

This proves that a uniformly distributed boundary flux on a finite sphere has
the same monopole interaction term:

    E_cross = Q1*Q2/(4*pi*d).

Output:
    40_finite_sphere_monopole_interaction.md
"""

from pathlib import Path
import sympy as sp


d, R1 = sp.symbols("d R1", positive=True)
Q1, Q2 = sp.symbols("Q1 Q2", real=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# Spherical average of 1/|d e_z - R1 n|. With mu=cos(theta):
#
#   average = (1/2) integral_-1^1 dmu / sqrt(d^2 + R1^2 - 2 d R1 mu).
#
# For d > R1, sqrt((d+R1)^2)=d+R1 and sqrt((d-R1)^2)=d-R1.
avg_kernel_d_gt_R = sp.Rational(1, 2) * (
    ((d + R1) - (d - R1)) / (d * R1)
)

require_equal("finite sphere average kernel", avg_kernel_d_gt_R, 1 / d)
checks.append("finite sphere average kernel")

avg_potential_from_Q2 = Q2 / (4 * pi) * avg_kernel_d_gt_R
require_equal(
    "average external monopole potential on sphere",
    avg_potential_from_Q2,
    Q2 / (4 * pi * d),
)
checks.append("average external monopole potential on sphere")

# Uniform flux density on sphere 1:
#   sigma_Q = Q1/(4*pi*R1^2)
# Cross boundary coupling is integral sigma_Q * phi_2 dA = Q1 * average(phi_2).
cross_energy = Q1 * avg_potential_from_Q2
require_equal("finite sphere monopole cross energy", cross_energy, Q1 * Q2 / (4 * pi * d))
checks.append("finite sphere monopole cross energy")

force_derivative = -sp.diff(cross_energy, d)
require_equal("finite sphere inverse-square derivative", force_derivative, Q1 * Q2 / (4 * pi * d**2))
checks.append("finite sphere inverse-square derivative")

# The finite radius R1 drops out of the monopole term.
require_zero("no R1 derivative in monopole cross term", sp.diff(cross_energy, R1))
checks.append("no R1 derivative in monopole cross term")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 40: Finite-Sphere Monopole Interaction

## Purpose

This report checks whether the point-charge cross-energy result survives the
first finite-radius upgrade.

The tested setup is:

```text
sphere 1 radius R1
source 2 at center distance d, with d > R1
uniform total boundary flux Q1 on sphere 1
monopole flux Q2 at source 2
```

## Validated Checks

{validation_bullets}

## Spherical Mean Identity

For a point outside the sphere, the spherical average of the Green kernel over
the sphere is:

```text
(1/2) integral_-1^1 [dmu / sqrt(d^2+R1^2-2dR1 mu)] = 1/d.
```

This is the spherical mean-value property for harmonic functions, written
explicitly for the monopole kernel.

## Cross Energy

The average potential from `Q2` over sphere 1 is:

```text
<phi_2>_sphere1 = Q2/(4*pi*d).
```

Uniform flux on sphere 1 gives:

```text
E_cross = Q1 <phi_2>_sphere1
        = Q1*Q2/(4*pi*d).
```

Therefore:

```text
-dE_cross/dd = Q1*Q2/(4*pi*d^2).
```

## Interpretation

The leading monopole interaction is not an artifact of ideal point sources.
For uniform boundary flux on a finite sphere, the same `1/d` interaction term is
obtained exactly as long as the other source lies outside the sphere.

What remains open is the induced-multipole problem: fixed-potential or mixed
boundary conditions can polarize the boundary and add finite-radius corrections.
"""

out = Path(__file__).with_name("40_finite_sphere_monopole_interaction.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
