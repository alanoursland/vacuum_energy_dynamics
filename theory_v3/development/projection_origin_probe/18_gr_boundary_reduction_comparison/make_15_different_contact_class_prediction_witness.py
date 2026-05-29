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

k = sp.symbols('k', positive=True, integer=True)
r0 = (2*k-1)/(2*k+3)
r1 = (2*k-1)/(2*k+5)
# Witness at k=1: r0=1/5, r1=1/7.
require_equal(r0.subs(k,1), sp.Rational(1,5), 'R=0 k=1 witness')
require_equal(r1.subs(k,1), sp.Rational(1,7), 'R=1 k=1 witness')
require_zero(sp.simplify(r0-r1) - sp.simplify(2*(2*k-1)/((2*k+3)*(2*k+5))), 'difference formula')

write_report('15_different_contact_class_prediction_witness.md', r'''
# 15. Different contact class prediction witness

Changing the contact class changes the ratio immediately. At `k=1`,

```text
R=0 -> r = 1/5,
R=1 -> r = 1/7.
```

Validated difference:

```text
r_(0,k)-r_(1,k)=2(2k-1)/[(2k+3)(2k+5)].
```

Interpretation: if a fully normalized GR reduction produced `R=1` instead of
`R=0`, the difference would be detectable directly in the projection ratio.
''')
print('wrote', '15_different_contact_class_prediction_witness.md')
