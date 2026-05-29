#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("7_conformal_trace_only_gate.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

sigma,sqrtg=sp.symbols('sigma sqrtg')
T00,T11=sp.symbols('T00 T11')
# Euclidean 2D conformal perturbation h_ab=2 sigma g_ab with g=I.
h00=2*sigma; h11=2*sigma
trace=T00+T11
dS=sp.Rational(1,2)*sqrtg*(T00*h00+T11*h11)
require_equal(dS, sqrtg*sigma*trace, 'conformal trace coupling')


content = r"""# Conformal Trace-Only Gate

A purely conformal/scalar metric response sees only the trace.  For
`h_ab = 2σ g_ab`,

```text
δS_m = ∫ sqrt(g) σ T^a_a.
```

This proves a key limitation: conformal response cannot supply general
traceless/shear stress coupling.  Full matter coupling needs full metric
variation, not trace-only variation.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
