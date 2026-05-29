#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("1_metric_volume_variation_gate.md")
TITLE = 'Variation of the metric volume density'
DESC = 'sqrt(g) variation produces the standard 1/2 trace factor.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

g,h=sp.symbols('g h', positive=True)
res=sp.diff(sp.sqrt(g),g)*h - sp.Rational(1,2)*sp.sqrt(g)*h/g
require_zero(res,'sqrt variation')
md=f"""# {TITLE}

{DESC}

Validated one-component identity:

```text
delta sqrt(g) = 1/2 sqrt(g) g^ab delta g_ab
```

Residual: `{sp.simplify(res)}`

This is the volume-density factor used by EH and metric matter variation.
"""
write_report(md)
