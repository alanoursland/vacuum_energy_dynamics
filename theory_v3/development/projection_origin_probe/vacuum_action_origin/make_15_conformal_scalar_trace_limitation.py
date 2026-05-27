#!/usr/bin/env python3
"""
make_15_conformal_scalar_trace_limitation.py

Validate that a scalar/conformal metric response couples only to the trace and
misses traceless/shear stress.

Output:
    15_conformal_scalar_trace_limitation.md
"""

from pathlib import Path
import sympy as sp


sigma, h00, h01, h11 = sp.symbols("sigma h00 h01 h11")
A, B = sp.symbols("A B")


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# Contravariant stress components in 2D with eta_ab=diag(-1,1).
T00 = A
T11 = A
T01 = B

trace = -T00 + T11
require_equal("traceless source condition", trace, 0)
checks.append("traceless source condition")

conformal_h00 = -2 * sigma
conformal_h11 = 2 * sigma
conformal_h01 = 0

conformal_coupling = sp.Rational(1, 2) * (
    conformal_h00 * T00 + 2 * conformal_h01 * T01 + conformal_h11 * T11
)
require_equal("conformal coupling to traceless source vanishes", conformal_coupling, 0)
checks.append("conformal coupling to traceless source vanishes")

general_metric_coupling = sp.Rational(1, 2) * (h00 * T00 + 2 * h01 * T01 + h11 * T11)
require_equal("general metric coupling to traceless source", general_metric_coupling, sp.Rational(1, 2) * A * (h00 + h11) + B * h01)
checks.append("general metric coupling to traceless source")

require_equal("pure shear source seen by metric shear", general_metric_coupling.subs({A: 0}), B * h01)
checks.append("pure shear source seen by metric shear")

require_equal("pure shear source missed by conformal response", conformal_coupling.subs({A: 0}), 0)
checks.append("pure shear source missed by conformal response")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 15: Conformal Scalar Trace Limitation

## Purpose

This report validates why the scalar prototype cannot be the full gravitational
field.

The gate is:

```text
conformal/scalar metric response
  -> trace coupling only
  -> misses traceless and shear stress.
```

## Validated Checks

{validation_bullets}

## Traceless Source

Use a two-dimensional stress tensor with:

```text
T^00 = A
T^11 = A
T^01 = B.
```

With `eta_ab = diag(-1,1)`, its trace is:

```text
eta_ab T^ab = -A + A = 0.
```

## Conformal Coupling

A conformal response has:

```text
h_ab = 2 sigma eta_ab.
```

The source coupling:

```text
1/2 h_ab T^ab
```

vanishes for this traceless source.

## General Metric Coupling

A general metric response gives:

```text
1/2 h_ab T^ab = 1/2 A(h_00+h_11) + B h_01.
```

So shear stress is visible to the metric shear component `h_01`.

## Interpretation

A scalar or conformal response can model the trace sector of metric response.
It cannot encode the full universal coupling required by stress-energy. The
next lift must include traceless/shear metric degrees of freedom.
"""

out = Path(__file__).with_name("15_conformal_scalar_trace_limitation.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
