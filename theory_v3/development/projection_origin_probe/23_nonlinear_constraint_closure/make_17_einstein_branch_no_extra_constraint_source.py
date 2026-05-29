#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("17_einstein_branch_no_extra_constraint_source.md")

def require_zero(expr, label):
    expr = simplify(expr)
    if expr != 0:
        raise AssertionError(f"{label} failed: {expr}")

def require_true(cond, label):
    if not bool(cond):
        raise AssertionError(f"{label} failed")

def write_report(text):
    tmp = OUT.with_suffix(".tmp")
    tmp.write_text(text)
    tmp.replace(OUT)

J, divT=symbols('J divT')
require_zero(solve(Eq(0, 8*pi*divT), divT)[0], 'closed Einstein ledger')
require_zero(solve(Eq(J, 8*pi*divT), divT)[0]-J/(8*pi), 'hidden source changes ledger')


report = r'''# Einstein branch no-extra-source gate

The minimal Einstein branch has no extra geometric divergence source:
\(\nabla_aG^{ab}=0\). Adding a hidden current \(J^b\) changes stress
conservation and must be explicitly routed.
'''

write_report(report)
print(f"wrote {OUT.name}")
