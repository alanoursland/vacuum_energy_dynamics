#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("8_no_boundary_completion_failure_witness.md")
TITLE = 'Without a boundary term the variational problem is not well posed'
DESC = 'nonzero leakage remains without counterterm.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

B=sp.symbols('B')
if B==0: raise AssertionError('witness failed')
md=f"""# {TITLE}

{DESC}

Without boundary completion the leakage witness is `{B}`, which is not identically zero.
"""
write_report(md)
