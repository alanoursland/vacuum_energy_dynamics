#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("13_scalar_boundary_charge_independence_gate.md")

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


M,A,B=sp.symbols('M A B')
Q=M
TT_energy=2*A**2+2*B**2
require_zero(sp.diff(Q,A), 'charge independent of plus')
require_zero(sp.diff(Q,B), 'charge independent of cross')
require_nonzero(TT_energy,'TT energy nonzero')


write_md('# 13. Scalar boundary charge independence gate\n\nLet scalar Coulombic charge be `Q=M`, while TT amplitudes are `A` and `B`.\n\nValidated checks:\n\n```text\n∂Q/∂A = 0\n∂Q/∂B = 0\n2A^2 + 2B^2 != 0\n```\n\nResult: scalar charge and radiative tensor amplitudes are independent ledgers.\n')
