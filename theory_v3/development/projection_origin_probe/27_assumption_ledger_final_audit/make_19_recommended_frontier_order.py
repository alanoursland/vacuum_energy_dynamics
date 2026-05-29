#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
priority={'quadratic_response_physical_selector':1,'weyl_tensor_origin_gate':2,'radiative_boundary_memory_gate':3,'matter_microstructure_origin':4,'eh_ghy_tightening':5}
assert priority['quadratic_response_physical_selector'] < priority['matter_microstructure_origin']
assert len(priority)==5

REPORT = r"""
# 19. Recommended Frontier Order

## Recommended next frontier groups

```text
1. quadratic_response_physical_selector
2. weyl_tensor_origin_gate
3. radiative_boundary_memory_gate
4. matter_microstructure_origin
5. eh_ghy_tightening
```

## Reason

The scalar-boundary ledger is now largely consolidated. The largest remaining
load-bearing issue is whether exact quadratic response is physically selected,
not just chosen as the metric branch. After that, the next real beasts are Weyl
origin, radiation/memory, matter microstructure, and nonlinear action closure.
"""

Path(__file__).with_name('19_recommended_frontier_order.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 19_recommended_frontier_order.md')
