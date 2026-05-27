#!/usr/bin/env python3
"""
make_4_scalar_tail_flux_exclusion.py

Prove the reduced scalar-tail flux witness.

Output:
    4_scalar_tail_flux_exclusion.md
"""

from pathlib import Path
import sympy as sp


r = sp.symbols("r", positive=True)
C0, C1 = sp.symbols("C0 C1", real=True)


def require_equal(label, lhs, rhs):
    result = sp.simplify(lhs - rhs)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


phi = C0 + C1 / r
sphere_flux = sp.simplify(4 * sp.pi * r**2 * sp.diff(phi, r))
require_equal("scalar tail flux", sphere_flux, -4 * sp.pi * C1)

laplacian_exterior = sp.simplify((1 / r**2) * sp.diff(r**2 * sp.diff(phi, r), r))
require_equal("source-free exterior scalar equation", laplacian_exterior, 0)

md = f"""# Source Safety Gate 4: Scalar-Tail Flux Exclusion

## Purpose

This proof reconstructs the reduced scalar-tail witness used in the archive.
It applies to a source-free exterior scalar profile:

```text
phi(r) = C0 + C1/r.
```

## Source-Free Exterior Check

SymPy verifies:

```text
(1/r^2) d/dr [r^2 phi'(r)] = 0.
```

So `C0 + C1/r` is the general spherical source-free harmonic tail.

## Flux Witness

The sphere flux is:

```text
F_phi = 4*pi*r^2 phi'(r).
```

SymPy gives:

```text
F_phi = -4*pi*C1.
```

## Result

Zero exterior scalar flux requires:

```text
C1 = 0.
```

If ordinary exterior scalar silence also forbids a constant scalar offset, then:

```text
C0 = 0
C1 = 0.
```

## Gate Status

This is a reduced scalar-tail exclusion witness. It does not by itself prove
that every residual scalar sector is absent; it states the exterior tail a
successful source-safety theorem must eliminate or route as non-metric.
"""

out = Path(__file__).with_name("4_scalar_tail_flux_exclusion.md")
out.write_text(md, encoding="utf-8")

print("Scalar-tail flux exclusion passed.")
print(f"Wrote {out.resolve()}")
