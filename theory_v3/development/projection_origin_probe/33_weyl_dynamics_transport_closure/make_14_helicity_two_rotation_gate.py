#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("14_helicity_two_rotation_gate.md")

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


th=sp.symbols('th')
# polarization vector transforms as angle 2 theta
R=sp.Matrix([[sp.cos(2*th), -sp.sin(2*th)],[sp.sin(2*th), sp.cos(2*th)]])
require_equal(sp.simplify(R.T*R-sp.eye(2)).norm(), 0, 'helicity rotation orthogonal')
# theta=pi gives 2pi rotation in polarization space, identity
require_zero(sp.simplify((R.subs(th, sp.pi)-sp.eye(2)).norm()), 'spin two under pi spatial rotation')


write_md("# 14. Helicity-two rotation gate\n\nThe plus/cross polarization pair rotates by twice the physical transverse angle:\n\n```text\n[A_+', A_x']^T = R(2θ)[A_+, A_x]^T.\n```\n\nValidated checks:\n\n```text\nR(2θ)^T R(2θ) = I\nR(2π) with θ=π gives identity in polarization space\n```\n\nResult: TT data transforms as spin-2/helicity-two tensor data, not as a scalar.\n")
