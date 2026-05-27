#!/usr/bin/env python3
"""
make_70_bulk_to_boundary_multipole_equivalence.py

Validate equivalence between exterior bulk multipole coefficients and boundary
mode data on an enclosing sphere.

Output:
    70_bulk_to_boundary_multipole_equivalence.md
"""

from pathlib import Path
import sympy as sp


r, R, A = sp.symbols("r R A", positive=True)
l = sp.symbols("l", integer=True, nonnegative=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# One exterior multipole coefficient A_l:
#   u_l(r)=A_l r^-(l+1) Y_lm.
mode = A * r ** (-(l + 1))
boundary_potential_amp = mode.subs(r, R)
boundary_flux_amp = -sp.diff(mode, r).subs(r, R)

require_equal("boundary potential from multipole coefficient", boundary_potential_amp, A / R ** (l + 1))
checks.append("boundary potential from multipole coefficient")
require_equal("boundary flux from multipole coefficient", boundary_flux_amp, (l + 1) * A / R ** (l + 2))
checks.append("boundary flux from multipole coefficient")

U, q = sp.symbols("U q", real=True)
A_from_U = U * R ** (l + 1)
A_from_q = q * R ** (l + 2) / (l + 1)

require_equal("multipole coefficient from boundary potential", (A_from_U / R ** (l + 1)), U)
checks.append("multipole coefficient from boundary potential")
require_equal("multipole coefficient from boundary flux", (l + 1) * A_from_q / R ** (l + 2), q)
checks.append("multipole coefficient from boundary flux")

for ell in range(0, 8):
    mode_ell = A * r ** (-(ell + 1))
    U_ell = mode_ell.subs(r, R)
    q_ell = -sp.diff(mode_ell, r).subs(r, R)
    require_equal(f"explicit boundary potential l={ell}", U_ell, A / R ** (ell + 1))
    require_equal(f"explicit boundary flux l={ell}", q_ell, (ell + 1) * A / R ** (ell + 2))

checks.append("explicit multipole-boundary equivalence for l=0..7")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 70: Bulk-to-Boundary Multipole Equivalence

## Purpose

This report validates that exterior multipole coefficients can be represented
equivalently as boundary potential modes or boundary flux modes on an enclosing
sphere.

## Validated Checks

{validation_bullets}

## Exterior Multipole

For one exterior mode:

```text
u_l(r,Omega) = A_l r^(-(l+1)) Y_lm(Omega).
```

At an enclosing sphere of radius `R`:

```text
U_l = A_l/R^(l+1)
q_l = (l+1)A_l/R^(l+2).
```

Thus:

```text
A_l = U_l R^(l+1)
A_l = q_l R^(l+2)/(l+1).
```

## Interpretation

Bulk multipole information outside a compact source can be encoded completely
as boundary data on any enclosing sphere. The monopole/charge case is the
`l=0` member of this general boundary representation.
"""

out = Path(__file__).with_name("70_bulk_to_boundary_multipole_equivalence.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
