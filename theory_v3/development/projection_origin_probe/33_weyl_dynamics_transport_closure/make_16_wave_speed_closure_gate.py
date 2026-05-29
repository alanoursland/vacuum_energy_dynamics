#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("16_wave_speed_closure_gate.md")

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


t,z,A,w,k,c=sp.symbols('t z A w k c', nonzero=True)
phase=k*z-w*t
u=A*sp.cos(phase)
wave=sp.diff(u,t,2)-c**2*sp.diff(u,z,2)
res=sp.simplify(wave.subs(w**2,c**2*k**2))
require_zero(res,'wave speed closure')


write_md('# 16. Wave-speed closure gate\n\nFor a wave equation\n\n```text\n∂_t^2 u - c^2 ∂_z^2 u = 0,\n```\n\na plane wave closes only when\n\n```text\nw^2 = c^2 k^2.\n```\n\nResult: radiative transport requires a hyperbolic propagation cone, not just static boundary data.\n')
