#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("12_lovelock_dimension_classification.md")
TITLE = 'Lovelock order dimension classification'
DESC = 'Lovelock terms vanish/topologize/become dynamical depending on D and p.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

def cls(D,p):
    return 'vanishes' if D<2*p else ('topological' if D==2*p else 'dynamical')
rows=[(D,cls(D,1),cls(D,2),cls(D,3)) for D in range(2,8)]
md=f"""# {TITLE}

{DESC}

| D | p=1 | p=2 | p=3 |
|---:|---|---|---|
"""
for row in rows:
    md += f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |\n"
md += "\nThis is the Lovelock dimension/order gate.\n"
write_report(md)
