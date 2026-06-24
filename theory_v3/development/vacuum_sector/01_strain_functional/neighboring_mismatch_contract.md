# Neighboring Mismatch Contract

Field equations require more than pointwise interval response. A strain branch
must say how neighboring vacuum configurations compare.

This document defines the minimum contract for that comparison.

Current managed inventory:

```text
neighboring_mismatch_inventory_vacuumforge.md
```

That inventory classifies the currently inventoried comparison rules. Its
current conclusion is that no currently inventoried non-baseline
neighboring-mismatch rule is complete enough to open candidate strain dynamics
without additional routing. Levi-Civita metric transport is usable as the GR
baseline, but remains a metric-transport placeholder for the vacuum ontology
unless a selector explains why vacuum strain uses that comparison rule.

## Required Questions

Any candidate `K_strain` must answer:

```text
What does it mean to compare X(p) and X(q)?
```

Possible comparison rules include:

```text
Levi-Civita transport
independent connection
calibration map
holonomy or loop mismatch
medium strain tensor
Finsler direction map
nonlocal kernel
not yet specified
```

The branch must also answer:

```text
What object is minimized?
What scalar or invariant is built from mismatch?
What derivative order is admitted?
What boundary term makes the variation well posed?
What conservation identity follows?
What variables carry propagating modes?
What residual coefficient epsilon, if any, is introduced?
```

## Mismatch Is The Strain Branch

The local map:

```text
X(p) -> Q_p(v) -> g_ab(p)
```

does not determine how `X(p)` and `X(q)` compare.

That missing between-point comparison is exactly the strain problem:

```text
neighboring mismatch -> K_strain -> transport law -> field equation.
```

## Boundary And Conservation Requirements

A mismatch rule must identify:

```text
bulk variational equation;
total derivative terms;
boundary data or boundary counterterm;
Noether or Bianchi-type identity;
source-ledger implications.
```

If a candidate cannot account for boundary terms or conservation identities, it
is not yet a field-equation-generating strain branch.

## Contract Status Labels

Use these labels when evaluating a neighboring-mismatch rule:

```text
complete mismatch contract
partial mismatch contract
metric-transport placeholder
extra-connection route required
nonlocal route required
underdetermined without new axiom
fails accumulated gate
not yet evaluated
```

## Current Inventory Summary

```text
Levi-Civita metric transport:
  status: metric-transport placeholder
  burden: explain why vacuum ontology selects Levi-Civita metric transport

independent affine connection:
  status: extra-connection route required
  burden: derive compatibility or route torsion/nonmetric residuals

calibration map:
  status: partial mismatch contract
  burden: define calibration variable, invariant, and matter-coupling route

holonomy or loop mismatch:
  status: partial mismatch contract
  burden: explain why the leading scalar is EH-like or classify residual modes

medium strain tensor:
  status: underdetermined without new axiom
  burden: state constitutive law and route extra modes and frame effects

Finsler direction map:
  status: partial mismatch contract
  burden: route nonquadratic response through epsilon tests before physical use

nonlocal kernel:
  status: nonlocal route required
  burden: quarantine to Lambda/dark/large-scale sector unless local equations stay closed
```

Next target:

```text
complete the residual gate ledger.
```

Non-conclusion:

```text
no K_strain is selected;
no epsilon is computed;
no residual branch is licensed;
no global no-go theorem against nonbaseline mismatch rules is claimed.
```
