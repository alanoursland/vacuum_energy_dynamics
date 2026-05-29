#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("13_nonmetric_channel_routing_gate.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

T,h,J,A=sp.symbols('T h J A')
metric_route=T*h
extra_route=J*A
total=metric_route+extra_route
# The extra channel vanishes iff J*A = 0.
require_equal(total-metric_route, J*A, 'extra route witness')


content = r"""# Nonmetric Channel Routing Gate

If a matter action contains an additional nonmetric channel, its variation
has an extra source ledger:

```text
δS = metric route + J δA.
```

That term is silent only if `J δA=0`.  Otherwise it must be routed as an
explicit additional field branch rather than hidden inside metric stress.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
