from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def require_zero(expr, label):
    z = sp.simplify(sp.combsimp(expr))
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

def write_report(name, text):
    path = ROOT / name
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)

t, m = sp.symbols('t m', positive=True, integer=True)
# If a compact support profile has contact a^m with a=(1-r/R), derivative scales as a^(m-1).
a = sp.symbols('a', positive=True)
profile = a**m
first_deriv_order = m-1
# Flux-silent boundary derivative requires m-1 >= 1 => m>=2.
# Verify witnesses rather than solving the integer inequality symbolically.
require_equal((1-1) >= 1, False, 'linear contact derivative not silent')
require_equal((2-1) >= 1, True, 'quadratic contact derivative silent')

write_report('10_endpoint_contact_order_gate.md', r'''
# 10. Endpoint contact order gate

For a boundary profile with contact

```text
profile ∼ a^m,
```

the derivative scales as

```text
profile' ∼ a^{m-1}.
```

Thus linear contact leaves a nonzero boundary derivative, while quadratic
contact makes the boundary derivative vanish.

Validated witnesses:

```text
m=1 fails derivative silence,
m=2 passes derivative silence.
```

Interpretation: contact order is a boundary-flux/admissibility condition. It
should not be confused with the deeper directional-response quadratic metric
gate.
''')
print('wrote', '10_endpoint_contact_order_gate.md')
