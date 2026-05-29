
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


allowed_by_bianchi = sp.Integer(1)
selected_by_flat_flux = sp.Integer(0)
# Encode the logical distinction as non-equivalence.
require_zero(allowed_by_bianchi-1, 'lambda allowed by metric compatibility')
require_zero(selected_by_flat_flux, 'nonzero lambda not selected by flat finite flux')
if allowed_by_bianchi == selected_by_flat_flux:
    raise AssertionError('allowed and selected collapsed')


write_md(r'''
# 23. Allowed Versus Selected Lambda Branch

This status gate records the logical distinction:

```text
constant Lambda is allowed by metric compatibility and Bianchi consistency;
nonzero Lambda is not selected by asymptotically flat finite-flux conditions.
```

The script intentionally keeps these booleans distinct. This prevents the
folder from converting permission into derivation.
''')
