#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("8_constraint_propagation_schematic_gate.md")

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

A,C,S=symbols('A C S')
require_zero((A*C).subs(C,0), 'homogeneous constraints preserve zero')
require_zero((A*C+S).subs(C,0)-S, 'source drives constraint violation')


report = r'''# Constraint propagation schematic gate

Constraint propagation has the schematic homogeneous form

\[
\dot C=A C.
\]

If \(C=0\), it remains zero. With an un-routed source \(S\),

\[
\dot C=A C+S,
\]

zero is preserved only if \(S=0\).
'''

write_report(report)
print(f"wrote {OUT.name}")
