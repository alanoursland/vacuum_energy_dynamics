#!/usr/bin/env python3
"""
make_14_metric_variation_universal_stress_coupling.py

Validate that varying the metric in a matter action produces universal
stress-energy coupling at first order.

Output:
    14_metric_variation_universal_stress_coupling.md
"""

from pathlib import Path
import sympy as sp


eps = sp.symbols("eps")
p0, p1, V = sp.symbols("p0 p1 V")
h00, h01, h11 = sp.symbols("h00 h01 h11")


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# Two-dimensional flat background eta = diag(-1,1).
K_flat = -p0**2 + p1**2
h_trace = -h00 + h11

# Covariant metric perturbation h_ab. To first order:
#   g^ab = eta^ab - h^ab
# with h^00=h00, h^01=-h01, h^11=h11.
g_inv_00 = -1 - eps * h00
g_inv_01 = eps * h01
g_inv_11 = 1 - eps * h11
sqrt_minus_g = 1 + eps * h_trace / 2

K_g = g_inv_00 * p0**2 + 2 * g_inv_01 * p0 * p1 + g_inv_11 * p1**2
L_density = -sp.Rational(1, 2) * sqrt_minus_g * K_g - sqrt_minus_g * V
linear_coeff = simplify_expr(sp.diff(L_density, eps).subs(eps, 0))

T_up_00 = p0**2 + sp.Rational(1, 2) * K_flat + V
T_up_01 = -p0 * p1
T_up_11 = p1**2 - sp.Rational(1, 2) * K_flat - V

metric_source_coupling = sp.Rational(1, 2) * (h00 * T_up_00 + 2 * h01 * T_up_01 + h11 * T_up_11)

require_equal("metric variation gives stress coupling", linear_coeff, metric_source_coupling)
checks.append("metric variation gives stress coupling")

require_equal("stress component T00", T_up_00, sp.Rational(1, 2) * p0**2 + sp.Rational(1, 2) * p1**2 + V)
checks.append("stress component T00")

require_equal("stress component T11", T_up_11, sp.Rational(1, 2) * p0**2 + sp.Rational(1, 2) * p1**2 - V)
checks.append("stress component T11")

require_equal("off-diagonal stress component", T_up_01, -p0 * p1)
checks.append("off-diagonal stress component")

conformal_substitution = {h00: -2 * sp.Symbol("sigma"), h11: 2 * sp.Symbol("sigma"), h01: 0}
sigma = sp.Symbol("sigma")
conformal_coupling = simplify_expr(metric_source_coupling.subs(conformal_substitution))
trace_coupling = simplify_expr(sigma * (-T_up_00 + T_up_11))
require_equal("conformal metric coupling is trace coupling", conformal_coupling, trace_coupling)
checks.append("conformal metric coupling is trace coupling")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 14: Metric Variation Universal Stress Coupling

## Purpose

This report validates the universal coupling gate:

```text
if the vacuum response variable is the metric,
then varying matter energy with respect to that metric produces stress-energy.
```

## Validated Checks

{validation_bullets}

## Matter Density

Use a scalar matter density on a two-dimensional background:

```text
L = -1/2 sqrt(-g) g^ab p_a p_b - sqrt(-g) V.
```

Perturb the covariant metric:

```text
g_ab = eta_ab + eps h_ab.
```

To first order:

```text
g^ab = eta^ab - eps h^ab
sqrt(-g) = 1 + eps h/2.
```

## Result

SymPy verifies that the first-order metric variation is:

```text
delta L = 1/2 h_ab T^ab.
```

The stress components are:

```text
T^00 = 1/2 p0^2 + 1/2 p1^2 + V
T^01 = -p0 p1
T^11 = 1/2 p0^2 + 1/2 p1^2 - V.
```

## Conformal Subcase

For a conformal metric response:

```text
h_ab = 2 sigma eta_ab,
```

the coupling becomes:

```text
sigma eta_ab T^ab.
```

So a conformal scalar mode couples only to the trace.

## Interpretation

Metric variation gives universal stress coupling because every energy density
uses the same interval and volume element. This is the action-origin reason the
metric, unlike an ordinary scalar field, is a universal source variable.
"""

out = Path(__file__).with_name("14_metric_variation_universal_stress_coupling.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
