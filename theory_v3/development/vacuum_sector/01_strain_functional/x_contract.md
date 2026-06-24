# X Contract

This document defines the minimum interface a vacuum configuration variable
`X` must provide before a strain functional can be treated as meaningful.

It is a contract, not a choice of final theory.

Current managed inventory:

```text
x_contract_inventory_vacuumforge.md
```

That inventory classifies the currently inventoried `X` options as contract
states. Its current conclusion is that no currently inventoried non-metric `X`
option is complete enough to open candidate strain dynamics without additional
routing. The metric-data branch is usable as the GR baseline but remains a
metric-only placeholder for the vacuum ontology unless a selector explains why
vacuum configuration reduces to `g_ab`.

## Required Questions

Any candidate branch must answer:

```text
What is the vacuum configuration variable X?
```

Possible statuses include:

```text
metric data g_ab
interval-response data Q_p(v)
frame or coframe data
connection or transport data
internal medium data
deeper premetric variable
not yet specified
```

A candidate must also answer:

```text
How does X transform under relabelings?
How does X reduce to g_ab in the metric branch?
What map sends X to the local interval response Q_p(v)?
What map sends X to the metric/Hessian response when the quadratic gate holds?
What is the matter-coupling route?
What boundary data are admissible?
Which variables are physical?
Which variables are gauge?
```

## Metric-Branch Reduction

The metric branch must recover:

```text
Q_p(v) = g_ab(p) v^a v^b
```

at lowest order when the local response is exact quadratic.

If `X` is not simply metric data, the branch must state the reduction map:

```text
X -> Q_p(v) -> g_ab(p).
```

If the reduction is nonquadratic, Finsler-like, frame-dependent, or species
dependent, that fact must be explicitly routed outside the pure metric branch.

## Matter Coupling Route

A candidate branch must state whether matter couples to:

```text
g_ab only;
X directly;
a derived frame/coframe;
an independent connection;
a nonmetric calibration field;
an effective metric plus routed residual fields.
```

If matter couples to anything beyond the shared metric interval, the candidate
must identify the implied observable channel and route it through residual
tests.

## Boundary Data

The branch must state what is fixed on the boundary:

```text
metric or induced metric;
interval response;
frame/coframe;
connection data;
normal derivative data;
nonlocal/global data;
other branch-specific data.
```

Boundary data are not decoration. They determine whether the variational
problem is well posed and whether the branch silently changes the gravitational
sector.

## Contract Status Labels

Use these labels when evaluating a proposed `X`:

```text
complete contract
partial contract
metric-only placeholder
extra-field route required
underdetermined without new axiom
fails accumulated gate
not yet evaluated
```

## Current Inventory Summary

```text
metric data g_ab:
  status: metric-only placeholder
  burden: explain why vacuum ontology chooses metric data as X

interval-response data Q_p(v):
  status: partial contract
  burden: supply neighboring mismatch rule across points

frame/coframe data:
  status: extra-field route required
  burden: route torsion/spin/frame observables and hidden preferred-frame risk

connection/transport data:
  status: extra-field route required
  burden: derive metric compatibility or route nonmetric/torsion residuals

internal medium data:
  status: underdetermined without new axiom
  burden: state constitutive law and route modes, anisotropy, and frame effects

deeper premetric variable:
  status: underdetermined without new axiom
  burden: define X before strain dynamics can be evaluated
```

Next target:

```text
complete the neighboring-mismatch contract.
```

Non-conclusion:

```text
no final X is selected;
no K_strain is derived;
no epsilon is computed;
no global no-go theorem against non-metric X is claimed.
```
