#!/usr/bin/env python3
from pathlib import Path
import sympy as sp
OUT = Path(__file__).with_name("20_eh_ghy_tightening_conclusion.md")
TITLE = 'EH/GHY derivation tightening conclusion'
DESC = 'summarizes closed results and imported assumptions.'

def require_zero(expr, label):
    z = sp.simplify(expr)
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def write_report(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(OUT)

closed=5; imported=6
if closed<=0 or imported<=0: raise AssertionError('ledger')
md=f"""# {TITLE}

{DESC}

## Closed by this group

```text
EH-type second-derivative variation has boundary derivative leakage.
GHY-like completion cancels that leakage.
Hamiltonian differentiability uses the same boundary-generator logic.
In D=4, Lovelock minimality leaves EH as the unique dynamical local curvature term.
Curvature-squared branches carry higher-order / extra-mode routing burdens.
```

## Still imported

```text
metric interval structure;
diffeomorphism/relabeling invariance;
second-order locality;
boundary differentiability as a physical requirement;
absence/routing of extra fields;
D=4 Lovelock setting.
```

## Conclusion

```text
metric + diffeomorphism + second-order locality + boundary differentiability
+ no extra un-routed fields + D=4
    -> EH+GHY is the minimal local metric action branch.
```

This is an action-side closure result under assumptions, not a derivation of EH+GHY from `r_k` alone.
"""
write_report(md)
