#!/usr/bin/env python3
"""
make_5_boundary_current_flux_silence.py

Prove the far-zone current-flux witness.

Output:
    5_boundary_current_flux_silence.md
"""

from pathlib import Path
import sympy as sp


r = sp.symbols("r", positive=True)
I = sp.symbols("I", real=True)


def require_equal(label, lhs, rhs):
    result = sp.simplify(lhs - rhs)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


radial_current = I / (4 * sp.pi * r**2)
sphere_flux = sp.simplify(4 * sp.pi * r**2 * radial_current)
require_equal("current sphere flux", sphere_flux, I)

divergence = sp.simplify((1 / r**2) * sp.diff(r**2 * radial_current, r))
require_equal("source-free far-zone current divergence", divergence, 0)

md = f"""# Source Safety Gate 5: Boundary Current Flux Silence

## Purpose

This proof reconstructs the far-zone radial-current witness:

```text
J_r(r) = I/(4*pi*r^2).
```

## Flux Witness

The sphere flux is:

```text
F_J = 4*pi*r^2 J_r.
```

SymPy verifies:

```text
F_J = I.
```

The far-zone current is divergence-free away from the source:

```text
(1/r^2) d/dr [r^2 J_r] = 0.
```

## Result

Zero exterior current flux requires:

```text
I = 0.
```

## Gate Status

This is the current analogue of scalar-tail silence. A residual or boundary
current cannot be silently present in the exterior unless its flux coefficient
vanishes or it is explicitly routed as a non-metric diagnostic object.
"""

out = Path(__file__).with_name("5_boundary_current_flux_silence.md")
out.write_text(md, encoding="utf-8")

print("Boundary current flux silence passed.")
print(f"Wrote {out.resolve()}")
