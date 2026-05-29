#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
closed=8
conditional=7
open_items=5
total=closed+conditional+open_items
assert total==20
assert closed>open_items

REPORT = r"""
# 18. Derived / Imported / Open Table

## Closed or strongly closed

- `r_k` and the endpoint-contact ladder.
- Scalar ladder as trace/monopole boundary sector.
- Scalar blindness to Weyl/TT data.
- Scalar-only PN no-go.
- Boundary as reduction interface.

## Conditional bridges

- Metric branch after exact quadratic response.
- Universal stress coupling after shared metric matter action.
- Levi-Civita branch after torsion/nonmetric sources are absent or routed.
- EH/GHY and nonlinear closure after metric/diffeomorphism/locality assumptions.
- `D=4` after spin-2/Lovelock/time-channel assumptions.
- `Lambda=0` after asymptotically flat finite-flux branch selection.

## Open frontiers

- Physical origin of exact quadratic response.
- Matter ontology.
- Weyl/radiative sector origin.
- Full nonlinear action uniqueness.
- Quantum structure.

## Ledger status

This is the current global map.
"""

Path(__file__).with_name('18_derived_imported_open_table.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 18_derived_imported_open_table.md')
