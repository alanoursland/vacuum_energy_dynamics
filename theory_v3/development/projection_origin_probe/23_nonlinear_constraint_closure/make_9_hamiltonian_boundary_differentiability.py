#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("9_hamiltonian_boundary_differentiability.md")

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

B,dQ=symbols('B dQ')
require_zero((B+dQ).subs(dQ,-B), 'boundary cancellation')


report = r'''# Hamiltonian boundary differentiability gate

A Hamiltonian variation with an uncancelled boundary term is not differentiable:

\[
\delta H_{\mathrm{bulk}}=\text{EOM}+B.
\]

Adding a boundary generator with \(\delta Q=-B\) cancels the boundary variation.
'''

write_report(report)
print(f"wrote {OUT.name}")
