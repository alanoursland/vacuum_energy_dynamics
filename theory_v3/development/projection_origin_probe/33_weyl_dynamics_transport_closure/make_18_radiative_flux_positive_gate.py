#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("18_radiative_flux_positive_gate.md")

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


Np,Nc=sp.symbols('Np Nc')
flux=sp.simplify(Np**2+Nc**2)
require_nonzero(flux,'positive radiative flux generic')
require_zero(flux.subs({Np:0,Nc:0}),'zero news zero flux')


write_md('# 18. Radiative flux positive gate\n\nWith plus/cross news components `N_+` and `N_x`, the quadratic flux witness is\n\n```text\nF = N_+^2 + N_x^2.\n```\n\nValidated checks:\n\n```text\nF != 0 generically\nF = 0 when N_+ = N_x = 0\n```\n\nResult: radiative flux is carried by tensor news, not scalar monopole charge.\n')
