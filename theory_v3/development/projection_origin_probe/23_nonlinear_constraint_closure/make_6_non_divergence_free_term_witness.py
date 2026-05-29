#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("6_non_divergence_free_term_witness.md")

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

J, divT = symbols('J divT')
eq = Eq(8*pi*divT, J)
require_zero(solve(eq, divT)[0] - J/(8*pi), 'nonzero correction divergence changes conservation')
require_zero(solve(eq.subs(J,0), divT)[0], 'zero correction recovers conservation')


report = r'''# Non-divergence-free term witness

Adding a correction \(X^{ab}\) with nonzero divergence gives

\[
\nabla_a(G^{ab}+X^{ab})=J^b.
\]

Then \(8\pi\nabla_aT^{ab}=J^b\). Unless \(J^b=0\), the correction introduces
an extra source ledger.
'''

write_report(report)
print(f"wrote {OUT.name}")
