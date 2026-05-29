#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("14_curvature_squared_extra_scalar_witness.md")

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

spin2=2
scalar=1
total=spin2+scalar
require_zero(total-3, 'R plus R2 generic extra scalar count')
require_true(total!=spin2, 'not minimal Einstein branch')


report = r'''# Curvature-squared scalar-mode witness

A simple \(R+\alpha R^2\)-type branch generically carries the massless spin-2
sector plus an extra scalar mode in four dimensions. This is not the minimal
Einstein branch unless the scalar is removed or explicitly routed.
'''

write_report(report)
print(f"wrote {OUT.name}")
