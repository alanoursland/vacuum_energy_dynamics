# Matter Source Origin Gate: Covariant Matter Lift Status After Proofs 13-17

## Purpose

This report summarizes the first covariant weak-matter-coupling lift.

The result is still conditional: it uses the standard weak metric matter
coupling and checks that it reduces to the A-sector source law already proved
in the reduced chain.

## Proofs Completed

Proof `13` validates the point-particle weak limit:

```text
g_00 = -(1+2 Phi/c^2)
L = -m c^2 + (1/2)m v^2 - m Phi.
```

So ordinary matter feels:

```text
F = -m grad Phi.
```

With `u=-Phi`, the geometric bridge variable satisfies:

```text
h_00 = 2u/c^2.
```

Proof `14` validates the stress-source reduction:

```text
delta S_m = (1/2) T^00 delta g_00
g_00 = -A
T^00 approximately rho c^2
```

so the A-component source is proportional to ordinary mass density.

Proof `15` validates the gauge/source consistency gate:

```text
T xi' = d(T xi)/dx - T' xi.
```

The tensor version is:

```text
partial_mu T^mu_nu = 0.
```

Proof `16` validates the radial reduction:

```text
Delta f = (1/r^2)(r^2 f')'
A = 1 + 2 Phi/c^2
Delta Phi = 4*pi*G rho
```

implies:

```text
Delta A = 8*pi*G rho/c^2.
```

Proof `17` validates the projection-source routing exclusion:

```text
F_total = alpha M + gamma b
F_target = alpha M
```

for independent `M,b` forces:

```text
gamma = 0.
```

## Current Result

The source-origin chain now has a clean reduced-to-covariant bridge:

```text
standard weak metric matter coupling
  -> Newtonian point-particle motion
  -> stress source proportional to rho
  -> conserved-source consistency
  -> static radial A-sector source law
  -> projection/residual source exclusion unless routed.
```

## Remaining Gap

This does not yet prove that the vacuum ontology forces the standard metric
matter coupling.

The next proof target is therefore:

```text
matter coupling origin from vacuum interval / clock-rate response.
```

Concrete gates:

```text
1. derive why matter follows the local interval defined by the vacuum state;
2. derive why the coupling is universal, not species-dependent;
3. derive why nonmetric residual/projection channels do not alter clock-rate
   coupling except through allowed zero-monopole diagnostics;
4. connect the boundary-source representation to the covariant stress tensor.
```
