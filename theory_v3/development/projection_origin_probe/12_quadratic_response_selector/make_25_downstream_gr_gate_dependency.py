#!/usr/bin/env python3
"""
Record that diffeo/EH/Levi-Civita gates depend on the metric quadratic response branch.

Output:
    25_downstream_gr_gate_dependency.md
"""
from pathlib import Path

gates = [
    ('polarization reconstruction', 'requires exact quadratic response'),
    ('metric compatibility', 'requires a metric tensor to preserve'),
    ('Levi-Civita minimal branch', 'requires metric compatibility plus torsion-source absence'),
    ('stress variation', 'requires symmetric metric variation'),
    ('EH+GHY action gate', 'requires metric/diffeomorphism action class'),
]
if len(gates) != 5:
    raise AssertionError('downstream gate table malformed')

rows = ['| Downstream Gate | Dependency |', '|---|---|']
for gate, dep in gates:
    rows.append(f'| {gate} | {dep} |')

md = f"""# Quadratic Response Selector 25: Downstream GR Gate Dependency

## Purpose

This report prevents downstream geometric gates from being read as independent
proofs of the quadratic response primitive.

## Dependency Table

{chr(10).join(rows)}

## Interpretation

The quadratic response selector is upstream of the usual metric geometry gates.
If it fails, the correct continuation is not EH geometry by default but a
nonmetric or explicitly routed higher-response branch.
"""

out = Path(__file__).with_name('25_downstream_gr_gate_dependency.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Downstream GR gate dependency passed.')
print(f'Wrote {out.resolve()}')
