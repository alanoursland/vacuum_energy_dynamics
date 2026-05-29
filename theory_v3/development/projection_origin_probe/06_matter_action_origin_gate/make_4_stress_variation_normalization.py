#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("4_stress_variation_normalization.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

sqrtg = sp.symbols('sqrtg', positive=True)
T00,T01,T11,h00,h01,h11 = sp.symbols('T00 T01 T11 h00 h01 h11')
contraction = T00*h00 + 2*T01*h01 + T11*h11
dS = sp.Rational(1,2)*sqrtg*contraction
# Functional derivative with respect to symmetric components recovers the expected factors.
require_equal(sp.diff(dS,h00), sp.Rational(1,2)*sqrtg*T00, 'T00 normalization')
require_equal(sp.diff(dS,h01), sqrtg*T01, 'T01 symmetric normalization')
require_equal(sp.diff(dS,h11), sp.Rational(1,2)*sqrtg*T11, 'T11 normalization')


content = r"""# Stress Variation Normalization

The source ledger used by the metric equation is the coefficient of
`δg_ab` in the matter variation.  With symmetric off-diagonal components,

```text
δS_m = 1/2 ∫ sqrt(|g|) T^{ab} δg_ab.
```

The off-diagonal factor appears twice because `h_01=h_10`.  This script checks
the component normalization explicitly.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
