#!/usr/bin/env python3
"""
make_25_symbolic_determinant_pattern_probe.py

Probe determinant patterns for balanced signature matrices using normalized
determinants and prime factor data.

Output:
    25_symbolic_determinant_pattern_probe.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
a = 1 - x**2
w = a**4


def integrate_poly(expr):
    return sp.integrate(sp.expand(expr), (x, 0, 1))


def psi(k):
    r = sp.Rational(2 * k - 1, 2 * k + 3)
    return x ** (2 * k) - r * x ** (2 * k - 2)


def c_Rq(R, q):
    return sp.factor(integrate_poly(a ** (R + 1) * x ** (2 * q)) / integrate_poly(a ** (R + 1)))


def balanced_det(R, N):
    P = sp.Matrix(
        [
            [
                sp.factor(integrate_poly(psi(k) * a**R * (x ** (2 * q) - c_Rq(R, q)) * w))
                for q in range(1, N + 1)
            ]
            for k in range(1, N + 1)
        ]
    )
    return sp.factor(P.det())


checks = []
rows = []

for R in range(0, 5):
    prev = None
    for N in range(1, 7):
        det = balanced_det(R, N)
        if det == 0:
            raise AssertionError(f"zero determinant R={R} N={N}")
        ratio = None if prev is None else sp.factor(det / prev)
        rows.append((R, N, det, ratio, sp.factorint(abs(sp.numer(det))), sp.factorint(abs(sp.denom(det)))))
        prev = det

checks.append("balanced determinants nonzero for R=0..4 N=1..6")
checks.append("successive determinant ratios computed")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
row_lines = "\n".join(
    (
        f"R={R}, N={N}: det={det}, det_N/det_prev={ratio}, "
        f"num_factors={numfac}, den_factors={denfac}"
    )
    for R, N, det, ratio, numfac, denfac in rows
)

md = f"""# Synthesis Proof 25: Determinant Pattern Probe

## Purpose

This report probes exact determinant patterns for balanced signature matrices:

```text
P_R[k,q] = integral psi_k a^R[x^(2q)-c_(R,q)]a^4 dx.
```

It is exploratory. It does not claim a closed formula.

## Validated Checks

{validation_bullets}

## Determinant Data

```text
{row_lines}
```

## Interpretation

The determinants are exactly nonzero over the tested grid. The successive
ratios and prime factor data may help identify a closed product formula.

This is the next remaining internal target: replace determinant evidence with
a general determinant theorem.
"""

out = Path(__file__).with_name("25_symbolic_determinant_pattern_probe.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All determinant checks passed.")
print(f"Wrote {out.resolve()}")


