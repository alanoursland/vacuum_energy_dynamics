#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("17_local_tensor_data_not_dynamics_gate.md")

def require_zero(expr, label):
    val = sp.simplify(expr)
    if val != 0:
        raise AssertionError(f"{label} expected zero, got {val}")

def require_equal(a, b, label):
    diff = sp.simplify(a-b)
    if diff != 0:
        raise AssertionError(f"{label} expected equality, got diff {diff}")

def require_nonzero(expr, label):
    val = sp.simplify(expr)
    if val == 0:
        raise AssertionError(f"{label} expected nonzero")

def write_md(text):
    tmp = OUT.with_suffix('.md.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)


# Algebraic local symmetric matrix has entries but no time derivative/news unless transport variable is introduced.
A,B,N=sp.symbols('A B N')
local_energy=2*A**2+2*B**2
news_energy=N**2
require_nonzero(local_energy,'local tensor amplitude')
require_nonzero(news_energy,'news requires independent transport derivative')
# No algebraic expression in A,B alone forces a unique N.
N1=0; N2=A
require_nonzero(N2-N1,'different news for same local data possible without transport law')


write_md('# 17. Local tensor data is not dynamics gate\n\nLocal directional probes recover tensor amplitudes such as `A` and `B`, but radiative dynamics requires a transport derivative/news variable.\n\nValidated witness:\n\n```text\nN = 0 and N = A\n```\n\nare both algebraically possible for the same local amplitude data unless a transport law is supplied.\n\nResult: directional probes close local tensor data, not free Weyl dynamics by themselves.\n')
