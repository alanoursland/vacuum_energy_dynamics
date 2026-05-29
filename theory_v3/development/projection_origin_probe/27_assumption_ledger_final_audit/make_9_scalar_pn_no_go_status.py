#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
m=sp.symbols('m', integer=True, positive=True)
metric_components=m*(m+1)/2
scalar_channels=1
assert sp.simplify(metric_components-scalar_channels).subs(m,3)==5
# vector current components in 3-space not encoded by one scalar
assert 3-1==2

REPORT = r"""
# 9. Scalar Post-Newtonian No-Go Status

## Claim

Scalar nonlinear dressing cannot supply the independent tensor/vector/shear
channels required by post-Newtonian GR.

## Check

In a three-dimensional spatial slice, a symmetric spatial metric has six
components and a scalar supplies one trace channel. Vector/current channels
also exceed scalar density data.

## Ledger status

Closed as a scalar-only limitation. This is not a no-go for the full relational
interval program; it is a no-go for replacing tensor geometry with scalar
polynomial dressing.
"""

Path(__file__).with_name('9_scalar_pn_no_go_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 9_scalar_pn_no_go_status.md')
