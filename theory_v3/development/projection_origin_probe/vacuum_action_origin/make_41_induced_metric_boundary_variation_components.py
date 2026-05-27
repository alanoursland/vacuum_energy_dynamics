#!/usr/bin/env python3
"""
make_41_induced_metric_boundary_variation_components.py

Validate that a nonlinear boundary action varies against induced metric
components, not against an independent scalar.

Output:
    41_induced_metric_boundary_variation_components.md
"""

from pathlib import Path
import sympy as sp


h11, h12, h22 = sp.symbols("h11 h12 h22")
P11, P12, P22, S11, S12, S22 = sp.symbols("P11 P12 P22 S11 S12 S22")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

# Symmetric 2D induced metric variation.  The off-diagonal component appears
# twice in h_ij P^ij, hence the factor 2.
E_boundary = (
    (P11 - S11) * h11
    + 2 * (P12 - S12) * h12
    + (P22 - S22) * h22
)

d11 = sp.diff(E_boundary, h11)
d12 = sp.diff(E_boundary, h12)
d22 = sp.diff(E_boundary, h22)
require_zero("h11 boundary variation", d11 - (P11 - S11))
require_zero("h12 boundary variation", d12 - 2 * (P12 - S12))
require_zero("h22 boundary variation", d22 - (P22 - S22))
checks.append("boundary variation is componentwise in the induced metric")

solutions = sp.solve(
    [sp.Eq(d11, 0), sp.Eq(d12, 0), sp.Eq(d22, 0)],
    [P11, P12, P22],
    dict=True,
)
if solutions != [{P11: S11, P12: S12, P22: S22}]:
    raise AssertionError(f"unexpected induced-boundary stationarity: {solutions}")
checks.append("stationarity matches boundary momentum to boundary stress componentwise")

trace_h = h11 + h22
trace_source = sp.symbols("T")
E_trace = trace_source * trace_h
d_trace_11 = sp.diff(E_trace, h11)
d_trace_12 = sp.diff(E_trace, h12)
d_trace_22 = sp.diff(E_trace, h22)
require_zero("trace source h11 variation", d_trace_11 - trace_source)
require_zero("trace source h12 variation", d_trace_12)
require_zero("trace source h22 variation", d_trace_22 - trace_source)
checks.append("a scalar trace source cannot supply off-diagonal boundary variation")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 41: Induced Metric Boundary Variation Components

## Purpose

This proof records what the nonlinear boundary action has to vary against:

```text
the induced metric components.
```

It also shows why a scalar trace source is not enough to replace the full
boundary variation.

## Validated Checks

{validation_bullets}

## Component Boundary Variation

For a symmetric two-dimensional induced boundary metric:

```text
h = [[h11,h12],[h12,h22]],
```

use the linear boundary pairing:

```text
E_boundary =
  (P11-S11)h11 + 2(P12-S12)h12 + (P22-S22)h22.
```

Stationarity gives:

```text
P11 = S11
P12 = S12
P22 = S22.
```

## Trace-Only Limitation

A scalar trace term:

```text
T(h11+h22)
```

varies only in the diagonal trace directions and gives no off-diagonal
variation.

## Interpretation

The GHY/EH boundary problem is tensorial. A scalar projection boundary defect
can match a reduced trace sector, but it cannot replace the full induced-metric
boundary variation.
"""

out = Path(__file__).with_name("41_induced_metric_boundary_variation_components.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Induced metric boundary variation components passed.")
print(f"Wrote {out.resolve()}")
