#!/usr/bin/env python3
"""
make_10_boundary_point_source_equivalence.py

Validate reduced equivalence between a boundary source coupling and exterior
A-sector flux.

Output:
    10_boundary_point_source_equivalence.md
"""

from pathlib import Path
import sympy as sp


R, K, q, M, G, c = sp.symbols("R K q M G c", positive=True)
Api, Ape, eta = sp.symbols("A_prime_in A_prime_ext eta")
pi = sp.pi


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

# With E_boundary = + q A(R), stationarity at the interface gives:
# 4*pi*K*R^2*(A'_in - A'_ext) + q = 0.
interface_coeff = 4 * pi * K * R**2 * (Api - Ape) + q
solution = sp.solve([sp.Eq(interface_coeff, 0)], [Ape], dict=True)
expected_Ape = Api + q / (4 * pi * K * R**2)
if len(solution) != 1 or Ape not in solution[0]:
    raise AssertionError(f"unexpected interface condition: {solution}")
require_zero("interface solution equivalence", solution[0][Ape] - expected_Ape)
checks.append("boundary coupling fixes exterior derivative jump")

F_ext = simplify_expr(4 * pi * R**2 * expected_Ape.subs(Api, 0))
require_zero("boundary source exterior flux", F_ext - q / K)
checks.append("regular interior gives exterior flux F_A=q/K")

q_mass = K * 8 * pi * G * M / c**2
F_mass = simplify_expr(F_ext.subs(q, q_mass))
require_zero("boundary source mass normalization", F_mass - 8 * pi * G * M / c**2)
checks.append("q=K*8*pi*G*M/c^2 reproduces the A-sector mass flux")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 10: Boundary Point Source Equivalence

## Purpose

This proof checks the reduced boundary-source version of the A-sector mass
coupling.

It is useful because the broader ontology often treats matter as a boundary or
constraint on the vacuum rather than as an arbitrary bulk field.

## Validated Checks

{validation_bullets}

## Interface Variation

For two radial bulk regions joined at `R`, with source coupling:

```text
E_boundary = + q A(R),
```

the interface variation coefficient is:

```text
4*pi*K*R^2 (A'_in - A'_ext) + q.
```

Stationarity gives:

```text
A'_ext = A'_in + q/(4*pi*K*R^2).
```

If the interior is regular with:

```text
A'_in = 0,
```

then:

```text
F_A = 4*pi*R^2 A'_ext = q/K.
```

Choosing:

```text
q = K * 8*pi*G*M/c^2
```

reproduces:

```text
F_A = 8*pi*G*M/c^2.
```

## Gate Interpretation

This proves a reduced equivalence between ordinary A-sector mass flux and a
boundary source coupling. It does not yet derive the boundary coupling from a
covariant matter action.
"""

out = Path(__file__).with_name("10_boundary_point_source_equivalence.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Boundary point source equivalence passed.")
print(f"Wrote {out.resolve()}")
