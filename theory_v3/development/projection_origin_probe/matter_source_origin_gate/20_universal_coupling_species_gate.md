# Matter Source Origin Gate 20: Universal Coupling Species Gate

## Purpose

This proof records the species-universality condition for interval/clock-rate
coupling.

## Validated Checks

- inertial mass cancels from acceleration for clock-rate coupling: passed
- species-independent acceleration requires equal clock coupling: passed
- beta1=beta2=1 gives universal Newtonian acceleration: passed
- different beta values produce a nonzero universality violation: passed

## Setup

Allow a species-dependent clock coupling:

```text
U_i = beta_i m_i Phi.
```

Then:

```text
F_i = -beta_i m_i grad Phi
a_i = F_i/m_i = -beta_i grad Phi.
```

The inertial mass cancels, but species universality still requires:

```text
beta_1 = beta_2.
```

The standard metric/interval coupling has:

```text
beta_i = 1
```

for every matter species.

## Gate Interpretation

If the vacuum interval is the universal clock-rate structure, the coupling is
universal. If any species has an independent coefficient, the weak-limit
source law is no longer universal and the A-sector mass ledger is not closed.
