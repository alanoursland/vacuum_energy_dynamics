#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("1_tt_plane_wave_tracefree_gate.md")

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


t, z, A, w, k = sp.symbols('t z A w k', nonzero=True)
phase = k*z - w*t
h = sp.Matrix([[A*sp.cos(phase), 0, 0],
               [0, -A*sp.cos(phase), 0],
               [0, 0, 0]])
trace = sp.trace(h)
require_zero(trace, 'TT plus trace')
energy = sp.simplify(sum(h[i,j]**2 for i in range(3) for j in range(3)))
require_nonzero(energy, 'nonzero tensor amplitude')


write_md('# 1. TT plane wave trace-free gate\n\nA plus-polarized plane wave\n\n```text\nh_xx = A cos(kz - wt),  h_yy = -A cos(kz - wt),  h_zz = 0\n```\n\nhas zero spatial trace but nonzero tensor amplitude.\n\nValidated checks:\n\n```text\ntr(h) = 0\nsum_ij h_ij h_ij = 2 A^2 cos(kz - wt)^2 != 0\n```\n\nResult: propagating TT data can be invisible to scalar trace while remaining physically nonzero.\n')
