#!/usr/bin/env python3
"""
make_40_eh_ghy_prefactor_to_a_flux.py

Validate that the reduced EH/GHY weak boundary prefactor matches the A-sector
flux normalization imported from the matter-source gate.

Output:
    40_eh_ghy_prefactor_to_a_flux.md
"""

from pathlib import Path
import sympy as sp


c, G, M, F, K = sp.symbols("c G M F K", positive=True)
pi = sp.pi


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

alpha_A = 8 * pi * G / c**2
K_target = 1 / (2 * alpha_A)
K_EH_reduced = c**2 / (16 * pi * G)
require_zero("EH/GHY reduced prefactor target", K_target - K_EH_reduced)
checks.append("K=c^2/(16*pi*G) is equivalent to K=1/(2 alpha_A)")

boundary_balance = K * F - M / 2
F_solution = sp.solve([sp.Eq(boundary_balance, 0)], [F], dict=True)
if F_solution != [{F: M / (2 * K)}]:
    raise AssertionError(f"unexpected boundary balance solution: {F_solution}")
checks.append("weak boundary balance gives F=M/(2K)")

F_with_eh = simplify_expr((M / (2 * K)).subs(K, K_EH_reduced))
require_zero("EH/GHY reduced prefactor gives A flux", F_with_eh - alpha_A * M)
checks.append("K=c^2/(16*pi*G) gives F_A=(8*pi*G/c^2)M")

K_wrong = sp.symbols("K_wrong", positive=True)
flux_error = simplify_expr(M / (2 * K_wrong) - alpha_A * M)
solution_wrong = sp.solve([sp.Eq(flux_error, 0)], [K_wrong], dict=True)
if solution_wrong != [{K_wrong: K_EH_reduced}]:
    raise AssertionError(f"unexpected wrong-K solution: {solution_wrong}")
checks.append("the A-sector target fixes the weak boundary prefactor uniquely")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 40: EH/GHY Prefactor To A-Flux

## Purpose

This proof validates the coefficient handoff:

```text
matter-source gate -> weak boundary normalization -> EH/GHY reduced prefactor.
```

## Validated Checks

{validation_bullets}

## Target Flux

The reduced A-sector source law uses:

```text
alpha_A = 8*pi*G/c^2.
```

The matter-source boundary balance has:

```text
K F - M/2 = 0,
```

so:

```text
F = M/(2K).
```

Matching:

```text
F_A = alpha_A M
```

requires:

```text
K = 1/(2 alpha_A) = c^2/(16*pi*G).
```

## Interpretation

In the reduced static boundary convention used by the A-sector chain, the weak
EH/GHY boundary prefactor must be:

```text
c^2/(16*pi*G).
```

This is the same coefficient supplied by the matter-source-origin handoff.
"""

out = Path(__file__).with_name("40_eh_ghy_prefactor_to_a_flux.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("EH/GHY prefactor to A-flux passed.")
print(f"Wrote {out.resolve()}")
