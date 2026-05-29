#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
h11,h22,h12=sp.symbols('h11 h22 h12')
Qe1=h11
Qe2=h22
Qsum=h11+h22+2*h12
recover=sp.simplify((Qsum-Qe1-Qe2)/2)
assert recover==h12

REPORT = r"""
# 7. Directional Probe Tensor Status

## Claim

Directional quadratic probes recover tensor components by polarization.

## SymPy check

For a symmetric bilinear form in two directions,

```text
Q(e1+e2) - Q(e1) - Q(e2)
```

recovers `2 h12`.

## Ledger status

Closed once exact quadratic directional response is granted. This is the bridge
from scalar trace data to full metric data.
"""

Path(__file__).with_name('7_directional_probe_tensor_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 7_directional_probe_tensor_status.md')
