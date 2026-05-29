#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("22_shared_interval_to_universal_stress_status.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

# Summary algebra: same h contracted with sum T_i is universal; beta_i creates residual.
b1,b2,T1,T2,h=sp.symbols('b1 b2 T1 T2 h')
universal=(T1+T2)*h
nonuniversal=(b1*T1+b2*T2)*h
residual=sp.expand(nonuniversal-universal)
require_equal(residual, ((b1-1)*T1+(b2-1)*T2)*h, 'nonuniversal residual')


content = r"""# Shared Interval to Universal Stress Status

Universal stress coupling means all matter sectors vary with the same
metric perturbation and the same normalization.  Any species-dependent factor
leaves a residual source ledger:

```text
[(β_1-1)T_1 + (β_2-1)T_2] h.
```

So universality is equivalent to locking the interval normalization across
matter sectors, or explicitly routing deviations.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
