#!/usr/bin/env python3
"""
Create dependency table for quadratic response selector.

Output:
    27_quadratic_response_dependency_table.md
"""
from pathlib import Path

rows_data = [
    ('Quadratic form algebra', 'assume Q is degree-two', 'polarization gives bilinear metric', 'does not explain why Q is quadratic'),
    ('Hessian approximation', 'smooth stationary response', 'local quadratic sector exists', 'higher terms remain'),
    ('Nonquadratic witness', 'allow quartic response', 'metric reconstruction fails', 'branch must be routed'),
    ('Calibration coherence', 'one shared interval calibration', 'pressures degree-two homogeneity', 'does not alone prove absence of all corrections'),
    ('GR downstream gates', 'metric branch already selected', 'Levi-Civita/EH gates become available', 'cannot prove their own upstream metric premise'),
]
if rows_data[0][3] != 'does not explain why Q is quadratic':
    raise AssertionError('dependency table lost key warning')

rows = ['| Gate | Required Assumption | Result | Remaining Dependency |', '|---|---|---|---|']
for row in rows_data:
    rows.append('| ' + ' | '.join(row) + ' |')

md = f"""# Quadratic Response Selector 27: Quadratic Response Dependency Table

## Purpose

This report makes dependencies explicit so the folder cannot be read as a
completed derivation of metric ontology.

## Dependency Table

{chr(10).join(rows)}

## Interpretation

The central open question is isolated: does the parent vacuum ontology force
exact parallelogram/quadratic response, or does it merely permit a metric branch
among other directional-response branches?
"""

out = Path(__file__).with_name('27_quadratic_response_dependency_table.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Quadratic response dependency table passed.')
print(f'Wrote {out.resolve()}')
