#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
D=sp.symbols('D', integer=True, positive=True)
spin2=sp.simplify(D*(D-3)/2)
assert spin2.subs(D,4)==2
first_class_removed=2*D
components=D*(D+1)/2
assert sp.simplify(components-first_class_removed-spin2)==0

REPORT = r"""
# 13. Nonlinear Closure Conditional Status

## Claim

Under metric, diffeomorphism, second-order locality, boundary differentiability,
and no-extra-field assumptions, Einstein-like constraint closure is the minimal
known branch.

## SymPy check

The massless spin-2 degree count in `D=4` is two after first-class gauge
reduction.

## Ledger status

Conditional closure pressure, not an ontology-level derivation from the scalar
projection ladder.
"""

Path(__file__).with_name('13_nonlinear_closure_conditional_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 13_nonlinear_closure_conditional_status.md')
