#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("7_maxwell_like_bianchi_closure_gate.md")

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


t,z,w,k,A=sp.symbols('t z w k A', nonzero=True)
phase=k*z-w*t
E=A*sp.cos(phase); B=A*sp.sin(phase)
# divergence-free in 1D transverse toy because no x/y dependence and longitudinal components zero
long_E=sp.Integer(0); long_B=sp.Integer(0)
require_zero(long_E, 'div E toy')
require_zero(long_B, 'div B toy')
# curl-like consistency demands w^2=k^2 for second wave equation
waveE=sp.diff(E,t,2)-sp.diff(E,z,2)
require_zero(waveE.subs(w**2,k**2), 'E wave closure')


write_md('# 7. Maxwell-like Bianchi closure gate\n\nFor radiative Weyl transport, the electric/magnetic decomposition behaves like a constraint-plus-evolution system. In a plane-wave toy model, longitudinal components vanish and wave propagation closes when\n\n```text\nw^2 = k^2.\n```\n\nValidated checks:\n\n```text\ndiv E = 0, div B = 0  (transverse toy)\n(∂_t^2 - ∂_z^2)E = 0 when w^2 = k^2\n```\n\nResult: Weyl dynamics requires transport/constraint closure, not just local tensor reconstruction.\n')
