#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("2_first_class_constraint_count.md")

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

q=6
phase=2*q
first_class=4
remaining=phase-2*first_class
require_zero(remaining-4, 'remaining phase-space dof')
require_zero(Rational(remaining,2)-2, 'remaining configuration dof')


report = r'''# First-class constraint count gate

In four dimensions, a spatial metric has six configuration components and
twelve phase-space components. Four first-class constraints remove eight
phase-space directions:

\[
12-2\cdot4=4.
\]

That leaves two configuration degrees of freedom, matching the TT count.
'''

write_report(report)
print(f"wrote {OUT.name}")
