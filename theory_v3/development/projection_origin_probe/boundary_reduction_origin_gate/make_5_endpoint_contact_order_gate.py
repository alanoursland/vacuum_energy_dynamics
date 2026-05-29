#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '5_endpoint_contact_order_gate.md'

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} expected 0, got {simplified}")
    return simplified

def require_equal(a, b, label):
    return require_zero(sp.simplify(a-b), label)

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text)
    tmp.replace(OUT)


x=sp.symbols('x')
R=sp.symbols('R', integer=True, nonnegative=True)
# Test finite list instead symbolic derivative order
checks=[]
for m in range(1,6):
    a=(1-x)**m
    vals=[]
    for j in range(m):
        vals.append(sp.diff(a,x,j).subs(x,1))
        require_zero(vals[-1],f'contact derivative m={m} j={j}')
    nonzero=sp.diff(a,x,m).subs(x,1)
    checks.append((m, vals, nonzero))
report="# 5. Endpoint contact order gate\n\n"
report += "For `(1-x)^m`, all derivatives of order `< m` vanish at `x=1`, while the `m`th derivative is generally nonzero.\n\n"
report += "This is the elementary endpoint-contact mechanism behind boundary-safe compact support and admissibility ladders.\n\n"
for m, vals, nonzero in checks:
    report += f"- m={m}: lower derivatives = {vals}; mth derivative = {nonzero}\n"
report += "\nConclusion: endpoint contact is ordinary boundary regularity bookkeeping. It is a condition imposed by reduction/variation, not a claim that physics is located at the endpoint.\n"


write_report(report)
