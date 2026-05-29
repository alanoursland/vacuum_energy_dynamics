#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("3_massive_spin2_extra_modes.md")

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

D=symbols('D', integer=True, positive=True)
N_massive=(D+1)*(D-2)/2
require_zero(N_massive.subs(D,4)-5, 'massive spin2 in D=4 has 5 modes')
require_zero(N_massive.subs(D,4)-2-3, 'massive branch adds 3 modes')


report = r'''# Massive spin-2 extra-mode witness

A massive spin-2 field in four dimensions carries five polarizations, not two.
This is not the same branch as the massless diffeomorphism-constrained metric
field.

\[
N_{\mathrm{massive}}=\frac{(D+1)(D-2)}2.
\]
'''

write_report(report)
print(f"wrote {OUT.name}")
