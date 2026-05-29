#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("11_momentum_constraint_spatial_diff_gate.md")

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

C, xi, A=symbols('C xi A')
require_zero((xi*C).subs(C,0), 'Lie transport preserves zero constraint')
require_zero((xi*C + A).subs(C,0)-A, 'anomaly remains')


report = r'''# Momentum constraint spatial diffeomorphism gate

Spatial diffeomorphism transport of a constraint has the schematic form
\(\delta C=\mathcal L_\xi C\). If \(C=0\), it stays zero. An additive anomaly
survives on the constraint surface.
'''

write_report(report)
print(f"wrote {OUT.name}")
