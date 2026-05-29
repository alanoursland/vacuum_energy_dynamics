#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("4_second_derivative_boundary_leakage_gate.md")
TITLE = 'Second-derivative actions create boundary derivative leakage'
DESC = 'Dirichlet field data alone does not kill derivative variation leakage.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

B0,B1=sp.symbols('B0 B1')
boundary=3*B0+5*B1
res=boundary.subs(B0,0)
if res==0: raise AssertionError('leakage witness failed')
md=f"""# {TITLE}

{DESC}

Boundary model: `3 delta q + 5 delta q'`.

With Dirichlet `delta q=0`, residual is `{res}`.

So second-derivative actions require boundary completion if only field values are fixed.
"""
write_report(md)
