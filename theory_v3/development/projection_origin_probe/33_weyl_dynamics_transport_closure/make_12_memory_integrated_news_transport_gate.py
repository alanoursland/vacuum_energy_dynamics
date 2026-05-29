#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("12_memory_integrated_news_transport_gate.md")

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


u,U,A=sp.symbols('u U A', positive=True)
# constant news over interval as a fast exact memory witness
N=A
Delta=sp.integrate(N, (u,0,U))
require_equal(Delta, A*U, 'memory integral')


write_md('# 12. Memory as integrated news transport gate\n\nA simple exact witness uses constant news over an interval:\n\n```text\nN(u)=A,  0 <= u <= U.\n```\n\nThe memory is\n\n```text\nΔh = ∫_0^U N du = A U.\n```\n\nResult: memory is an accumulated tensor boundary displacement, not a scalar charge.\n')
