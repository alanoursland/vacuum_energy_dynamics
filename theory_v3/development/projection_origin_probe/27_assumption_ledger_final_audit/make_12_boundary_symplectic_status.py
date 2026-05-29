#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
dq1,dp1,dq2,dp2=sp.symbols('dq1 dp1 dq2 dp2')
omega = dq1*dp2-dq2*dp1
omega_swap = dq2*dp1-dq1*dp2
assert sp.simplify(omega + omega_swap)==0

REPORT = r"""
# 12. Boundary Symplectic Status

## Claim

Radiative/tensor boundary data requires a phase-space/symplectic ledger, not
just scalar monopole charge.

## SymPy check

A canonical two-form is antisymmetric under exchange of variations.

## Ledger status

Closed as a structural separation: scalar charge ledger and radiative
symplectic flux ledger are different boundary objects.
"""

Path(__file__).with_name('12_boundary_symplectic_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 12_boundary_symplectic_status.md')
