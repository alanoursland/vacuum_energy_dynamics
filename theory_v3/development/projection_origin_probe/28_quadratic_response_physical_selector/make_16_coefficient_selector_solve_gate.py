
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

x,y,u1,u2,v1,v2,a,b,c,d=sp.symbols('x y u1 u2 v1 v2 a b c d')
Q=a*x**2+b*y**2+c*x*y+d*x**4
def E(A,B): return Q.subs({x:A,y:B})
defect=sp.Poly(sp.expand(E(u1+v1,u2+v2)+E(u1-v1,u2-v2)-2*E(u1,u2)-2*E(v1,v2)),u1,u2,v1,v2)
coeffs=defect.coeffs()
# all coefficients are multiples of d; solve coefficients=0
sol=sp.solve(coeffs,[d], dict=True)
if not sol or sol[0].get(d)!=0:
    raise AssertionError(sol)
write(f'''# 16. Coefficient Selector Solve Gate

For the response ansatz

```text
Q = a*x^2 + b*y^2 + c*x*y + d*x^4
```

the parallelogram defect coefficients are

```text
{coeffs}
```

Solving them gives

```text
{sol}
```

The exact quadratic gate does not constrain the metric coefficients `a,b,c`, but it kills the nonquadratic coefficient `d`.
''')
