#!/usr/bin/env python3
"""
make_38_shared_interval_variation_gate.py

Validate that matter source variation and vacuum boundary variation must use
the same interval variable to balance directly.

Output:
    38_shared_interval_variation_gate.md
"""

from pathlib import Path
import sympy as sp


A, A_v, A_m, F, M = sp.symbols("A A_v A_m F M", positive=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

E_split = F * A_v - M * sp.sqrt(A_m)
dEv = sp.diff(E_split, A_v)
dEm = sp.diff(E_split, A_m)
require_zero("split vacuum variation", dEv - F)
require_zero("split matter variation", dEm + M / (2 * sp.sqrt(A_m)))
checks.append("independent variables produce separate variation equations")

E_shared = F * A - M * sp.sqrt(A)
dE_shared = simplify_expr(sp.diff(E_shared, A))
expected_shared = F - M / (2 * sp.sqrt(A))
require_zero("shared interval variation", dE_shared - expected_shared)
checks.append("shared variable produces direct boundary/source balance")

stationary_F = sp.solve([sp.Eq(dE_shared, 0)], [F], dict=True)
if stationary_F != [{F: M / (2 * sp.sqrt(A))}]:
    raise AssertionError(f"unexpected shared stationarity: {stationary_F}")
checks.append("stationarity sets vacuum boundary coefficient equal to matter interval source")

eps = sp.symbols("epsilon")
weak_balance = sp.series((M / (2 * sp.sqrt(1 + eps))), eps, 0, 2).removeO()
require_zero("weak shared source coefficient", weak_balance - (M / 2 - M * eps / 4))
checks.append("near A=1 the leading matter boundary coefficient is M/2")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Matter Source Origin Gate 38: Shared Interval Variation Gate

## Purpose

This proof checks a variable-ownership condition:

```text
matter source variation and vacuum boundary variation must act on the same
interval variable if they are to balance directly.
```

## Validated Checks

{validation_bullets}

## Split Variables

If the vacuum boundary term uses `A_v` while matter proper time uses a
separate `A_m`:

```text
E = F A_v - M sqrt(A_m),
```

then the variations are separate:

```text
dE/dA_v = F
dE/dA_m = -M/(2 sqrt(A_m)).
```

No direct source/boundary balance follows unless another constraint identifies
the variables.

## Shared Variable

If both terms use the same interval component `A`:

```text
E = F A - M sqrt(A),
```

then:

```text
dE/dA = F - M/(2 sqrt(A)).
```

Stationarity gives:

```text
F = M/(2 sqrt(A)).
```

Near `A=1`, the leading matter coefficient is:

```text
F = M/2 + higher-order terms.
```

## Gate Interpretation

The source-origin chain requires the matter interval and the vacuum boundary
interval to be the same variable, or else requires an explicit identification
constraint. Hidden duplicate interval variables do not close the source law.
"""

out = Path(__file__).with_name("38_shared_interval_variation_gate.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Shared interval variation gate passed.")
print(f"Wrote {out.resolve()}")
