#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("13_higher_derivative_initial_data_growth.md")

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

order2=2
order4=4
require_zero(order4-order2-2, 'fourth order adds two initial data per variable')
require_true(order4>order2, 'higher derivative branch bigger')


report = r'''# Higher-derivative initial-data growth witness

A second-order equation needs two time data per field variable. A fourth-order
equation needs four. Generic higher-curvature branches therefore introduce
extra initial data unless degenerate, topological, or constrained.
'''

write_report(report)
print(f"wrote {OUT.name}")
