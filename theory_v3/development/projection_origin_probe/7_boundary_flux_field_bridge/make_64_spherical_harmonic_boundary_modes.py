#!/usr/bin/env python3
"""
make_64_spherical_harmonic_boundary_modes.py

Validate exterior spherical harmonic radial modes:

    u_l(r,Omega) = U_l (R/r)^(l+1) Y_lm(Omega)

solve the exterior Laplace equation and have boundary normal derivative:

    partial_n u_l |_{r=R} = ((l+1)/R) U_l Y_lm.

Output:
    64_spherical_harmonic_boundary_modes.md
"""

from pathlib import Path
import sympy as sp


r, R, U = sp.symbols("r R U", positive=True)
l = sp.symbols("l", integer=True, nonnegative=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

radial = U * R ** (l + 1) * r ** (-(l + 1))

# If Y_lm is an angular eigenfunction with angular Laplacian eigenvalue
# -l(l+1), the separated 3D Laplacian radial factor is:
laplace_radial_factor = (
    sp.diff(radial, r, 2)
    + 2 * sp.diff(radial, r) / r
    - l * (l + 1) * radial / r**2
)

require_zero("exterior spherical harmonic mode is harmonic", laplace_radial_factor)
checks.append("exterior spherical harmonic mode is harmonic")

boundary_value = radial.subs(r, R)
require_equal("boundary mode value", boundary_value, U)
checks.append("boundary mode value")

# Exterior domain inner boundary outward normal is -e_r.
normal_derivative_amplitude = -sp.diff(radial, r).subs(r, R)
require_equal("Dirichlet-to-Neumann eigenvalue", normal_derivative_amplitude, (l + 1) * U / R)
checks.append("Dirichlet-to-Neumann eigenvalue")

for ell in range(0, 8):
    mode = U * R ** (ell + 1) * r ** (-(ell + 1))
    lap = sp.diff(mode, r, 2) + 2 * sp.diff(mode, r) / r - ell * (ell + 1) * mode / r**2
    require_zero(f"explicit harmonic check l={ell}", lap)

checks.append("explicit harmonic checks for l=0..7")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 64: Spherical Harmonic Boundary Modes

## Purpose

This report validates the exterior spherical harmonic modes for a radius `R`
boundary.

## Validated Checks

{validation_bullets}

## Exterior Mode

For a boundary mode `Y_lm`, the decaying exterior harmonic field is:

```text
u_l(r,Omega) = U_l (R/r)^(l+1) Y_lm(Omega).
```

Using:

```text
Delta_S Y_lm = -l(l+1)Y_lm,
```

SymPy verifies the separated radial equation:

```text
u_l'' + (2/r)u_l' - l(l+1)u_l/r^2 = 0.
```

## Boundary Operator

At `r=R`:

```text
u_l(R)=U_l Y_lm.
```

For the exterior domain, the inner boundary outward normal is `-e_r`, so:

```text
partial_n u_l = -partial_r u_l.
```

SymPy verifies:

```text
partial_n u_l|_R = ((l+1)/R) U_l Y_lm.
```

Thus the exterior Dirichlet-to-Neumann eigenvalue for mode `l` is:

```text
lambda_l = (l+1)/R.
```
"""

out = Path(__file__).with_name("64_spherical_harmonic_boundary_modes.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
