#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("2_volume_factor_variation.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

a,b,c = sp.symbols('a b c', positive=True)
h00,h01,h11 = sp.symbols('h00 h01 h11')
g = sp.Matrix([[a,b],[b,c]])
h = sp.Matrix([[h00,h01],[h01,h11]])
detg = sp.det(g)
# derivative of sqrt(det(g)) in direction h
ε=sp.symbols('ε')
g_eps = g + ε*h
deriv = sp.diff(sp.sqrt(sp.det(g_eps)), ε).subs(ε,0)
expected = sp.sqrt(detg)*sp.trace(g.inv()*h)/2
require_zero(sp.factor(deriv-expected), 'delta sqrt det')


content = r"""# Volume Factor Variation

For a metric-dependent matter action, the invariant volume element is part
of the shared interval structure.  This script verifies in a 2×2 symbolic
metric that

```text
δ sqrt(det g) = 1/2 sqrt(det g) g^{ab} δg_ab.
```

So even matter terms with no explicit inverse metric still source the metric
through the volume response.  The volume factor is not an optional extra
ledger.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
