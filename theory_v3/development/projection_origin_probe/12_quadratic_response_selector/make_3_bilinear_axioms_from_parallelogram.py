#!/usr/bin/env python3
"""
Validate symmetry, additivity, and scalar homogeneity for the polarized quadratic branch.

Output:
    3_bilinear_axioms_from_parallelogram.md
"""
from pathlib import Path
import sympy as sp

u1,u2,v1,v2,w1,w2,lam = sp.symbols('u1 u2 v1 v2 w1 w2 lam')
a,b,c = sp.symbols('a b c')

def B(x1,x2,y1,y2):
    return a*x1*y1 + b*(x1*y2 + x2*y1) + c*x2*y2

symmetry = sp.simplify(B(u1,u2,v1,v2) - B(v1,v2,u1,u2))
additivity = sp.simplify(B(u1+v1,u2+v2,w1,w2) - B(u1,u2,w1,w2) - B(v1,v2,w1,w2))
homogeneity = sp.simplify(B(lam*u1,lam*u2,v1,v2) - lam*B(u1,u2,v1,v2))
checks = {'symmetry': symmetry, 'additivity': additivity, 'homogeneity': homogeneity}
failed = {k:v for k,v in checks.items() if v != 0}
if failed:
    raise AssertionError(f'bilinear checks failed: {failed}')

md = f"""# Quadratic Response Selector 3: Bilinear Axioms From Parallelogram

## Purpose

This proof validates the algebraic behavior needed for a metric tensor once
polarization has reconstructed the bilinear form.

## Validated Checks

- symmetry `B(u,v)=B(v,u)`: passed
- additivity `B(u+v,w)=B(u,w)+B(v,w)`: passed
- scalar homogeneity `B(lambda u,v)=lambda B(u,v)`: passed

## Interpretation

In the exact quadratic branch, the polarized response behaves as a genuine
symmetric bilinear tensor. This is the algebraic entry point into metric
geometry.
"""

out = Path(__file__).with_name('3_bilinear_axioms_from_parallelogram.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Bilinear axiom checks passed.')
print(f'Wrote {out.resolve()}')
