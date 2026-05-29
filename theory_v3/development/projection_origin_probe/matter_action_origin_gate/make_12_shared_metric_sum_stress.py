#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("12_shared_metric_sum_stress.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

sqrtg,h,T1,T2,T3=sp.symbols('sqrtg h T1 T2 T3')
dS_total=sp.Rational(1,2)*sqrtg*(T1*h+T2*h+T3*h)
Ttot=T1+T2+T3
require_equal(dS_total, sp.Rational(1,2)*sqrtg*Ttot*h, 'stress additivity')


content = r"""# Shared Metric Sum Stress

When several matter sectors use the same metric interval, their stress
sources add linearly in the metric variation:

```text
T_total = Σ_i T_i.
```

This is the clean source ledger for universal coupling.  There is one metric
source route, with additive sector contributions.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
