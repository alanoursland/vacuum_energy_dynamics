#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("11_bianchi_lambda_compatibility.md")
TITLE = 'Lambda term is divergence-compatible under metric compatibility'
DESC = 'constant Lambda is compatible with Bianchi/stress conservation.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

Lam,divg,gradLam=sp.symbols('Lambda div_g grad_Lambda')
res=(Lam*divg+gradLam).subs({divg:0,gradLam:0})
require_zero(res,'Lambda Bianchi')
md=f"""# {TITLE}

{DESC}

Schematic divergence: `nabla(Lambda g) = Lambda nabla g + (nabla Lambda) g`.

For metric compatibility and constant Lambda, residual is `{res}`.
"""
write_report(md)
