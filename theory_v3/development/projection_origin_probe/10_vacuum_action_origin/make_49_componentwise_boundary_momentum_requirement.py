#!/usr/bin/env python3
"""
make_49_componentwise_boundary_momentum_requirement.py

Validate that full induced-metric boundary stationarity requires componentwise
boundary momenta.

Output:
    49_componentwise_boundary_momentum_requirement.md
"""

from pathlib import Path
import sympy as sp


p11, p12, p22, s11, s12, s22 = sp.symbols("p11 p12 p22 s11 s12 s22")
h11, h12, h22 = sp.symbols("h11 h12 h22")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

E_full = (p11 - s11) * h11 + 2 * (p12 - s12) * h12 + (p22 - s22) * h22
variation_vector = [
    sp.diff(E_full, h11),
    sp.diff(E_full, h12) / 2,
    sp.diff(E_full, h22),
]
target_vector = [p11 - s11, p12 - s12, p22 - s22]

for idx, (lhs, rhs) in enumerate(zip(variation_vector, target_vector)):
    require_zero(f"component variation {idx}", lhs - rhs)
checks.append("full boundary stationarity requires all component momenta")

solutions = sp.solve(
    [sp.Eq(v, 0) for v in variation_vector],
    [p11, p12, p22],
    dict=True,
)
if solutions != [{p11: s11, p12: s12, p22: s22}]:
    raise AssertionError(f"unexpected componentwise stationarity: {solutions}")
checks.append("stationarity sets p_ij=s_ij componentwise")

trace_only = sp.symbols("q")
E_trace_only = (trace_only - (s11 + s22)) * (h11 + h22)
trace_variation_vector = [
    sp.diff(E_trace_only, h11),
    sp.diff(E_trace_only, h12),
    sp.diff(E_trace_only, h22),
]
require_zero("trace-only offdiagonal variation", trace_variation_vector[1])
checks.append("trace-only boundary term has no off-diagonal momentum")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 49: Componentwise Boundary Momentum Requirement

## Purpose

This proof records the boundary momentum requirement for a full induced metric
variation.

## Validated Checks

{validation_bullets}

## Full Componentwise Pairing

For:

```text
E_boundary =
  (p11-s11)h11 + 2(p12-s12)h12 + (p22-s22)h22,
```

variation gives:

```text
p11 = s11
p12 = s12
p22 = s22.
```

The off-diagonal component is an independent boundary momentum condition.

## Trace-Only Failure

A trace-only term:

```text
(q - tr S)(h11+h22)
```

has no `h12` variation.

## Interpretation

Full GHY-like boundary stationarity requires componentwise induced-metric
momentum. A scalar trace ladder can only supply the trace part.
"""

out = Path(__file__).with_name("49_componentwise_boundary_momentum_requirement.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Componentwise boundary momentum requirement passed.")
print(f"Wrote {out.resolve()}")
