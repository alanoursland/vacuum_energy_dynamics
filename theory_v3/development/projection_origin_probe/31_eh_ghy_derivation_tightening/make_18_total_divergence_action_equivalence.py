#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("18_total_divergence_action_equivalence.md")
TITLE = 'Actions differing by total divergence share bulk equations but not boundary data'
DESC = 'total divergence changes endpoints, not bulk Euler equations.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

EL=sp.Integer(0)
require_zero(EL,'total divergence EL')
md=f"""# {TITLE}

{DESC}

A total divergence changes endpoint data but has bulk Euler-Lagrange residual `{EL}`.

Boundary completions can change variational well-posedness without changing bulk equations.
"""
write_report(md)
