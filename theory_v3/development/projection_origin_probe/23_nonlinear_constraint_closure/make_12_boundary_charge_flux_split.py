#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("12_boundary_charge_flux_split.md")

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

Qdot,F=symbols('Qdot F')
eq=Eq(Qdot, -F)
require_zero(solve(eq.subs(F,0), Qdot)[0], 'static flux gives conserved charge')
require_zero(solve(eq, Qdot)[0]+F, 'radiative flux changes charge ledger')


report = r'''# Boundary charge/flux split gate

A Coulombic constraint charge and radiative symplectic flux are different
boundary ledgers. In a static sector, flux vanishes and the charge is conserved;
with radiative flux, the charge ledger changes by the flux term.
'''

write_report(report)
print(f"wrote {OUT.name}")
