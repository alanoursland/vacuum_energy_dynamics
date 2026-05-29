# Proof Chain Plan: Vacuum Strain Functional Frontier

## Purpose

The project began by solving the projection coefficient mystery. It then reconstructed the GR branch conditionally from scalar boundary admissibility, directional metric response, tensor/Weyl data, matter stress coupling, symplectic boundary dynamics, nonlinear constraint pressure, and EH/GHY action closure.

That work does not leave the remaining problem diffuse. It localizes the next field-equation question to one object:

```text
the vacuum strain / gradient functional.
```

The plan is not to write another GR reconstruction folder. The plan is to state what functional must now be specified, derived, or shown underdetermined for the vacuum ontology to become a field-equation-generating theory.

## Core diagnosis

The existing chain strongly constrains local response:

```text
local directional response Q_p(v)
  -> quadratic/parallelogram gate
  -> Hessian metric g_ab(p)
  -> local tensor data.
```

But the existing chain repeatedly imports between-point dynamics:

```text
transport law
connection dynamics
curvature propagation
field equation
radiation
constraint closure
EH/GHY action branch.
```

Those imported structures should come from a strain/gradient term:

```text
K_strain(X, ∇X, ∇∇X, ...).
```

## Target object

The vacuum theory needs a functional of the schematic form:

```text
S_vac[X] = ∫ [ V_local(X) + K_strain(X, ∇X, ∇∇X, ...) ].
```

`V_local` controls pointwise response and supplies the metric/Hessian branch.

`K_strain` controls neighboring-configuration mismatch and must generate transport, field equations, radiation, and possible deviations from GR.

## Constrained residual form

The prior gates do not leave an arbitrary functional menu. They constrain the strain sector to lie near the Einstein branch:

```text
K_strain = K_EH + ε K_residual.
```

The residual must preserve or explicitly route every prior gate:

```text
locality
calibration coherence
diffeomorphism / relabeling invariance
Lorentzian hyperbolicity
two TT degrees of freedom
boundary differentiability
symplectic radiative ledger
metric reduction at lowest order
source-ledger purity.
```

The frontier question is therefore not merely “what is `K_strain`?” It is:

```text
Do the accumulated gates force ε = 0, permit a controlled ε != 0, or show
that an additional strain axiom is required?
```

## Folder status

This folder is a frontier specification. It contains no fake proof scripts. Scripts should be added later only for candidate functional branches whose algebra can actually be checked.
