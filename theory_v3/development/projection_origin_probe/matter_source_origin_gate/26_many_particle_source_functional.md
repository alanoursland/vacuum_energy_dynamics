# Matter Source Origin Gate 26: Many-Particle Source Functional

## Purpose

This proof records how the weak proper-time coupling becomes an ordinary source
functional for many particles.

## Validated Checks

- variation of weak proper-time interaction gives each particle mass: passed
- constant potential couples to total ordinary mass: passed
- source functional is additive and linear in field perturbations: passed

## Discrete Source Functional

For two particles, the weak interaction term is:

```text
L_int = -m_1 Phi(x_1) - m_2 Phi(x_2).
```

Varying with respect to the field values gives:

```text
-d L_int/d Phi(x_1) = m_1
-d L_int/d Phi(x_2) = m_2.
```

For a constant potential:

```text
L_int = -(m_1 + m_2) Phi_0.
```

So the source weight is the total ordinary mass.

## Continuum Reading

The continuum expression is the standard weak source functional:

```text
L_int = - integral rho(x) Phi(x) dV.
```

The proof above is its finite-particle version.

## Gate Interpretation

This explains how proper-time coupling produces the ordinary mass density
source used by the reduced A-sector law. It still assumes the interval coupling
already established in the previous gate.
