#!/usr/bin/env python3
"""
make_3_source_role_purity_gate.py

Formalize ordinary source role-purity for the A-sector route.

Output:
    3_source_role_purity_gate.md
"""

from pathlib import Path
import sympy as sp


i_A, i_Bs, i_zeta, i_kappa, S = sp.symbols("i_A i_Bs i_zeta i_kappa S")

incidences = [i_A, i_Bs, i_zeta, i_kappa]
source_error = sp.expand(sum(incidences) - 1)
source_load = sp.expand(S * source_error)

rows = []
clean_count_once = []
ordinary_clean = []

for a in (0, 1):
    for bs in (0, 1):
        for zeta in (0, 1):
            for kappa in (0, 1):
                subs = {i_A: a, i_Bs: bs, i_zeta: zeta, i_kappa: kappa}
                total = a + bs + zeta + kappa
                err = int(source_error.subs(subs))
                if total == 1:
                    status = "count-once"
                    clean_count_once.append((a, bs, zeta, kappa))
                elif total == 0:
                    status = "missing source"
                else:
                    status = "duplicate source"

                if (a, bs, zeta, kappa) == (1, 0, 0, 0):
                    role = "ordinary A-only source route"
                    ordinary_clean.append((a, bs, zeta, kappa))
                elif total == 1:
                    role = "single non-A route; not ordinary A-source"
                elif total == 0:
                    role = "source disappears"
                else:
                    role = "ordinary source duplicated"

                rows.append((a, bs, zeta, kappa, err, status, role))

if ordinary_clean != [(1, 0, 0, 0)]:
    raise AssertionError(f"unexpected ordinary clean rows: {ordinary_clean}")

if len(clean_count_once) != 4:
    raise AssertionError(f"expected four count-once placements, got {clean_count_once}")

if sp.simplify(source_load.subs({i_A: 1, i_Bs: 0, i_zeta: 0, i_kappa: 0})) != 0:
    raise AssertionError("A-only source route should be count-once")

if sp.simplify(source_load.subs({i_A: 1, i_Bs: 1, i_zeta: 0, i_kappa: 0})) == 0:
    raise AssertionError("A+B_s duplicate route should not vanish")

table = "\n".join(
    f"| {a} | {bs} | {zeta} | {kappa} | {err} | {status} | {role} |"
    for a, bs, zeta, kappa, err, status, role in rows
)

md = f"""# Source Safety Gate 3: Ordinary Source Role-Purity

## Purpose

This proof formalizes the ordinary-source count-once condition:

```text
i_A + i_Bs + i_zeta + i_kappa = 1.
```

It then isolates the ordinary A-sector route:

```text
i_A = 1
i_Bs = i_zeta = i_kappa = 0.
```

## Symbolic Setup

The source duplication/missing-entry load is:

```text
S_source * (i_A + i_Bs + i_zeta + i_kappa - 1).
```

## Exhaustive Binary Check

| i_A | i_Bs | i_zeta | i_kappa | source_error | status | role |
|---:|---:|---:|---:|---:|---|---|
{table}

## Result

There are four count-once placements at pure incidence level. Only one is the
ordinary A-sector source route:

```text
(i_A, i_Bs, i_zeta, i_kappa) = (1, 0, 0, 0).
```

Routes with more than one active incidence duplicate the ordinary source.
Routes with no active incidence lose the ordinary source.

## Gate Status

This proves role-purity as bookkeeping. It does not derive why matter enters
the A-sector; it states the condition a clean matter-source theorem must meet.
"""

out = Path(__file__).with_name("3_source_role_purity_gate.md")
out.write_text(md, encoding="utf-8")

print("Source role-purity gate passed.")
print(f"Wrote {out.resolve()}")
