#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("16_trace_reversed_source_combination.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

D=sp.symbols('D')
T00,T11,T22,T33=sp.symbols('T00 T11 T22 T33')
# In D dimensions, trace-reversed source S_ab = T_ab - 1/(D-2) g_ab T.
# Check D=4 coefficient is 1/2.
coef=1/(D-2)
require_equal(coef.subs(D,4), sp.Rational(1,2), 'D=4 trace reverse coefficient')


content = r"""# Trace-Reversed Source Combination

Metric gravity does not couple only to `T_00`; the weak Newtonian limit uses
a trace-reversed combination.  In four dimensions the coefficient is

```text
1/(D-2) = 1/2.
```

This script records the trace-reversal normalization that connects matter
stress to the Newtonian scalar sector.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
