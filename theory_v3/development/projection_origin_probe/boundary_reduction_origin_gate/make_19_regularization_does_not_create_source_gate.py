#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '19_regularization_does_not_create_source_gate.md'

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


s,C=sp.symbols('s C', positive=True)
# Profiles s^m have second derivative near boundary; m=2 gives constant local curvature inside but flux derivative at boundary zero? check derivative zero for m>=2.
rows=[]
for m in range(2,6):
    phi=C*s**m
    first=sp.limit(sp.diff(phi,s),s,0,dir='+')
    rows.append((m,first))
    require_zero(first,f'first derivative vanishes m={m}')
report="# 19. Boundary regularization does not create source gate\n\n"
report += "For contact order `m >= 2`, a compact-support cutoff profile `s^m` has zero first derivative at the support edge.\n\n"
for m,first in rows:
    report += f"- m={m}: d(s^m)/ds at boundary = {first}\n"
report += "\nConclusion: flux-safe regularization can remove boundary leakage. It should not be misread as creating the underlying source; it prevents the cutoff from adding a spurious boundary source.\n"


write_report(report)
