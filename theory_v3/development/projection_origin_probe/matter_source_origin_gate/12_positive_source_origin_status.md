# Matter Source Origin Gate: Positive Source-Origin Status After Proofs 7-11

## Purpose

This report summarizes the first positive source-origin batch.

The previous batch proved exclusions and routing constraints. This batch proves
the reduced A-sector coupling that actually carries ordinary matter source.

## Proofs Completed

Proof `7` derives the reduced A-sector source law from a radial variational
principle:

```text
E_A = integral [ (K/2) r^2 (A')^2 + lambda r^2 rho A ] dr
```

which gives:

```text
Delta_areal A = (lambda/K) rho.
```

The Newtonian normalization is:

```text
lambda/K = 8*pi*G/c^2.
```

Proof `8` proves the Gauss-flux mass ledger:

```text
F_A = 4*pi*r^2 A' = 8*pi*G*M/c^2.
```

Proof `9` proves the weak-limit match:

```text
A = 1 + 2 Phi/c^2
Delta Phi = 4*pi*G rho
```

implies:

```text
Delta A = 8*pi*G rho/c^2.
```

Proof `10` proves the reduced boundary-source equivalent:

```text
E_boundary = + q A(R)
F_A = q/K.
```

With:

```text
q = K * 8*pi*G*M/c^2,
```

the boundary source gives the same A-sector mass flux.

Proof `11` proves the zero-monopole auxiliary-source silence gate:

```text
4*pi integral H r^2 dr = 0
```

implies no exterior A-sector mass-flux shift.

## Current Result

The reduced matter-source origin is now sharper:

```text
ordinary matter couples to the A-sector through the Newtonian-normalized
Dirichlet/Poisson source law;
the same source can be represented as a reduced boundary flux;
only the monopole controls exterior A-sector mass;
auxiliary residual/projection structures are safe only if their routed
ordinary monopole vanishes or they remain outside the source ledger.
```

## Remaining Gap

The open step is the covariant lift:

```text
derive the matter coupling from a coordinate-independent action;
show how the A-sector source law appears as the static weak spherical limit;
prove that projection/admissibility diagnostics remain auxiliary under that
lift, or specify a zero-monopole routing rule for them.
```
