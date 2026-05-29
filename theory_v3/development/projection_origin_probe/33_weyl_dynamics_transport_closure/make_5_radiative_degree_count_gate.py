#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("5_radiative_degree_count_gate.md")

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


D=sp.symbols('D', integer=True, positive=True)
dof=sp.simplify(D*(D-3)/2)
require_equal(dof.subs(D,4),2,'D=4 graviton DOF')
# compare scalar dof
require_equal(dof.subs(D,4)-1,1,'tensor radiation exceeds scalar by one polarization')


write_md('# 5. Radiative degree count gate\n\nFor a massless spin-2 field in `D` spacetime dimensions, the physical propagating count is\n\n```text\nD(D-3)/2.\n```\n\nValidated in `D=4`:\n\n```text\n4(4-3)/2 = 2.\n```\n\nResult: the radiative sector has two tensor polarizations in four dimensions. A scalar channel cannot supply the radiative degree count.\n')
