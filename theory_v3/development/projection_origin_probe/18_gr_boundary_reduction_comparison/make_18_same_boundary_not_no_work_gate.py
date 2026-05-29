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

# Assumption-count toy model.
A_GR = sp.symbols('A_GR', integer=True, positive=True)
A_ont = sp.symbols('A_ont', integer=True, positive=True)
# If ontology derives the boundary using fewer imported assumptions, it does work.
# Validate algebraic reduction measure Delta = A_GR - A_ont.
Delta = A_GR - A_ont
require_equal(Delta.subs({A_GR:5,A_ont:3}), 2, 'assumption reduction witness')

write_report('18_same_boundary_not_no_work_gate.md', r'''
# 18. Same boundary does not mean no work

A boundary match can still be meaningful if the ontology reduces assumptions.
As a toy ledger, if GR imports five assumptions and the ontology imports three
before reaching the same boundary class, the reduction measure is

```text
Δ = 5 - 3 = 2.
```

Interpretation: sameness of output does not settle whether the ontology is
doing work. The question is which structures were imported versus derived.
''')
print('wrote', '18_same_boundary_not_no_work_gate.md')
