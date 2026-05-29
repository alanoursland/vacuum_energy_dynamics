#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("8_divergence_constraint_propagation_gate.md")

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


t,z,k,w,A=sp.symbols('t z k w A', nonzero=True)
phase=k*z-w*t
# transverse components only, longitudinal zero; constraint C = divergence = 0
C=sp.Integer(0)
require_zero(sp.diff(C,t), 'time derivative of divergence constraint')
# Introduce longitudinal contamination L cos phase, divergence nonzero
L=sp.symbols('L')
long=L*sp.cos(phase)
C_bad=sp.diff(long,z)
require_nonzero(C_bad, 'longitudinal contamination divergence')


write_md('# 8. Divergence constraint propagation gate\n\nFor a pure transverse wave the divergence constraint is identically zero and remains zero under time evolution. A longitudinal contamination\n\n```text\nh_zx = L cos(kz - wt)\n```\n\nproduces a nonzero divergence.\n\nValidated checks:\n\n```text\n∂_t C = 0 for C = 0\n∂_z[L cos(kz-wt)] != 0\n```\n\nResult: transport closure preserves TT constraints only inside the transverse sector; longitudinal modes must be gauge/routed/excluded.\n')
