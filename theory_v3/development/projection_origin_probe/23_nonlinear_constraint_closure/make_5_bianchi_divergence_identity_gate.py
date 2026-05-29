#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("5_bianchi_divergence_identity_gate.md")

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

divG, divT, extra = symbols('divG divT extra')
eq = Eq(divG, 8*pi*divT)
require_zero(solve(eq.subs(divG,0), divT)[0], 'Bianchi implies stress conservation')
eq_extra = Eq(divG+extra, 8*pi*divT)
require_zero(solve(eq_extra.subs(divG,0), divT)[0] - extra/(8*pi), 'extra divergence routes to source')


report = r'''# Bianchi divergence identity gate

Universal metric coupling requires a divergence-free geometric response:

\[
\nabla_a G^{ab}=0.
\]

Then \(G^{ab}=8\pi T^{ab}\) enforces \(\nabla_aT^{ab}=0\). A geometric side
with nonzero divergence requires an additional routed current.
'''

write_report(report)
print(f"wrote {OUT.name}")
