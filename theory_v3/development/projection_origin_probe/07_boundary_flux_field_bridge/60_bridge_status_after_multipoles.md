# Boundary Flux Field Bridge: Status After Proofs 53-59

## Main Update

This batch clarifies finite boundary behavior and the first safe geometry lift.

The bridge now separates three boundary regimes:

```text
fixed flux:
  conserved source strength

fixed potential:
  induced net charge changes with environment

neutral floating:
  net induced charge stays zero, but induced multipoles appear
```

## Induced Boundary Response

Proof `53` validates the Kelvin image response for a grounded sphere.

An external source `q` at distance `d` from a sphere of radius `R` induces:

```text
q_img = -(R/d)q
b = R^2/d.
```

This holds the spherical boundary at zero potential. The induced net charge
depends on distance, so fixed-potential boundaries are not fixed-source
boundaries.

Proof `54` adds a compensating central source to keep the induced net charge
zero. The neutral floating sphere has:

```text
q_img + q_center = 0
p_induced = -q R^3/d^2.
```

So finite boundaries can polarize through induced multipoles even when total
flux is fixed.

## Boundary Source Action

Proof `55` upgrades the point coupling to a boundary integral:

```text
E[u] = 1/2 integral_Omega |grad u|^2 dV
       - integral_boundary q u dA.
```

The natural boundary condition is:

```text
partial_n u = q.
```

For an exterior sphere this gives:

```text
-u'(R)=Q/(4*pi*R^2).
```

## Reduced Action

Proof `56` packages the reduced-action sign in a two-source Green matrix:

```text
E_red = -1/2 J^T G J.
```

The cross term is:

```text
E_cross = -G Q1Q2.
```

If `G(d)=K/d`, same-sign sources attract under the reduced-action
bookkeeping.

## Fixed-Potential Monopole Approximation

Proof `57` shows that, even in the monopole approximation, fixed-potential
sphere charges depend on separation:

```text
Q1 = 4*pi*R1*d*(U1*d - R2*U2)/(d^2 - R1R2)
Q2 = 4*pi*R2*d*(U2*d - R1*U1)/(d^2 - R1R2).
```

So fixed potential remains a response condition rather than a conserved source
condition.

## Multipole Kernel

Proof `58` validates the Legendre expansion and shows uniform spherical flux
keeps only `l=0`. This explains why the uniform finite-sphere monopole result
has no radius correction, while induced or nonuniform data can carry higher
multipoles.

## First Geometry Lift

Proof `59` validates only the componentwise Dirichlet lift:

```text
E[h] = 1/2 integral sum_A |grad h_A|^2 dV
```

which gives:

```text
-Delta h_A = source_A.
```

This is not a gravitational tensor equation. It is the controlled first step
from one scalar field to a multi-component configuration field.

## Current State

The scalar weak-field bridge is now substantially stable:

```text
boundary flux
source-free exterior Laplace equation
inverse-square 3D field strength
attractive reduced action
finite-sphere monopole stability
induced multipole response
boundary-integral source coupling
componentwise multi-field lift
```

## Remaining Hard Step

The next hard step is not another scalar inverse-square proof.

It is to derive the correct field variable and source coupling from the vacuum
ontology:

```text
What is the physical configuration variable?
What is the invariant energy/strain?
What constraint makes the reduced action the correct interaction bookkeeping?
What replaces the componentwise Laplacian once geometry and gauge freedom are
included?
```
