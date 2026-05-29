#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("18_nonmetric_clock_tail_detectability.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

s,A,eps1,eps2=sp.symbols('s A eps1 eps2')
tau1=s+eps1*A; tau2=s+eps2*A
# Difference in identical background interval is visible.
diff=sp.expand(tau1-tau2)
require_equal(diff, (eps1-eps2)*A, 'nonmetric clock tail difference')


content = r"""# Nonmetric Clock Tail Detectability

A nonmetric clock tail is not silent.  If two clock sectors read

```text
τ_i = s + ε_i A,
```

then their difference contains `(ε_1-ε_2)A`.  Such a channel must be routed as
an explicit additional field or excluded by universality.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
