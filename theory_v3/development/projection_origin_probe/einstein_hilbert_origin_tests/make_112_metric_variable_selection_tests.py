#!/usr/bin/env python3
"""
make_112_metric_variable_selection_tests.py

Validate algebraic selection tests for using a symmetric metric perturbation as
the geometric field variable in the weak-field lift.

Output:
    112_metric_variable_selection_tests.md
"""

from pathlib import Path
import sympy as sp


t, x = sp.symbols("t x")
D = sp.symbols("D", integer=True, positive=True)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

metric_components = D * (D + 1) / 2
massless_spin2_dof = simplify_expr(metric_components - 2 * D)
require_equal("massless spin-2 dof formula", massless_spin2_dof, D * (D - 3) / 2)
checks.append("massless spin-2 dof formula")

require_equal("four-dimensional graviton dof count", massless_spin2_dof.subs(D, 4), 2)
checks.append("four-dimensional graviton dof count")

require_equal("three-dimensional local graviton dof count", massless_spin2_dof.subs(D, 3), 0)
checks.append("three-dimensional local graviton dof count")

vector_dof = D - 2
scalar_dof = sp.Integer(1)
require_equal("four-dimensional vector dof count", vector_dof.subs(D, 4), 2)
checks.append("four-dimensional vector dof count")
require_equal("scalar dof count", scalar_dof, 1)
checks.append("scalar dof count")

# Source-coupling gauge check in 2D:
# For symmetric T_ab and delta h_ab = partial_a xi_b + partial_b xi_a,
#   1/2 T^ab delta h_ab
# equals a boundary divergence minus xi_b partial_a T^ab.
T00 = sp.Function("T00")(t, x)
T01 = sp.Function("T01")(t, x)
T11 = sp.Function("T11")(t, x)
xi0 = sp.Function("xi0")(t, x)
xi1 = sp.Function("xi1")(t, x)

variation_density = (
    T00 * sp.diff(xi0, t)
    + T01 * sp.diff(xi1, t)
    + T01 * sp.diff(xi0, x)
    + T11 * sp.diff(xi1, x)
)

boundary_divergence = sp.diff(T00 * xi0 + T01 * xi1, t) + sp.diff(T01 * xi0 + T11 * xi1, x)
conservation_residual = -xi0 * (sp.diff(T00, t) + sp.diff(T01, x)) - xi1 * (
    sp.diff(T01, t) + sp.diff(T11, x)
)

require_equal(
    "metric source gauge variation is boundary plus conservation residual",
    variation_density,
    boundary_divergence + conservation_residual,
)
checks.append("metric source gauge variation is boundary plus conservation residual")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 112: Metric Variable Selection Tests

## Purpose

This report records algebraic tests that support the metric perturbation as the
weak-field geometric variable under a local massless spin-2 lift with universal
conserved-source coupling.

This is not yet a derivation of the metric from the vacuum ontology. It is a
selection gate.

## Validated Checks

{validation_bullets}

## Degree-of-Freedom Gate

A symmetric rank-two perturbation in `D` dimensions has:

```text
D(D+1)/2
```

components. Linearized diffeomorphism gauge structure removes `2D` phase-space
degrees of freedom, leaving:

```text
D(D-3)/2.
```

In four dimensions:

```text
D(D-3)/2 = 2.
```

This is the massless spin-2 count.

## Source-Coupling Gate

For:

```text
delta h_ab = partial_a xi_b + partial_b xi_a,
S_source = (1/2) integral h_ab T^ab,
```

SymPy verifies in a two-coordinate symbolic model:

```text
(1/2)T^ab delta h_ab
  = boundary divergence
    - xi_b partial_a T^ab.
```

So the source coupling is gauge invariant up to a boundary term exactly when:

```text
partial_a T^ab = 0.
```

## Interpretation

The scalar field alone carries the Newtonian potential. Under the assumption of
a local massless spin-2 lift with universal conserved-source coupling, the
symmetric metric perturbation is selected. This supports the route:

```text
scalar boundary flux
  -> Newtonian metric sector
  -> linearized spin-2 field
  -> Einstein-Hilbert nonlinear completion under the Lovelock gate.
```
"""

out = Path(__file__).with_name("112_metric_variable_selection_tests.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
