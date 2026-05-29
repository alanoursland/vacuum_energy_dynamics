#!/usr/bin/env python3
"""
make_111_eh_plus_boundary_source_reduced_newtonian.py

Validate the reduced Newtonian interaction from the EH linearized source
normalization and boundary-flux variable.

Output:
    111_eh_plus_boundary_source_reduced_newtonian.md
"""

from pathlib import Path
import sympy as sp


Gconst, M1, M2, d, r = sp.symbols("G M1 M2 d r", positive=True)
pi = sp.pi


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# Trace-reversed Newtonian variable:
#   B = bar h_00 = -4 Phi = 4u.
# Static field equation in the Newtonian sector:
#   -Delta B = 16*pi*G*rho.
c = 1 / (64 * pi * Gconst)
alpha = sp.Rational(1, 4)
field_coeff = simplify_expr(alpha / c)
require_equal("EH trace-reversed static source coefficient", field_coeff, 16 * pi * Gconst)
checks.append("EH trace-reversed static source coefficient")

B_ext = 4 * Gconst * M1 / r
boundary_flux_B = -4 * pi * r**2 * sp.diff(B_ext, r)
require_equal("trace-reversed boundary flux", boundary_flux_B, 16 * pi * Gconst * M1)
checks.append("trace-reversed boundary flux")

Phi_ext = -B_ext / 4
require_equal("metric potential conversion", Phi_ext, -Gconst * M1 / r)
checks.append("metric potential conversion")

Green_d = 1 / (4 * pi * d)
B_from_M2_at_1 = field_coeff * M2 * Green_d
require_equal("trace-reversed Green solution", B_from_M2_at_1, 4 * Gconst * M2 / d)
checks.append("trace-reversed Green solution")

cross_prefactor = simplify_expr(alpha**2 / c)
require_equal("reduced action cross prefactor", cross_prefactor, 4 * pi * Gconst)
checks.append("reduced action cross prefactor")

E_cross = -cross_prefactor * M1 * M2 * Green_d
require_equal("EH reduced Newtonian interaction", E_cross, -Gconst * M1 * M2 / d)
checks.append("EH reduced Newtonian interaction")

force_from_energy = -sp.diff(E_cross, d)
require_equal("EH reduced Newtonian force sign", force_from_energy, -Gconst * M1 * M2 / d**2)
checks.append("EH reduced Newtonian force sign")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 111: EH Boundary Source Reduced Newtonian Sector

## Purpose

This report validates the reduced-action Newtonian interaction using the
Einstein-Hilbert linearized source normalization.

## Validated Checks

{validation_bullets}

## Trace-Reversed Variable

Let:

```text
B = bar h_00 = -4 Phi = 4u.
```

The static Newtonian-sector quadratic/source energy can be written:

```text
E[B] = 1/2 c <B, -Delta B> - alpha <rho, B>
```

with:

```text
c = 1/(64*pi*G)
alpha = 1/4.
```

SymPy verifies:

```text
alpha/c = 16*pi*G.
```

So:

```text
-Delta B = 16*pi*G rho.
```

## Boundary Flux

For a point mass exterior:

```text
B = 4GM/r,
```

the boundary flux is:

```text
- integral partial_n B dA = 16*pi*G M.
```

This is the trace-reversed metric version of the scalar boundary flux.

## Reduced Interaction

Eliminating `B` from the quadratic/source energy gives:

```text
E_cross = -G M1 M2/d.
```

The separation derivative is:

```text
F_d = -dE/dd = -G M1 M2/d^2.
```

## Interpretation

The Einstein-Hilbert weak-field source coupling reproduces the same attractive
reduced interaction found in the scalar boundary-flux bridge, with the standard
metric normalization.
"""

out = Path(__file__).with_name("111_eh_plus_boundary_source_reduced_newtonian.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
