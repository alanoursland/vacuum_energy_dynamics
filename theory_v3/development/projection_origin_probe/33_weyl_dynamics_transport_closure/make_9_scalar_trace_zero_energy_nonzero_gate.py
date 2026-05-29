#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("9_scalar_trace_zero_energy_nonzero_gate.md")

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


A,B=sp.symbols('A B')
h=sp.Matrix([[A,B,0],[B,-A,0],[0,0,0]])
tr=sp.trace(h)
require_zero(tr,'trace zero')
energy=sp.simplify(sum(h[i,j]**2 for i in range(3) for j in range(3)))
require_equal(energy, 2*A**2+2*B**2, 'TT energy')
require_nonzero(energy,'nonzero TT energy')


write_md('# 9. Scalar trace zero but energy nonzero gate\n\nA general TT polarization matrix\n\n```text\n[[A, B, 0],\n [B,-A, 0],\n [0, 0, 0]]\n```\n\nhas zero scalar trace but nonzero quadratic amplitude.\n\nValidated checks:\n\n```text\ntr(h) = 0\nh_ij h_ij = 2A^2 + 2B^2\n```\n\nResult: scalar trace blindness does not mean no physical radiative content.\n')
