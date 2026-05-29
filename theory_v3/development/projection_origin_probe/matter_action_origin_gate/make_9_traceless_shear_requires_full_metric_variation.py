#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name("9_traceless_shear_requires_full_metric_variation.md")

def require_zero(expr, label):
    value = sp.simplify(expr)
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

A,sqrtg,h=sp.symbols('A sqrtg h')
T00=A; T11=-A
# traceless metric variation h_ab=diag(h,-h)
dS=sp.Rational(1,2)*sqrtg*(T00*h + T11*(-h))
require_equal(dS, sqrtg*A*h, 'traceless shear detected')


content = r"""# Traceless Shear Requires Full Metric Variation

The same traceless stress that is invisible to conformal response is seen by
a traceless metric perturbation.  Thus the full tensor matter source requires
directional/shear-sensitive metric data.

"""

tmp = OUT.with_suffix(OUT.suffix + ".tmp")
tmp.write_text(content)
tmp.replace(OUT)
print(f"wrote {OUT.name}")
