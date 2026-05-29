#!/usr/bin/env python3
"""
make_48_gauss_law_boundary_flux_theorem.py

Package the radial flux relation as the Gauss-law boundary-flux theorem for the
scalar bridge.

Output:
    48_gauss_law_boundary_flux_theorem.md
"""

from pathlib import Path
import sympy as sp


r = sp.symbols("r", positive=True)
A, Q = sp.symbols("A Q", real=True)
pi = sp.pi

u = sp.Function("u")


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

radial_laplacian = sp.diff(u(r), r, 2) + 2 * sp.diff(u(r), r) / r
outward_flux = -4 * pi * r**2 * sp.diff(u(r), r)

gauss_identity = sp.diff(outward_flux, r) + 4 * pi * r**2 * radial_laplacian
require_zero("radial Gauss-law differential identity", gauss_identity)
checks.append("radial Gauss-law differential identity")

u_harmonic = A / r
flux_harmonic = outward_flux.subs(u(r), u_harmonic)

# The substitution above does not replace derivatives, so compute directly.
flux_harmonic = -4 * pi * r**2 * sp.diff(u_harmonic, r)
lap_harmonic = sp.diff(u_harmonic, r, 2) + 2 * sp.diff(u_harmonic, r) / r

require_zero("monopole field is harmonic off source", lap_harmonic)
checks.append("monopole field is harmonic off source")
require_equal("monopole flux through any sphere", flux_harmonic, 4 * pi * A)
checks.append("monopole flux through any sphere")
require_zero("monopole flux radius derivative vanishes", sp.diff(flux_harmonic, r))
checks.append("monopole flux radius derivative vanishes")

u_Q = Q / (4 * pi * r)
flux_Q = -4 * pi * r**2 * sp.diff(u_Q, r)
require_equal("flux normalized Green field", flux_Q, Q)
checks.append("flux normalized Green field")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 48: Gauss-Law Boundary Flux Theorem

## Purpose

This report packages the radial flux statements into the scalar Gauss-law form
used by the boundary-flux bridge.

## Validated Checks

{validation_bullets}

## Differential Identity

For a radial field in 3D:

```text
Delta u = u'' + (2/r)u'.
```

Define outward positive flux:

```text
Q(r) = -4*pi*r^2*u'(r).
```

SymPy verifies:

```text
Q'(r) = -4*pi*r^2 Delta u.
```

Therefore, if:

```text
-Delta u = rho,
```

then:

```text
Q'(r) = 4*pi*r^2 rho.
```

## Harmonic Exterior

For:

```text
u(r)=A/r,
```

SymPy verifies:

```text
Delta u = 0
Q(r)=4*pi*A
Q'(r)=0.
```

The flux-normalized field is:

```text
u(r)=Q/(4*pi*r).
```

## Interpretation

This is the coordinate-free idea behind the bridge, expressed radially:

```text
source-free exterior
  -> conserved boundary flux
  -> field determined by enclosed charge.
```

The earlier radial proofs are special cases of this Gauss-law bookkeeping.
"""

out = Path(__file__).with_name("48_gauss_law_boundary_flux_theorem.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
