# Neighboring Mismatch Contract

Field equations require more than pointwise interval response. A strain branch
must say how neighboring vacuum configurations compare.

This document defines the minimum contract for that comparison.

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
