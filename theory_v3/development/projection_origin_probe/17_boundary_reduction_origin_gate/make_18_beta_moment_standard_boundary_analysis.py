#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '18_beta_moment_standard_boundary_analysis.md'

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} expected 0, got {simplified}")
    return simplified

def require_equal(a, b, label):
    return require_zero(sp.simplify(a-b), label)

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text)
    tmp.replace(OUT)


y=sp.symbols('y', positive=True)
# Use a specific representative Beta moment to avoid conditional symbolic integration.
specific=sp.integrate(y**(sp.Rational(3,2)-1)*(1-y)**(2-1),(y,0,1))
expected=sp.Rational(4,15)
require_equal(specific,expected,'specific beta moment')
report=f"""# 18. Beta moment standard boundary analysis

The moment integrals used in the admissibility ladder are Beta moments:

```text
∫_0^1 y^(a-1)(1-y)^(b-1) dy = B(a,b).
```

For a representative case, SymPy verifies

```text
∫ y^(1/2)(1-y) dy = {specific} = B(3/2,2) = 4/15.
```

Conclusion: the `r_k` ladder lives in standard weighted endpoint moment
analysis. The unusual-looking ratio is not exotic by itself; its importance is
where it sits in the reduction chain.
"""


write_report(report)
