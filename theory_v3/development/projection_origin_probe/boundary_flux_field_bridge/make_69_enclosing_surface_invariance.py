#!/usr/bin/env python3
"""
make_69_enclosing_surface_invariance.py

Validate enclosing-surface invariance of scalar flux in source-free annuli.

Output:
    69_enclosing_surface_invariance.md
"""

from pathlib import Path
import sympy as sp


r, R1, R2 = sp.symbols("r R1 R2", positive=True)
A, B, Q = sp.symbols("A B Q", real=True)
pi = sp.pi


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

u_annulus = A / r + B
lap = sp.diff(u_annulus, r, 2) + 2 * sp.diff(u_annulus, r) / r
flux = -4 * pi * r**2 * sp.diff(u_annulus, r)

require_zero("harmonic annulus solution", lap)
checks.append("harmonic annulus solution")
require_equal("annulus flux", flux, 4 * pi * A)
checks.append("annulus flux")
require_zero("annulus flux derivative", sp.diff(flux, r))
checks.append("annulus flux derivative")
require_zero("flux difference between enclosing radii", flux.subs(r, R2) - flux.subs(r, R1))
checks.append("flux difference between enclosing radii")

u_Q = Q / (4 * pi * r) + B
flux_Q = -4 * pi * r**2 * sp.diff(u_Q, r)
require_equal("flux-normalized annulus solution", flux_Q, Q)
checks.append("flux-normalized annulus solution")

# General source-free radial Gauss identity.
u = sp.Function("u")
radial_lap = sp.diff(u(r), r, 2) + 2 * sp.diff(u(r), r) / r
radial_flux = -4 * pi * r**2 * sp.diff(u(r), r)
require_zero("radial source-free flux identity", sp.diff(radial_flux, r) + 4 * pi * r**2 * radial_lap)
checks.append("radial source-free flux identity")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 69: Enclosing-Surface Invariance

## Purpose

This report validates that scalar boundary charge measured by flux is invariant
under movement of the enclosing surface through a source-free region.

## Validated Checks

{validation_bullets}

## Source-Free Annulus

In a radial source-free annulus, the harmonic solution is:

```text
u(r) = A/r + B.
```

SymPy verifies:

```text
Delta u = 0
Q(r) = -4*pi*r^2 u'(r) = 4*pi*A
Q'(r) = 0.
```

Therefore:

```text
Q(R1) = Q(R2)
```

for any two enclosing radii inside the source-free annulus.

## Interpretation

The scalar charge is not tied to a particular enclosing sphere. In source-free
regions, it is a conserved flux invariant.
"""

out = Path(__file__).with_name("69_enclosing_surface_invariance.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
