#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

# Symbolic checks
import sympy as sp
rho1,rho2=sp.symbols('rho1 rho2')
T=rho1+rho2
assert sp.diff(T,rho1)==1 and sp.diff(T,rho2)==1
# infinitely many decompositions rho1 + rho2 = T
s=sp.symbols('s')
assert sp.simplify((s)+(T-s)-T)==0

REPORT = r"""
# 11. Matter Ontology Open Status

## Claim

Stress tensors are source ledgers, not microscopic matter generators.

## SymPy check

A total source `T` admits infinitely many decompositions

```text
T = s + (T-s).
```

Thus the stress ledger alone does not determine species, internal symmetries,
charges, masses, spin, or quantization.

## Ledger status

Open frontier. Matter coupling is conditionally closed; matter ontology is not.
"""

Path(__file__).with_name('11_matter_ontology_open_status.md').write_text(REPORT.strip()+"\n", encoding='utf-8')
print('wrote 11_matter_ontology_open_status.md')
