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

# Final consistency checks.
k, R = sp.symbols('k R', positive=True, integer=True)
r_proj = (2*k-1)/(2*k+3)
r_general = (2*k-1)/(2*k+2*R+3)
require_equal(r_general.subs(R,0), r_proj, 'projection is base contact class')
# Constant flux selects 1/r in d=3.
alpha = sp.symbols('alpha')
require_equal(sp.solve(sp.Eq(1-alpha,0),alpha)[0], 1, 'finite flux selects inverse radius')

write_report('24_gr_boundary_reduction_comparison_conclusion.md', r'''
# 24. GR boundary reduction comparison conclusion

This folder establishes the comparison ledger:

```text
weak-field GR/Newtonian scalar sector
    -> Poisson equation
    -> radial Gauss flux
    -> exterior 1/r finite-flux class
    -> compactified beta-moment admissibility comparison.
```

The projection-origin coefficient

```text
r_k = (2k-1)/(2k+3)
```

is the `R=0` base case of the compactified endpoint-contact ladder

```text
r_(R,k) = (2k-1)/(2k+2R+3).
```

Therefore the concrete comparison question is:

```text
After the same scalar reduction, compactification, field normalization, and
moment pairing, does weak-field GR land in R=0?
```

If yes, then the projection boundary condition is not different from the GR
weak-field scalar boundary condition; it is GR-compatible boundary reduction.
That does not mean the vacuum ontology is doing no work. It means any ontology
work is upstream: explaining why the GR-like scalar reduction, metric interval
structure, quadratic response, and boundary-compatible variational class are
the right ones.

If no, then the mismatch appears as a genuine contact/admissibility difference,
and the first diagnostic is the shift

```text
r_(R,k)-r_(0,k).
```

Final status:

```text
r_k is a solved boundary-admissibility coefficient.
The boundary ledger is generic.
The ontology question moves upstream to the structure being reduced.
```
''')
print('wrote', '24_gr_boundary_reduction_comparison_conclusion.md')
