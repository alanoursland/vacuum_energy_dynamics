#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("10_hypersurface_deformation_closure_shape.md")

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

Dcon,L,beta=symbols('Dcon L beta')
bracket=beta*Dcon+L
require_zero(bracket.subs({Dcon:0,L:0}), 'closed algebra vanishes on constraint surface')
require_zero(bracket.subs(Dcon,0)-L, 'leftover anomaly witness')


report = r'''# Hypersurface deformation closure shape

The Hamiltonian constraints must close into momentum/diffeomorphism
constraints:

\[
\{H[N],H[M]\}=D[\beta(N,M)].
\]

A leftover term \(L\) is an anomaly or an extra branch.
'''

write_report(report)
print(f"wrote {OUT.name}")
