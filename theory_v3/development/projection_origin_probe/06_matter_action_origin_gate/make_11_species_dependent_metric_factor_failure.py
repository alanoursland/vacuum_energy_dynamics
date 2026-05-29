#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("11_species_dependent_metric_factor_failure.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

b1,b2,T,h=sp.symbols('b1 b2 T h')
response1=b1*T*h
response2=b2*T*h
diff=sp.factor(response1-response2)
require_equal(diff, (b1-b2)*T*h, 'species coupling difference')


content = r"""# Species-Dependent Metric Factor Failure

If two species use different metric coupling factors `β_1` and `β_2`, their
metric responses differ by

```text
(β_1-β_2) T^{ab} h_ab.
```

Universal interval comparison therefore requires a shared normalization or an
explicitly routed violation.  Species-dependent metric factors are not silent.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
