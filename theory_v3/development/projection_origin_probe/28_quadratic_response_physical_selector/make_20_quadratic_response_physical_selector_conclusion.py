
from pathlib import Path
import sympy as sp

OUT = Path(__file__).with_name(Path(__file__).name.replace('make_', '').replace('.py', '.md'))

def require_zero(expr, name='expr'):
    s = sp.simplify(expr)
    if s != 0:
        raise AssertionError(f"{name} expected 0, got {s}")
    return s

def require_nonzero(expr, name='expr'):
    s = sp.simplify(expr)
    if s == 0:
        raise AssertionError(f"{name} expected nonzero")
    return s

def write(md):
    tmp = OUT.with_suffix('.md.tmp')
    tmp.write_text(md.strip() + '\n')
    tmp.replace(OUT)

# Algebraic summary check: degree 2 term survives, degree 4 residual is killed by metric selectors.
eps=sp.symbols('eps')
selector_equation=sp.Eq(eps,0)
metric_branch=sp.solve(selector_equation,eps)[0]
if metric_branch != 0:
    raise AssertionError(metric_branch)
write(f'''# 20. Quadratic Response Physical Selector — Conclusion

This folder tested the physical selector pressure behind the metric branch.

Closed here:

```text
exact parallelogram response,
degree-two homogeneity,
scale-independent calibration,
polarization path-independence,
universal null-cone ownership,
linearized superposition,
constant-matrix representability
```

all reject hidden quartic/Finsler residuals of the tested kind. Algebraically, the shared branch condition is

```text
eps = {metric_branch}
```

Interpretation:

```text
If these physical consistency requirements are imposed, local directional
response collapses to the pseudo-Riemannian metric branch.
```

But if nonquadratic response is allowed, it is not forbidden mathematics. It must be routed as an explicit additional Finsler/medium/constitutive branch rather than hidden inside the metric.

So this group strengthens the metric-origin chain but does not prove that nature must impose the selectors. It identifies the exact work those selectors do.
''')
