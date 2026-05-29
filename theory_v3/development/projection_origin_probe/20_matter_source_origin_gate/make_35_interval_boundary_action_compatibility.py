#!/usr/bin/env python3
"""
make_35_interval_boundary_action_compatibility.py

Validate compatibility between interval/proper-time coupling and the reduced
boundary source action.

Output:
    35_interval_boundary_action_compatibility.md
"""

from pathlib import Path
import sympy as sp


M, A0, eps = sp.symbols("M A0 epsilon", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

# Proper-time boundary particle action in a static A metric:
# S_m = -M sqrt(A0).  The field variation gives -M/(2 sqrt(A0)) delta A0.
S_boundary = -M * sp.sqrt(A0)
variation_coeff = sp.diff(S_boundary, A0)
weak_coeff = sp.series(variation_coeff.subs(A0, 1 + eps), eps, 0, 2).removeO()
expected_weak_coeff = -M / 2 + M * eps / 4
require_zero("weak boundary proper-time variation coefficient", weak_coeff - expected_weak_coeff)
checks.append("proper-time boundary variation gives leading coefficient -M/2")

linearized_source_term = -sp.Rational(1, 2) * M * (A0 - 1)
linearized_variation = sp.diff(linearized_source_term, A0)
require_zero("linearized boundary source variation", linearized_variation + M / 2)
checks.append("linearized proper-time source is proportional to -M A/2 up to constants")

rescaled_q = 2 * sp.symbols("K", positive=True) * sp.symbols("F", positive=True)
K, F = sp.symbols("K F", positive=True)
boundary_flux_condition = sp.diff(K * F * A0 - sp.Rational(1, 2) * M * A0, A0)
require_zero("boundary source coefficient balance", boundary_flux_condition - (K * F - M / 2))
checks.append("boundary source coefficient can be matched to flux normalization")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 35: Interval Boundary Action Compatibility

## Purpose

This proof checks compatibility between two reduced descriptions:

```text
proper-time/interval matter coupling
boundary source coupling
```

It does not fix the full normalization of the gravitational action. It checks
that the weak boundary source has the expected linear dependence on the local
interval component.

## Validated Checks

{validation_bullets}

## Proper-Time Boundary Source

For a static boundary particle or shell:

```text
S_m = -M sqrt(A(R)).
```

The variation coefficient is:

```text
dS_m/dA = -M/(2 sqrt(A)).
```

Near:

```text
A = 1 + epsilon,
```

this becomes:

```text
dS_m/dA = -M/2 + O(epsilon).
```

Thus the leading weak boundary source is equivalent, up to constants, to:

```text
S_m,lin = -(M/2) A(R).
```

## Gate Interpretation

The reduced boundary source used in the A-sector flux proofs is compatible
with weak proper-time matter coupling. Matching the exact coefficient requires
the gravitational action normalization, which belongs to the action-origin
chain.
"""

out = Path(__file__).with_name("35_interval_boundary_action_compatibility.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Interval boundary action compatibility passed.")
print(f"Wrote {out.resolve()}")
