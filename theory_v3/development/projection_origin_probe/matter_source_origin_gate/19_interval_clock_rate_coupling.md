# Matter Source Origin Gate 19: Interval Clock-Rate Coupling

## Purpose

This proof records the first interval-origin gate:

```text
if matter action is proper-time based,
then weak clock-rate response gives the Newtonian matter coupling.
```

It is conditional. It does not yet prove why matter must follow the vacuum
interval; it proves what follows if it does.

## Validated Checks

- sqrt(1+2Phi/c^2) gives clock-rate shift Phi/c^2: passed
- proper-time action gives potential term -m Phi: passed
- variation with respect to Phi gives source weight m: passed
- with u=-Phi, clock-rate shift is -u/c^2: passed

## Weak Clock Rate

For a static weak interval:

```text
d tau/dt = sqrt(1 + 2 Phi/c^2).
```

SymPy verifies the first-order expansion:

```text
d tau/dt = 1 + Phi/c^2.
```

## Matter Action

The proper-time particle action is:

```text
L = -m c^2 d tau/dt.
```

Therefore:

```text
L = -m c^2 - m Phi.
```

The interaction term is the standard Newtonian one:

```text
L_int = -m Phi.
```

Equivalently, the potential energy is:

```text
U = m Phi.
```

## Relation To Bridge Variable

With:

```text
u = -Phi,
```

the clock-rate shift is:

```text
d tau/dt = 1 - u/c^2.
```

## Gate Interpretation

This is the cleanest reduced route from interval response to ordinary matter
coupling. The next question is whether the vacuum ontology forces matter to
use this local interval universally.
