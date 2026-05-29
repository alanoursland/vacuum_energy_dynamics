#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name('7_weyl_vanishes_in_three_spacetime_dimensions.md')

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} != 0: {z}")


D=sp.symbols('D', integer=True, positive=True)
weyl=sp.simplify(D*(D+1)*(D+2)*(D-3)/12)
require_zero(weyl.subs(D,3), 'Weyl D=3')
require_zero(weyl.subs(D,4)-10, 'Weyl D=4')


md = f"""# 7. Weyl vanishes in D=3 not D=4

## Checked identities

The Weyl component count has a factor `(D-3)`, so it vanishes in three spacetime dimensions and is nonzero in four.

## Conclusion

Four-dimensional GR has genuine Weyl/free-curvature content beyond scalar/Ricci boundary ledgers.
"""
TMP = OUT.with_suffix('.tmp')
TMP.write_text(md)
TMP.replace(OUT)
print(f"wrote {OUT.name}")
