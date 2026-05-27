#!/usr/bin/env python3
"""
make_41_boundary_flux_normalization_bridge.py

Validate the reduced normalization bridge between weak proper-time boundary
variation and the A-sector flux ledger.

Output:
    41_boundary_flux_normalization_bridge.md
"""

from pathlib import Path
import sympy as sp


K, F, M, alpha = sp.symbols("K F M alpha", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

# Linearized shared-boundary variation: K*F - M/2 = 0.
balance = K * F - M / 2
F_solution = sp.solve([sp.Eq(balance, 0)], [F], dict=True)
if F_solution != [{F: M / (2 * K)}]:
    raise AssertionError(f"unexpected flux solution: {F_solution}")
checks.append("linearized proper-time boundary variation gives F=M/(2K)")

target_flux = alpha * M
K_required = sp.solve([sp.Eq(M / (2 * K), target_flux)], [K], dict=True)
if K_required != [{K: 1 / (2 * alpha)}]:
    raise AssertionError(f"unexpected K normalization: {K_required}")
checks.append("target flux alpha*M fixes K=1/(2*alpha)")

F_with_K = simplify_expr((M / (2 * K)).subs(K, 1 / (2 * alpha)))
require_zero("target flux recovered", F_with_K - target_flux)
checks.append("with K=1/(2*alpha), boundary variation recovers F=alpha*M")

G, c = sp.symbols("G c", positive=True)
alpha_A = 8 * sp.pi * G / c**2
K_A = simplify_expr(1 / (2 * alpha_A))
require_zero("A-sector K normalization", K_A - c**2 / (16 * sp.pi * G))
checks.append("for alpha=8*pi*G/c^2, K=c^2/(16*pi*G)")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 41: Boundary Flux Normalization Bridge

## Purpose

This proof links the weak proper-time boundary source coefficient to the
reduced A-sector flux ledger.

## Validated Checks

{validation_bullets}

## Linearized Boundary Variation

From weak proper-time coupling, the matter boundary variation contributes:

```text
-M/2.
```

Let the vacuum boundary flux coefficient be:

```text
K F.
```

Stationarity gives:

```text
K F - M/2 = 0.
```

Therefore:

```text
F = M/(2K).
```

To match a target flux:

```text
F = alpha M,
```

one needs:

```text
K = 1/(2 alpha).
```

For the A-sector:

```text
alpha = 8*pi*G/c^2,
```

so:

```text
K = c^2/(16*pi*G).
```

## Gate Interpretation

The weak interval boundary source and A-sector flux ledger are compatible once
the vacuum action normalization is fixed. This is a bridge to the
vacuum-action-origin folder, not an independent derivation of the nonlinear
action.
"""

out = Path(__file__).with_name("41_boundary_flux_normalization_bridge.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Boundary flux normalization bridge passed.")
print(f"Wrote {out.resolve()}")
