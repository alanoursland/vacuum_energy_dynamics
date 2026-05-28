#!/usr/bin/env python3
"""
make_3_green_function_dimension_classes.py

Validate radial source-free Green-function classes in n spatial dimensions.

Output:
    3_green_function_dimension_classes.md
"""

from pathlib import Path
import sympy as sp


r, n, Q, Omega = sp.symbols("r n Q Omega", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def radial_laplacian(u, dim):
    return simplify_expr(sp.diff(u, r, 2) + (dim - 1) * sp.diff(u, r) / r)


u_power = r ** (2 - n)
lap_power = simplify_expr(radial_laplacian(u_power, n))
require_zero("power-law harmonic for n>2", lap_power)

u_log = sp.log(r)
lap_log_2d = simplify_expr(radial_laplacian(u_log, 2))
require_zero("log harmonic in n=2", lap_log_2d)

u_linear = r
lap_linear_1d = simplify_expr(radial_laplacian(u_linear, 1))
require_zero("linear harmonic in n=1", lap_linear_1d)

field_power = simplify_expr(-sp.diff(u_power, r))
field_3d = simplify_expr(field_power.subs(n, 3))
require_zero("3D inverse-square derivative", field_3d - r**-2)

md = f"""# Vacuum Dimension Selector 3: Green Function Dimension Classes

## Purpose

This proof separates the radial Green-function classes by spatial dimension.

## Validated Checks

- for `n>2`, `r^(2-n)` is source-free harmonic away from the origin: passed
- for `n=2`, `log(r)` is source-free harmonic away from the origin: passed
- for `n=1`, the linear potential is source-free harmonic away from the source: passed
- for `n=3`, the power-law derivative is inverse-square: passed

## Radial Laplacian

For a radial function:

```text
Delta u = u'' + (n-1)u'/r.
```

Sympy verifies:

```text
Delta r^(2-n) = {lap_power}
Delta log(r) | n=2 = {lap_log_2d}
Delta r | n=1 = {lap_linear_1d}
```

For the power-law class:

```text
-d/dr r^(2-n) = {field_power}.
```

At `n=3`:

```text
-d/dr r^(-1) = {field_3d}.
```

## Interpretation

The inverse-square law is the three-dimensional power-law Green branch. Other
spatial dimensions have conserved flux, but their potential/field behavior is
different.
"""

out = Path(__file__).with_name("3_green_function_dimension_classes.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Green function dimension classes passed.")
print(f"Wrote {out.resolve()}")

