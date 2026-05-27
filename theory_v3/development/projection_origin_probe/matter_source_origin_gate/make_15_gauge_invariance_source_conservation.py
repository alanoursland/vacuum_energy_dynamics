#!/usr/bin/env python3
"""
make_15_gauge_invariance_source_conservation.py

Validate the linearized gauge-invariance source-conservation gate.

Output:
    15_gauge_invariance_source_conservation.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x")
T = sp.Function("T")(x)
xi = sp.Function("xi")(x)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

ibp_identity = T * sp.diff(xi, x) - (sp.diff(T * xi, x) - sp.diff(T, x) * xi)
require_zero("source conservation integration by parts", ibp_identity)
checks.append("T xi' = d(T xi)/dx - T' xi")

conserved_variation = (T * sp.diff(xi, x)).subs(sp.diff(T, x), 0)
boundary_only = sp.diff(T * xi, x).subs(sp.diff(T, x), 0)
require_zero("conserved source leaves boundary variation", conserved_variation - boundary_only)
checks.append("if T' = 0, gauge variation is boundary-only")

nonconservation_witness = sp.diff(T, x) * xi
if simplify_expr(nonconservation_witness) == 0:
    raise AssertionError("nonconservation witness should remain symbolic")
checks.append("nonzero source divergence leaves a bulk gauge-variation witness")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 15: Gauge Invariance Source Conservation

## Purpose

This proof records the linearized source-consistency gate:

```text
gauge/diffeomorphism consistency requires conserved source.
```

The proof is written as a one-dimensional integration-by-parts witness for the
standard tensor statement.

## Validated Checks

{validation_bullets}

## Model Identity

For a source coupling, the gauge variation contains terms of the form:

```text
T xi'.
```

SymPy verifies:

```text
T xi' = d(T xi)/dx - T' xi.
```

So the variation is boundary-only if:

```text
T' = 0.
```

The tensor version is:

```text
delta h_mu_nu = partial_mu xi_nu + partial_nu xi_mu
```

and the source coupling is gauge-compatible only when:

```text
partial_mu T^mu_nu = 0.
```

## Gate Interpretation

This is a source-origin constraint, not a new field equation. Any candidate
matter, residual, or projection source coupled to the metric lift must satisfy
the appropriate conservation/no-leak condition.
"""

out = Path(__file__).with_name("15_gauge_invariance_source_conservation.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Gauge-invariance source conservation passed.")
print(f"Wrote {out.resolve()}")
