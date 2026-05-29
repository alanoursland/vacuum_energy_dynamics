#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("1_massless_spin2_degree_count.md")

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
N_h=D*(D+1)/2
N_phys=simplify(N_h-2*D)
require_zero(N_phys-D*(D-3)/2, 'spin2 count formula')
require_zero(N_phys.subs(D,4)-2, 'D=4 two polarizations')


report = r'''# Massless spin-2 degree count gate

A symmetric metric perturbation in \(D\) spacetime dimensions has

\[
N_h=\frac{D(D+1)}2.
\]

Linear diffeomorphism redundancy removes \(2D\) phase-space directions, leaving

\[
N_{\mathrm{phys}}=\frac{D(D-3)}2.
\]

For \(D=4\), this gives two propagating polarizations. This is the massless
spin-2 branch whose nonlinear closure is being tested.
'''

write_report(report)
print(f"wrote {OUT.name}")
