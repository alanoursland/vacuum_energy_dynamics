#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '22_rk_not_independent_physical_selector.md'

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


k=sp.symbols('k', positive=True, integer=True)
r0=(2*k-1)/(2*k+3)
r1=(2*k-1)/(2*k+5)
base=sp.simplify(r0.subs(k,1))
higher=sp.simplify(r1.subs(k,1))
require_equal(base,sp.Rational(1,5),'base ratio k=1')
require_equal(higher,sp.Rational(1,7),'higher contact ratio k=1 R=1')
report=f"""# 22. r_k is not an independent physical selector

The base ratio is

```text
r_(0,k) = (2k-1)/(2k+3).
```

A higher endpoint-contact family gives

```text
r_(1,k) = (2k-1)/(2k+5).
```

For `k=1`, SymPy checks

```text
r_(0,1) = {base}
r_(1,1) = {higher}
```

Conclusion: the ratio changes with the boundary/contact admissibility class.
Thus `r_k` is evidence of a particular reduced boundary class, not by itself a
complete physical selection principle.
"""


write_report(report)
