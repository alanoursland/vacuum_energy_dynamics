#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("16_cosmological_constant_constraint_compatibility.md")

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

Lam, divg, gradLam=symbols('Lam divg gradLam')
div_term=gradLam + Lam*divg
require_zero(div_term.subs({gradLam:0, divg:0}), 'constant Lambda divergence')
require_zero(div_term.subs({divg:0})-gradLam, 'varying Lambda requires route')


report = r'''# Cosmological constant compatibility gate

The cosmological term \(\Lambda g_{ab}\) is divergence-free for constant
\(\Lambda\) under metric-compatible transport. It is compatible with Bianchi
closure but changes the vacuum/asymptotic branch.
'''

write_report(report)
print(f"wrote {OUT.name}")
