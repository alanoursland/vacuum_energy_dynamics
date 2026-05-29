#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
u,v,a,b,c=sp.symbols('u v a b c')
Q=lambda z: a*z**2
para=sp.expand(Q(u+v)+Q(u-v)-2*Q(u)-2*Q(v))
assert para==0
Q4=lambda z: a*z**2+b*z**4
para4=sp.expand(Q4(u+v)+Q4(u-v)-2*Q4(u)-2*Q4(v))
assert sp.expand(para4 - (12*b*u**2*v**2))==0

REPORT = r"""
# 6. Quadratic Metric Gate Status

## Claim

Exact metric reconstruction requires exact quadratic/parallelogram response.
A Hessian approximation alone is not the same as a globally exact metric
branch.

## SymPy check

For `Q(z)=az^2`, the parallelogram defect vanishes. For `Q(z)=az^2+bz^4`, the
parallelogram defect is nonzero.

## Ledger status

Conditional gate. Metric geometry is closed downstream of exact quadratic
response; exact quadratic response itself remains a load-bearing selector.
"""

Path(__file__).with_name('6_quadratic_metric_gate_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 6_quadratic_metric_gate_status.md')
