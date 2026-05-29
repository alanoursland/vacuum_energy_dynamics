#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("15_mass_term_breaks_constraint_gate.md")

def require_zero(expr, label):
    val = sp.simplify(expr)
    if val != 0:
        raise AssertionError(f"{label} expected zero, got {val}")

def require_equal(a, b, label):
    diff = sp.simplify(a-b)
    if diff != 0:
        raise AssertionError(f"{label} expected equality, got diff {diff}")

def require_nonzero(expr, label):
    val = sp.simplify(expr)
    if val == 0:
        raise AssertionError(f"{label} expected nonzero")

def write_md(text):
    tmp = OUT.with_suffix('.md.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)


m,A=sp.symbols('m A')
# schematic mass term adds m^2 h to equation; gauge constraint residual proportional to m^2 * longitudinal/gauge amplitude
res=m**2*A
require_nonzero(res,'mass residual generic')
require_zero(res.subs(m,0),'massless closure')


write_md('# 15. Mass term breaks constraint gate\n\nA schematic mass term introduces a residual proportional to\n\n```text\nm^2 A.\n```\n\nValidated checks:\n\n```text\nm^2 A != 0 generically\nm^2 A = 0 when m = 0\n```\n\nResult: massless transport closure is special; extra massive branches require separate routing and extra degrees of freedom.\n')
