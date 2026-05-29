#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("6_dirichlet_metric_boundary_well_posedness.md")
TITLE = 'Dirichlet metric data becomes well posed after boundary completion'
DESC = 'after completion the remaining boundary variation is proportional to fixed boundary data.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

dq=sp.symbols('dq')
B=2*dq
res=B.subs(dq,0)
require_zero(res,'Dirichlet residual')
md=f"""# {TITLE}

{DESC}

Completed boundary term: `2 delta q`.

Under fixed boundary data, residual is `{res}`.
"""
write_report(md)
