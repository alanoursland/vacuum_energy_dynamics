#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("19_closure_dependency_table.md")

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


# Boolean dependency sanity: dynamics requires local tensor data AND transport law.
L,T=sp.symbols('L T')
# Use algebraic Boolean-like product: closure = L*T. It vanishes if either missing.
closure=L*T
require_zero(closure.subs(L,0),'no local tensor data no Weyl dynamics')
require_zero(closure.subs(T,0),'no transport law no Weyl dynamics')
require_equal(closure.subs({L:1,T:1}),1,'both inputs give closure flag')


write_md('# 19. Closure dependency table\n\nThis folder separates two inputs:\n\n```text\nL = local traceless tensor data,\nT = transport / constraint law.\n```\n\nA schematic closure flag is\n\n```text\nclosure = L T.\n```\n\nValidated checks:\n\n```text\nL=0 -> no Weyl dynamics\nT=0 -> no Weyl dynamics\nL=T=1 -> closure flag present\n```\n\nResult: local tensor probes and transport closure are both required.\n')
