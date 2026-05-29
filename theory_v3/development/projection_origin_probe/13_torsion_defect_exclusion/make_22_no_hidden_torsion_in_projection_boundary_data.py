#!/usr/bin/env python3
"""
make_22_no_hidden_torsion_in_projection_boundary_data.py

Validate that scalar projection boundary defects cannot silently absorb
torsion boundary data.

Output:
    22_no_hidden_torsion_in_projection_boundary_data.md
"""

from pathlib import Path
import sympy as sp


p, F_scalar = sp.symbols("p F_scalar")
C12, C13, C23 = sp.symbols("C12 C13 C23")
eta12, eta13, eta23 = sp.symbols("eta12 eta13 eta23")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


scalar_boundary_action = p * F_scalar
for component in [C12, C13, C23]:
    require_zero(
        f"scalar action insensitive to torsion component {component}",
        sp.diff(scalar_boundary_action, component),
    )

routed_torsion_action = p * (eta12 * C12 + eta13 * C13 + eta23 * C23)
grad_components = [
    simplify_expr(sp.diff(routed_torsion_action, C12)),
    simplify_expr(sp.diff(routed_torsion_action, C13)),
    simplify_expr(sp.diff(routed_torsion_action, C23)),
]

require_zero("routed gradient C12", grad_components[0] - p * eta12)
require_zero("routed gradient C13", grad_components[1] - p * eta13)
require_zero("routed gradient C23", grad_components[2] - p * eta23)

carrier_sensitivity = simplify_expr(sp.diff(routed_torsion_action, eta12))
require_zero("carrier sensitivity", carrier_sensitivity - p * C12)

md = f"""# Torsion Defect Exclusion 22: No Hidden Torsion In Projection Boundary Data

## Purpose

This proof checks whether scalar projection boundary data can absorb torsion
boundary data.

It cannot do so silently. An oriented carrier must be supplied explicitly.

## Validated Checks

- scalar projection boundary action is insensitive to torsion components: passed
- torsion boundary coupling requires explicit carriers: passed
- carrier sensitivity is nonzero when carrier is introduced: passed

## Scalar Boundary Data

Let scalar projection boundary data have the form:

```text
B_scalar = p F_scalar.
```

For torsion boundary components:

```text
C12, C13, C23,
```

Sympy verifies:

```text
dB_scalar/dC12 = dB_scalar/dC13 = dB_scalar/dC23 = 0.
```

## Routed Torsion Coupling

To couple scalar projection data to torsion components, one must introduce
explicit carriers:

```text
B_torsion = p(eta12 C12 + eta13 C13 + eta23 C23).
```

Then:

```text
dB_torsion/dC12 = {grad_components[0]}
dB_torsion/dC13 = {grad_components[1]}
dB_torsion/dC23 = {grad_components[2]}.
```

The carrier is visible:

```text
dB_torsion/deta12 = {carrier_sensitivity}.
```

## Interpretation

The scalar projection ladder cannot hide torsion boundary data. If torsion is
coupled to projection defects, the orientation carriers are additional fields
or routing data.
"""

out = Path(__file__).with_name("22_no_hidden_torsion_in_projection_boundary_data.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("No hidden torsion in projection boundary data passed.")
print(f"Wrote {out.resolve()}")

