#!/usr/bin/env python3
"""
make_116_diffeomorphism_noether_divergence_gate.py

Validate the flat-symbolic Noether bookkeeping behind:

    diffeomorphism gauge invariance -> divergence-free field equation.

Output:
    116_diffeomorphism_noether_divergence_gate.md
"""

from pathlib import Path
import sympy as sp


t, x = sp.symbols("t x")


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

E00 = sp.Function("E00")(t, x)
E01 = sp.Function("E01")(t, x)
E11 = sp.Function("E11")(t, x)
xi0 = sp.Function("xi0")(t, x)
xi1 = sp.Function("xi1")(t, x)

# Symmetric field equation tensor E_ab in 2D flat notation.
# Gauge variation: delta h_ab = partial_a xi_b + partial_b xi_a.
# Then 1/2 E^ab delta h_ab = E^ab partial_a xi_b.
variation_density = (
    E00 * sp.diff(xi0, t)
    + E01 * sp.diff(xi1, t)
    + E01 * sp.diff(xi0, x)
    + E11 * sp.diff(xi1, x)
)

boundary_divergence = sp.diff(E00 * xi0 + E01 * xi1, t) + sp.diff(E01 * xi0 + E11 * xi1, x)
divergence_residual = -xi0 * (sp.diff(E00, t) + sp.diff(E01, x)) - xi1 * (
    sp.diff(E01, t) + sp.diff(E11, x)
)

require_equal(
    "gauge variation is boundary plus field divergence residual",
    variation_density,
    boundary_divergence + divergence_residual,
)
checks.append("gauge variation is boundary plus field divergence residual")

kappa = sp.symbols("kappa")
T00 = sp.Function("T00")(t, x)
T01 = sp.Function("T01")(t, x)
T11 = sp.Function("T11")(t, x)

H00 = E00 - kappa * T00
H01 = E01 - kappa * T01
H11 = E11 - kappa * T11

total_residual_0 = sp.diff(H00, t) + sp.diff(H01, x)
total_residual_1 = sp.diff(H01, t) + sp.diff(H11, x)

expected_residual_0 = (sp.diff(E00, t) + sp.diff(E01, x)) - kappa * (
    sp.diff(T00, t) + sp.diff(T01, x)
)
expected_residual_1 = (sp.diff(E01, t) + sp.diff(E11, x)) - kappa * (
    sp.diff(T01, t) + sp.diff(T11, x)
)

require_equal("total equation divergence component 0", total_residual_0, expected_residual_0)
require_equal("total equation divergence component 1", total_residual_1, expected_residual_1)
checks.append("field equation divergence matches source conservation bookkeeping")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 116: Diffeomorphism Noether Divergence Gate

## Purpose

This report validates the local bookkeeping behind the statement:

```text
diffeomorphism gauge invariance
  -> divergence-free geometric field equation.
```

The proof is a flat symbolic model. It records the integration-by-parts
identity that survives in covariant form.

## Validated Checks

{validation_bullets}

## Gauge Variation

For a symmetric field equation tensor `E_ab` and:

```text
delta h_ab = partial_a xi_b + partial_b xi_a,
```

the variation density is:

```text
1/2 E^ab delta h_ab = E^ab partial_a xi_b.
```

SymPy verifies:

```text
E^ab partial_a xi_b
  = boundary divergence
    - xi_b partial_a E^ab.
```

Therefore gauge invariance for arbitrary `xi_b` requires:

```text
partial_a E^ab = 0
```

up to the corresponding covariant replacement in nonlinear geometry.

## Source Bookkeeping

For:

```text
E_ab = kappa T_ab,
```

the total equation has consistent gauge bookkeeping only when the same
divergence identity is matched by source conservation.

## Interpretation

This is the action-level reason the nonlinear metric equation must have a
covariant divergence identity. The Einstein tensor has this identity through
the contracted Bianchi identity, which is why it can couple consistently to
conserved stress-energy.
"""

out = Path(__file__).with_name("116_diffeomorphism_noether_divergence_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
