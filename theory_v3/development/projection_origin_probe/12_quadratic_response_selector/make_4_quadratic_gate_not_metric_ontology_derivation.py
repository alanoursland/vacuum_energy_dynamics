#!/usr/bin/env python3
"""
Record that the algebraic quadratic gate is not itself a derivation of metric ontology.

Output:
    4_quadratic_gate_not_metric_ontology_derivation.md
"""
from pathlib import Path

statements = [
    ('proved', 'quadratic Q satisfies parallelogram identity'),
    ('proved', 'polarization of quadratic Q recovers a symmetric bilinear form'),
    ('not_proved', 'the parent vacuum ontology must make Q exactly quadratic'),
    ('not_proved', 'all nonquadratic directional response branches are absent'),
]
if len(statements) != 4 or statements[2][0] != 'not_proved':
    raise AssertionError('dependency ledger malformed')

rows = ['| Status | Claim |', '|---|---|']
for status, claim in statements:
    rows.append(f'| `{status}` | {claim} |')

md = f"""# Quadratic Response Selector 4: Quadratic Gate Is Not Metric Ontology Derivation

## Purpose

This report prevents a hidden overclaim. The previous algebra proves what
follows if the local response is quadratic. It does not prove that the parent
ontology forces exact quadraticity.

## Ledger

{chr(10).join(rows)}

## Interpretation

The metric branch begins only after the quadratic/parallelogram condition is
secured. Without that condition, the natural continuation may be Finsler-like,
medium-like, or an explicitly routed higher directional response branch.
"""

out = Path(__file__).with_name('4_quadratic_gate_not_metric_ontology_derivation.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Quadratic ontology ledger passed.')
print(f'Wrote {out.resolve()}')
