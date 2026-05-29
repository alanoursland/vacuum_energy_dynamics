#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("15_four_dimensional_lovelock_minimality.md")

def require_zero(expr, label):
    expr = simplify(expr)
    if expr != 0:
        raise AssertionError(f"{label} failed: {expr}")

def require_true(cond, label):
    if not bool(cond):
        raise AssertionError(f"{label} failed")

def write_report(text):
    tmp = OUT.with_suffix(".tmp")
    tmp.write_text(text)
    tmp.replace(OUT)

D=4
def status(p):
    return 'vanishing' if D < 2*p else ('topological' if D == 2*p else 'dynamical')
require_true(status(1)=='dynamical', 'EH dynamical')
require_true(status(2)=='topological', 'GB topological')
require_true(status(3)=='vanishing', 'p=3 vanishes')


report = r'''# Four-dimensional Lovelock minimality gate

For Lovelock order \(p\):

```text
D < 2p: vanishing
D = 2p: topological
D > 2p: dynamical
```

In \(D=4\), Einstein-Hilbert is dynamical, Gauss-Bonnet is topological, and
higher Lovelock terms vanish.
'''

write_report(report)
print(f"wrote {OUT.name}")
