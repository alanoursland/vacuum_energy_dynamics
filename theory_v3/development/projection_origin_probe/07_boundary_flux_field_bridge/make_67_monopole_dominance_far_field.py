#!/usr/bin/env python3
"""
make_67_monopole_dominance_far_field.py

Validate far-field monopole dominance for exterior spherical harmonic modes.

Mode l decays as:

    u_l(r) ~ r^(-(l+1)).

Relative to the monopole l=0, mode l has potential suppression:

    (R/r)^l

up to amplitude ratios.

Output:
    67_monopole_dominance_far_field.md
"""

from pathlib import Path
import sympy as sp


r, R, U0, Ul = sp.symbols("r R U0 Ul", positive=True)
l = sp.symbols("l", integer=True, nonnegative=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

u0 = U0 * R / r
ul = Ul * (R / r) ** (l + 1)
potential_ratio = sp.simplify(ul / u0)
require_equal("mode-to-monopole potential ratio", potential_ratio, (Ul / U0) * (R / r) ** l)
checks.append("mode-to-monopole potential ratio")

field0 = -sp.diff(u0, r)
fieldl = -sp.diff(ul, r)
field_ratio = sp.simplify(fieldl / field0)
require_equal("mode-to-monopole field ratio", field_ratio, ((l + 1) * Ul / U0) * (R / r) ** l)
checks.append("mode-to-monopole field ratio")

for ell in range(1, 8):
    ratio_l = potential_ratio.subs(l, ell)
    require_equal(
        f"explicit potential suppression l={ell}",
        ratio_l,
        (Ul / U0) * (R / r) ** ell,
    )

checks.append("explicit potential suppression for l=1..7")

# If the first nonzero mode is L, potential and field exponents are L+1 and L+2.
L = sp.symbols("L", integer=True, nonnegative=True)
uL = Ul * (R / r) ** (L + 1)
fieldL = -sp.diff(uL, r)

scaled_potential = sp.simplify(uL * r ** (L + 1))
scaled_field = sp.simplify(fieldL * r ** (L + 2))
require_equal("leading mode potential exponent", scaled_potential, Ul * R ** (L + 1))
checks.append("leading mode potential exponent")
require_equal("leading mode field exponent", scaled_field, (L + 1) * Ul * R ** (L + 1))
checks.append("leading mode field exponent")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 67: Monopole Dominance in the Far Field

## Purpose

This report validates why the monopole controls the far field whenever it is
present.

## Validated Checks

{validation_bullets}

## Exterior Mode Decay

The monopole mode is:

```text
u_0(r) = U_0 R/r.
```

The `l`th exterior mode is:

```text
u_l(r) = U_l (R/r)^(l+1).
```

Therefore:

```text
u_l/u_0 = (U_l/U_0)(R/r)^l.
```

For `r >> R`, every `l>0` mode is suppressed relative to the monopole.

## Field Strength

The field ratio is:

```text
(-u_l')/(-u_0') = (l+1)(U_l/U_0)(R/r)^l.
```

So higher modes are also suppressed in field strength by the same far-field
power, up to the factor `l+1`.

## Leading Nonzero Mode

If the first nonzero mode is `L`, then:

```text
u_L(r) ~ r^(-(L+1))
|grad u_L| ~ r^(-(L+2)).
```

The inverse-square field is therefore specifically the nonzero monopole case
in three spatial dimensions.
"""

out = Path(__file__).with_name("67_monopole_dominance_far_field.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
