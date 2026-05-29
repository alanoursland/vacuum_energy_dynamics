#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("19_metric_variation_sees_pressure.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

rho,p,h00,h11,h22,h33=sp.symbols('rho p h00 h11 h22 h33')
# Perfect fluid rest frame schematic: T^{ab} h_ab = rho h00 + p(h11+h22+h33)
contraction=rho*h00+p*(h11+h22+h33)
trace_only=(-rho+3*p)*sp.symbols('sigma')
# Pressure terms are independent of trace-only scalar unless h is conformal.
require_equal(sp.diff(contraction,p), h11+h22+h33, 'pressure metric response')


content = r"""# Metric Variation Sees Pressure

Matter stress is more than rest density.  In a rest-frame perfect-fluid
schematic,

```text
T^{ab} h_ab = ρ h_00 + p(h_11+h_22+h_33).
```

Pressure appears through spatial metric variation.  A matter-origin story must
handle full stress, not just scalar mass density.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
