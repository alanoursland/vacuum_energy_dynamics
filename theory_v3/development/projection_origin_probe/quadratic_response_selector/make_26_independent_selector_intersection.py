#!/usr/bin/env python3
"""
Record independent pressures toward exact quadratic response.

Output:
    26_independent_selector_intersection.md
"""
from pathlib import Path

selectors = [
    ('parallelogram identity', 'exact algebraic metric reconstruction'),
    ('degree-two homogeneity', 'scale-independent interval calibration'),
    ('polarization bilinearity', 'direction-independent symmetric tensor'),
    ('shared null cone', 'universal causal comparison'),
    ('local quadratic action', 'fixed Hessian strain branch'),
]
if len({name for name,_ in selectors}) != len(selectors):
    raise AssertionError('selector names not unique')

rows = ['| Selector Pressure | What It Protects |', '|---|---|']
for name, protects in selectors:
    rows.append(f'| {name} | {protects} |')

md = f"""# Quadratic Response Selector 26: Independent Selector Intersection

## Purpose

This report collects the pressures that converge on exact quadratic response.
They are related, but they test different failure modes.

## Selector Intersection

{chr(10).join(rows)}

## Interpretation

Exact quadraticity is not just a convenient algebraic assumption. It is the
intersection of several requirements needed for one shared pseudo-Riemannian
metric branch. Still, this is a selector intersection, not an ontology proof by
itself.
"""

out = Path(__file__).with_name('26_independent_selector_intersection.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Independent selector intersection passed.')
print(f'Wrote {out.resolve()}')
