#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("18_constraint_algebra_anomaly_witness.md")

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

C,A,f=symbols('C A f')
require_zero((f*C).subs(C,0), 'closed bracket vanishes')
require_zero((f*C+A).subs(C,0)-A, 'anomaly survives')


report = r'''# Constraint algebra anomaly witness

A closed constraint bracket is proportional to constraints and vanishes on the
constraint surface. An anomaly remains even when the constraints vanish.
'''

write_report(report)
print(f"wrote {OUT.name}")
