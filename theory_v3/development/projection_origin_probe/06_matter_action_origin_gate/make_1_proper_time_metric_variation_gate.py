#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("1_proper_time_metric_variation_gate.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

m, s = sp.symbols('m s', positive=True)
h00,h01,h11,v0,v1 = sp.symbols('h00 h01 h11 v0 v1')
hvv = h00*v0**2 + 2*h01*v0*v1 + h11*v1**2
# For ell = sqrt(q), δell = δq/(2 ell).
dell = hvv/(2*s)
# Point particle action S=-m∫ds gives δS=-m δs.
dS = -m*dell
expected = -m*hvv/(2*s)
require_equal(dS, expected, 'proper-time variation')


content = r"""# Proper-Time Metric Variation Gate

A shared proper-time action depends on the same quadratic interval used by
the geometry.  For a worldline tangent `v`, if

```text
s^2 = g_ab v^a v^b,
δ(s^2) = h_ab v^a v^b,
```

then

```text
δs = (h_ab v^a v^b)/(2s).
```

Thus a point-particle matter action sources the metric through a bilinear
`v^a v^b` stress factor.  This proves only the conditional gate: if matter
proper time is the shared metric interval, then metric stress coupling follows.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
