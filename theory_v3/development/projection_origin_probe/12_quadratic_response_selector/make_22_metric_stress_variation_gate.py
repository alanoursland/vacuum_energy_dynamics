#!/usr/bin/env python3
"""
Validate the algebraic stress variation gate for a symmetric metric variable.

Output:
    22_metric_stress_variation_gate.md
"""
from pathlib import Path
import sympy as sp

h00,h01,h11,T00,T01,T11 = sp.symbols('h00 h01 h11 T00 T01 T11')
# Symmetric 2D contraction: T^{ab} h_ab = T00 h00 + 2 T01 h01 + T11 h11.
L = sp.Rational(1,2)*(T00*h00 + 2*T01*h01 + T11*h11)
variations = [sp.diff(L,h00), sp.diff(L,h01), sp.diff(L,h11)]
expected = [sp.Rational(1,2)*T00, T01, sp.Rational(1,2)*T11]
if variations != expected:
    raise AssertionError(f'stress variation mismatch: {variations}')

md = f"""# Quadratic Response Selector 22: Metric Stress Variation Gate

## Purpose

This proof checks the algebraic form of a symmetric metric variation coupling.
It is not a matter-origin proof; it only records what becomes available after a
symmetric metric variable exists.

## Computation

For the symmetric contraction

```text
L = 1/2 (T00 h00 + 2 T01 h01 + T11 h11),
```

SymPy computes:

```text
dL/dh00 = {sp.sstr(variations[0])}
dL/dh01 = {sp.sstr(variations[1])}
dL/dh11 = {sp.sstr(variations[2])}
```

## Interpretation

Standard stress coupling presupposes a symmetric metric variable. It is
downstream of the quadratic response gate, not upstream of it.
"""

out = Path(__file__).with_name('22_metric_stress_variation_gate.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Metric stress variation gate passed.')
print(f'Wrote {out.resolve()}')
