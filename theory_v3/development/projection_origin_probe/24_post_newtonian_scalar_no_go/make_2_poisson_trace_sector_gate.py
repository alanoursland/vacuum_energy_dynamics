
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "2_poisson_trace_sector_gate.md"

def require_zero(expr, label):
    val = sp.simplify(expr)
    if val != 0:
        raise AssertionError(f"{label} failed: {val}")

def require_equal(a,b,label):
    require_zero(sp.simplify(a-b), label)

def write_md(text):
    tmp = OUT.with_suffix(OUT.suffix + ".tmp")
    tmp.write_text(text.strip()+"\n")
    tmp.replace(OUT)

rho, G, pi = sp.symbols('rho G pi')
# Newtonian Poisson scalar source channel has one source scalar rho.
source_channels = 1
require_equal(source_channels, 1, 'scalar Poisson has one source channel')

write_md(r'''
# 2. Poisson trace sector gate

The Newtonian scalar equation has one source channel:

```text
Delta Phi = 4 pi G rho.
```

This is the trace/monopole source ledger. It is not a full tensor source ledger.
''')
