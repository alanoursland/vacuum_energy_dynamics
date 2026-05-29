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

# Boolean implication ledger: same boundary does not imply no upstream work.
B, U = sp.symbols('B U')
# Model as logical expression: U -> B, but B does not imply U.
# Truth table witness: B=True, U=False is allowed, so B => U is not tautological.
vals = [(False,False),(False,True),(True,False),(True,True)]
# Check witness exists for B and not U.
witness = any((b and not u) for b,u in vals)
if not witness:
    raise AssertionError('logic witness failed')

write_report('17_ontology_work_upstream_gate.md', r'''
# 17. Ontology work is upstream gate

Logical ledger:

```text
upstream ontology may imply a boundary ledger,
but the same boundary ledger does not imply the ontology.
```

The script includes the truth-table witness:

```text
B = true, U = false
```

is logically possible.

Interpretation: matching GR's boundary reduction would not prove the vacuum
ontology. Conversely, it also would not prove the ontology is idle. The work is
upstream and must be assessed by assumption reduction, not by boundary novelty.
''')
print('wrote', '17_ontology_work_upstream_gate.md')
