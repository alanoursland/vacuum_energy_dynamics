#!/usr/bin/env python3
"""
make_2_non_a_scalar_tail_mass_exclusion.py

Validate the reduced scalar-tail exclusion gate for non-A sectors.

Output:
    2_non_a_scalar_tail_mass_exclusion.md
"""

from pathlib import Path
import sympy as sp


r, C0, C1, K = sp.symbols("r C0 C1 K", positive=True)
pi = sp.pi


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

phi = C0 + C1 / r
lap_phi = simplify_expr((1 / r**2) * sp.diff(r**2 * sp.diff(phi, r), r))
require_zero("source-free scalar exterior", lap_phi)
checks.append("C0 + C1/r is source-free outside the boundary")

flux_phi = simplify_expr(4 * pi * r**2 * sp.diff(phi, r))
require_zero("scalar tail flux", flux_phi + 4 * pi * C1)
checks.append("scalar 1/r tail carries flux -4*pi*C1")

mass_shift = simplify_expr(K * flux_phi)
require_zero("zero tail removes scalar mass shift", mass_shift.subs(C1, 0))
checks.append("zero C1 removes any flux-proportional scalar mass shift")

if simplify_expr(mass_shift).subs({C1: 1, K: 1}) == 0:
    raise AssertionError("nonzero scalar tail should produce nonzero flux witness")
checks.append("nonzero C1 is a nonzero far-zone flux witness")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 2: Non-A Scalar Tail Mass Exclusion

## Purpose

This proof records the reduced scalar-tail gate that protects the ordinary
A-sector mass channel from duplication by non-A sectors.

## Validated Checks

{validation_bullets}

## Exterior Scalar Tail

For a source-free radial scalar exterior:

```text
phi(r) = C0 + C1/r,
```

SymPy verifies:

```text
(1/r^2) d/dr [r^2 phi'] = 0.
```

The far-zone flux is:

```text
F_phi = 4*pi*r^2 phi'
      = -4*pi*C1.
```

## Gate Interpretation

A nonzero `C1` is a source-like exterior tail. If a non-A sector is supposed
to remain source-neutral, it must satisfy:

```text
C1 = 0.
```

If the constant mode is also not an allowed background shift, then:

```text
C0 = 0.
```

This proof does not exclude all scalar fields. It excludes unlicensed scalar
mass tails in sectors that are supposed to be neutral.
"""

out = Path(__file__).with_name("2_non_a_scalar_tail_mass_exclusion.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Non-A scalar tail mass exclusion passed.")
print(f"Wrote {out.resolve()}")
