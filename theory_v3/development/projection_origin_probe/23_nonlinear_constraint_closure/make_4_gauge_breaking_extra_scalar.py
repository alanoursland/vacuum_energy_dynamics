#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("4_gauge_breaking_extra_scalar.md")

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

massless=2
extra_scalar=1
require_zero(massless+extra_scalar-3, 'extra scalar mode count')
require_true((massless+extra_scalar)!=massless, 'extra scalar changes branch')


report = r'''# Gauge breaking extra scalar witness

If the scalar trace is not removed by gauge/constraint structure, it survives
as an additional scalar mode. The minimal massless spin-2 branch in \(D=4\)
has two modes; adding one un-routed scalar gives three.
'''

write_report(report)
print(f"wrote {OUT.name}")
