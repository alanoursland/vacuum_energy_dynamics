#!/usr/bin/env python3
"""
make_1_n_dimensional_flux_scaling.py

Validate conserved radial flux scaling in n spatial dimensions.

Output:
    1_n_dimensional_flux_scaling.md
"""

from pathlib import Path
import sympy as sp


n, r, Q, Omega = sp.symbols("n r Q Omega", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


area = Omega * r ** (n - 1)
field = Q / area
flux = simplify_expr(area * field)
field_exponent = simplify_expr(r * sp.diff(sp.log(field), r))

require_zero("conserved flux", flux - Q)
require_zero("field exponent", field_exponent - (1 - n))

field_n3 = simplify_expr(field.subs({n: 3, Omega: 4 * sp.pi}))
require_zero("three-dimensional field", field_n3 - Q / (4 * sp.pi * r**2))

md = f"""# Vacuum Dimension Selector 1: N-Dimensional Flux Scaling

## Purpose

This proof restates the radial flux scaling gate inside the dimension selector
folder.

## Validated Checks

- conserved radial flux equals `Q`: passed
- field strength scales as `r^(1-n)`: passed
- in three spatial dimensions the field is inverse-square: passed

## Computation

In `n` spatial dimensions, the area factor is:

```text
A_n(r) = Omega_n r^(n-1).
```

Conserved flux requires:

```text
A_n(r) F(r) = Q.
```

Thus:

```text
F(r) = Q/(Omega_n r^(n-1)).
```

Sympy verifies:

```text
d log(F)/d log(r) = {field_exponent}.
```

For `n=3` and `Omega_3=4*pi`:

```text
F(r) = {field_n3}.
```

## Interpretation

Inverse-square behavior is not generic. It is the `n=3` member of the
dimension-dependent conserved-flux family.
"""

out = Path(__file__).with_name("1_n_dimensional_flux_scaling.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("N-dimensional flux scaling passed.")
print(f"Wrote {out.resolve()}")
