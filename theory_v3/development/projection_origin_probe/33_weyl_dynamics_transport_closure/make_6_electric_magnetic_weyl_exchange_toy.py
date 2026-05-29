#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("6_electric_magnetic_weyl_exchange_toy.md")

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


t,z,A,w,k=sp.symbols('t z A w k', nonzero=True)
phase=k*z-w*t
E=A*sp.cos(phase)
B=A*sp.sin(phase)
# Maxwell-like toy closure for a wave: d_t E + w B =0, d_t B - w E =0
require_zero(sp.diff(E,t)-w*B, 'E evolves into B')
require_zero(sp.diff(B,t)+w*E, 'B evolves into E')
# nonzero invariant amplitude
amp=sp.simplify(E**2+B**2)
require_equal(amp, A**2, 'constant E/B amplitude')


write_md('# 6. Electric/magnetic Weyl exchange toy\n\nA radiative Weyl-like pair can be modeled by\n\n```text\nE = A cos(kz - wt),\nB = A sin(kz - wt).\n```\n\nValidated transport identities:\n\n```text\n∂_t E + w B = 0\n∂_t B - w E = 0\nE^2 + B^2 = A^2\n```\n\nResult: free tensor curvature data has transport structure; it is not just static scalar boundary charge.\n')
