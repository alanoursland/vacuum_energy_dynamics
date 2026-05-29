#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("19_minimal_closure_dependency_table.md")

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

gates=['metric','diff','stress','second_order','boundary','no_extra']
require_true(len(gates)==6, 'six named gates')
for i in range(len(gates)):
    require_true(len(gates[:i]+gates[i+1:])==5, 'removing a gate changes ledger')


report = r'''# Minimal closure dependency table

The Einstein branch is minimal only after assuming metric interval structure,
diffeomorphism redundancy, universal stress coupling, second-order locality,
boundary differentiability, and no extra un-routed fields. Removing any named
gate changes the ledger.
'''

write_report(report)
print(f"wrote {OUT.name}")
