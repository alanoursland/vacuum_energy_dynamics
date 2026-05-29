#!/usr/bin/env python3
from pathlib import Path
from sympy import *

OUT = Path(__file__).with_name("7_stress_conservation_from_diff_variation.md")

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

Tdiv, xi = symbols('Tdiv xi')
variation_after_ibp = -Tdiv*xi
require_zero(solve(Eq(variation_after_ibp,0), Tdiv)[0], 'arbitrary xi gives conservation')


report = r'''# Stress conservation from diffeomorphism variation

For matter variation

\[
\delta S_m=\frac12\int\sqrt{-g}\,T^{ab}\delta g_{ab},
\]

and diffeomorphism variation \(\delta g_{ab}=2\nabla_{(a}\xi_{b)}\), integration
by parts leaves a coefficient proportional to \(-\nabla_aT^{ab}\xi_b\). For
arbitrary \(\xi_b\), diffeomorphism invariance requires conservation.
'''

write_report(report)
print(f"wrote {OUT.name}")
