#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("4_plus_cross_polarization_basis_gate.md")

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


plus=sp.Matrix([[1,0,0],[0,-1,0],[0,0,0]])
cross=sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])
def inner(A,B): return sp.simplify(sum(A[i,j]*B[i,j] for i in range(3) for j in range(3)))
require_zero(sp.trace(plus), 'plus trace')
require_zero(sp.trace(cross), 'cross trace')
require_zero(inner(plus,cross), 'plus cross orthogonal')
require_equal(inner(plus,plus), sp.Integer(2), 'plus norm')
require_equal(inner(cross,cross), sp.Integer(2), 'cross norm')


write_md('# 4. Plus/cross polarization basis gate\n\nThe two standard TT basis tensors for propagation in the `z` direction are\n\n```text\ne_+ = diag(1,-1,0)\ne_x = [[0,1,0],[1,0,0],[0,0,0]].\n```\n\nValidated checks:\n\n```text\ntr(e_+) = tr(e_x) = 0\n<e_+, e_x> = 0\n<e_+, e_+> = <e_x, e_x> = 2\n```\n\nResult: the free radiative tensor sector contains two independent TT polarizations, not one scalar mode.\n')
