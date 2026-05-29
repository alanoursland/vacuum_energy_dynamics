#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("10_null_radiation_trace_failure.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

rho=sp.symbols('rho')
eta=sp.diag(-1,1,1,1)
k=sp.Matrix([1,1,0,0])
T=rho*(k*k.T)
trace=sum(eta[i,i]*T[i,i] for i in range(4))
energy=T[0,0]
require_zero(trace, 'null radiation trace')
require_equal(energy, rho, 'null radiation energy nonzero')


content = r"""# Null Radiation Trace Failure

Null radiation gives a decisive witness against trace-only matter coupling.
For a null vector `k`,

```text
T_ab = ρ k_a k_b
```

has zero trace but nonzero energy.  Any matter-origin story that only couples
to trace misses radiation-like stress.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
