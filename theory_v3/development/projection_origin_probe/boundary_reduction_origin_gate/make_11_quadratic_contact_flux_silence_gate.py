#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '11_quadratic_contact_flux_silence_gate.md'

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} expected 0, got {simplified}")
    return simplified

def require_equal(a, b, label):
    return require_zero(sp.simplify(a-b), label)

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text)
    tmp.replace(OUT)


s,R,C=sp.symbols('s R C', positive=True)
# s=R-r near boundary. profile s^m; radial derivative wrt r = -d/ds.
rows=[]
for m in range(1,5):
    phi=C*s**m
    dr=-sp.diff(phi,s)
    boundary=sp.limit(dr,s,0,dir='+')
    rows.append((m,sp.simplify(boundary)))
report="# 11. Quadratic contact flux-silence gate\n\n"
report += "Near a support boundary, write `s = R-r`. If `phi ~ s^m`, then radial flux is proportional to `-d phi/ds`.\n\n"
for m,b in rows:
    report += f"- m={m}: boundary derivative limit = {b}\n"
report += "\nLinear contact leaves finite boundary derivative; quadratic and higher contact make the derivative vanish.\n\n"
report += "Conclusion: quadratic contact is a standard boundary-regularity requirement for flux silence. It is not itself the underlying source dynamics.\n"


write_report(report)
