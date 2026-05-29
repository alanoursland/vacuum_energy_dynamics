#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("19_minimal_action_dependency_table.md")
TITLE = 'Dependency table for the EH+GHY minimal branch'
DESC = 'records which imported assumptions do work in the minimality claim.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

assumptions=['metric interval structure','diffeomorphism/relabeling invariance','second-order locality','boundary differentiability','no extra un-routed fields','D=4 Lovelock class']
roles=['curvature variables','invariant action density','excludes generic higher-curvature order','requires GHY/Hamiltonian terms','routes extra modes away','makes EH uniquely dynamical']
if len(assumptions)!=6: raise AssertionError('table')
md=f"""# {TITLE}

{DESC}

| Assumption | Role |
|---|---|
"""
for a,r in zip(assumptions,roles):
    md += f"| {a} | {r} |\n"
md += "\nThe EH+GHY minimality claim is conditional on this ledger.\n"
write_report(md)
