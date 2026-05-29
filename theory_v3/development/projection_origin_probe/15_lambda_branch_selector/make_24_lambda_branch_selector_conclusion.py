
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, label):
    simplified = sp.simplify(expr)
    if simplified != 0:
        raise AssertionError(f"{label} failed: {simplified}")

def write_md(text):
    tmp = OUT.with_suffix('.tmp')
    tmp.write_text(text.strip() + "\n", encoding='utf-8')
    tmp.replace(OUT)


# Check that the load-bearing generated reports exist before writing conclusion.
from pathlib import Path
here = Path(__file__).parent
required = [
    '5_asymptotic_flat_selects_lambda_zero.md',
    '10_trace_equation_lambda_shift.md',
    '14_finite_flux_boundary_condition_gate.md',
    '15_lambda_requires_global_or_auxiliary_route.md',
    '21_branch_intersection_selector.md',
    '23_allowed_vs_selected_lambda_branch.md',
]
missing = [name for name in required if not (here/name).exists()]
if missing:
    raise AssertionError(f'missing required reports: {missing}')


write_md(r'''
# 24. Lambda Branch Selector Conclusion

This folder closes with a conditional selector, not an absolute derivation.

The exact checks establish:

```text
1. Lambda is a volume baseline term, not connection strain.
2. Nonzero Lambda changes the radial weak-field asymptotic class.
3. Finite asymptotically flat flux selects Lambda = 0.
4. Localized source accounting does not determine the global baseline.
5. Constant Lambda is permitted by metric compatibility and Bianchi structure.
6. Dynamic relaxation requires an explicitly routed auxiliary/global channel.
```

Therefore the zero-Lambda branch is selected only after imposing the
asymptotically flat inverse-square boundary normalization. A nonzero Lambda
branch remains an allowed metric-action branch, but it changes the global
asymptotics and needs separate physical routing if it is to be explained rather
than chosen.
''')
