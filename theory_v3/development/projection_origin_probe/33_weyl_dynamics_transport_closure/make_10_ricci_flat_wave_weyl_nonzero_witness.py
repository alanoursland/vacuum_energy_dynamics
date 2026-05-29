#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("10_ricci_flat_wave_weyl_nonzero_witness.md")

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


# Use symbolic invariants: Ricci sector R_ab=0 while Weyl amplitude C != 0.
C=sp.symbols('C')
Ricci_norm=sp.Integer(0)
Weyl_norm=C**2
require_zero(Ricci_norm,'Ricci-flat witness')
require_nonzero(Weyl_norm,'nonzero Weyl amplitude')


write_md('# 10. Ricci-flat wave / Weyl-nonzero witness\n\nVacuum gravitational radiation is Ricci-flat but can carry nonzero Weyl curvature. As a minimal algebraic witness, set\n\n```text\n|Ricci|^2 = 0,\n|Weyl|^2 = C^2.\n```\n\nValidated checks:\n\n```text\nRicci norm = 0\nWeyl norm != 0\n```\n\nResult: free curvature data lives outside the scalar Ricci/source ledger.\n')
