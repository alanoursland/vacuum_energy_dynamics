#!/usr/bin/env python3
"""
make_6_compact_support_no_shell_gate.py

Prove reduced boundary-flux witnesses for compact support matching.

Output:
    6_compact_support_no_shell_gate.md
"""

from pathlib import Path
import sympy as sp


r, R = sp.symbols("r R", positive=True)
phi0 = sp.symbols("phi0", real=True)
n = sp.symbols("n", integer=True, positive=True)


def require_equal(label, lhs, rhs):
    result = sp.simplify(lhs - rhs)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def boundary_flux(profile):
    return sp.simplify((4 * sp.pi * r**2 * sp.diff(profile, r)).subs(r, R))


C1_profile = phi0 * (1 - r / R)
C2_profile = phi0 * (1 - r / R) ** 2
smooth_profile = phi0 * (1 - r**2 / R**2) ** 2

C1_flux = boundary_flux(C1_profile)
C2_flux = boundary_flux(C2_profile)
smooth_flux = boundary_flux(smooth_profile)

require_equal("C1 boundary flux", C1_flux, -4 * sp.pi * R * phi0)
require_equal("C2 boundary flux", C2_flux, 0)
require_equal("smooth compact boundary flux", smooth_flux, 0)

general_profile = phi0 * (1 - r / R) ** n
general_derivative_at_boundary = sp.simplify(sp.diff(general_profile, r).subs(r, R))

explicit_general = []
for power in range(1, 7):
    flux = sp.simplify(boundary_flux(general_profile.subs(n, power)))
    explicit_general.append((power, flux))

if explicit_general[0][1] == 0:
    raise AssertionError("linear contact should have nonzero boundary flux")

for power, flux in explicit_general[1:]:
    require_equal(f"power {power} boundary flux", flux, 0)

table = "\n".join(f"| {power} | `{flux}` |" for power, flux in explicit_general)

md = f"""# Source Safety Gate 6: Compact Support No-Shell Gate

## Purpose

This proof reconstructs the reduced compact-support matching witness. The
question is whether a compact cutoff has zero boundary flux at `r = R`.

The spherical boundary flux is:

```text
F_boundary = 4*pi*r^2 phi'(r) evaluated at r = R.
```

## Explicit Checks

SymPy verifies:

```text
phi0*(1 - r/R)       -> F_boundary = -4*pi*R*phi0
phi0*(1 - r/R)^2     -> F_boundary = 0
phi0*(1 - r^2/R^2)^2 -> F_boundary = 0
```

## Contact-Order Table

For:

```text
phi_n(r) = phi0*(1 - r/R)^n,
```

the first six boundary fluxes are:

| n | boundary flux |
|---:|---|
{table}

## Result

Value continuity alone is insufficient. Linear contact can leave nonzero
boundary flux. Quadratic or higher contact kills this reduced flux witness.

## Gate Status

This is a reduced no-shell diagnostic. A full matching theorem still needs the
actual field law and all distributional boundary terms, but any acceptable
compact-support route must at least satisfy this boundary-flux gate.
"""

out = Path(__file__).with_name("6_compact_support_no_shell_gate.md")
out.write_text(md, encoding="utf-8")

print("Compact support no-shell gate passed.")
print(f"Wrote {out.resolve()}")
