#!/usr/bin/env python3
"""
make_11_boundary_source_full_tensor_coupling.py

Validate that trace-only boundary coupling misses shear/traceless source data,
while full h_ab coupling sees it.

Output:
    11_boundary_source_full_tensor_coupling.md
"""

from pathlib import Path
import sympy as sp


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


tau, s, eps, off, eta = sp.symbols("tau s eps off eta")

dh_shear = sp.Matrix([[eps, 0], [0, -eps]])
T_shear = sp.Matrix([[s, 0], [0, -s]])

dh_offdiag = sp.Matrix([[0, eta], [eta, 0]])
T_offdiag = sp.Matrix([[0, off], [off, 0]])


def contraction(A, B):
    return simplify_expr(sum(A[i, j] * B[i, j] for i in range(A.rows) for j in range(A.cols)))


full_shear = contraction(T_shear, dh_shear)
trace_shear = simplify_expr(tau * sp.trace(dh_shear))
require_zero("full shear coupling", full_shear - 2 * s * eps)
require_zero("trace shear blindness", trace_shear)

full_offdiag = contraction(T_offdiag, dh_offdiag)
trace_offdiag = simplify_expr(tau * sp.trace(dh_offdiag))
require_zero("full offdiag coupling", full_offdiag - 2 * off * eta)
require_zero("trace offdiag blindness", trace_offdiag)

md = f"""# Vacuum Interval Directional Probe Origin 11: Boundary Source Full-Tensor Coupling

## Purpose

This proof checks the action/source side of the directional selector.

If boundary data includes shear/traceless components, a trace-only source
coupling cannot use that information. A full tensor coupling can.

## Validated Checks

- full tensor coupling sees diagonal shear: passed
- trace-only coupling is blind to diagonal shear: passed
- full tensor coupling sees off-diagonal shear: passed
- trace-only coupling is blind to off-diagonal shear: passed

## Diagonal Shear Test

Let:

```text
delta h = [[eps,0],[0,-eps]]
T = [[s,0],[0,-s]]
```

The full contraction gives:

```text
T^ab delta h_ab = {full_shear}
```

The trace-only coupling gives:

```text
tau tr(delta h) = {trace_shear}
```

## Off-Diagonal Shear Test

Let:

```text
delta h = [[0,eta],[eta,0]]
T = [[0,off],[off,0]]
```

The full contraction gives:

```text
T^ab delta h_ab = {full_offdiag}
```

The trace-only coupling gives:

```text
tau tr(delta h) = {trace_offdiag}
```

## Interpretation

Directional interval probes supply tensor data only if the boundary/source
action has a place to use tensor data. A scalar trace coupling is insufficient;
the relevant coupling must be of the form:

```text
T^ab delta h_ab
```

or an equivalent full-tensor boundary pairing.
"""

out = Path(__file__).with_name("11_boundary_source_full_tensor_coupling.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Boundary source full-tensor coupling passed.")
print(f"Wrote {out.resolve()}")

