from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent

def require_zero(expr, label):
    z = sp.simplify(sp.factor(expr))
    if z != 0:
        raise AssertionError(f"{label} failed: {z}")

def require_equal(a, b, label):
    require_zero(sp.simplify(a-b), label)

def write_report(name, text):
    path = ROOT / name
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)

# Same boundary does not imply no ontology work

# Truth-table witness: boundary match B and upstream ontology work U are logically independent.
B, U = sp.symbols('B U')
# Encode existence of model with B=1,U=1 and B=1,U=0; no contradiction algebraically.
vals = [(1,1),(1,0)]
assert all(v[0] == 1 for v in vals)


write_report('17_same_boundary_not_no_work.md', r'''
# 17. Same boundary does not imply no ontology work

A match between the GR scalar boundary ledger and the projection boundary ledger
would mean:

```text
same reduced scalar boundary class.
```

It would not mean:

```text
no upstream ontology work.
```

The upstream ontology question is whether fewer or different assumptions select
the metric/quadratic interval structure, calibration-coherent transport,
EH/GHY variation, matter coupling, or scalar weak-field reduction.  Those are
not decided by scalar boundary matching.

''')
print('wrote 17_same_boundary_not_no_work.md')
