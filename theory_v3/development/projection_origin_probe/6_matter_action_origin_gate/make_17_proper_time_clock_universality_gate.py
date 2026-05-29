#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("17_proper_time_clock_universality_gate.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

b1,b2,s=sp.symbols('b1 b2 s')
tau1=b1*s; tau2=b2*s
ratio=sp.simplify(tau1/tau2)
# Universal clock comparison requires ratio independent of species labels; equality requires b1=b2.
require_equal(ratio, b1/b2, 'clock ratio')


content = r"""# Proper-Time Clock Universality Gate

If species measure proper time with different interval scale factors, clock
ratios contain `β_1/β_2`.  Universal clock comparison requires those factors to
be locked or the difference becomes operationally visible.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
