#!/usr/bin/env python3
"""
make_59_componentwise_tensor_strain_variation.py

Validate the safest first geometry-lift identity: a componentwise tensor
Dirichlet strain energy has componentwise Laplace Euler-Lagrange equations.

This is not a derivation of GR. It is only the first controlled lift from a
scalar strain field to a multi-component configuration field.

Output:
    59_componentwise_tensor_strain_variation.md
"""

from pathlib import Path
import sympy as sp


x, y, z = sp.symbols("x y z", real=True)
coords = (x, y, z)
h = sp.Function("h")
v = sp.Function("v")


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

hxyz = h(x, y, z)
vxyz = v(x, y, z)

grad_dot = sum(sp.diff(hxyz, c) * sp.diff(vxyz, c) for c in coords)
div_term = sum(sp.diff(vxyz * sp.diff(hxyz, c), c) for c in coords)
lap_h = sum(sp.diff(hxyz, c, 2) for c in coords)

require_zero("componentwise Dirichlet variation identity", grad_dot - div_term + vxyz * lap_h)
checks.append("componentwise Dirichlet variation identity")

# Repeat for a finite list of symbolic tensor components by linearity.
component_names = ["h00", "h01", "h11", "h22"]
for name in component_names:
    hc = sp.Function(name)(x, y, z)
    vc = sp.Function("v_" + name)(x, y, z)
    gd = sum(sp.diff(hc, c) * sp.diff(vc, c) for c in coords)
    div = sum(sp.diff(vc * sp.diff(hc, c), c) for c in coords)
    lap = sum(sp.diff(hc, c, 2) for c in coords)
    require_zero(f"variation identity for {name}", gd - div + vc * lap)

checks.append("componentwise identities verified for representative tensor components")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 59: Componentwise Tensor Strain Variation

## Purpose

This report validates the safest first geometry-lift identity.

It does not derive general relativity. It only proves what happens if the
scalar Dirichlet strain model is lifted componentwise to a multi-component
configuration field.

## Validated Checks

{validation_bullets}

## Identity

For one component `h` and variation `v`:

```text
grad h . grad v
  =
  div(v grad h) - v Delta h.
```

Therefore a componentwise energy:

```text
E[h] = 1/2 integral sum_A |grad h_A|^2 dV
```

has Euler-Lagrange equations:

```text
-Delta h_A = source_A.
```

## Interpretation

This is the first controlled lift from scalar field to configuration field:

```text
scalar boundary-flux model
  -> componentwise multi-field strain model.
```

It is not yet a tensorial theory of gravity. A real geometric lift still needs
constraints, gauge structure, coordinate invariance, and nonlinear connection
terms.
"""

out = Path(__file__).with_name("59_componentwise_tensor_strain_variation.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
