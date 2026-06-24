# Underdetermination Witness

This is the first theorem-shaped target for the vacuum-sector phase.

Status:

```text
contract-level witness established
SymPy scalar prototype validation passed
```

## Claim

Local quadratic interval response determines metric data at a point. It does
not, by itself, determine strain dynamics between points.

In schematic form:

```text
Q_p(v) = g_ab(p) v^a v^b
```

determines `g_ab(p)` at each point when the quadratic gate holds.

It does not determine:

```text
connection/transport
curvature action
derivative order
boundary term
propagating modes
residual coefficient epsilon
```

Therefore a between-point strain principle is required unless the accumulated
gates independently force EH/GHY.

## Assumptions Used

The witness uses only the local-response content already admitted by the
vacuum-sector program:

```text
1. At each point p, there is local directional response Q_p(v).
2. If Q_p is exact quadratic, polarization reconstructs g_ab(p).
3. The reconstruction is pointwise.
```

It does not assume a transport law, curvature action, connection, boundary
term, or field equation.

## Minimal Argument

Pointwise metric reconstruction supplies:

```text
p -> g_ab(p).
```

But a field equation requires a rule for comparing nearby points:

```text
g_ab(p) compared with g_ab(q),
```

or, before metric reduction:

```text
X(p) compared with X(q).
```

The local Hessian does not specify that comparison. It does not say whether the
comparison is made by Levi-Civita transport, independent connection,
calibration map, holonomy, elastic medium strain, Finsler direction map, or
nonlocal kernel.

Therefore the local response branch determines the pointwise metric candidate
but not the between-point strain rule.

## Witness Form

Two functionals can share the same local response sector:

```text
S_1[X] = integral V_local(X) + integral K_1
S_2[X] = integral V_local(X) + integral K_2
```

with the same local metric/Hessian limit but different gradient terms.

In metric language, the comparison can be represented schematically as:

```text
K_1 = K_EH/GHY
K_2 = K_EH/GHY + epsilon K_residual
```

Both can share the same local metric branch while producing different field
equations, boundary terms, derivative orders, or propagating content unless the
residual is killed, made boundary-equivalent, or explicitly routed.

## Concrete Witness Classes

The witness does not need a physical residual to be useful. It only needs
mathematically distinct strain choices that preserve the same local metric
branch before the accumulated gates are applied.

```text
same V_local + EH/GHY strain
same V_local + EH/GHY strain + boundary/topological term
same V_local + EH/GHY strain + higher-curvature residual
same V_local + EH/GHY strain + nonlocal relaxation term
same V_local + direct configuration-gradient strain
```

These classes all leave the pointwise question:

```text
what is g_ab(p)?
```

separate from the strain question:

```text
what action or mismatch law governs variation between points?
```

The accumulated gates may later kill, quarantine, or identify some of these
classes as physically equivalent to `epsilon = 0`. That is downstream of the
witness. The witness only establishes that local response alone did not choose
among them.

## What The Accumulated Gates May Still Do

The witness is compatible with three later outcomes:

```text
the gates force EH/GHY and epsilon = 0;
the gates permit a controlled routed residual;
the gates leave K_strain underdetermined, requiring a new strain axiom.
```

The witness rules out only one move:

```text
claiming K_strain follows from local interval response alone.
```

## What This Does Not Claim

This is not a physical theory.

It does not claim that any particular residual is allowed.

It does not claim that `epsilon != 0`.

It claims only that:

```text
local response alone does not choose K_strain.
```

## Ledger Consequence

The admissibility matrix should include a local-response-only selector row with
this status:

```text
underdetermined without new axiom
```

The kill condition for that row is:

```text
using pointwise metric reconstruction as if it supplied transport, curvature
action, boundary variation, mode content, or epsilon classification.
```

## SymPy Validation

The companion script:

```text
make_underdetermination_witness_sympy.py
```

validates a scalar prototype:

```text
same local Hessian;
different Euler-Lagrange equations;
different boundary data;
different derivative order.
```

It writes:

```text
underdetermination_witness_sympy.md
```

The generated report records all symbolic checks as passed.

The VacuumForge-managed script:

```text
../../../../vacuum_forge/src/vacuum_sector/001_strain_underdetermination/strain_underdetermination_witness.py
```

records the same witness as an archived derivation, licensed governance claim,
and open obligation. It writes:

```text
underdetermination_witness_vacuumforge.md
```

## Useful Result

This witness classifies the current local-response-only ontology as:

```text
underdetermined without new axiom
```

This does not settle the full vacuum ontology. It says the next selector must
come from accumulated gates plus a strain principle, not from `V_local` alone.

Until a stronger selector is completed, the working null hypothesis remains:

```text
the current ontology underdetermines K_strain.
```
